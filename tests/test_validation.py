from rdflib import OWL, RDF
import sys
from brickschema import Graph
import pytest


@pytest.mark.shacl
def test_brick_against_itself(brick_with_imports):
    """
    Tests Brick against itself. This is a regression test to ensure that Brick is valid against itself.
    """
    valid, _, report = brick_with_imports.validate(engine="topquadrant")
    assert valid, report


@pytest.mark.shacl
def test_brick_against_validation_shapes_with_imports(brick_with_imports):
    """
    Tests Brick against itself. This is a regression test to ensure that Brick is valid against itself.
    """
    g = Graph().parse("validation.ttl", format="turtle")
    valid, _, report = (brick_with_imports + g).validate(engine="topquadrant")
    assert valid, report


@pytest.mark.shacl
def test_point_substances_ok(brick_with_imports):
    g = Graph().parse(data="""
@prefix bldg: <http://example.com/mybuilding#> .
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix qudtqk: <http://qudt.org/vocab/quantitykind/> .

bldg:myPoint a brick:Air_Temperature_Sensor ;
    brick:hasQuantity qudtqk:Temperature ;
    brick:hasSubstance brick:Air .
""")
    valid, _, report = (brick_with_imports + g).validate(engine="topquadrant")
    assert valid, report

@pytest.mark.shacl
def test_point_substances_bad(brick_with_imports):
    g = Graph().parse(data="""
@prefix bldg: <http://example.com/mybuilding#> .
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix qudtqk: <http://qudt.org/vocab/quantitykind/> .

bldg:myPoint a brick:Air_Temperature_Sensor ;
    brick:hasQuantity brick:Temperature ;
    brick:hasSubstance brick:Air .
""")
    valid, _, report = (brick_with_imports + g).validate(engine="topquadrant")
    assert not valid, report
