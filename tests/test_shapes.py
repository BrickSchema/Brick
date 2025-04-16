import brickschema

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
    conforms, _, report_str = data_g.validate([brick_with_imports], engine="topquadrant")
    assert conforms, report_str


def test_equip(brick_with_imports):
    valid_data = (
        base_data
        + """
:equip brick:hasLocation :loc.
"""
    )
    valid_g = brickschema.Graph().parse(data=valid_data, format="turtle")
    conforms, _, report_str = valid_g.validate([brick_with_imports], engine="topquadrant")
    assert conforms, report_str

    invalid_data = (
        base_data
        + """
:equip brick:hasLocation :point.

"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate([brick_with_imports], engine="topquadrant")
    assert not conforms


def test_type(brick_with_imports):
    invalid_data = (
        base_data
        + """
:loc a brick:Point.
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate([brick_with_imports], engine="topquadrant")
    assert not conforms


def test_point(brick_with_imports):
    invalid_data = (
        base_data
        + """
:point brick:hasLocation :loc.
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate([brick_with_imports], engine="topquadrant")
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
    conforms, _, _ = invalid_g.validate([brick_with_imports], engine="topquadrant")
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
    conforms, _, _ = invalid_g.validate([brick_with_imports], engine="topquadrant")
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
    conforms, _, report_str = valid_g.validate([brick_with_imports], engine="topquadrant")
    assert conforms, report_str

    invalid_data = (
        base_data
        + """
:meter a brick:Meter ;
    brick:isMeteredBy :equip .
:equip a brick:AHU .
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate([brick_with_imports], engine="topquadrant")
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
    conforms, _, _ = invalid_g.validate([brick_with_imports], engine="topquadrant")
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
    conforms, _, report_str = valid_g.validate([brick_with_imports], engine="topquadrant")
    assert conforms, report_str
