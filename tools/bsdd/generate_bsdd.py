#!/usr/bin/env python3
"""Export the Brick ontology as one bSDD import document.

The mapping is intentionally direct: Brick classes become bSDD classes;
quantities and EntityProperties become bSDD properties; and Brick assertions
link them through ClassProperties. The exporter has no IFC alignment or
network dependency.
"""

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

from rdflib import Graph, Namespace, RDF, RDFS, OWL, URIRef
from rdflib.collection import Collection
from rdflib.namespace import SKOS, XSD

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(REPO_ROOT))
from bricksrc.version import BRICK_FULL_VERSION  # noqa: E402

BRICK = Namespace("https://brickschema.org/schema/Brick#")
QUDT = Namespace("http://qudt.org/schema/qudt/")
QUDTQK = Namespace("http://qudt.org/vocab/quantitykind/")
SH = Namespace("http://www.w3.org/ns/shacl#")
DCTERMS = Namespace("http://purl.org/dc/terms/")

DEFAULT_SOURCE = REPO_ROOT / "Brick+imports.ttl"
UNITS_CSV = Path(__file__).resolve().parent / "mappings" / "units.csv"
ORGANIZATION_CODE, DICTIONARY_CODE, DICTIONARY_NAME = "brick", "brick", "Brick Schema"
DICTIONARY_URI = "https://brickschema.org/schema/Brick"
PSET_QUANTITY, PSET_SUBSTANCE, PSET_COMMON = (
    "cPSET_BrickQuantity",
    "cPSET_BrickSubstance",
    "cPSET_BrickCommon",
)
ILLEGAL_CODE_CHARS, MAX_CODE_LENGTH = set('"#%/\\\\:`{}[]|;<>?~'), 100
DIMENSION_RE = re.compile(r"([AELIMHTD])(-?[0-9.]+)")
BSDD_DIMENSION_ORDER, DIMENSIONLESS = [
    "L",
    "M",
    "T",
    "E",
    "H",
    "A",
    "I",
], "0 0 0 0 0 0 0"
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


def local_name(term):
    return str(term).rsplit("#", 1)[-1].rsplit("/", 1)[-1]


def load_graph(path):
    graph = Graph()
    graph.parse(str(path), format="turtle")
    return graph


def label_for(graph, term):
    labels = list(graph.objects(term, RDFS.label))
    english = [label for label in labels if label.language == "en"]
    return str((english or labels or [local_name(term).replace("_", " ")])[0])


def definition_for(graph, term):
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


def validate_code(code):
    if not code:
        return "empty code"
    if len(code) > MAX_CODE_LENGTH:
        return f"longer than {MAX_CODE_LENGTH} characters"
    if invalid := sorted(set(code) & ILLEGAL_CODE_CHARS):
        return f"contains forbidden characters: {''.join(invalid)}"
    if code[:3].lower() == "ifc":
        return "uses the reserved Ifc prefix"
    return None


def require_code(code, source):
    if reason := validate_code(code):
        raise ValueError(f"Invalid bSDD code {code!r} for {source}: {reason}")
    return code


def owned_uri(code):
    return f"{DICTIONARY_URI}#{code}"


def property_uri(code):
    return f"{DICTIONARY_URI}#property/{code}"


def selected_classes(graph):
    classes = set(graph.subjects(RDF.type, OWL.Class)) | set(
        graph.subjects(RDF.type, RDFS.Class)
    )
    return {
        term
        for term in classes
        if str(term).startswith(str(BRICK))
        and (term, OWL.deprecated, None) not in graph
    }


def named_parents(graph, term, selected):
    return sorted(
        {
            parent
            for parent in graph.objects(term, RDFS.subClassOf)
            if isinstance(parent, URIRef) and parent != term and parent in selected
        },
        key=str,
    )


def depth(graph, term, selected, memo):
    if term in memo:
        return memo[term]
    memo[term] = 0
    parents = named_parents(graph, term, selected)
    memo[term] = (
        0
        if not parents
        else 1 + max(depth(graph, parent, selected, memo) for parent in parents)
    )
    return memo[term]


def export_classes(graph):
    selected, memo, classes = selected_classes(graph), {}, []
    for term in sorted(selected, key=str):
        code = require_code(local_name(term), term)
        entry = {
            "Code": code,
            "Name": label_for(graph, term),
            "ClassType": "Class",
            "OwnedUri": owned_uri(code),
        }
        if definition := definition_for(graph, term):
            entry["Definition"] = definition
        parents = named_parents(graph, term, selected)
        if parents:
            primary = max(
                parents,
                key=lambda parent: (depth(graph, parent, selected, memo), str(parent)),
            )
            entry["ParentClassCode"] = local_name(primary)
            if extra := [parent for parent in parents if parent != primary]:
                entry["ClassRelations"] = [
                    {
                        "RelationType": "IsChildOf",
                        "RelatedClassUri": owned_uri(local_name(parent)),
                        "RelatedClassName": label_for(graph, parent),
                    }
                    for parent in extra
                ]
        equivalents = [
            term_
            for term_ in graph.objects(term, OWL.equivalentClass)
            if isinstance(term_, URIRef) and term_ in selected and term_ != term
        ]
        if equivalents:
            entry.setdefault("ClassRelations", []).extend(
                {
                    "RelationType": "IsEqualTo",
                    "RelatedClassUri": owned_uri(local_name(term_)),
                    "RelatedClassName": label_for(graph, term_),
                }
                for term_ in sorted(equivalents, key=str)
            )
            entry["Synonyms"] = sorted(
                {label_for(graph, term_) for term_ in equivalents}
            )
        classes.append(entry)
    return classes


