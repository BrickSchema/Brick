"""
Tests all example files. See tests/conftest.py for the fixture that generates each of the individual test cases
"""
import ontoenv
from rdflib import OWL, RDF
from brickschema import Graph

env = ontoenv.OntoEnv(
    search_directories=[
        "Brick.ttl",
        "examples/",
        "support/",
        "extensions/",
        "rec/Source/SHACL/RealEstateCore",
    ],
    strict=False,
    offline=True,
    excludes=[".venv/*"],
    temporary=True,
)


def test_example_file_with_reasoning(filename):
    g = Graph()
    g.load_file(filename)
    shapes, imported = env.get_dependencies_graph(g)
    profile = "brick"
    g.expand(profile)(extra_graphs=[shapes], engine="topquadrant")

    valid, _, report = g.validate(extra_graphs=[shapes], engine="topquadrant")
    assert valid, report
