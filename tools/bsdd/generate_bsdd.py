#!/usr/bin/env python3
"""
Generate a buildingSMART Data Dictionary (bSDD) import file from Brick.

bSDD accepts a dictionary as a single JSON document; content cannot be
uploaded in parts. This script derives that document from the built
ontology (Brick+imports.ttl) so the dictionary never drifts from the
ontology it describes.

Only terms in the Brick namespace are published. Brick imports its location
classes from RealEstateCore, but bSDD's UseOwnUri requires every owned URI to
begin with this dictionary's DictionaryUri, so publishing them would mean
republishing another vocabulary's content under Brick identifiers. That is
RealEstateCore's to do, not Brick's. The consequence is that the dictionary
carries no rooms or spaces at all, and that the Brick classes which subclass
rec:Collection -- System, Loop, PV_Array and the rest -- are emitted as roots
with no ParentClassCode. The report lists them.

Usage:
    python tools/bsdd/generate_bsdd.py --output bsdd/brick-bsdd.json

See tools/bsdd/README.md for the upload procedure and the mapping rationale.
"""

import argparse
import csv
import hashlib
import json
import re
import sys
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

from rdflib import Graph, Namespace, RDF, RDFS, OWL, URIRef
from rdflib.collection import Collection
from rdflib.namespace import SKOS, XSD

# Allow `from bricksrc...` when run from anywhere in the repo.
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(REPO_ROOT))

from bricksrc.version import BRICK_FULL_VERSION, BRICK_VERSION  # noqa: E402

BRICK = Namespace("https://brickschema.org/schema/Brick#")
QUDT = Namespace("http://qudt.org/schema/qudt/")
QUDTQK = Namespace("http://qudt.org/vocab/quantitykind/")
SH = Namespace("http://www.w3.org/ns/shacl#")
DCTERMS = Namespace("http://purl.org/dc/terms/")

DEFAULT_SOURCE = REPO_ROOT / "Brick+imports.ttl"
MAPPINGS_DIR = Path(__file__).resolve().parent / "mappings"
UNITS_CSV = MAPPINGS_DIR / "units.csv"
IFC_CSV = MAPPINGS_DIR / "ifc.csv"
# buildingSMART's own IFC dictionary, from fetch_ifc_dictionary.py. Entity
# names are checked against it because a curated row is inherited by every
# subclass, so one typo would reach hundreds of classes.
IFC_REFERENCE = Path(__file__).resolve().parent / "reference" / "ifc-4.3-classes.csv"

BSDD_UNIT_API = "https://api.bsdd.buildingsmart.org/api/Unit/v1"

# Dictionary-level metadata. OrganizationCode must match an organisation
# registered with buildingSMART before a non-test upload will be accepted.
ORGANIZATION_CODE = "brick"
DICTIONARY_CODE = "brick"
DICTIONARY_NAME = "Brick Schema"
LANGUAGE_ISO_CODE = "en-GB"
MORE_INFO_URL = "https://brickschema.org"
QA_PROCEDURE = "Brick Consortium open review process"
QA_PROCEDURE_URL = "https://github.com/BrickSchema/Brick/blob/master/CONTRIBUTING.md"
CHANGE_REQUEST_EMAIL = "info@brickschema.org"

SCHEMA_ROOT = "https://brickschema.org/schema"
CANONICAL_NAMESPACE = f"{SCHEMA_ROOT}/Brick"
VERSIONED_NAMESPACE = f"{SCHEMA_ROOT}/{BRICK_VERSION}/Brick"

# Property sets group properties when serialised into IFC. 'Pset_' is
# reserved for official IFC content (PRP-03); 'cPSET_' is the documented
# convention for custom sets.
PSET_QUANTITY = "cPSET_BrickQuantity"
PSET_SUBSTANCE = "cPSET_BrickSubstance"
PSET_COMMON = "cPSET_BrickCommon"

# bSDD forbids these characters in codes.
ILLEGAL_CODE_CHARS = set('"#%/\\:`{}[]|;<>?~')
MAX_CODE_LENGTH = 100

# QUDT writes dimension vectors as A<n>E<n>L<n>I<n>M<n>H<n>T<n>D<n>:
# amount, electric current, length, luminous intensity, mass,
# thermodynamic temperature, time, dimensionless.
DIMENSION_RE = re.compile(r"([AELIMHTD])(-?[0-9.]+)")
# bSDD orders them: length, mass, time, current, temperature, amount, luminous.
BSDD_DIMENSION_ORDER = ["L", "M", "T", "E", "H", "A", "I"]
DIMENSIONLESS = "0 0 0 0 0 0 0"

XSD_TO_BSDD_DATATYPE = {
    XSD.string: "String",
    XSD.boolean: "Boolean",
    XSD.integer: "Integer",
    XSD.nonNegativeInteger: "Integer",
    XSD.positiveInteger: "Integer",
    XSD.int: "Integer",
    XSD.long: "Integer",
    XSD.decimal: "Real",
    XSD.double: "Real",
    XSD.float: "Real",
    XSD.dateTime: "Time",
    XSD.date: "Time",
    XSD.time: "Time",
}


# ---------------------------------------------------------------------------
# graph helpers
# ---------------------------------------------------------------------------


def local_name(term):
    """Return the fragment or last path segment of a URI."""
    text = str(term)
    if "#" in text:
        return text.rsplit("#", 1)[1]
    return text.rsplit("/", 1)[1]


def load_graph(path):
    graph = Graph()
    graph.parse(str(path), format="turtle")
    return graph


def all_classes(graph):
    """
    Every declared class, however typed. Imported vocabularies use rdfs:Class
    as readily as owl:Class, and the selection below filters by namespace, so
    read both rather than assume how a term was declared.
    """
    return set(graph.subjects(RDF.type, OWL.Class)) | set(
        graph.subjects(RDF.type, RDFS.Class)
    )


def is_deprecated(graph, term):
    return (term, OWL.deprecated, None) in graph


def label_for(graph, term):
    """Prefer an English rdfs:label; fall back to the code with underscores
    turned into spaces, which is how Brick derives labels anyway."""
    labels = list(graph.objects(term, RDFS.label))
    english = [x for x in labels if getattr(x, "language", None) == "en"]
    chosen = english or labels
    if chosen:
        return str(chosen[0])
    return local_name(term).replace("_", " ")


