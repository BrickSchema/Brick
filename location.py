from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.collection import Collection
from rdflib.extras.infixowl import Restriction

BRICK = Namespace("https://brickschema.org/schema/1.0.3/Brick#")
TAG = Namespace("https://brickschema.org/schema/1.0.3/BrickTag#")
BLDG = Namespace("https://brickschema.org/schema/1.0.3/ExampleBuilding#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
A = RDF.type

"""
Location class structure
"""
location_subclasses = {
    "Building": {
    },
    "Floor": {
    },
    "Roof": {
    },
    "Basement": {
    },
    "Outside": {
    },
    "City": {
    },
    "Wing": {
    },
    "Space": {
    },
    "Zone": {
        "subclasses": {
            "HVAC_Zone": {},
            "Lighting_Zone": {},
            "Fire_Zone": {},
        },
    },
    "Room": {
        "subclasses": {
            "Laboratory": {
                "subclasses": {
                    "Freezer": {},
                    "Cold_Box": {},
                    "Hot_Box": {},
                    "Environment_Box": {},
                },
            },
            "Server_Room": {},
        },
    },
}
