import brickschema
from rdflib import Namespace
from bricksrc.namespaces import REC

prefixes = """
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix : <http://example.com#> .
"""

base_data = (
    prefixes
    + """
:equip a brick:Equipment.
:point a brick:Point.
:loc a brick:Location.
"""
)


def test_no_relations(brick_with_imports):
    data = base_data
    data_g = brickschema.Graph().parse(data=data, format="turtle")
    conforms, _, report_str = data_g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
    assert conforms, report_str


def test_equip(brick_with_imports):
    valid_data = (
        base_data
        + """
:equip brick:hasLocation :loc.
"""
    )
    valid_g = brickschema.Graph().parse(data=valid_data, format="turtle")
    conforms, _, report_str = valid_g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
    assert conforms, report_str

    invalid_data = (
        base_data
        + """
:equip brick:hasLocation :point.

"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
    assert not conforms


def test_type(brick_with_imports):
    invalid_data = (
        base_data
        + """
:loc a brick:Point.
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
    assert not conforms


def test_point(brick_with_imports):
    invalid_data = (
        base_data
        + """
:point brick:hasLocation :loc.
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
    assert not conforms


def test_meter_shapes(brick_with_imports):
    invalid_data = (
        base_data
        + """
:meter a brick:Meter .
:equip a brick:AHU ;
    brick:meters :meter .
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
    assert not conforms

    invalid_data = (
        base_data
        + """
:meter a brick:Meter .
:loc a brick:Space ;
    brick:meters :meter .
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
    assert not conforms

    valid_data = (
        base_data
        + """
:meter a brick:Meter .
:equip a brick:AHU ;
    brick:isMeteredBy :meter .
"""
    )
    valid_g = brickschema.Graph().parse(data=valid_data, format="turtle")
    conforms, _, report_str = valid_g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
    assert conforms, report_str


def test_automation_collection_points_require_ispointof(brick_with_imports):
    invalid_data = (
        prefixes
        + """
@prefix rec: <https://w3id.org/rec#> .

:group a brick:Automation_Collection .
:equip a brick:AHU .
:point a brick:Temperature_Sensor .
:group rec:includes :point .
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
    assert not conforms

    valid_data = (
        prefixes
        + """
@prefix rec: <https://w3id.org/rec#> .

:group a brick:Automation_Collection .
:equip a brick:AHU .
:point a brick:Temperature_Sensor ;
    brick:isPointOf :equip .
:group rec:includes :point .
"""
    )
    valid_g = brickschema.Graph().parse(data=valid_data, format="turtle")
    conforms, _, report_str = valid_g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
    assert conforms, report_str


def test_automation_collection_requires_rec_includes(brick_with_imports):
    invalid_data = (
        prefixes
        + """
@prefix rec: <https://w3id.org/rec#> .

:group a brick:Automation_Collection .
:equip a brick:AHU .
:group brick:hasPart :equip .
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
    assert not conforms

    valid_data = (
        prefixes
        + """
@prefix rec: <https://w3id.org/rec#> .

:ahu a brick:AHU ;
    rec:includes :group .
:group a brick:Automation_Collection ;
    rec:includes :equip .
:equip a brick:Fan .
"""
    )
    valid_g = brickschema.Graph().parse(data=valid_data, format="turtle")
    conforms, _, report_str = valid_g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
    assert conforms, report_str


def test_meter_relationship_shapes(brick_with_imports):
    invalid_data = (
        base_data
        + """
:meter a brick:Meter ;
    brick:isMeteredBy :equip .
:equip a brick:AHU .
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
    assert not conforms

    invalid_data = (
        base_data
        + """
:meter a brick:Meter ;
    brick:isMeteredBy :loc .
:loc a brick:Space .
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
    assert not conforms

    valid_data = (
        base_data
        + """
:meter a brick:Meter ;
    brick:meters :equip .
:equip a brick:AHU .
"""
    )
    valid_g = brickschema.Graph().parse(data=valid_data, format="turtle")
    conforms, _, report_str = valid_g.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
    assert conforms, report_str


def test_system_haspart_warns_and_infers_rec_includes(brick_with_imports):
    EX = Namespace("http://example.com/ns#")
    g = brick_with_imports
    g.bind("ex", EX)
    g.parse(
        data="""
    @prefix brick: <https://brickschema.org/schema/Brick#> .
    @prefix rec: <https://w3id.org/rec#> .
    @prefix ex: <http://example.com/ns#> .

    ex:sys a brick:System ;
        brick:hasPart ex:ahu .
    ex:ahu a brick:AHU .
    """,
        format="turtle",
    )
    g.compile()

    assert (EX.sys, REC.includes, EX.ahu) in g

    valid, repG, report = g.validate(engine="topquadrant")
    assert valid, report

    res = list(
        repG.query(
            """PREFIX sh: <http://www.w3.org/ns/shacl#>
        SELECT ?node WHERE {
            ?res a sh:ValidationResult .
            ?res sh:focusNode ?node .
            ?res sh:resultSeverity sh:Warning .
            ?res sh:value <http://example.com/ns#ahu> .
        }"""
        )
    )
    assert len(set(res)) == 1, "System legacy hasPart usage should emit a warning"


def test_loop_haspart_warns_and_infers_rec_includes(brick_with_imports):
    EX = Namespace("http://example.com/ns#")
    g = brick_with_imports
    g.bind("ex", EX)
    g.parse(
        data="""
    @prefix brick: <https://brickschema.org/schema/Brick#> .
    @prefix rec: <https://w3id.org/rec#> .
    @prefix ex: <http://example.com/ns#> .

    ex:loop a brick:Loop ;
        brick:hasPart ex:point .
    ex:point a brick:Temperature_Sensor .
    """,
        format="turtle",
    )
    g.compile()

    assert (EX.loop, REC.includes, EX.point) in g

    valid, repG, report = g.validate(engine="topquadrant")
    assert valid, report

    res = list(
        repG.query(
            """PREFIX sh: <http://www.w3.org/ns/shacl#>
        SELECT ?node WHERE {
            ?res a sh:ValidationResult .
            ?res sh:focusNode ?node .
            ?res sh:resultSeverity sh:Warning .
            ?res sh:value <http://example.com/ns#point> .
        }"""
        )
    )
    assert len(set(res)) == 1, "Loop legacy hasPart usage should emit a warning"
