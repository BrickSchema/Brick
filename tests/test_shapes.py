import brickschema
from rdflib import Literal, Namespace
from bricksrc.namespaces import BRICK, OWL, REC, RDFS

prefixes = """
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix rec: <https://w3id.org/rec#> .
@prefix : <http://example.com#> .
"""

base_data = (
    prefixes
    + """
:equip a brick:Equipment.
:point a brick:Point.
:loc a rec:Room.
"""
)


def test_no_relations(brick_with_imports):
    data = base_data
    data_g = brickschema.Graph().parse(data=data, format="turtle")
    conforms, _, report_str = data_g.validate(extra_graphs=[brick_with_imports])
    assert conforms, report_str


def test_equip(brick_with_imports):
    valid_data = (
        base_data
        + """
:equip brick:hasLocation :loc.
"""
    )
    valid_g = brickschema.Graph().parse(data=valid_data, format="turtle")
    conforms, _, report_str = valid_g.validate(extra_graphs=[brick_with_imports])
    assert conforms, report_str

    invalid_data = (
        base_data
        + """
:equip brick:hasLocation :point.

"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate(extra_graphs=[brick_with_imports])
    assert not conforms


def test_type(brick_with_imports):
    invalid_data = (
        base_data
        + """
:loc a brick:Point.
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate(extra_graphs=[brick_with_imports])
    assert not conforms


def test_point(brick_with_imports):
    invalid_data = (
        base_data
        + """
:point brick:hasLocation :loc.
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate(extra_graphs=[brick_with_imports])
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
    conforms, _, _ = invalid_g.validate(extra_graphs=[brick_with_imports])
    assert not conforms

    invalid_data = (
        base_data
        + """
:meter a brick:Meter .
:loc a rec:Room ;
    brick:meters :meter .
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate(extra_graphs=[brick_with_imports])
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
    conforms, _, report_str = valid_g.validate(extra_graphs=[brick_with_imports])
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
    conforms, _, _ = invalid_g.validate(extra_graphs=[brick_with_imports])
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
    conforms, _, report_str = valid_g.validate(extra_graphs=[brick_with_imports])
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
    conforms, _, _ = invalid_g.validate(extra_graphs=[brick_with_imports])
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
    conforms, _, report_str = valid_g.validate(extra_graphs=[brick_with_imports])
    assert conforms, report_str


def test_plant_is_equipment_and_can_have_points_and_feeds(brick_with_imports):
    valid_data = (
        prefixes
        + """
@prefix rec: <https://w3id.org/rec#> .

:plant a brick:Chiller_Plant ;
    brick:hasPoint :sensor ;
    brick:feeds :ahu ;
    rec:includes :chiller, :pump, :group .
:sensor a brick:Supply_Chilled_Water_Temperature_Sensor .
:ahu a brick:AHU .
:chiller a brick:Chiller .
:pump a brick:Chilled_Water_Pump .
:group a brick:Point_Collection .
"""
    )
    valid_g = brickschema.Graph().parse(data=valid_data, format="turtle")
    conforms, _, report_str = valid_g.validate(extra_graphs=[brick_with_imports])
    assert conforms, report_str


def test_plant_uses_haspoint_not_rec_includes_for_points(brick_with_imports):
    # rec:includes is for logical grouping; points are attached with brick:hasPoint
    invalid_data = (
        prefixes
        + """
@prefix rec: <https://w3id.org/rec#> .

:plant a brick:Chiller_Plant ;
    rec:includes :sensor .
:sensor a brick:Supply_Chilled_Water_Temperature_Sensor .
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate(extra_graphs=[brick_with_imports])
    assert not conforms


def test_plant_requires_rec_includes_for_logical_grouping(brick_with_imports):
    invalid_data = (
        prefixes
        + """
:plant a brick:Boiler_Plant ;
    brick:hasPart :boiler .
:boiler a brick:Boiler .
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate(extra_graphs=[brick_with_imports])
    assert not conforms

    # the same grouping authored from the other side is rejected too
    invalid_data = (
        prefixes
        + """
:plant a brick:Boiler_Plant .
:boiler a brick:Boiler ;
    brick:isPartOf :plant .
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate(extra_graphs=[brick_with_imports])
    assert not conforms


def test_system_and_loop_can_include_points(brick_with_imports):
    valid_data = (
        prefixes
        + """
@prefix rec: <https://w3id.org/rec#> .

:system a brick:System ;
    rec:includes :system_point .
:loop a brick:Loop ;
    rec:includes :loop_point .
:system_point a brick:Temperature_Sensor .
:loop_point a brick:Temperature_Sensor .
"""
    )
    valid_g = brickschema.Graph().parse(data=valid_data, format="turtle")
    conforms, _, report_str = valid_g.validate(extra_graphs=[brick_with_imports])
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
    conforms, _, _ = invalid_g.validate(extra_graphs=[brick_with_imports])
    assert not conforms

    invalid_data = (
        base_data
        + """
:meter a brick:Meter ;
    brick:isMeteredBy :loc .
:loc a rec:Room .
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate(extra_graphs=[brick_with_imports])
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
    conforms, _, report_str = valid_g.validate(extra_graphs=[brick_with_imports])
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

    valid, repG, _ = g.validate()
    assert valid

    res = list(
        repG.query(
            """PREFIX sh: <http://www.w3.org/ns/shacl#>
        PREFIX brick: <https://brickschema.org/schema/Brick#>
        SELECT ?node WHERE {
            ?res a sh:ValidationResult .
            ?res sh:focusNode ?node .
            ?res sh:resultSeverity sh:Warning .
            ?res sh:resultPath brick:hasPart .
        }"""
        )
    )
    assert (
        len(set(res)) == 1
    ), f"System legacy hasPart usage should emit a warning\n{repG.serialize()}"


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

    valid, repG, _ = g.validate()
    assert valid

    res = list(
        repG.query(
            """PREFIX sh: <http://www.w3.org/ns/shacl#>
        PREFIX brick: <https://brickschema.org/schema/Brick#>
        SELECT ?node WHERE {
            ?res a sh:ValidationResult .
            ?res sh:focusNode ?node .
            ?res sh:resultSeverity sh:Warning .
            ?res sh:resultPath brick:hasPart .
        }"""
        )
    )
    assert (
        len(set(res)) == 1
    ), f"Loop legacy hasPart usage should emit a warning\n{repG.serialize()}"


def test_system_and_loop_cannot_include_non_architecture_spaces(brick_with_imports):
    # REC groupings are covered by examples/rec-with-brick; these are REC
    # spaces that are not designed architecture (a plain rec:Space, a
    # rec:Region) and must not be grouped into Brick systems or loops
    for grouping in ("brick:HVAC_System", "brick:Hot_Water_Loop"):
        for space in ("rec:Space", "rec:Region"):
            invalid_data = (
                prefixes
                + """
:grouping a %s ;
    rec:includes :space .
:space a %s .
"""
                % (
                    grouping,
                    space,
                )
            )
            invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
            conforms, _, _ = invalid_g.validate(extra_graphs=[brick_with_imports])
            assert not conforms, f"{grouping} should not include a {space}"


def test_equipment_and_points_cannot_target_non_architecture_spaces(brick_with_imports):
    # feeds, hasLocation and isPointOf accept designed spaces (and deprecated
    # Brick locations), not administrative regions or plain rec:Space
    for relationship in (
        ":vav a brick:VAV ; brick:feeds :space .",
        ":vav a brick:VAV ; brick:hasLocation :space .",
        ":sensor a brick:Temperature_Sensor ; brick:isPointOf :space .",
    ):
        for space in ("rec:Space", "rec:Region"):
            invalid_data = prefixes + "\n%s\n:space a %s .\n" % (relationship, space)
            invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
            conforms, _, _ = invalid_g.validate(extra_graphs=[brick_with_imports])
            assert not conforms, f"'{relationship}' should reject a {space}"
