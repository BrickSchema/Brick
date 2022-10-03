from datetime import datetime
from rdflib import Literal, BNode, URIRef
from rdflib.collection import Collection

from .namespaces import DCTERMS, SDO, RDFS, RDF, OWL, BRICK, TAG, BSH
from .version import BRICK_VERSION, BRICK_FULL_VERSION

# defines metadata about the Brick ontology
ontology = {
    DCTERMS.creator: [
        {
            RDF.type: SDO.Person,
            SDO.email: Literal("gtfierro@mines.edu"),
            SDO.name: Literal("Gabe Fierro"),
        },
        {
            RDF.type: SDO.Person,
            SDO.email: Literal("jbkoh@eng.ucsd.edu"),
            SDO.name: Literal("Jason Koh"),
        },
    ],
    DCTERMS.license: URIRef("https://github.com/BrickSchema/brick/blob/master/LICENSE"),
    DCTERMS.issued: Literal("2016-11-16"),
    DCTERMS.modified: Literal(datetime.now().strftime("%Y-%m-%d")),
    DCTERMS.publisher: {
        RDF.type: SDO.Consortium,
        SDO.legalName: Literal("Brick Consortium, Inc"),
        SDO.sameAs: URIRef("https://brickschema.org/consortium/"),
    },
    OWL.versionInfo: Literal(BRICK_FULL_VERSION),
    RDFS.label: Literal("Brick"),
    RDFS.seeAlso: URIRef("https://brickschema.org"),
}


def define_ontology(G):
    brick_iri_version = URIRef(f"https://brickschema.org/schema/{BRICK_VERSION}/Brick")
    G.add((brick_iri_version, RDF.type, OWL.Ontology))
    G.add((brick_iri_version, RDFS.isDefinedBy, brick_iri_version))

    # add creators from ontology markup above
    creators = []
    creator_list = BNode("ontology_creators")
    for creator in ontology.pop(DCTERMS.creator):
        creator1 = BNode(f"ontology_creator_{creator[SDO.name]}")
        creators.append(creator1)
        for k, v in creator.items():
            G.add((creator1, k, v))

    # add publisher info
    publisher = BNode("publisher")
    G.add((brick_iri_version, DCTERMS.publisher, publisher))
    for k, v in ontology.pop(DCTERMS.publisher).items():
        G.add((publisher, k, v))
    Collection(G, creator_list, creators)
    G.add((brick_iri_version, DCTERMS.creator, creator_list))

    # add other simple attributes
    for k, v in ontology.items():
        G.add((brick_iri_version, k, v))
