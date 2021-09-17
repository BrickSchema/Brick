from rdflib import Literal
from .namespaces import A, OWL, RDFS, BRICK, VCARD, UNIT, QUDT, XSD, SDO

"""
Defining properties
"""
properties = {
    "value": {RDFS.subPropertyOf: QUDT.value, RDFS.label: Literal("Value")},
    "latitude": {RDFS.subPropertyOf: SDO.latitude, RDFS.label: Literal("Latitude")},
    "longitude": {RDFS.subPropertyOf: SDO.longitude, RDFS.label: Literal("Longitude")},
    "hasQUDTReference": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.label: Literal("Has QUDT reference"),
    },
    "isLocationOf": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasLocation"],
        RDFS.domain: BRICK.Location,
        RDFS.label: Literal("Is location of"),
    },
    "hasLocation": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isLocationOf"],
        RDFS.range: BRICK.Location,
        RDFS.label: Literal("Has location"),
    },
    "hasInputSubstance": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.range: BRICK.Substance,
        RDFS.label: Literal("Has input substance"),
    },
    "hasOutputSubstance": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.range: BRICK.Substance,
        RDFS.label: Literal("Has output substance"),
    },
    "feeds": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isFedBy"],
        "subproperties": {"feedsAir": {}},
        RDFS.label: Literal("Feeds"),
    },
    "isFedBy": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["feeds"],
        RDFS.label: Literal("Is fed by"),
    },
    "hasPoint": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isPointOf"],
        RDFS.range: BRICK.Point,
        RDFS.label: Literal("Has point"),
    },
    "isPointOf": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasPoint"],
        RDFS.domain: BRICK.Point,
        RDFS.label: Literal("Is point of"),
    },
    "hasPart": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isPartOf"],
        RDFS.label: Literal("Has part"),
    },
    "isPartOf": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasPart"],
        RDFS.label: Literal("Is part of"),
    },
    "hasTag": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isTagOf"],
        RDFS.range: BRICK.Tag,
        RDFS.label: Literal("Has tag"),
    },
    "isTagOf": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.domain: BRICK.Tag,
        RDFS.label: Literal("Is tag of"),
    },
    "measures": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isMeasuredBy"],
        RDFS.domain: BRICK.Point,
        RDFS.range: BRICK.Measurable,
        RDFS.label: Literal("Measures"),
    },
    "isMeasuredBy": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.domain: BRICK.Measurable,
        RDFS.range: BRICK.Point,
        RDFS.label: Literal("Is measured by"),
    },
    "regulates": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isRegulatedBy"],
        RDFS.domain: BRICK.Equipment,
        RDFS.range: BRICK.Substance,
        RDFS.label: Literal("Regulates"),
    },
    "isRegulatedBy": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.domain: BRICK.Substance,
        RDFS.range: BRICK.Equipment,
        RDFS.label: Literal("Is regulated by"),
    },
    "hasAssociatedTag": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isAssociatedWith"],
        RDFS.domain: OWL.Class,
        RDFS.range: BRICK.Tag,
        RDFS.label: Literal("Has associated tag"),
    },
    "isAssociatedWith": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
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
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.range: UNIT.Unit,
        RDFS.label: Literal("Has unit"),
    },
    "timeseries": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.domain: BRICK.Point,
        RDFS.range: BRICK.TimeseriesReference,
        RDFS.label: Literal("Timeseries"),
    },
    "hasTimeseriesId": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.domain: BRICK.TimeseriesReference,
        RDFS.range: XSD.string,
        RDFS.label: Literal("Has timeseries ID"),
    },
    "storedAt": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.domain: BRICK.TimeseriesReference,
        # RDFS.range: XSD.string,
        RDFS.label: Literal("Stored at"),
    },
}
