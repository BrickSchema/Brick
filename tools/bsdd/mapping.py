"""Direct Brick-to-bSDD transformations.

Each public function corresponds to one output collection: Classes,
Properties, or ClassProperties.
"""

import csv
from pathlib import Path

from rdflib import URIRef

from bricksrc.namespaces import BRICK, OWL, QUDT, RDF, RDFS, SH

from brick_graph import (
    XSD_TO_BSDD_DATATYPE,
    allowed_values,
    definition_for,
    label_for,
    local_name,
    quantity_for_shape,
    require_code,
    shape_constraints,
    units_and_dimension,
    value_shape_for,
)

DICTIONARY_URI = "https://brickschema.org/schema/Brick"
PSET_QUANTITY = "cPSET_BrickQuantity"
PSET_SUBSTANCE = "cPSET_BrickSubstance"
PSET_COMMON = "cPSET_BrickCommon"
IFC_CSV = Path(__file__).resolve().parent / "mappings" / "ifc.csv"


def class_uri(code):
    return f"{DICTIONARY_URI}#{code}"


def property_uri(code):
    return f"{DICTIONARY_URI}#property/{code}"


def entity_property_code(term):
    """Keep relationship-style EntityProperties distinct from physical quantities."""
    code = local_name(term)
    return f"entityProperty{code[:1].upper()}{code[1:]}"


def selected_classes(graph):
    """Brick-owned, non-deprecated classes; imports are not republished."""
    classes = set(graph.subjects(RDF.type, OWL.Class)) | set(
        graph.subjects(RDF.type, RDFS.Class)
    )
    return {
        term
        for term in classes
        if str(term).startswith(str(BRICK))
        and (term, OWL.deprecated, None) not in graph
    }


def load_ifc_map(path=IFC_CSV):
    """Read explicit Brick-class to IFC-entity mappings from the static CSV."""
    with open(path, newline="", encoding="utf-8") as handle:
        return {
            row["code"]: [entity for entity in row["ifc_entities"].split(";") if entity]
            for row in csv.DictReader(handle)
            if row["ifc_entities"]
        }


def named_parents(graph, term, selected):
    return sorted(
        {
            parent
            for parent in graph.objects(term, RDFS.subClassOf)
            if parent != term and parent in selected
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


def export_classes(graph, ifc_map):
    """Brick classes -> bSDD Classes, retaining multiple inheritance as relations."""
    selected, memo, classes = selected_classes(graph), {}, []
    for term in sorted(selected, key=str):
        code = require_code(local_name(term), term)
        entry = {
            "Code": code,
            "Name": label_for(graph, term),
            "ClassType": "Class",
            "OwnedUri": class_uri(code),
        }
        if definition := definition_for(graph, term):
            entry["Definition"] = definition
        if entities := ifc_map.get(code):
            entry["RelatedIfcEntityNamesList"] = entities
        parents = named_parents(graph, term, selected)
        if parents:
            # bSDD permits one tree parent; the other Brick parents remain edges.
            primary = max(
                parents,
                key=lambda parent: (depth(graph, parent, selected, memo), str(parent)),
            )
            entry["ParentClassCode"] = local_name(primary)
            if extra := [parent for parent in parents if parent != primary]:
                entry["ClassRelations"] = [
                    {
                        "RelationType": "IsChildOf",
                        "RelatedClassUri": class_uri(local_name(parent)),
                        "RelatedClassName": label_for(graph, parent),
                    }
                    for parent in extra
                ]
        equivalents = [
            other
            for other in graph.objects(term, OWL.equivalentClass)
            if other in selected and other != term
        ]
        if equivalents:
            entry.setdefault("ClassRelations", []).extend(
                {
                    "RelationType": "IsEqualTo",
                    "RelatedClassUri": class_uri(local_name(other)),
                    "RelatedClassName": label_for(graph, other),
                }
                for other in sorted(equivalents, key=str)
            )
            entry["Synonyms"] = sorted(
                {label_for(graph, other) for other in equivalents}
            )
        classes.append(entry)
    return classes


def scalar_property(
    graph, code, name, definition, constraint, quantity, unit_iris, unit_map
):
    """One Brick quantity or SHACL scalar field -> one bSDD Property."""
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
    """Brick EntityProperties -> namespaced scalar or Complex bSDD Properties."""
    properties = []
    for term in sorted(graph.subjects(RDF.type, BRICK.EntityProperty), key=str):
        code = require_code(entity_property_code(term), term)
        shape = value_shape_for(graph, term)
        fields, quantity = shape_constraints(graph, shape), quantity_for_shape(
            graph, shape
        )
        units = [str(unit) for unit in fields.get("hasUnit", {}).get("in", [])]
        if not units and quantity:
            units = [str(unit) for unit in graph.objects(quantity, QUDT.applicableUnit)]
        fields = {key: value for key, value in fields.items() if key != "hasUnit"}
        definition = definition_for(graph, term)
        if len(fields) <= 1:
            entry = scalar_property(
                graph,
                code,
                label_for(graph, term),
                definition,
                fields.get("value", {}),
                quantity,
                units,
                unit_map,
            )
            entry["_source"] = str(term)
            properties.append(entry)
            continue
        # Complex children are namespaced, so `value` has no global meaning.
        child_codes = []
        for field, constraint in sorted(fields.items()):
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
            "_source": str(term),
        }
        if definition:
            entry["Definition"] = definition
        properties.append(entry)
    return properties


def export_quantities(graph, unit_map):
    """Quantity kinds -> numeric Properties, using Brick's QUDT alignments."""
    def canonical_quantity(quantity):
        references = list(graph.objects(quantity, BRICK.hasQUDTReference))
        return references[0] if references else quantity

    terms = {
        canonical_quantity(quantity)
        for quantity in graph.objects(None, BRICK.hasQuantity)
        if isinstance(quantity, URIRef)
    }
    for quantity in graph.subjects(RDF.type, BRICK.Quantity):
        # A Brick quantity aligned with QUDT is exported under the QUDT code,
        # keeping one bSDD property per quantity concept.
        terms.add(canonical_quantity(quantity))
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
    """Brick Substance instances -> one enumerated observation property."""
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
    """Assign owned URIs, rejecting collisions instead of merging concepts."""
    grouped = {}
    for property_ in properties:
        grouped.setdefault(property_["Code"].lower(), []).append(property_)
    collisions = {key: entries for key, entries in grouped.items() if len(entries) > 1}
    if collisions:
        details = "; ".join(
            f"{key!r}: {', '.join(entry['_source'] for entry in entries)}"
            for key, entries in sorted(collisions.items())
        )
        raise ValueError(
            f"Case-insensitive bSDD property-code collision(s): {details}. "
            "Add an explicit mapping before exporting."
        )
    properties = {key: entries[0] for key, entries in grouped.items()}
    for property_ in properties.values():
        property_["OwnedUri"] = property_uri(property_["Code"])
        property_.pop("_source")
    return properties


def attach_class_properties(graph, classes, properties):
    """Brick hasQuantity, hasSubstance, and property shapes -> ClassProperties."""
    classes = {entry["Code"]: entry for entry in classes}
    entity_properties = set(graph.subjects(RDF.type, BRICK.EntityProperty))

    def add(class_code, property_code, property_set, **extra):
        if class_code in classes and property_code.lower() in properties:
            property_code = properties[property_code.lower()]["Code"]
            classes[class_code].setdefault("ClassProperties", []).append(
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
                    add(local_name(owner), entity_property_code(path), PSET_COMMON)