def load_unit_map(path=UNITS_CSV):
    with open(path, newline="", encoding="utf-8") as handle:
        return {
            row["qudt_uri"]: row["bsdd_code"]
            for row in csv.DictReader(handle)
            if row["bsdd_code"]
        }


def dimension_vector(graph, term):
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
    for shape in graph.subjects(SH.path, entity_property):
        if node := next(iter(graph.objects(shape, SH.node)), None):
            return node
    return None


def shape_constraints(graph, shape):
    """Flatten inherited SHACL property constraints; local constraints win."""
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
    if shape is None or not (name := local_name(shape)).endswith("QuantityShape"):
        return None
    stem = name.removesuffix("QuantityShape")
    return next(
        (
            candidate
            for candidate in (BRICK[stem], QUDTQK[stem], QUDTQK[stem.replace("_", "")])
            if any(graph.objects(candidate, QUDT.applicableUnit))
        ),
        None,
    )


def allowed_values(values):
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


def scalar_property(
    graph, code, name, definition, constraint, quantity, unit_iris, unit_map
):
    require_code(code, name)
    if "in" in constraint:
        datatype, values = "String", allowed_values(constraint["in"])
    elif constraint.get("numeric"):
        datatype, values = "Real", []
    else:
        datatype, values = (
            XSD_TO_BSDD_DATATYPE.get(constraint.get("datatype"), "String"),
            [],
        )
    entry = {
        "Code": code,
        "Name": name,
        "DataType": datatype,
        "PropertyValueKind": "Single",
    }
    if definition:
        entry["Definition"] = definition
    if values:
        entry["AllowedValues"] = values
    if datatype in {"Real", "Integer"}:
        dimension, unit_iris = units_and_dimension(graph, quantity, unit_iris)
        entry["Dimension"] = dimension
    if codes := sorted({unit_map[unit] for unit in unit_iris if unit in unit_map}):
        entry["Units"] = codes
    for bound in ("MinInclusive", "MaxInclusive", "MinExclusive", "MaxExclusive"):
        if (key := bound[0].lower() + bound[1:]) in constraint:
            entry[bound] = constraint[key]
    return entry


def export_entity_properties(graph, unit_map):
    properties = []
    for term in sorted(graph.subjects(RDF.type, BRICK.EntityProperty), key=str):
        code, shape = require_code(local_name(term), term), value_shape_for(graph, term)
        fields, quantity = shape_constraints(graph, shape), quantity_for_shape(
            graph, shape
        )
        units = [str(unit) for unit in fields.get("hasUnit", {}).get("in", [])]
        if not units and quantity:
            units = [str(unit) for unit in graph.objects(quantity, QUDT.applicableUnit)]
        value_fields, definition = {
            key: value for key, value in fields.items() if key != "hasUnit"
        }, definition_for(graph, term)
        if len(value_fields) <= 1:
            entry = scalar_property(
                graph,
                code,
                label_for(graph, term),
                definition,
                value_fields.get("value", {}),
                quantity,
                units,
                unit_map,
            )
            entry["_source"] = str(term)
            properties.append(entry)
            continue
        child_codes = []
        for field, constraint in sorted(value_fields.items()):
            child_code = require_code(f"{code}.{field}", f"{term} / {field}")
            child_codes.append(child_code)
            entry = scalar_property(
                graph,
                child_code,
                field.replace("_", " "),
                None,
                constraint,
                quantity,
                units,
                unit_map,
            )
            entry["_source"] = f"{term} / {field}"
            properties.append(entry)
        entry = {
            "Code": code,
            "Name": label_for(graph, term),
            "DataType": "String",
            "PropertyValueKind": "Complex",
            "ConnectedPropertyCodes": child_codes,
        }
        if definition:
            entry["Definition"] = definition
        entry["_source"] = str(term)
        properties.append(entry)
    return properties


def export_quantities(graph, unit_map):
    terms = set(graph.subjects(RDF.type, BRICK.Quantity)) | {
        quantity
        for quantity in graph.objects(None, BRICK.hasQuantity)
        if isinstance(quantity, URIRef)
    }
    properties = []
    for term in sorted(terms, key=str):
        entry = scalar_property(
            graph,
            require_code(local_name(term), term),
            label_for(graph, term),
            definition_for(graph, term),
            {"numeric": True},
            term,
            [str(unit) for unit in graph.objects(term, QUDT.applicableUnit)],
            unit_map,
        )
        entry["_source"] = str(term)
        properties.append(entry)
    return properties


