from rdflib import Namespace, Literal, XSD
from brickschema.namespaces import BRICK, A
import brickschema


def test_entity_property_validation():
    g = brickschema.Graph()
    EX = Namespace("urn:ex#")
    g.load_file("Brick.ttl")

    # test success
    g.add((EX["bldg"], A, BRICK.Building))
    g.add(
        (
            EX["bldg"],
            BRICK.buildingPrimaryFunction,
            [(BRICK.value, Literal("Aquarium", datatype=XSD.string))],
        )
    )

    g.expand("brick")
    valid, _, report = g.validate()
    assert valid, report

    # test failure
    g = brickschema.Graph()
    g.load_file("Brick.ttl")

    g.add((EX["bldg"], A, BRICK.Building))
    g.add(
        (
            EX["bldg"],
            BRICK.buildingPrimaryFunction,
            [(BRICK.value, Literal("AquariumFail", datatype=XSD.string))],
        )
    )

    g.expand("brick", backend="owlrl")
    valid, _, report = g.validate()
    assert not valid, "'AquariumFail' should have thrown a validation error"
