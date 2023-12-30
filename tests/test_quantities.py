from rdflib import RDF, OWL, RDFS, Namespace, BNode
import pytest
import brickschema
from .util import make_readable
from collections import defaultdict
import sys

sys.path.append("..")
from bricksrc.namespaces import BRICK, TAG  # noqa: E402

BLDG = Namespace("https://brickschema.org/schema/ExampleBuilding#")


@pytest.fixture()
def quantity_fixtures(brick_with_imports):
    g = brick_with_imports

    # adding instances to the graph to test validation
    res = g.query(
        """SELECT ?m ?class WHERE {
        ?class rdfs:subClassOf brick:Class .
        ?class owl:equivalentClass ?restrictions .
        ?restrictions owl:intersectionOf ?inter .
        ?inter rdf:rest*/rdf:first ?node .
        ?node owl:onProperty brick:measures .
        ?node owl:hasValue ?m
        }"""
    )
    measurable_mapping = defaultdict(set)
    for row in res:
        m, c = row[0], row[1]
        if isinstance(c, BNode):
            continue
        measurable_mapping[c].add(m)
    desired_inferences = {}
    for c, measurables in measurable_mapping.items():
        # print(f"{c} => {measurables}")
        inst = BLDG[f"test_inst_{c.split('#')[-1]}"]
        desired_inferences[inst] = c
        for m in measurables:
            g.add((inst, BRICK.measures, m))

    g.expand(profile="shacl", backend="topquadrant")
    return desired_inferences, g


def test_measurables_defined(quantity_fixtures):
    _, g = quantity_fixtures
    # test to make sure all objects of the
    # brick:measures relationship are a Measurable
    measurable = make_readable(
        g.query(
            "SELECT ?m WHERE {\
                                        ?m a brick:Measurable\
                                        }"
        )
    )

    measured = make_readable(
        g.query(
            """SELECT ?m WHERE {
        ?class rdfs:subClassOf brick:Class .
        ?class owl:equivalentClass ?restrictions .
        ?restrictions owl:intersectionOf ?inter .
        ?inter rdf:rest*/rdf:first ?node .
        ?node owl:onProperty brick:measures .
        ?node owl:hasValue ?m
        }"""
        )
    )
    for m in measured:
        assert m in measurable


def test_measurable_inference(quantity_fixtures):
    desired_inferences, g = quantity_fixtures
    for inst, klass in desired_inferences.items():
        res = g.query(f"SELECT ?class WHERE {{ <{inst}> rdf:type ?class }}")
        assert klass in [row[0] for row in res]
