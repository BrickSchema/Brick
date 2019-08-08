from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.collection import Collection
from rdflib.extras.infixowl import Restriction

from namespaces import *


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

    # substance flavors + process
    "Chilled": {},
}
