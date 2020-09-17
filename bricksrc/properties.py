from rdflib import Literal
from .namespaces import A, OWL, RDFS, BRICK, VCARD, UNIT

"""
Defining properties
"""
properties = {
    "isLocationOf": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasLocation"],
        RDFS.domain: BRICK.Location,
        "subproperties": {
            "isSiteOf": {
                RDFS.domain: BRICK.Site,
                OWL.inverseOf: BRICK["hasSite"],
            },
        },
    },
    "hasLocation": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isLocationOf"],
        RDFS.range: BRICK.Location,
        "subproperties": {
            "hasSite": {
                RDFS.range: BRICK.Site,
                OWL.inverseOf: BRICK["isSiteOf"],
            },
        },
    },
    "hasInputSubstance": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.range: BRICK.Substance,
    },
    "hasOutputSubstance": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.range: BRICK.Substance,
    },
    "controls": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isControlledBy"],
    },
    "isControlledBy": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["controls"],
    },
    "feeds": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isFedBy"],
        "subproperties": {
            "feedsAir": {
                # TODO: add restriction that it needs an air-based equipment on either side?
                # this is equivalent with the classes that have :
                # Restriction (onProperty=brick:hasInputSubstance, hasValue=brick:Air) AND
                # Restriction (onProperty=brick:hasOutputSubstance, hasValue=brick:Air)
                # looks something like this
                # "domain_value_prop": [
                #    [BRICK.hasTag, TAG.Air],
                # ],
                # "range_value_prop": [
                #    [BRICK.hasTag, TAG.Air],
                # ],
            },
        },
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
        RDFS.domain: BRICK.Point,
        RDFS.range: UNIT.Unit,
    },
}