def definition_for(graph, term):
    """
    skos:definition is Brick's definition predicate, with rdfs:comment as the
    fallback for terms that only carry one.

    Brick carries some definitions both with and without a language tag, so
    prefer the tagged one and fall back rather than emitting either at random.
    """
    for predicate in (SKOS.definition, RDFS.comment):
        values = list(graph.objects(term, predicate))
        if not values:
            continue
        english = [x for x in values if getattr(x, "language", None) == "en"]
        chosen = english or values
        return str(chosen[0]).strip()
    return None


def rdf_list(graph, node):
    """Materialise an RDF collection, tolerating malformed lists."""
    try:
        return list(Collection(graph, node))
    except Exception:
        return []


# ---------------------------------------------------------------------------
# codes and URIs
# ---------------------------------------------------------------------------


def code_for(term):
    """
    Brick's local names are already valid bSDD codes: underscores are allowed,
    the longest is well inside the 100-character limit, and they carry no
    forbidden characters. Using them verbatim keeps the code that lands in an
    IFC file resolvable straight back to the ontology term.
    """
    return local_name(term)


def owned_uri(term, uri_style):
    """
    The identifier bSDD publishes for this term.

    'canonical' reuses Brick's own unversioned term IRI, which is the identity
    Brick actually publishes -- Brick deliberately does not version term IRIs,
    so the version is carried by DictionaryVersion instead. 'versioned' mints
    a per-release IRI for platforms that expect the version in the path.
    """
    text = str(term)
    if uri_style == "versioned" and text.startswith(CANONICAL_NAMESPACE + "#"):
        return text.replace(CANONICAL_NAMESPACE + "#", VERSIONED_NAMESPACE + "#", 1)
    return text


def dictionary_uri(uri_style):
    return VERSIONED_NAMESPACE if uri_style == "versioned" else CANONICAL_NAMESPACE


def property_owned_uri(code, uri_style):
    """Mint a Brick-owned URI for a property in the generated dictionary.

    Properties are assembled from several RDF vocabularies and some are merged
    on case-insensitive code collisions, so no single source term IRI reliably
    identifies the exported property.  Keep them in a dedicated namespace to
    avoid colliding with class IRIs such as ``brick:Substance``.
    """
    return f"{dictionary_uri(uri_style)}#property/{code}"


def validate_code(code):
    """Return a complaint about this code, or None if it is acceptable."""
    if not code:
        return "empty code"
    if len(code) > MAX_CODE_LENGTH:
        return f"code longer than {MAX_CODE_LENGTH} characters"
    bad = sorted(set(code) & ILLEGAL_CODE_CHARS)
    if bad:
        return f"code contains forbidden characters: {''.join(bad)}"
    if code[:3].lower() == "ifc":
        return "the 'Ifc' prefix is reserved for the IFC standard"
    return None


def allowed_value_code(value, used_codes):
    """Return a stable, valid bSDD code for a human-readable allowed value."""
    base = "".join("_" if char in ILLEGAL_CODE_CHARS else char for char in value)
    base = base or "value"

    digest = hashlib.sha256(value.encode("utf-8")).hexdigest()[:8]
    if len(base) > MAX_CODE_LENGTH:
        suffix = f"_{digest}"
        base = base[: MAX_CODE_LENGTH - len(suffix)] + suffix

    candidate = base
    if candidate.lower() in used_codes:
        suffix = f"_{digest}"
        candidate = base[: MAX_CODE_LENGTH - len(suffix)] + suffix

    used_codes.add(candidate.lower())
    return candidate


# ---------------------------------------------------------------------------
# units and dimensions
# ---------------------------------------------------------------------------


def load_unit_map(path=UNITS_CSV):
    """QUDT unit IRI -> bSDD unit code, for units bSDD actually knows."""
    mapping = {}
    if not Path(path).exists():
        return mapping
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row.get("bsdd_code"):
                mapping[row["qudt_uri"]] = row["bsdd_code"]
    return mapping


def refresh_unit_map(graph, path=UNITS_CSV):
    """
    Rebuild mappings/units.csv by joining Brick's QUDT units against the bSDD
    unit list, which publishes a qudtUri for many of its entries.

    Manually curated rows win: bSDD's own qudtUri coverage is partial, so
    hand-added codes must survive a refresh.
    """
    existing_manual = {}
    if Path(path).exists():
        with open(path, newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                if row.get("source") == "manual" and row.get("bsdd_code"):
                    existing_manual[row["qudt_uri"]] = row["bsdd_code"]

    with urllib.request.urlopen(BSDD_UNIT_API, timeout=60) as response:
        bsdd_units = json.load(response)
    by_qudt = {u["qudtUri"]: u["code"] for u in bsdd_units if u.get("qudtUri")}

    used = used_unit_iris(graph)
    rows = []
    for iri in sorted(used):
        if iri in existing_manual:
            rows.append((iri, existing_manual[iri], "manual"))
            continue
        # bSDD records some qudtUri values as http even though Brick uses https.
        code = by_qudt.get(iri) or by_qudt.get(iri.replace("https://", "http://"))
        rows.append((iri, code or "", "bsdd-api" if code else ""))

    MAPPINGS_DIR.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["qudt_uri", "bsdd_code", "source"])
        writer.writerows(rows)
    mapped = sum(1 for row in rows if row[1])
    print(f"units.csv: {mapped}/{len(rows)} QUDT units mapped to bSDD codes")
    return mapped, len(rows)


def used_unit_iris(graph):
    """
    QUDT units reachable from the terms this dictionary exports.

    Deliberately not every qudt:applicableUnit in the import closure: QUDT
    ships ~1200 quantity kinds, and sweeping them all would bury the units
    Brick actually needs under thousands of irrelevant rows.
    """
    quantities = set(graph.subjects(RDF.type, BRICK.Quantity))
    quantities |= {
        o for o in graph.objects(None, BRICK.hasQuantity) if isinstance(o, URIRef)
    }

    iris = set()
    for quantity in quantities:
        iris |= {str(u) for u in graph.objects(quantity, QUDT.applicableUnit)}
    for pshape in graph.subjects(SH.path, BRICK.hasUnit):
        for enumeration in graph.objects(pshape, SH["in"]):
            for unit in rdf_list(graph, enumeration):
                iris.add(str(unit))
    return iris


def dimension_vector(graph, term):
    """
    Convert a QUDT dimension vector into bSDD's Dimension string.

    bSDD requires a Dimension on every numeric property (PRP-01). Every unit
    and quantity kind in the import closure carries one, so any property with
    at least one unit can be given a correct dimension.
    """
    vectors = list(graph.objects(term, QUDT.hasDimensionVector))
    if not vectors:
        return None
    exponents = dict(DIMENSION_RE.findall(local_name(vectors[0])))
    if not exponents:
        return None
    parts = []
    for key in BSDD_DIMENSION_ORDER:
        value = float(exponents.get(key, "0"))
        parts.append(str(int(value)) if value.is_integer() else str(value))
    return " ".join(parts)


