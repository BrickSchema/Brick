from rdflib import Namespace, Literal, XSD
from brickschema.namespaces import BRICK, A
import brickschema


def test_deprecation():
    """
    Test deprecation of old Brick elements
    """
    g = brickschema.Graph()
    EX = Namespace("urn:ex#")
    g.load_file("Brick.ttl")
    g.bind("ex", EX)

    g.parse(
        data="""
    @prefix brick: <https://brickschema.org/schema/Brick#> .
    brick:Fresh_Air_Fan brick:deprecation [
        brick:deprecationInVersion "1.3.0" ;
        brick:deprecationMitigation "Replace with brick:Outside_Fan" ;
    ] .""",
        format="turtle",
    )

    g.expand("shacl")

    rows = list(g.query("SELECT ?dep WHERE { ?dep owl:deprecated true }"))
    assert len(rows) == 1, "Should infer OWL deprecation notice"

    valid, repG, report = g.validate()
    assert valid, report

    for row in repG.query("""SELECT ?s ?p ?o WHERE { ?s ?p ?o }"""):
        print(row)
