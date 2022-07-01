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
    @prefix ex: <urn:ex#> .
    ex:fan a brick:Fresh_Air_Fan .
    """,
        format="turtle",
    )
    g.expand("shacl")

    rows = list(g.query("SELECT ?dep WHERE { ?dep owl:deprecated true }"))
    assert len(rows) > 1, "Should infer OWL deprecation notice"

    rows = list(g.query("SELECT ?fan WHERE { ?fan a brick:Outside_Fan }"))
    assert len(rows) == 1, "Outside fan should exist because of mitigation rule"

    valid, repG, report = g.validate()
    assert valid, report

    res = repG.query(
        """SELECT ?node WHERE {
        ?res a sh:ValidationResult .
        ?res sh:focusNode ?node .
        ?res sh:resultSeverity sh:Warning .
        ?res sh:value ex:fan .
    }"""
    )
    assert len(list(res)) == 1, "Should have a warning for deprecation"
