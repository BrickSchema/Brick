from rdflib import Namespace, Literal
from brickschema.namespaces import BRICK, A
import brickschema


def test_entity_property_validation():
    g = brickschema.Graph()
    EX = Namespace("urn:ex#")
    g.load_file("Brick.ttl")

    g.add((EX["bldg"], A, BRICK.Building))
    g.add(
        (
            EX["bldg"],
            BRICK.buildingPrimaryFunction,
            [(BRICK.value, Literal("Aquarium"))],
        )
    )

    g.expand("brick")
    valid, _, report = g.validate()
    assert valid, report

    g = brickschema.Graph()
    EX = Namespace("urn:ex#")
    g.load_file("Brick.ttl")

    g.add((EX["bldg"], A, BRICK.Building))
    g.add(
        (
            EX["bldg"],
            BRICK.buildingPrimaryFunction,
            [(BRICK.value, Literal("AquariumFail"))],
        )
    )

    g.expand("brick")
    valid, _, report = g.validate()
    assert not valid, "'AquariumFail' should have thrown a validation error"
