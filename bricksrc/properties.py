from rdflib import Literal
from .namespaces import A, OWL, RDFS, SKOS, BRICK

"""
Defining properties
"""
properties = {
    # About expectedDomain and expectedRange: They replace temporarily
    # RDFS.domin and RDFS.range. The RDFS.domain and RDFS.range infer
    # the type of the subject and object of a property, respectively.
    # However, rather than imply the type of the subject or object by
    # the use of the property, we want to verify that the property is
    # used correctly given the types of the subject and object.
    # Thus, we adopt the brick:expectedDomain and brick:expectedRange
    # properties which imply nothing about the subject/object of the
    # property they are annotating, but can be used to validate the type
    # of their subject or object.  See shacl/DESIGN.md for more discussion.
    "expectedDomain": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        SKOS.definition: Literal("Temporary replacement for RDFS.domain"),
    },

    "expectedRange": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        SKOS.definition: Literal("Temporary replacement for RDFS.range"),
    },

    "hasSubproperty": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: RDFS.subPropertyOf,
        BRICK.expectedRange: RDFS.Property,
        BRICK.expectedDomain: RDFS.Property,
        SKOS.definition: Literal("Subject is a property that has the object as its sub-properity")
    },

    "isLocationOf": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasLocation"],
        BRICK.expectedDomain: BRICK.Location,
        SKOS.definition: Literal("Subject is the physical location encapsulating the object"),
    },
    "hasLocation": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isLocationOf"],
        RDFS.range: BRICK.Location,
        SKOS.definition: Literal("Subject is physically located in the location given by the object"),
    },

    "hasInputSubstance": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        BRICK.expectedRange: BRICK.Substance,
        SKOS.definition: Literal("The subject receives the given substance as an input to its internal process"),
    },
    "hasOutputSubstance": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        BRICK.expectedRange: BRICK.Substance,
        SKOS.definition: Literal("The subject produces or exports the given substance from its internal process"),
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
        SKOS.definition: Literal("The subject is upstream of the object in the context of some sequential process; some media is passed between them"),
        OWL.inverseOf: BRICK["isFedBy"],
        "subproperties": {
            "feedsAir": {
                SKOS.definition: Literal("Passes air"),
            },
        },

        # TODO: add restriction that it needs an air-based equipment on either side?
        # this is equivalent with the classes that have :
        # Restriction (onProperty=brick:hasInputSubstance, hasValue=brick:Air) AND
        # Restriction (onProperty=brick:hasOutputSubstance, hasValue=brick:Air)

        # looks something like this
        #"domain_value_prop": [
        #    [BRICK.hasTag, TAG.Air],
        #],
        #"range_value_prop": [
        #    [BRICK.hasTag, TAG.Air],
        #],
    },
    "isFedBy": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["feeds"],
    },

    "hasPoint": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isPointOf"],
        SKOS.definition: Literal("The subject has a digital/analog input/output point given by the object"),
        BRICK.expectedRange: BRICK.Point,
    },
    "isPointOf": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasPoint"],
        BRICK.expectedDomain: BRICK.Point,
    },

    "hasPart": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        SKOS.definition: Literal("The subject is composed in part of the entity given by the object"),
        OWL.inverseOf: BRICK["isPartOf"],
    },
    "isPartOf": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasPart"],
    },

    "hasTag": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isTagOf"],
        SKOS.definition: Literal("The subject has the given tag"),
        BRICK.expectedRange: BRICK.Tag,
    },
    "isTagOf": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        BRICK.expectedDomain: BRICK.Tag,
    },

    "measures": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isMeasuredBy"],
        SKOS.definition: Literal("The subject measures a quantity or substance given by the object"),
        BRICK.expectedDomain: BRICK.Point,
        BRICK.expectedRange: BRICK.Measurable,
    },
    "isMeasuredBy": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        BRICK.expectedDomain: BRICK.Measurable,
        BRICK.expectedRange: BRICK.Point,
    },
    "regulates": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isRegulatedBy"],
        SKOS.definition: Literal("The subject contributes to or performs the regulation of the substance given by the object"),
        BRICK.expectedDomain: BRICK.Equipment,
        BRICK.expectedRange: BRICK.Substance,
    },
    "isRegulatedBy": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        BRICK.expectedDomain: BRICK.Substance,
        BRICK.expectedRange: BRICK.Equipment,
    },

    "hasAssociatedTag": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isAssociatedWith"],
        SKOS.definition: Literal("The class is associated with the given tag"),
        BRICK.expectedDomain: OWL.Class,
        BRICK.expectedRange: BRICK.Tag,
    },
    "isAssociatedWith": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasAssociatedTag"],
        SKOS.definition: Literal("The tag is associated with the given class"),
        BRICK.expectedDomain: BRICK.Tag,
        BRICK.expectedRange: OWL.Class,
    },
}
