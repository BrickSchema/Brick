from .namespaces import A, OWL, RDFS, BRICK, VCARD, UNIT, QUDT, XSD, SDO

"""
Defining properties
"""
properties = {
    "value": {RDFS.subPropertyOf: QUDT.value},
    "latitude": {RDFS.subPropertyOf: SDO.latitude},
    "longitude": {RDFS.subPropertyOf: SDO.longitude},
    "hasQUDTReference": {A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty]},
    "isLocationOf": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasLocation"],
        RDFS.domain: BRICK.Location,
    },
    "hasLocation": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isLocationOf"],
        RDFS.range: BRICK.Location,
    },
    "hasInputSubstance": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.range: BRICK.Substance,
    },
    "hasOutputSubstance": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.range: BRICK.Substance,
    },
    "feeds": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isFedBy"],
        "subproperties": {"feedsAir": {}},
    },
    "isFedBy": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["feeds"],
    },
    "hasPoint": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isPointOf"],
        RDFS.range: BRICK.Point,
    },
    "isPointOf": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasPoint"],
        RDFS.domain: BRICK.Point,
    },
    "hasPart": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isPartOf"],
    },
    "isPartOf": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasPart"],
    },
    "hasTag": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isTagOf"],
        RDFS.range: BRICK.Tag,
    },
    "isTagOf": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.domain: BRICK.Tag,
    },
    "measures": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isMeasuredBy"],
        RDFS.domain: BRICK.Point,
        RDFS.range: BRICK.Measurable,
    },
    "isMeasuredBy": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.domain: BRICK.Measurable,
        RDFS.range: BRICK.Point,
    },
    "regulates": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isRegulatedBy"],
        RDFS.domain: BRICK.Equipment,
        RDFS.range: BRICK.Substance,
    },
    "isRegulatedBy": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.domain: BRICK.Substance,
        RDFS.range: BRICK.Equipment,
    },
    "hasAssociatedTag": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isAssociatedWith"],
        RDFS.domain: OWL.Class,
        RDFS.range: BRICK.Tag,
    },
    "isAssociatedWith": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasAssociatedTag"],
        RDFS.domain: BRICK.Tag,
        RDFS.range: OWL.Class,
    },
    "hasAddress": {
        RDFS.subPropertyOf: VCARD.hasAddress,
        RDFS.domain: BRICK.Building,
        RDFS.range: VCARD.Address,
    },
    "hasUnit": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.range: UNIT.Unit,
    },
    "timeseries": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.domain: BRICK.Point,
        RDFS.range: BRICK.TimeseriesReference,
    },
    "hasTimeseriesId": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.domain: BRICK.TimeseriesReference,
        RDFS.range: XSD.string,
    },
    "storedAt": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.domain: BRICK.TimeseriesReference,
        # RDFS.range: XSD.string,
    },
}