def unit_dimensions(graph, unit_iris):
    """Map each unit IRI to the dimension QUDT gives it, skipping any without."""
    result = {}
    for iri in unit_iris:
        dimension = dimension_vector(graph, URIRef(iri))
        if dimension:
            result[iri] = dimension
    return result


def resolve_dimension(graph, quantity, unit_iris, code, report):
    """
    Decide a property's Dimension, and which of its units may keep it.

    Returns (dimension, kept_unit_iris). bSDD checks that every unit on a
    property matches that property's dimension (PRP-01), so the two must be
    consistent in the output whatever the source says.

    Units decide when they exist: they are the concrete, checkable signal, and
    Brick sometimes declares a quantity dimensionless while giving it units
    that are not (PM10_Concentration is dimensionless yet measured in µg/m³).
    The quantity's own vector is used only when there are no units at all;
    absent both, a numeric property is dimensionless, which PRP-01 wants
    stated rather than left blank.

    Where units disagree with each other, the most common dimension wins and
    the rest are dropped. Every disagreement is reported, because it is a
    defect in the source ontology rather than something to paper over.
    """
    by_unit = unit_dimensions(graph, unit_iris)

    if not by_unit:
        if quantity is not None:
            declared = dimension_vector(graph, quantity)
            if declared:
                return declared, []
        return DIMENSIONLESS, []

    tally = Counter(by_unit.values())
    # Sort by frequency, then by the dimension string, so ties are stable.
    dimension = sorted(tally.items(), key=lambda item: (-item[1], item[0]))[0][0]

    if len(tally) > 1:
        report["conflicting_dimensions"].append((code, sorted(tally), dimension))

    if quantity is not None:
        declared = dimension_vector(graph, quantity)
        if declared and declared != dimension:
            report["declared_dimension_mismatch"].append((code, declared, dimension))

    kept = [iri for iri, value in by_unit.items() if value == dimension]
    dropped = sorted(set(unit_iris) - set(kept))
    if dropped:
        report["dropped_units"].append((code, dropped))
    return dimension, kept


# ---------------------------------------------------------------------------
# term selection
# ---------------------------------------------------------------------------


def select_classes(graph, include_deprecated):
    """
    The classes the dictionary publishes: everything in the Brick namespace,
    and nothing else. Terms Brick imports from other vocabularies stay out --
    see the module docstring on why the REC location classes are excluded.
    """
    declared = all_classes(graph)

    brick_terms = {c for c in declared if str(c).startswith(str(BRICK))}

    if not include_deprecated:
        brick_terms = {c for c in brick_terms if not is_deprecated(graph, c)}
    return brick_terms


def depth_from_root(graph, term, selected, cache=None):
    """
    Longest rdfs:subClassOf chain from term up to a root inside `selected`.

    Used to pick a primary parent: bSDD allows a single ParentClassCode, so
    for a multiply-inherited class the deepest parent is kept in the tree
    (it is the most specific) and the rest become IsChildOf relations.
    """
    if cache is None:
        cache = {}
    if term in cache:
        return cache[term]
    cache[term] = 0  # guards against cycles in the source hierarchy
    parents = [
        p
        for p in graph.objects(term, RDFS.subClassOf)
        if isinstance(p, URIRef) and p in selected and p != term
    ]
    depth = (
        0
        if not parents
        else 1 + max(depth_from_root(graph, p, selected, cache) for p in parents)
    )
    cache[term] = depth
    return depth


def named_parents(graph, term, selected):
    return sorted(
        {
            p
            for p in graph.objects(term, RDFS.subClassOf)
            if isinstance(p, URIRef) and p in selected and p != term
        },
        key=str,
    )


def unselected_parents(graph, term, selected):
    """Named superclasses this dictionary does not publish."""
    return sorted(
        {
            p
            for p in graph.objects(term, RDFS.subClassOf)
            if isinstance(p, URIRef) and p not in selected and p != term
        },
        key=str,
    )


# ---------------------------------------------------------------------------
# classes
# ---------------------------------------------------------------------------


def load_ifc_reference(path=IFC_REFERENCE):
    """Rows of buildingSMART's IFC 4.3 dictionary, or [] if it was never
    fetched. See fetch_ifc_dictionary.py."""
    if not Path(path).exists():
        return []
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_ifc_map(path=IFC_CSV, report=None):
    """Class code -> IFC entity names. Curated by hand; Brick has no IFC
    alignment to derive this from."""
    mapping = {}
    if not Path(path).exists():
        return mapping
    known = {row["code"] for row in load_ifc_reference()}
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            entities = [e.strip() for e in row.get("ifc_entities", "").split(";")]
            entities = [e for e in entities if e]
            if known and report is not None:
                for entity in entities:
                    if entity not in known:
                        report["unknown_ifc_entities"].append((row["code"], entity))
            if entities:
                mapping[row["code"]] = entities
    return mapping


def propagate_ifc_map(graph, selected, ifc_map, report):
    """
    Extend the curated IFC map down the class hierarchy.

    `mappings/ifc.csv` names an entity for `Fan`; every Brick fan is an IfcFan,
    so its thirteen descendants carry the same entity without each needing a
    row. Only 30 codes are curated, but they reach 623 of the 1,400 classes
    this way. A class with its own row always keeps it, which is how a subclass
    overrides a parent whose entity is only approximately right.

    owl:equivalentClass is followed too. Brick's abbreviation aliases (`AHU`,
    `VAV`, `HX`) are equivalent to their spelled-out forms but sit under a
    generic parent, so subclass inheritance alone would never reach them.

    Returns code -> (entity names, origin code); origin == code means the row
    was curated rather than inherited.
    """
    by_code = {code_for(term): term for term in selected}
    depth_cache = {}
    resolved = {}

    def sources(term):
        """Named superclasses and equivalents, nearest first."""
        related = set(named_parents(graph, term, selected))
        for equivalent in graph.objects(term, OWL.equivalentClass):
            if isinstance(equivalent, URIRef) and equivalent in selected:
                related.add(equivalent)
        for equivalent in graph.subjects(OWL.equivalentClass, term):
            if isinstance(equivalent, URIRef) and equivalent in selected:
                related.add(equivalent)
        related.discard(term)
        return sorted(related, key=str)

    def resolve(code, path):
        if code in resolved:
            return resolved[code]
        curated = ifc_map.get(code)
        if curated:
            resolved[code] = (list(curated), code)
            return resolved[code]
        term = by_code.get(code)
        if term is None or code in path:  # unknown, or a cycle in the source
            return ([], "")

        # Distinct entity lists reaching the same class, keyed by list so a
        # parent and an equivalent agreeing on IfcFan counts once.
        candidates = {}
        for other in sources(term):
            entities, origin = resolve(code_for(other), path | {code})
            if entities:
                candidates.setdefault(tuple(entities), origin)

        if not candidates:
            resolved[code] = ([], "")
            return resolved[code]

        if len(candidates) > 1:
            # No Brick class hits this today. If one ever does, keep the entity
            # from the deepest origin -- the most specific claim, matching how
            # ParentClassCode resolves multiple inheritance -- and say so.
            report["ifc_conflicts"].append((code, sorted(candidates.values())))
        best = max(
            candidates.items(),
            key=lambda item: (
                (
                    depth_from_root(graph, by_code[item[1]], selected, depth_cache)
                    if item[1] in by_code
                    else 0
                ),
                item[1],
            ),
        )
        entities, origin = list(best[0]), best[1]
        resolved[code] = (entities, origin)
        report["ifc_inherited"].append((code, origin, entities))
        return resolved[code]

    for code in sorted(by_code):
        resolve(code, frozenset())
    return {code: value for code, value in resolved.items() if value[0]}


