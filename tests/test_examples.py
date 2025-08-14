"""
Tests all example files. See tests/conftest.py for the fixture that generates each of the individual test cases
"""
import ontoenv
from rdflib import OWL, RDF
from brickschema import Graph

cfg = ontoenv.Config(["Brick.ttl", "examples/", "support/", "extensions/", "rec/Source/SHACL/RealEstateCore"], strict=False, offline=True, temporary=True, excludes=[".venv/*"])
env = ontoenv.OntoEnv(cfg)


def test_example_file_with_reasoning(filename):
    g = Graph()
    g.load_file(filename)
    shapes, imported = env.get_dependencies_graph(g)
    g.compile(ontology_graph=shapes, backend="topquadrant")

    valid, _, report = g.validate(shape_graphs=shapes, engine="topquadrant")
    assert valid, report
