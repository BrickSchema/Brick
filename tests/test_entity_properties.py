from brickschema import Graph
from rdflib import Namespace, Literal, XSD
from brickschema.namespaces import BRICK, A, REF

EX = Namespace("urn:ex#")


def test_entity_property_validation(brick_with_imports):
    g = Graph()

    # test success
    g.add((EX["bldg"], A, BRICK.Building))
    g.add(
        (
            EX["bldg"],
            BRICK.buildingPrimaryFunction,
            [(BRICK.value, Literal("Aquarium", datatype=XSD.string))],
        )
    )

    profile = "brick"
    g.expand(profile)(extra_graphs=[brick_with_imports], engine="topquadrant")
    valid, _, report = g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
    assert valid, report


def test_entity_property_validation_failure(brick_with_imports):
    # test failure
    g = Graph()
    g.add((EX["bldg"], A, BRICK.Building))
    g.add(
        (
            EX["bldg"],
            BRICK.buildingPrimaryFunction,
            [(BRICK.value, Literal("AquariumFail", datatype=XSD.string))],
        )
    )

    profile = "brick"
    g.expand(profile)(extra_graphs=[brick_with_imports], engine="topquadrant")
    # g.serialize("/tmp/test.ttl", format="ttl")
    valid, _, report = g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
    print(report)
    assert not valid, "'AquariumFail' should have thrown a validation error"


def test_entity_property_type_inference(brick_with_imports):
    g = Graph()
    REF = Namespace("https://brickschema.org/schema/Brick/ref#")
    BACNET = Namespace("http://data.ashrae.org/bacnet/2020#")
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

    valid, _, report = g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
    g.serialize("test.ttl", format="ttl")
    assert valid, report
    profile = "brick"
    g.expand(profile)(extra_graphs=[brick_with_imports], engine="topquadrant")

    res = g.query(
        "SELECT ?ref WHERE { ?point ref:hasExternalReference ?ref . ?ref a ref:BACnetReference }"
    )
    assert len(res) == 1


def test_last_known_value(brick_with_imports):
    g = Graph()
    EX = Namespace("urn:ex#")
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
    valid, _, report = g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
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
    valid, _, report = g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
    assert not valid, report


def test_external_reference_rules(brick_with_imports):
    g = Graph()
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

    g = profile = "brick"
    g.expand(profile)(extra_graphs=[brick_with_imports], engine="topquadrant")
    g.serialize("/tmp/test.ttl")
    valid, _, report = g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
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
    print(g.serialize(format="ttl"))

    profile = "brick"
    g.expand(profile)(extra_graphs=[brick_with_imports], engine="topquadrant")
    valid, _, report = g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
    assert not valid, report