def build_classes(graph, selected, uri_style, ifc_map, report):
    """Emit the bSDD Class objects for every selected term."""
    depth_cache = {}
    classes = []

    for term in sorted(selected, key=str):
        code = code_for(term)
        complaint = validate_code(code)
        if complaint:
            report["invalid_codes"].append((code, complaint))
            continue

        entry = {
            "Code": code,
            "Name": label_for(graph, term),
            # Everything Brick describes is a class of objects. Brick has no
            # notion of what an entity is made of, so ClassType Material is
            # never correct here -- see the Substance property below.
            "ClassType": "Class",
            "OwnedUri": owned_uri(term, uri_style),
        }

        definition = definition_for(graph, term)
        if definition:
            entry["Definition"] = definition
        else:
            report["classes_without_definition"].append(code)

        parents = named_parents(graph, term, selected)
        if parents:
            primary = max(
                parents,
                key=lambda p: (
                    depth_from_root(graph, p, selected, depth_cache),
                    str(p),
                ),
            )
            entry["ParentClassCode"] = code_for(primary)
            extra = [p for p in parents if p != primary]
            if extra:
                report["multi_parent"].append(
                    (code, code_for(primary), [code_for(p) for p in extra])
                )
        else:
            extra = []
            # A Brick class whose only superclasses are imported terms becomes
            # a root here. That is a real change to the published hierarchy,
            # not an accident of the data, so it is reported rather than
            # silently accepted.
            outside = unselected_parents(graph, term, selected)
            if outside:
                report["roots_from_excluded_parents"].append(
                    (code, [str(p) for p in outside])
                )

        relations = []
        for parent in extra:
            relations.append(
                {
                    "RelationType": "IsChildOf",
                    "RelatedClassUri": owned_uri(parent, uri_style),
                    "RelatedClassName": label_for(graph, parent),
                }
            )

        synonyms = []
        for equivalent in sorted(graph.objects(term, OWL.equivalentClass), key=str):
            if not isinstance(equivalent, URIRef) or equivalent == term:
                continue
            synonyms.append(label_for(graph, equivalent))
            relations.append(
                {
                    "RelationType": "IsEqualTo",
                    "RelatedClassUri": owned_uri(equivalent, uri_style),
                    "RelatedClassName": label_for(graph, equivalent),
                }
            )
        if synonyms:
            entry["Synonyms"] = sorted(set(synonyms))
        if relations:
            entry["ClassRelations"] = relations

        ifc_entities, _origin = ifc_map.get(code, ([], ""))
        if ifc_entities:
            entry["RelatedIfcEntityNamesList"] = ifc_entities
        else:
            report["missing_ifc"].append(code)

        if is_deprecated(graph, term):
            messages = list(graph.objects(term, BRICK.deprecationMitigationMessage))
            if messages:
                entry["DeprecationExplanation"] = str(messages[0])
            replacements = [
                code_for(r)
                for r in graph.objects(term, BRICK.isReplacedBy)
                if isinstance(r, URIRef)
            ]
            if replacements:
                entry["ReplacingObjectCodes"] = sorted(replacements)

        classes.append(entry)

    return classes


# ---------------------------------------------------------------------------
# properties
# ---------------------------------------------------------------------------


def value_shape_for(graph, entity_property):
    """The sh:node value shape constraining this entity property, if any."""
    for pshape in graph.subjects(SH.path, entity_property):
        for node in graph.objects(pshape, SH.node):
            return node
    return None


def shape_constraints(graph, shape):
    """
    Flatten a value shape into {path_local_name: constraints}.

    Shapes inherit through rdfs:subClassOf (BSH.AreaShape -> BSH.ValueShape),
    so walk the ancestor chain; a subclass constraint wins over an inherited
    one for the same path.
    """
    if shape is None:
        return {}

    chain = []
    seen = set()
    frontier = [shape]
    while frontier:
        current = frontier.pop()
        if current in seen:
            continue
        seen.add(current)
        chain.append(current)
        frontier.extend(graph.objects(current, RDFS.subClassOf))

    fields = {}
    # Walk ancestors first so the most specific shape overwrites them.
    for node in reversed(chain):
        for pshape in graph.objects(node, SH.property):
            paths = list(graph.objects(pshape, SH.path))
            if not paths:
                continue
            key = local_name(paths[0])
            constraint = fields.setdefault(key, {})
            for datatype in graph.objects(pshape, SH.datatype):
                constraint["datatype"] = datatype
            for bound in (
                "minInclusive",
                "maxInclusive",
                "minExclusive",
                "maxExclusive",
            ):
                for value in graph.objects(pshape, SH[bound]):
                    constraint[bound] = str(value)
            for count in ("minCount", "maxCount"):
                for value in graph.objects(pshape, SH[count]):
                    constraint[count] = int(value)
            for enumeration in graph.objects(pshape, SH["in"]):
                constraint["in"] = rdf_list(graph, enumeration)
            if list(graph.objects(pshape, SH["or"])):
                constraint["numeric"] = True
    return fields


