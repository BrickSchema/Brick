from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.collection import Collection
from rdflib.extras.infixowl import Restriction

from namespaces import *


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
