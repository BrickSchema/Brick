from rdflib import Literal
from .namespaces import A, OWL, RDFS, BRICK, VCARD, UNIT, QUDT, SDO, RDF

"""
Defining properties
"""
properties = {
    "hasSubstance": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.label: Literal("Has QUDT reference"),
    },
    "connectsTo": {
        A: [OWL.SymmetricProperty],
        RDFS.label: Literal("connects to"),
    },
    "hasQuantity": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.label: Literal("Has QUDT reference"),
        RDFS.subPropertyOf: QUDT.hasQuantityKind,
    },
    "value": {
        RDFS.subPropertyOf: QUDT.value,
        RDFS.label: Literal("Value"),
        A: [RDF.Property],
    },
    "latitude": {
        RDFS.subPropertyOf: SDO.latitude,
        RDFS.label: Literal("Latitude"),
        A: [OWL.ObjectProperty],
    },
    "longitude": {
        RDFS.subPropertyOf: SDO.longitude,
        RDFS.label: Literal("Longitude"),
        A: [OWL.ObjectProperty],
    },
    "hasQUDTReference": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.label: Literal("Has QUDT reference"),
    },
    "isLocationOf": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasLocation"],
        RDFS.domain: BRICK.Location,
        RDFS.label: Literal("Is location of"),
    },
    "hasLocation": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isLocationOf"],
        RDFS.range: BRICK.Location,
        RDFS.label: Literal("Has location"),
    },
    "hasInputSubstance": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.range: BRICK.Substance,
        RDFS.label: Literal("Has input substance"),
    },
    "hasOutputSubstance": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.range: BRICK.Substance,
        RDFS.label: Literal("Has output substance"),
    },
    "feeds": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.subPropertyOf: BRICK.connectsTo,
        OWL.inverseOf: BRICK["isFedBy"],
        "subproperties": {"feedsAir": {}},
        RDFS.label: Literal("Feeds"),
    },
    "isFedBy": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.subPropertyOf: BRICK.connectsTo,
        OWL.inverseOf: BRICK["feeds"],
        RDFS.label: Literal("Is fed by"),
    },
    "hasPoint": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isPointOf"],
        RDFS.range: BRICK.Point,
        RDFS.label: Literal("Has point"),
    },
    "isPointOf": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasPoint"],
        RDFS.domain: BRICK.Point,
        RDFS.label: Literal("Is point of"),
    },
    "hasPart": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isPartOf"],
        RDFS.label: Literal("Has part"),
    },
    "isPartOf": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasPart"],
        RDFS.label: Literal("Is part of"),
    },
    "hasTag": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isTagOf"],
        RDFS.range: BRICK.Tag,
        RDFS.label: Literal("Has tag"),
    },
    "isTagOf": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.domain: BRICK.Tag,
        RDFS.label: Literal("Is tag of"),
    },
    "regulates": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isRegulatedBy"],
        RDFS.domain: BRICK.Equipment,
        RDFS.range: BRICK.Substance,
        RDFS.label: Literal("Regulates"),
    },
    "isRegulatedBy": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.domain: BRICK.Substance,
        RDFS.range: BRICK.Equipment,
        RDFS.label: Literal("Is regulated by"),
    },
    "hasAssociatedTag": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isAssociatedWith"],
        RDFS.domain: OWL.Class,
        RDFS.range: BRICK.Tag,
        RDFS.label: Literal("Has associated tag"),
    },
    "isAssociatedWith": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasAssociatedTag"],
        RDFS.domain: BRICK.Tag,
        RDFS.range: OWL.Class,
        RDFS.label: Literal("Is associated with"),
    },
    "hasAddress": {
        RDFS.subPropertyOf: VCARD.hasAddress,
        RDFS.domain: BRICK.Building,
        RDFS.range: VCARD.Address,
        RDFS.label: Literal("Has address"),
    },
    "hasUnit": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.range: UNIT.Unit,
        RDFS.label: Literal("Has unit"),
    },
}
