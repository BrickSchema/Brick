from rdflib import Literal, BNode, URIRef
from rdflib.collection import Collection

from .namespaces import DCTERMS, SDO, RDFS, RDF, OWL
from .version import BRICK_VERSION, BRICK_FULL_VERSION

# defines metadata about the Brick ontology
ontology = {
    DCTERMS.creator: [
        {
            SDO.email: Literal("gtfierro@cs.berkeley.edu"),
            SDO.name: Literal("Gabe Fierro"),
        },
        {SDO.email: Literal("jbkoh@eng.ucsd.edu"), SDO.name: Literal("Jason Koh")},
    ],
    DCTERMS.license: URIRef("https://github.com/BrickSchema/brick/blob/master/LICENSE"),
    DCTERMS.version: Literal(BRICK_FULL_VERSION),
    RDFS.label: Literal("Brick"),
    RDFS.seeAlso: URIRef("https://brickschema.org"),
}


def define_ontology(G):
    brick_ontology = URIRef(f"https://brickschema.org/schema/{BRICK_VERSION}/Brick")
    G.add((brick_ontology, RDF.type, OWL.Ontology))

    creators = []
    creator_list = BNode()

    for creator in ontology.pop(DCTERMS.creator):
        creator1 = BNode()
        creators.append(creator1)
        G.add((creator1, RDF.type, SDO.Person))
        for k, v in creator.items():
            G.add((creator1, k, v))
    Collection(G, creator_list, creators)
    G.add((brick_ontology, DCTERMS.creator, creator_list))

    for k, v in ontology.items():
        G.add((brick_ontology, k, v))
