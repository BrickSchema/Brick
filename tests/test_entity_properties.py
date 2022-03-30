from rdflib import Namespace, Literal
from brickschema.namespaces import BRICK, A, XSD
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

    g.expand("shacl")
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

    g.expand("shacl")
    valid, _, report = g.validate()
    assert not valid, "'AquariumFail' should have thrown a validation error"


def test_entity_property_type_inference():
    g = brickschema.Graph()
    EX = Namespace("urn:ex#")
    REF = Namespace("https://brickschema.org/schema/Brick/ref#")
    BACNET = Namespace("http://data.ashrae.org/bacnet/2020#")
    g.load_file("Brick.ttl")
    g.add(
        (
            EX["point"],
            REF.hasExternalReference,
            [
                (BACNET.objectOf, [(A, BACNET.BACnetDevice)]),
                (REF.BACnetURI, Literal("bacnet://123/analog-input,3/present-value")),
            ],
        )
    )

    valid, _, report = g.validate()
    assert valid, report
    g.expand("shacl")
    g.serialize("/tmp/test.ttl", format="ttl")

    res = g.query(
        "SELECT ?ref WHERE { ?point ref:hasExternalReference ?ref . ?ref a ref:BACnetReference }"
    )
    assert len(res) == 1
