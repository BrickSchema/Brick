from rdflib import Namespace
from .version import BRICK_VERSION

BRICK = Namespace(f"https://brickschema.org/schema/{BRICK_VERSION}/Brick#")
TAG = Namespace(f"https://brickschema.org/schema/{BRICK_VERSION}/BrickTag#")
BSH = Namespace(f"https://brickschema.org/schema/{BRICK_VERSION}/BrickShape#")
SH = Namespace(f"http://www.w3.org/ns/shacl#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
DCTERMS = Namespace("http://purl.org/dc/terms#")
SDO = Namespace("http://schema.org#")
SOSA = Namespace("http://www.w3.org/ns/sosa#")
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
    g.bind("tag", TAG)
    g.bind("bsh", BSH)
