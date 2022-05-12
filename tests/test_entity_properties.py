from rdflib import Namespace, Literal
from brickschema.namespaces import BRICK, A, REF, XSD
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


def test_last_known_value():
    g = brickschema.Graph()
    EX = Namespace("urn:ex#")
    g.load_file("Brick.ttl")
    g.add(
        (
            EX["point"],
            BRICK.lastKnownValue,
            [
                (BRICK.value, Literal("1.0", datatype=XSD.float)),
                (
                    BRICK.timestamp,
                    Literal("2020-01-01T00:00:00", datatype=XSD.dateTime),
                ),
            ],
        )
    )
    valid, _, report = g.validate()
    assert valid, report
    g.add(
        (
            EX["point"],
            BRICK.lastKnownValue,
            [
                (BRICK.value, Literal("2.0", datatype=XSD.float)),
                (
                    BRICK.timestamp,
                    Literal("2020-01-02T00:00:00", datatype=XSD.dateTime),
                ),
            ],
        )
    )
    valid, _, report = g.validate()
    assert not valid, report


def test_external_reference_rules():
    g = brickschema.Graph()
    EX = Namespace("urn:ex#")
    g.load_file("Brick.ttl")
    g.add((EX["p1"], A, BRICK.Point))
    g.add(
        (
            EX["p1"],
            REF.hasExternalReference,
            [
                (REF.hasTimeseriesId, Literal("abc")),
            ],
        )
    )

    g.expand("shacl")
    valid, _, report = g.validate()
    assert valid, report

    res = g.query(
        "SELECT ?ref WHERE { ?point ref:hasExternalReference ?ref . ?ref a ref:TimeseriesReference }"
    )
    assert len(res) == 1

    g.add((EX["e1"], A, BRICK.Equipment))
    g.add(
        (
            EX["e1"],
            REF.hasExternalReference,
            [
                (REF.hasTimeseriesId, Literal("def")),
            ],
        )
    )

    g.expand("shacl")
    valid, _, report = g.validate()
    assert not valid, report