def quantity_for_shape(graph, shape):
    """
    Recover the quantity behind a BSH.<Quantity>QuantityShape.

    These shapes are named after the quantity they constrain, so when one
    carries no value constraints of its own the quantity still supplies the
    units and dimension.

    The name may refer to a brick:Quantity or, for shapes like
    PowerQuantityShape, to a QUDT quantity kind. Brick only attaches units to
    the former, so resolving against both namespaces recovers units for the
    rated*/measured* properties that would otherwise come out unconstrained.
    Anything with applicable units will do -- the type varies.
    """
    if shape is None:
        return None
    name = local_name(shape)
    if not name.endswith("QuantityShape"):
        return None
    stem = name[: -len("QuantityShape")]
    # Brick writes multi-word quantities with underscores (Electric_Current);
    # QUDT runs them together (ElectricCurrent).
    candidates = (BRICK[stem], QUDTQK[stem], QUDTQK[stem.replace("_", "")])
    for candidate in candidates:
        if list(graph.objects(candidate, QUDT.applicableUnit)):
            return candidate
    return None


def datatype_and_values(constraint):
    """Map a brick:value constraint onto (bSDD DataType, AllowedValues)."""
    if "in" in constraint:
        values = [str(v) for v in constraint["in"]]
        used_codes = set()
        allowed = []
        for index, value in enumerate(values, start=1):
            allowed.append(
                {
                    "Code": allowed_value_code(value, used_codes),
                    "Value": value,
                    "SortNumber": index,
                }
            )
        return "String", allowed
    if constraint.get("numeric"):
        return "Real", []
    if "datatype" in constraint:
        return XSD_TO_BSDD_DATATYPE.get(constraint["datatype"], "String"), []
    return None, []


def apply_bounds(entry, constraint):
    for bound in ("MinInclusive", "MaxInclusive", "MinExclusive", "MaxExclusive"):
        key = bound[0].lower() + bound[1:]
        if key in constraint:
            entry[bound] = constraint[key]


def build_entity_properties(graph, unit_map, report):
    """
    bSDD Properties derived from brick:EntityProperty.

    Constraints come from the SHACL value shape rather than the property
    itself: Brick states the datatype, permitted units and enumerated values
    on brick:value / brick:hasUnit inside that shape.
    """
    properties = {}

    for term in sorted(graph.subjects(RDF.type, BRICK.EntityProperty), key=str):
        code = code_for(term)
        complaint = validate_code(code)
        if complaint:
            report["invalid_codes"].append((code, complaint))
            continue

        shape = value_shape_for(graph, term)
        fields = shape_constraints(graph, shape)

        entry = {"Code": code, "Name": label_for(graph, term)}
        definition = definition_for(graph, term)
        if definition:
            entry["Definition"] = definition
        else:
            report["properties_without_definition"].append(code)

        value = fields.get("value", {})
        datatype, allowed = datatype_and_values(value)

        unit_iris = [str(u) for u in fields.get("hasUnit", {}).get("in", [])]
        quantity = quantity_for_shape(graph, shape)
        if not unit_iris and quantity is not None:
            unit_iris = [str(u) for u in graph.objects(quantity, QUDT.applicableUnit)]

        # Shapes carrying several sub-fields (latitude and longitude, a value
        # plus a timestamp) describe a structure, not a scalar.
        payload = {k: v for k, v in fields.items() if k != "hasUnit"}
        is_complex = len(payload) > 1

        # A scalar shape with neither a value constraint nor units tells us
        # nothing. These are dangling BSH.<Quantity>QuantityShape references
        # where no quantity exists under that name; complex shapes are a
        # separate, expected case and are not counted here.
        if datatype is None and not unit_iris:
            if not is_complex:
                report["unconstrained_properties"].append(code)
            datatype = "String"
        elif datatype is None:
            datatype = "Real"

        entry["DataType"] = datatype

        if allowed:
            entry["AllowedValues"] = allowed

        if datatype in ("Real", "Integer"):
            dimension, unit_iris = resolve_dimension(
                graph, quantity, unit_iris, code, report
            )
            if dimension:
                entry["Dimension"] = dimension

        if unit_iris:
            codes = sorted({unit_map[u] for u in unit_iris if u in unit_map})
            if codes:
                entry["Units"] = codes
            report["unmapped_units"].update({u for u in unit_iris if u not in unit_map})

        apply_bounds(entry, value)

        if is_complex:
            entry["PropertyValueKind"] = "Complex"
            report["complex_properties"].append(code)
        else:
            entry["PropertyValueKind"] = "Single"

        properties[code] = entry

    return properties


def build_quantity_properties(graph, unit_map, report):
    """
    bSDD Properties derived from the quantities Brick Points measure.

    Covers both brick:Quantity terms and the QUDT quantity kinds referenced
    directly by brick:hasQuantity. Every one carries a QUDT dimension vector,
    so each numeric property gets the Dimension bSDD requires (PRP-01).
    """
    properties = {}
    terms = set(graph.subjects(RDF.type, BRICK.Quantity))
    terms |= {
        o for o in graph.objects(None, BRICK.hasQuantity) if isinstance(o, URIRef)
    }

    for term in sorted(terms, key=str):
        code = code_for(term)
        complaint = validate_code(code)
        if complaint:
            report["invalid_codes"].append((code, complaint))
            continue

        entry = {
            "Code": code,
            "Name": label_for(graph, term),
            "DataType": "Real",
            "PropertyValueKind": "Single",
        }
        definition = definition_for(graph, term)
        if definition:
            entry["Definition"] = definition
        else:
            report["properties_without_definition"].append(code)

        unit_iris = [str(u) for u in graph.objects(term, QUDT.applicableUnit)]

        dimension, unit_iris = resolve_dimension(graph, term, unit_iris, code, report)
        if dimension:
            entry["Dimension"] = dimension

        if unit_iris:
            codes = sorted({unit_map[u] for u in unit_iris if u in unit_map})
            if codes:
                entry["Units"] = codes
            report["unmapped_units"].update({u for u in unit_iris if u not in unit_map})

        properties[code] = entry

    return properties


def substance_concepts(graph):
    """Every brick:Substance concept, ordered by a walk of skos:broader.

    AllowedValues is a flat list, so ordering by the SKOS hierarchy is the
    only way to keep related substances (Supply_Air, Return_Air, ...) adjacent.
    """
    concepts = {
        s for s in graph.subjects(RDF.type, BRICK.Substance) if isinstance(s, URIRef)
    }

    children = defaultdict(list)
    roots = []
    for concept in concepts:
        parents = [p for p in graph.objects(concept, SKOS.broader) if p in concepts]
        if parents:
            children[sorted(parents, key=str)[0]].append(concept)
        else:
            roots.append(concept)

    ordered = []
    seen = set()

    def visit(node):
        if node in seen:
            return
        seen.add(node)
        ordered.append(node)
        for child in sorted(children.get(node, []), key=str):
            visit(child)

    for root in sorted(roots, key=str):
        visit(root)
    for concept in sorted(concepts, key=str):
        visit(concept)
    return ordered


