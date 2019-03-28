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

tags = {
    "Coil": {},
    "Valve": {},

    "Heat": {},
    "Cool": {},

    # all Equip have the Equip tag. This is accomplished by
    # using a Restriction onValue property that says that all members of
    # the Equipment class have the "Equip" value for at least one of their tags.
    # We could also accomplish this by having "rdfs:subclassof brick:Equipment" 
    # be the same as "brick:hasTag bricktag:Equip".
    # We use a similar idiom for these other tags
    "Equip": {},
    "Loc": {},
    "Point": {},
    "Lighting": {},
    "HVAC": {},

    # substance tags
    "Air": {},
    "Steam": {},
    "Ice": {},
}
