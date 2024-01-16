from rdflib import Namespace


def test_deprecation(brick_with_imports):
    """
    Test deprecation of old Brick elements
    """
    g = brick_with_imports
    EX = Namespace("urn:ex#")
    g.bind("ex", EX)
    g.parse(
        data="""
    @prefix brick: <https://brickschema.org/schema/Brick#> .
    @prefix ex: <urn:ex#> .
    ex:fan a brick:Fresh_Air_Fan .
    """,
        format="turtle",
    )
    g.expand("shacl", backend="topquadrant")

    rows = list(g.query("SELECT ?dep WHERE { ?dep owl:deprecated true }"))
    assert len(rows) > 1, "Should infer OWL deprecation notice"

    rows = list(g.query("SELECT ?fan WHERE { ?fan a brick:Outside_Fan }"))
    assert len(rows) == 1, "Outside fan should exist because of mitigation rule"

    valid, repG, report = g.validate(engine="topquadrant")
    assert valid, report

    res = repG.query(
        """SELECT ?node WHERE {
        ?res a sh:ValidationResult .
        ?res sh:focusNode ?node .
        ?res sh:resultSeverity sh:Warning .
        ?res sh:value <urn:ex#fan> .
    }"""
    )
    assert len(set(res)) == 1, "Should have a warning for deprecation"
