import pytest
import rdflib
from rdflib.namespace import OWL, RDF, SH
from bricksrc.version import BRICK_VERSION

BRICK_ONTOLOGY = rdflib.URIRef(
    "https://brickschema.org/schema/{}/Brick".format(BRICK_VERSION)
)

# predicates that only belong on an ontology header
ONTOLOGY_HEADER_PREDICATES = [
    OWL.imports,
    OWL.versionInfo,
    OWL.versionIRI,
    OWL.priorVersion,
    SH.declare,
]


@pytest.mark.parametrize("filename", ["Brick.ttl", "Brick-only.ttl"])
def test_only_define_brick_ontology(filename):
    g = rdflib.Graph()
    g.parse(filename, format="turtle")
    ontologies = list(g.subjects(RDF.type, OWL.Ontology))
    assert ontologies == [
        BRICK_ONTOLOGY
    ], f"{filename} should only define the Brick ontology, found {ontologies}"

    # merged ontologies can lose their rdf:type but keep the rest of their
    # header, so also check that no other subject carries header triples
    leftovers = {
        (s, p)
        for p in ONTOLOGY_HEADER_PREDICATES
        for s in g.subjects(p, None)
        if s != BRICK_ONTOLOGY
    }
    assert (
        not leftovers
    ), f"{filename} has ontology header triples on other subjects: {leftovers}"
