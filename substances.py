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

##### Defining substances
substances = {
    "Fluid": {
        "subclasses": {
            "Gas": {
                "subclasses": {
                    "Air": {
                        "subclasses": {
                            "Outside_Air": {},
                            "Mixed_Air": {},
                            "Return_Air": {},
                            "Exhaust_Air": {},
                        },
                    },
                    "Steam": {
                        SKOS.definition: Literal("Water in its gaseous form"),
                    },
                },
            },
            "Liquid": {
                "subclasses": {
                    "Water": {
                        SKOS.definition: Literal("Water in its liquid form"),
                        "subclasses": {
                            "Chilled_Water": {},
                        },
                    },
                },
            },
        },
    },
    "Solid": {
        "subclasses": {
            "Ice": {
                SKOS.definition: Literal("Water in its solid form"),
            },
        },
    }
}
