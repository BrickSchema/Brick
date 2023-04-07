"""
Tests all example files. See tests/conftest.py for the fixture that generates each of the individual test cases
"""
import ontoenv

env = ontoenv.OntoEnv()


def test_example_file_with_reasoning(brick_with_imports, filename):
    g = brick_with_imports
    g.load_file(filename)
    env.import_dependencies(g)
    g.expand("shacl")

    valid, _, report = g.validate()
    assert valid, report