def build_substance_property(graph, report):
    """
    A substance in Brick is *what is observed*, not what something is made
    of -- brick:Substance is rdfs:subClassOf sosa:FeatureOfInterest. It must
    therefore never become ClassType Material or a HasMaterial relation,
    both of which mean composition.

    The RDF rules that out independently: substances are instances of
    brick:Substance organised by skos:broader, not classes, so they cannot be
    emitted as classes at all. They become the enumerated values of a single
    Substance property instead.
    """
    concepts = substance_concepts(graph)
    allowed = []
    for index, concept in enumerate(concepts, start=1):
        value = {
            "Code": code_for(concept),
            "Value": label_for(graph, concept),
            "SortNumber": index,
        }
        definition = definition_for(graph, concept)
        if definition:
            value["Description"] = definition
        allowed.append(value)

    report["substance_values"] = len(allowed)
    return {
        "Code": "Substance",
        "Name": "Substance",
        "Definition": (
            "The substance that the entity observes, measures, controls or "
            "conveys, such as the air whose temperature a sensor reports."
        ),
        "DataType": "String",
        "PropertyValueKind": "Single",
        "AllowedValues": allowed,
    }


def attach_class_properties(graph, classes, aliases, report):
    """
    Link classes to properties through bSDD ClassProperty objects.

    Three sources: brick:hasQuantity (what a Point measures),
    brick:hasSubstance (what it observes) and SHACL property shapes that
    attach an entity property to a class.

    References go through `aliases` so a class pointing at a property whose
    code was merged away still resolves to the surviving code.
    """
    by_code = {entry["Code"]: entry for entry in classes}
    entity_properties = set(graph.subjects(RDF.type, BRICK.EntityProperty))
    attached = Counter()

    def add(class_code, class_property):
        entry = by_code.get(class_code)
        if entry is None:
            return False
        entry.setdefault("ClassProperties", []).append(class_property)
        return True

    for subject, quantity in sorted(
        graph.subject_objects(BRICK.hasQuantity), key=lambda x: (str(x[0]), str(x[1]))
    ):
        if not isinstance(quantity, URIRef):
            continue
        property_code = aliases.get(code_for(quantity))
        if property_code is None:
            continue
        if add(
            code_for(subject),
            {
                "Code": f"{code_for(subject)}-{property_code}",
                "PropertyCode": property_code,
                "PropertySet": PSET_QUANTITY,
            },
        ):
            attached["quantity"] += 1

    for subject, substance in sorted(
        graph.subject_objects(BRICK.hasSubstance), key=lambda x: (str(x[0]), str(x[1]))
    ):
        if not isinstance(substance, URIRef):
            continue
        substance_code = aliases.get("Substance")
        if substance_code is None:
            continue
        if add(
            code_for(subject),
            {
                "Code": f"{code_for(subject)}-Substance",
                "PropertyCode": substance_code,
                "PropertySet": PSET_SUBSTANCE,
                "PredefinedValue": code_for(substance),
            },
        ):
            attached["substance"] += 1

    for owner, pshape in sorted(
        graph.subject_objects(SH.property), key=lambda x: (str(x[0]), str(x[1]))
    ):
        if not isinstance(owner, URIRef):
            continue
        for path in graph.objects(pshape, SH.path):
            if path not in entity_properties:
                continue
            property_code = aliases.get(code_for(path))
            if property_code is None:
                continue
            if add(
                code_for(owner),
                {
                    "Code": f"{code_for(owner)}-{property_code}",
                    "PropertyCode": property_code,
                    "PropertySet": PSET_COMMON,
                },
            ):
                attached["entity_property"] += 1

    report["class_properties"] = dict(attached)


# ---------------------------------------------------------------------------
# assembly and reporting
# ---------------------------------------------------------------------------


def merge_property(winner, loser):
    """
    Fold two descriptions of the same property together.

    The winner keeps its code; any field it lacks is taken from the loser, and
    unit lists are unioned. Only ever called for a genuine duplicate.
    """
    merged = dict(winner)
    for key, value in loser.items():
        if key == "Code":
            continue
        if key == "Units":
            merged["Units"] = sorted(set(merged.get("Units", [])) | set(value))
        elif not merged.get(key):
            merged[key] = value
    return merged


def register_property(properties, aliases, entry, report):
    """
    Add a property, merging case-insensitive code collisions.

    bSDD codes are not case-sensitive, so brick:volume (an entity property,
    "entity has 3-dimensional volume") and the Volume quantity collide even
    though both name the same physical property with the same dimension.
    Merging keeps one coherent property instead of mangling either code.

    Registration order decides which code survives: quantities are registered
    first, so the Title Case quantity name wins, which also matches bSDD's
    naming guidance (GEN-05).
    """
    key = entry["Code"].lower()
    existing = properties.get(key)
    if existing is None:
        properties[key] = entry
        aliases[entry["Code"]] = entry["Code"]
        return

    merged = merge_property(existing, entry)
    properties[key] = merged
    aliases[existing["Code"]] = merged["Code"]
    aliases[entry["Code"]] = merged["Code"]
    report["merged_properties"].append((existing["Code"], entry["Code"]))


def new_report():
    return {
        "merged_properties": [],
        "classes_without_definition": [],
        "properties_without_definition": [],
        "missing_ifc": [],
        "ifc_inherited": [],
        "ifc_conflicts": [],
        "unknown_ifc_entities": [],
        "missing_dimensions": [],
        "conflicting_dimensions": [],
        "declared_dimension_mismatch": [],
        "dropped_units": [],
        "unmapped_units": set(),
        "multi_parent": [],
        "roots_from_excluded_parents": [],
        "invalid_codes": [],
        "complex_properties": [],
        "unconstrained_properties": [],
        "substance_values": 0,
        "class_properties": {},
    }


