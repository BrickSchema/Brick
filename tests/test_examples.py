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
    env.import_dependencies(g)
    g.expand("shacl", backend="topquadrant")

    valid, _, report = g.validate(engine="topquadrant")
    assert valid, report