def export_substance_property(graph):
    concepts = sorted(
        {
            term
            for term in graph.subjects(RDF.type, BRICK.Substance)
            if isinstance(term, URIRef)
        },
        key=str,
    )
    return {
        "Code": "Substance",
        "Name": "Substance",
        "DataType": "String",
        "PropertyValueKind": "Single",
        "Definition": "The substance that the entity observes, measures, controls or conveys.",
        "AllowedValues": [
            {
                "Code": local_name(term),
                "Value": label_for(graph, term),
                "SortNumber": index,
            }
            for index, term in enumerate(concepts, 1)
        ],
        "_source": "generated Brick substance vocabulary",
    }


def unique_properties(properties):
    by_code = {}
    for property_ in properties:
        key = property_["Code"].lower()
        by_code.setdefault(key, []).append(property_)
    collisions = {
        key: entries for key, entries in by_code.items() if len(entries) > 1
    }
    if collisions:
        details = "; ".join(
            f"{key!r}: {', '.join(entry['_source'] for entry in entries)}"
            for key, entries in sorted(collisions.items())
        )
        raise ValueError(
            "Case-insensitive bSDD property-code collision(s): "
            f"{details}. Add an explicit mapping before exporting."
        )
    by_code = {key: entries[0] for key, entries in by_code.items()}
    for property_ in by_code.values():
        property_["OwnedUri"] = property_uri(property_["Code"])
        property_.pop("_source")
    return by_code


def attach_class_properties(graph, classes, property_codes):
    by_code = {class_["Code"]: class_ for class_ in classes}
    entity_properties = set(graph.subjects(RDF.type, BRICK.EntityProperty))

    def add(class_code, property_code, property_set, **extra):
        if class_code in by_code and property_code.lower() in property_codes:
            property_code = property_codes[property_code.lower()]["Code"]
            by_code[class_code].setdefault("ClassProperties", []).append(
                {
                    "Code": f"{class_code}-{property_code}",
                    "PropertyCode": property_code,
                    "PropertySet": property_set,
                    **extra,
                }
            )

    for subject, quantity in graph.subject_objects(BRICK.hasQuantity):
        if isinstance(quantity, URIRef):
            add(local_name(subject), local_name(quantity), PSET_QUANTITY)
    for subject, substance in graph.subject_objects(BRICK.hasSubstance):
        if isinstance(substance, URIRef):
            add(
                local_name(subject),
                "Substance",
                PSET_SUBSTANCE,
                PredefinedValue=local_name(substance),
            )
    for owner, shape in graph.subject_objects(SH.property):
        if isinstance(owner, URIRef):
            for path in graph.objects(shape, SH.path):
                if path in entity_properties:
                    add(local_name(owner), local_name(path), PSET_COMMON)


def build_dictionary(graph):
    classes, unit_map = export_classes(graph), load_unit_map()
    properties = unique_properties(
        export_quantities(graph, unit_map)
        + export_entity_properties(graph, unit_map)
        + [export_substance_property(graph)]
    )
    attach_class_properties(graph, classes, properties)
    document = {
        "ModelVersion": "2.0",
        "OrganizationCode": ORGANIZATION_CODE,
        "DictionaryCode": DICTIONARY_CODE,
        "DictionaryName": DICTIONARY_NAME,
        "DictionaryVersion": BRICK_FULL_VERSION,
        "LanguageIsoCode": "en-GB",
        "LanguageOnly": False,
        "UseOwnUri": True,
        "DictionaryUri": DICTIONARY_URI,
        "License": "BSD-3-Clause",
        "LicenseUrl": "https://github.com/BrickSchema/Brick/blob/master/LICENSE",
        "ChangeRequestEmailAddress": "info@brickschema.org",
        "MoreInfoUrl": "https://brickschema.org",
        "QualityAssuranceProcedure": "Brick Consortium open review process",
        "QualityAssuranceProcedureUrl": "https://github.com/BrickSchema/Brick/blob/master/CONTRIBUTING.md",
        "Status": "Preview",
        "Classes": classes,
        "Properties": sorted(properties.values(), key=lambda entry: entry["Code"]),
    }
    ontology = URIRef("https://brickschema.org/schema/1.5/Brick")
    if modified := next(iter(graph.objects(ontology, DCTERMS.modified)), None):
        document["ReleaseDate"] = str(modified)
    return document


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Export Brick as a bSDD dictionary.")
    parser.add_argument("--source", default=str(DEFAULT_SOURCE))
    parser.add_argument("--output", default="bsdd/brick-bsdd.json")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    source = Path(args.source)
    if not source.exists():
        raise SystemExit(
            f"Source ontology not found: {source}. Run `make Brick.ttl` first."
        )
    document, output = build_dictionary(load_graph(source)), Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(
        f"Wrote {output}: {len(document['Classes'])} classes, {len(document['Properties'])} properties"
    )


if __name__ == "__main__":
    main()
