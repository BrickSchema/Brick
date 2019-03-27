from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.collection import Collection
from rdflib.extras.infixowl import Restriction

BRICK = Namespace("https://brickschema.org/schema/1.0.3/Brick#")
BRICKTAG = Namespace("https://brickschema.org/schema/1.0.3/BrickTag#")
BLDG = Namespace("https://brickschema.org/schema/1.0.3/ExampleBuilding#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
A = RDF.type


"""
Defining properties
"""
properties = {
    "isLocationOf": {
        OWL.inverseOf: "hasLocation",
        RDFS.domain: BRICK.Location,
    },
    "hasLocation": {
        OWL.inverseOf: "isLocationOf",
        RDFS.range: BRICK.Location,
    },

    "hasInputSubstance": {
        RDFS.range: BRICK.Substance,
    },
    "hasOutputSubstance": {
        RDFS.range: BRICK.Substance,
    },

    "feeds": {
        A: [OWL.TransitiveProperty],
        OWL.inverseOf: "isFedBy",
        "subproperties": {
            "feedsAir": {
                A: [OWL.TransitiveProperty],
                SKOS.definition: Literal("Passes air"),
                # TODO: add restriction that it needs an air-based equipment on either side?
                # this is equivalent with the classes that have :
                # Restriction (onProperty=brick:hasInputSubstance, hasValue=brick:Air) AND
                # Restriction (onProperty=brick:hasOutputSubstance, hasValue=brick:Air)
            },
        },
    },
    "isFedBy": {
        A: [OWL.TransitiveProperty],
        OWL.inverseOf: "feeds",
    },

    "hasPoint": {
        OWL.inverseOf: "isPointOf",
        RDFS.range: BRICK.Point,
    },
    "isPointOf": {
        OWL.inverseOf: "hasPoint",
        RDFS.domain: BRICK.Point,
    },

    "hasPart": {
        OWL.inverseOf: "isPartOf",
    },
    "isPartOf": {
        OWL.inverseOf: "hasPart",
    },

    "hasTag": {
        OWL.inverseOf: "hasTagOf",
    },

    # Haystack-style
    "ahuRef": {
        RDFS.range: BRICK.AHU,
    }
}