def build_dictionary(graph, args, report):
    unit_map = load_unit_map()
    ifc_map = load_ifc_map(report=report)

    selected = select_classes(graph, args.include_deprecated)

    ifc_map = propagate_ifc_map(graph, selected, ifc_map, report)
    classes = build_classes(graph, selected, args.uri_style, ifc_map, report)

    # Quantities register first so their Title Case codes survive a collision
    # with a same-named entity property -- see register_property.
    properties = {}
    aliases = {}
    for entry in build_quantity_properties(graph, unit_map, report).values():
        register_property(properties, aliases, entry, report)
    for entry in build_entity_properties(graph, unit_map, report).values():
        register_property(properties, aliases, entry, report)
    register_property(
        properties, aliases, build_substance_property(graph, report), report
    )

    # UseOwnUri requires an OwnedUri on every property. Assign these after
    # registration because case-insensitive collisions may have merged source
    # terms into a single exported property with a different surviving code.
    for entry in properties.values():
        entry["OwnedUri"] = property_owned_uri(entry["Code"], args.uri_style)

    attach_class_properties(graph, classes, aliases, report)

    report["counts"] = {
        "brick_classes": len(selected),
        "classes": len(classes),
        "properties": len(properties),
    }

    # The import closure also contains modification dates for QUDT and REC.
    # Only Brick's ontology metadata describes this dictionary release.
    brick_ontology = URIRef(VERSIONED_NAMESPACE)
    modified = list(graph.objects(brick_ontology, DCTERMS.modified))

    document = {
        "ModelVersion": "2.0",
        "OrganizationCode": args.organization_code,
        "DictionaryCode": DICTIONARY_CODE,
        "DictionaryName": DICTIONARY_NAME,
        "DictionaryVersion": BRICK_FULL_VERSION,
        "LanguageIsoCode": LANGUAGE_ISO_CODE,
        "LanguageOnly": False,
        "UseOwnUri": True,
        "DictionaryUri": dictionary_uri(args.uri_style),
        "License": "BSD-3-Clause",
        "LicenseUrl": "https://github.com/BrickSchema/Brick/blob/master/LICENSE",
        "ChangeRequestEmailAddress": CHANGE_REQUEST_EMAIL,
        "MoreInfoUrl": MORE_INFO_URL,
        "QualityAssuranceProcedure": QA_PROCEDURE,
        "QualityAssuranceProcedureUrl": QA_PROCEDURE_URL,
        # Always Preview. Activation is irreversible -- activated content gets
        # an immutable URI and can never be deleted -- so it stays a
        # deliberate manual step in the management portal.
        "Status": "Preview",
        "Classes": classes,
        "Properties": sorted(properties.values(), key=lambda p: p["Code"]),
    }
    if modified:
        document["ReleaseDate"] = str(modified[0])
    return document


def ifc_report_lines(report):
    """The report's IFC sections: what inheritance reached, and what is wrong
    with the curated rows."""
    lines = []

    if report["ifc_inherited"]:
        reach = Counter(origin for _, origin, _ in report["ifc_inherited"])
        entities_for = {origin: ents for _, origin, ents in report["ifc_inherited"]}
        lines += [
            "",
            "## IFC mappings reached by inheritance",
            "",
            "`mappings/ifc.csv` curates an entity for a class; its subclasses and",
            "equivalents inherit it, since every Brick fan is also an IfcFan. A",
            "subclass with its own row overrides the inherited one. Each curated",
            "row below is followed by the number of classes it reaches.",
            "",
        ]
        for origin, total in sorted(reach.items(), key=lambda kv: (-kv[1], kv[0])):
            entities = ", ".join(entities_for[origin])
            plural = "class" if total == 1 else "classes"
            lines.append(f"- `{origin}` ({entities}) -> {total} {plural}")

    if report["unknown_ifc_entities"]:
        lines += [
            "",
            "## Curated IFC entity names absent from IFC 4.3",
            "",
            "These appear in `mappings/ifc.csv` but not in buildingSMART's own",
            "IFC dictionary, so they will not resolve. Fix the row, or refresh",
            "`reference/ifc-4.3-classes.csv` if IFC has moved on.",
            "",
        ]
        for code, entity in sorted(report["unknown_ifc_entities"]):
            lines.append(f"- `{code}` -> `{entity}`")

    if report["ifc_conflicts"]:
        lines += [
            "",
            "## Classes inheriting conflicting IFC entities",
            "",
            "These reach more than one IFC entity through different parents. The",
            "entity from the deepest origin is kept; the others are dropped.",
            "",
        ]
        for code, origins in sorted(report["ifc_conflicts"]):
            lines.append(f"- `{code}`: {', '.join(f'`{o}`' for o in origins)}")

    return lines


