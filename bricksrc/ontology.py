from datetime import datetime
from rdflib import Literal, BNode, URIRef
from rdflib.collection import Collection

from .namespaces import DCTERMS, SDO, RDFS, RDF, OWL, BRICK, SH, XSD, REF, REC
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

# TODO: URL for RealEstateCore?
ontology_imports = {
    "bacnet": "http://data.ashrae.org/bacnet/2020",
    "ref": "https://brickschema.org/schema/Brick/ref",
    "rec": "https://w3id.org/rec",
    "recimports": "https://w3id.org/rec/recimports",
    "quantitykind": "http://qudt.org/3.1.0/vocab/quantitykind",
    "unit": "http://qudt.org/3.1.0/vocab/unit",
}

shacl_namespace_declarations = [
    {
        SH.namespace: Literal(str(RDF), datatype=XSD.anyURI),
        SH.prefix: Literal("rdf"),
    },
    {
        SH.namespace: Literal(str(XSD), datatype=XSD.anyURI),
        SH.prefix: Literal("xsd"),
    },
    {
        SH.namespace: Literal(str(RDFS), datatype=XSD.anyURI),
        SH.prefix: Literal("rdfs"),
    },
    {
        SH.namespace: Literal(str(BRICK), datatype=XSD.anyURI),
        SH.prefix: Literal("brick"),
    },
    {
        SH.namespace: Literal(str(OWL), datatype=XSD.anyURI),
        SH.prefix: Literal("owl"),
    },
    {
        SH.namespace: Literal(str(SH), datatype=XSD.anyURI),
        SH.prefix: Literal("sh"),
    },
    {
        SH.namespace: Literal(
            "http://data.ashrae.org/standard223#", datatype=XSD.anyURI
        ),
        SH.prefix: Literal("s223"),
    },
    {
        SH.namespace: Literal(str(REF), datatype=XSD.anyURI),
        SH.prefix: Literal("ref"),
    },
    {
        SH.namespace: Literal("https://w3id.org/rec#", datatype=XSD.anyURI),
        SH.prefix: Literal("rec"),
    },
]

BRICK_IRI_VERSION = URIRef(f"https://brickschema.org/schema/{BRICK_VERSION}/Brick")


def define_ontology(G):
    G.add((BRICK_IRI_VERSION, RDF.type, OWL.Ontology))
    G.add((BRICK_IRI_VERSION, RDFS.isDefinedBy, BRICK_IRI_VERSION))

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
    G.add((BRICK_IRI_VERSION, DCTERMS.publisher, publisher))
    for k, v in ontology.pop(DCTERMS.publisher).items():
        G.add((publisher, k, v))
    Collection(G, creator_list, creators)
    G.add((BRICK_IRI_VERSION, DCTERMS.creator, creator_list))

    # add other simple attributes
    for k, v in ontology.items():
        G.add((BRICK_IRI_VERSION, k, v))

    # add imports
    for imp in ontology_imports.values():
        G.add((BRICK_IRI_VERSION, OWL.imports, URIRef(imp)))

    # add SHACL namespace/prefix declarations for SHACL rules
    for declaration in shacl_namespace_declarations:
        decl = BNode()
        G.add((BRICK_IRI_VERSION, SH.declare, decl))
        for k, v in declaration.items():
            G.add((decl, k, v))


def define_extension(graph, defn):
    graph_name = URIRef(defn["namespace"])
    graph.add((graph_name, RDF.type, OWL.Ontology))
    graph.add((graph_name, RDFS.isDefinedBy, graph_name))

    # add creators from ontology markup above
    creators = []
    creator_list = BNode("ontology_creators")
    for creator in ontology.pop(DCTERMS.creator, []):
        if not creator:
            break
        creator1 = BNode(f"ontology_creator_{creator[SDO.name]}")
        creators.append(creator1)
        for k, v in creator.items():
            graph.add((creator1, k, v))
    if creators:
        Collection(graph, creator_list, creators)
        graph.add((graph_name, DCTERMS.creator, creator_list))

    # add publisher info
    publisher = BNode("publisher")
    publishers = ontology.pop(DCTERMS.publisher, {})
    for k, v in publishers.items():
        graph.add((publisher, k, v))
    if publishers:
        graph.add((graph_name, DCTERMS.publisher, publisher))

    # add imports
    ontology_imports = defn.pop("imports", {})
    for ns, imp in ontology_imports.items():
        graph.add((graph_name, OWL.imports, URIRef(imp)))
        graph.bind(ns, imp)

    # add other simple attributes
    for k, v in ontology.items():
        graph.add((graph_name, k, v))

    # add SHACL namespace/prefix declarations for SHACL rules
    for pfx, ns in defn.pop("decls", {}).items():
        decl = BNode()
        graph.add((graph_name, SH.declare, decl))
        graph.bind(pfx, ns)
        graph.add((decl, SH.prefix, Literal(pfx)))
        graph.add((decl, SH.namespace, Literal(str(ns), datatype=XSD.anyURI)))
