from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.collection import Collection
from rdflib.extras.infixowl import Restriction

from .namespaces import *

# defines metadata about the Brick ontology
ontology = {
    DCTERMS.creator: [
        {
            SDO.email: Literal("gtfierro@cs.berkeley.edu"),
            SDO.name: Literal("Gabe Fierro"),
        },
        {
            SDO.email: Literal("jbkoh@eng.ucsd.edu"),
            SDO.name: Literal("Jason Koh"),
        },
    ],
    DCTERMS.license: URIRef("https://github.com/BrickSchema/brick/blob/master/LICENSE"),
    RDFS.label: Literal("Brick"),
    RDFS.seeAlso: URIRef("https://brickschema.org"),
}

def define_ontology(G):
    brick_ontology = URIRef("https://brickschema.org/schema/1.1.0/Brick#")
    G.add( (brick_ontology, RDF.type, OWL.Ontology) )

    creators = []
    creator_list = BNode()

    for creator in ontology.pop(DCTERMS.creator):
        creator1 = BNode()
        creators.append(creator1)
        G.add((creator1, RDF.type, SDO.Person))
        for k, v in creator.items():
            G.add((creator1, k, v))
    c = Collection(G, creator_list, creators)
    G.add((brick_ontology, DCTERMS.creator, creator_list))

    for k,v in ontology.items():
        G.add((brick_ontology, k, v))
