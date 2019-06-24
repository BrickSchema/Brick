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
        "tags": [ TAG.Site ],
    },
    "Floor": {
        "tags": [ TAG.Floor, TAG.Location ],
    },
    "Roof": {
        "tags": [ TAG.Roof, TAG.Location ],
    },
    "Basement": {
        "tags": [ TAG.Basement, TAG.Location ],
    },
    "Outside": {
        "tags": [ TAG.Outside, TAG.Location ],
    },
    "City": {
        "tags": [ TAG.City, TAG.Location ],
    },
    "Wing": {
        "tags": [ TAG.Wing, TAG.Location ],
    },
    "Space": {
        "tags": [ TAG.Space, TAG.Location ],
    },
    "Zone": {
        "tags": [ TAG.Zone, TAG.Location ],
        "subclasses": {
            "HVAC_Zone": {
                "tags": [ TAG.HVAC, TAG.Zone, TAG.Location ],
            },
            "Lighting_Zone": {
                "tags": [ TAG.Lighting, TAG.Zone, TAG.Location ],
            },
            "Fire_Zone": {
                "tags": [ TAG.Fire, TAG.Zone, TAG.Location ],
            },
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
