"""Read the Brick graph in the forms needed by bSDD mappings.

This module deliberately works from the built ontology rather than individual
``bricksrc`` inputs: it needs both generated Brick shapes and imported QUDT
quantity metadata.
"""

import csv
import hashlib
import re
from collections import Counter
from pathlib import Path

from rdflib import Graph, URIRef
from rdflib.collection import Collection

from bricksrc.namespaces import (
    BRICK,
    DCTERMS,
    OWL,
    QUDT,
    QUDTQK,
    RDF,
    RDFS,
    SH,
    SKOS,
    XSD,
)

UNITS_CSV = Path(__file__).resolve().parent / "mappings" / "units.csv"
ILLEGAL_CODE_CHARS, MAX_CODE_LENGTH = set('"#%/\\\\:`{}[]|;<>?~'), 100
DIMENSION_RE = re.compile(r"([AELIMHTD])(-?[0-9.]+)")
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


def load_graph(path):
    graph = Graph()
    graph.parse(str(path), format="turtle")
    return graph


def local_name(term):
    """Return the final fragment or path component used as a bSDD code."""
    return str(term).rsplit("#", 1)[-1].rsplit("/", 1)[-1]


def label_for(graph, term):
    """Prefer English labels and retain a readable deterministic fallback."""
    labels = list(graph.objects(term, RDFS.label))
    english = [label for label in labels if label.language == "en"]
    return str((english or labels or [local_name(term).replace("_", " ")])[0])


def definition_for(graph, term):
    """Brick definitions are SKOS first, with rdfs:comment as a fallback."""
    for predicate in (SKOS.definition, RDFS.comment):
        values = list(graph.objects(term, predicate))
        if values:
            english = [value for value in values if value.language == "en"]
            return str((english or values)[0]).strip()
    return None


def rdf_list(graph, node):
    try:
        return list(Collection(graph, node))
    except Exception:
        return []


def require_code(code, source):
    """Fail at the source when a Brick name cannot be a bSDD code."""
    if not code:
        reason = "empty code"
    elif len(code) > MAX_CODE_LENGTH:
        reason = f"longer than {MAX_CODE_LENGTH} characters"
    elif invalid := sorted(set(code) & ILLEGAL_CODE_CHARS):
        reason = f"contains forbidden characters: {''.join(invalid)}"
    elif code[:3].lower() == "ifc":
        reason = "uses the reserved Ifc prefix"
    else:
        return code
    raise ValueError(f"Invalid bSDD code {code!r} for {source}: {reason}")


def allowed_values(values):
    """Create valid, stable codes for SHACL enumeration values."""
    used, result = set(), []
    for index, value in enumerate(map(str, values), start=1):
        code = (
            "".join("_" if char in ILLEGAL_CODE_CHARS else char for char in value)
            or "value"
        )
        digest = hashlib.sha256(value.encode()).hexdigest()[:8]
        if len(code) > MAX_CODE_LENGTH or code.lower() in used:
            code = f"{code[:MAX_CODE_LENGTH - 9]}_{digest}"
        used.add(code.lower())
        result.append({"Code": code, "Value": value, "SortNumber": index})
    return result


def load_unit_map(path=UNITS_CSV):
    """Read the checked-in QUDT-to-bSDD unit map; never access the network."""
    with open(path, newline="", encoding="utf-8") as handle:
        return {
            row["qudt_uri"]: row["bsdd_code"]
            for row in csv.DictReader(handle)
            if row["bsdd_code"]
        }


def dimension_vector(graph, term):
    """Convert QUDT's dimension-vector IRI to bSDD's seven exponents."""
    vector = next(iter(graph.objects(term, QUDT.hasDimensionVector)), None)
    if vector is None:
        return None
    exponents = dict(DIMENSION_RE.findall(local_name(vector)))
    if not exponents:
        return None
    values = [float(exponents.get(key, "0")) for key in BSDD_DIMENSION_ORDER]
    return " ".join(
        str(int(value)) if value.is_integer() else str(value) for value in values
    )


def units_and_dimension(graph, quantity, unit_iris):
    """Return bSDD's one dimension and units compatible with it."""
    dimensions = {iri: dimension_vector(graph, URIRef(iri)) for iri in unit_iris}
    dimensions = {iri: dimension for iri, dimension in dimensions.items() if dimension}
    if not dimensions:
        return dimension_vector(graph, quantity) if quantity else DIMENSIONLESS, []
    counts = Counter(dimensions.values())
    dimension = max(counts, key=lambda value: (counts[value], value))
    return dimension, sorted(
        iri for iri, value in dimensions.items() if value == dimension
    )


def value_shape_for(graph, entity_property):
    """Find the SHACL value shape attached to an EntityProperty."""
    for shape in graph.subjects(SH.path, entity_property):
        if node := next(iter(graph.objects(shape, SH.node)), None):
            return node
    return None


def shape_constraints(graph, shape):
    """Flatten inherited SHACL constraints; the local shape wins."""
    chain, seen, frontier = [], set(), [shape] if shape else []
    while frontier:
        node = frontier.pop()
        if node in seen:
            continue
        seen.add(node)
        chain.append(node)
        frontier.extend(graph.objects(node, RDFS.subClassOf))
    fields = {}
    for node in reversed(chain):
        for property_shape in graph.objects(node, SH.property):
            path = next(iter(graph.objects(property_shape, SH.path)), None)
            if path is None:
                continue
            constraint = fields.setdefault(local_name(path), {})
            if datatype := next(iter(graph.objects(property_shape, SH.datatype)), None):
                constraint["datatype"] = datatype
            if enumeration := next(iter(graph.objects(property_shape, SH["in"])), None):
                constraint["in"] = rdf_list(graph, enumeration)
            if any(graph.objects(property_shape, SH["or"])):
                constraint["numeric"] = True
            for bound in (
                "minInclusive",
                "maxInclusive",
                "minExclusive",
                "maxExclusive",
            ):
                if value := next(iter(graph.objects(property_shape, SH[bound])), None):
                    constraint[bound] = str(value)
    return fields


def quantity_for_shape(graph, shape):
    """Resolve the quantity conventionally named by a QuantityShape."""
    if shape is None or not (name := local_name(shape)).endswith("QuantityShape"):
        return None
    stem = name.removesuffix("QuantityShape")
    candidates = (BRICK[stem], QUDTQK[stem], QUDTQK[stem.replace("_", "")])
    return next(
        (
            candidate
            for candidate in candidates
            if any(graph.objects(candidate, QUDT.applicableUnit))
        ),
        None,
    )