def write_report(path, report, args):
    counts = report["counts"]
    lines = [
        "# Brick to bSDD export report",
        "",
        f"Brick version {BRICK_FULL_VERSION}, URI style `{args.uri_style}`, "
        f"deprecated terms {'included' if args.include_deprecated else 'excluded'}.",
        "",
        "## Counts",
        "",
        f"- Brick classes: {counts['brick_classes']}",
        f"- Classes emitted: {counts['classes']}",
        f"- Properties emitted: {counts['properties']}",
        f"- Substance allowed values: {report['substance_values']}",
    ]
    for kind, total in sorted(report["class_properties"].items()):
        lines.append(f"- Class properties from {kind}: {total}")

    lines += [
        "",
        "## Verification gaps",
        "",
        f"- Classes without a definition (GEN-01): "
        f"{len(report['classes_without_definition'])}",
        f"- Properties without a definition (GEN-01): "
        f"{len(report['properties_without_definition'])}",
        f"- Classes without an IFC mapping (CLS-01): {len(report['missing_ifc'])}",
        f"- Classes whose IFC mapping is inherited, not curated: "
        f"{len(report['ifc_inherited'])}",
        f"- Classes inheriting conflicting IFC entities: "
        f"{len(report['ifc_conflicts'])}",
        f"- Curated IFC entity names absent from IFC 4.3: "
        f"{len(report['unknown_ifc_entities'])}",
        f"- Properties whose units disagree on dimension (PRP-01): "
        f"{len(report['conflicting_dimensions'])}",
        f"- Properties whose declared dimension contradicts their units: "
        f"{len(report['declared_dimension_mismatch'])}",
        f"- Properties with units dropped to keep dimension consistent: "
        f"{len(report['dropped_units'])}",
        f"- QUDT units with no bSDD equivalent: {len(report['unmapped_units'])}",
        f"- Multiply-inherited classes resolved to one parent: "
        f"{len(report['multi_parent'])}",
        f"- Properties emitted as Complex: {len(report['complex_properties'])}",
        f"- Properties whose value shape carries no constraints: "
        f"{len(report['unconstrained_properties'])}",
        f"- Codes rejected as invalid: {len(report['invalid_codes'])}",
        f"- Properties merged on a case-insensitive code clash: "
        f"{len(report['merged_properties'])}",
    ]

    if report["merged_properties"]:
        lines += [
            "",
            "## Properties merged",
            "",
            "bSDD codes are not case-sensitive, so these Brick terms would",
            "collide. They name the same property, so they are merged into one",
            "entry and every reference is redirected to the surviving code.",
            "",
        ]
        for kept, folded in sorted(report["merged_properties"]):
            lines.append(f"- `{folded}` folded into `{kept}`")

    lines += ifc_report_lines(report)

    lines += [
        "",
        "## Relationships intentionally not exported",
        "",
        "bSDD's ClassRelation vocabulary is closed. Brick relationships with no",
        "bSDD equivalent -- `feeds`, `hasPoint`, `hasLocation`, `controls`,",
        "`isMeteredBy` and the rest -- are dropped rather than forced into",
        "`HasReference`, which REL-03 reserves for genuinely referential links.",
        "",
        "`HasMaterial` is never emitted. Nothing in Brick describes what an",
        "entity is made of; `hasSubstance`, the one predicate that resembles it,",
        "means the opposite and becomes the Substance property instead.",
    ]

    if report["unmapped_units"]:
        lines += [
            "",
            "## QUDT units missing from bSDD",
            "",
            "File these at https://github.com/buildingSMART/bSDD/issues to have",
            "them added, then re-run with `--refresh-units`.",
            "",
        ]
        lines += [f"- `{iri}`" for iri in sorted(report["unmapped_units"])]

    if report["unconstrained_properties"]:
        lines += [
            "",
            "## Properties with unconstrained value shapes",
            "",
            "These reference a `BSH.<Quantity>QuantityShape` that Brick never",
            "generates, because no `brick:Quantity` exists under that name.",
            "They fall back to a bare String with no units or dimension.",
            "",
        ]
        lines += [f"- `{code}`" for code in sorted(report["unconstrained_properties"])]

    if report["conflicting_dimensions"] or report["declared_dimension_mismatch"]:
        lines += [
            "",
            "## Dimension inconsistencies in the source ontology",
            "",
            "bSDD verifies that every unit on a property matches that property's",
            "dimension (PRP-01), so the export forces the two to agree: the most",
            "common unit dimension wins and units that disagree are dropped.",
            "Each entry below is a defect in Brick worth an upstream issue.",
            "",
        ]
        for code, dimensions, chosen in sorted(report["conflicting_dimensions"]):
            others = [d for d in dimensions if d != chosen]
            lines.append(
                f"- `{code}`: units span {', '.join(f'`{d}`' for d in dimensions)} "
                f"— kept `{chosen}`, dropped units of "
                f"{', '.join(f'`{d}`' for d in others)}"
            )
        for code, declared, chosen in sorted(report["declared_dimension_mismatch"]):
            lines.append(
                f"- `{code}`: declares `{declared}` but its units are "
                f"`{chosen}` — the units win"
            )

    if report["dropped_units"]:
        lines += ["", "## Units dropped", ""]
        for code, dropped in sorted(report["dropped_units"]):
            lines.append(f"- `{code}`: {', '.join(f'`{u}`' for u in dropped)}")

    if report["multi_parent"]:
        lines += [
            "",
            "## Multiple inheritance resolved",
            "",
            "bSDD allows one `ParentClassCode`. The deepest parent stays in the",
            "tree; the rest become `IsChildOf` relations, so no edge is lost.",
            "",
            "| Class | Primary parent | Also a child of |",
            "|---|---|---|",
        ]
        for code, primary, extra in sorted(report["multi_parent"]):
            lines.append(
                f"| `{code}` | `{primary}` | {', '.join(f'`{e}`' for e in extra)} |"
            )

    if report["roots_from_excluded_parents"]:
        lines += [
            "",
            "## Classes emitted as roots because their parents are not published",
            "",
            "Every named superclass of these classes lies outside the Brick",
            "namespace -- almost always a RealEstateCore location term, which",
            "this dictionary does not republish. They keep their own subtree,",
            "but hang at the top level rather than under the parent Brick",
            "declares for them.",
            "",
            "| Class | Superclass in Brick, not in the dictionary |",
            "|---|---|",
        ]
        for code, outside in sorted(report["roots_from_excluded_parents"]):
            lines.append(f"| `{code}` | {', '.join(f'`{p}`' for p in outside)} |")

    if report["invalid_codes"]:
        lines += ["", "## Rejected codes", ""]
        lines += [f"- `{code}`: {why}" for code, why in sorted(report["invalid_codes"])]

    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Generate a bSDD import file from the Brick ontology."
    )
    parser.add_argument(
        "--source",
        default=str(DEFAULT_SOURCE),
        help="Ontology to read. Must be Brick+imports.ttl or equivalent: "
        "the QUDT quantity kinds and units that Points reference are only "
        "described in the import closure.",
    )
    parser.add_argument(
        "--output",
        default="bsdd/brick-bsdd.json",
        help="Path of the JSON import file to write.",
    )
    parser.add_argument(
        "--report",
        default=None,
        help="Path of the Markdown report (defaults to report.md beside --output).",
    )
    parser.add_argument(
        "--uri-style",
        choices=["canonical", "versioned"],
        default="canonical",
        help="Whether OwnedUri values carry the Brick version.",
    )
    parser.add_argument(
        "--organization-code",
        default=ORGANIZATION_CODE,
        help="bSDD organisation code. Use the DEMO organisation for test uploads "
        "until Brick's own code is registered.",
    )
    parser.add_argument(
        "--include-deprecated",
        action="store_true",
        help="Also export deprecated terms, with their mitigation messages.",
    )
    parser.add_argument(
        "--refresh-units",
        action="store_true",
        help="Rebuild mappings/units.csv from the bSDD unit API, then exit.",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    source = Path(args.source)
    if not source.exists():
        parser_hint = "Run `make Brick.ttl` first."
        sys.exit(f"Source ontology not found: {source}. {parser_hint}")

    print(f"Reading {source} ...")
    graph = load_graph(source)
    print(f"  {len(graph)} triples")

    if args.refresh_units:
        refresh_unit_map(graph)
        return 0

    report = new_report()
    document = build_dictionary(graph, args, report)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    report_path = Path(args.report) if args.report else output.parent / "report.md"
    write_report(report_path, report, args)

    counts = report["counts"]
    print(
        f"Wrote {output}: {counts['classes']} classes, "
        f"{counts['properties']} properties"
    )
    print(f"Wrote {report_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
