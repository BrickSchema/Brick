import rdflib
from bricksrc.version import BRICK_VERSION


def test_only_define_brick_ontology():
    g = rdflib.Graph()
    g.parse("Brick.ttl", format="turtle")
    ontologies = list(g.subjects(rdflib.RDF.type, rdflib.OWL.Ontology))
    assert len(ontologies) == 1, "There should only be one ontology defined"

    assert ontologies[0] == rdflib.URIRef(
        f"https://brickschema.org/schema/{BRICK_VERSION}/Brick"
    )
