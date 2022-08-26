from rdflib import Namespace

BRICK = Namespace("https://brickschema.org/schema/Brick#")
TAG = Namespace("https://brickschema.org/schema/BrickTag#")
BSH = Namespace("https://brickschema.org/schema/BrickShape#")
REF = Namespace("https://brickschema.org/schema/Brick/ref#")
SH = Namespace("http://www.w3.org/ns/shacl#")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
DCTERMS = Namespace("http://purl.org/dc/terms/")
SDO = Namespace("http://schema.org/")
SOSA = Namespace("http://www.w3.org/ns/sosa/")
VCARD = Namespace("http://www.w3.org/2006/vcard/ns#")
S223 = Namespace("http://data.ashrae.org/standard223#")

# QUDT namespaces
QUDT = Namespace("http://qudt.org/schema/qudt/")
QUDTQK = Namespace("http://qudt.org/vocab/quantitykind/")
QUDTDV = Namespace("http://qudt.org/vocab/dimensionvector/")
UNIT = Namespace("http://qudt.org/vocab/unit/")

# TODO: fix these namespaces
BACNET = Namespace("http://data.ashrae.org/bacnet/2020#")
IFC = Namespace("https://brickschema.org/extension/ifc#")

A = RDF.type


def bind_prefixes(g):
    g.bind("rdf", RDF)
    g.bind("owl", OWL)
    g.bind("dcterms", DCTERMS)
    g.bind("sdo", SDO)
    g.bind("rdfs", RDFS)
    g.bind("skos", SKOS)
    g.bind("sosa", SOSA)
    g.bind("sh", SH)
    g.bind("brick", BRICK)
    g.bind("ref", REF)
    g.bind("tag", TAG)
    g.bind("vcard", VCARD)
    g.bind("bsh", BSH)
    g.bind("qudtqk", QUDTQK)
    g.bind("qudt", QUDT)
    g.bind("unit", UNIT)
    g.bind("xsd", XSD)
    g.bind("bacnet", BACNET)
    g.bind("ifc", IFC)
    g.bind("s223", S223)
