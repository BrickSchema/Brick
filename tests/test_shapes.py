import sys
from bricksrc.namespaces import A, OWL, RDFS, SKOS, BRICK, SH, BSH, bind_prefixes
import brickschema

schema_g = brickschema.Graph().load_file("Brick.ttl")
bind_prefixes(schema_g)

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


def test_no_relations():
    data = base_data
    data_g = brickschema.Graph().parse(data=data, format="turtle")
    conforms, r1, r2 = data_g.validate([schema_g])
    assert conforms


def test_equip():
    valid_data = (
        base_data
        + """
:equip brick:hasLocation :loc.
"""
    )
    valid_g = brickschema.Graph().parse(data=valid_data, format="turtle")
    conforms, _, _ = valid_g.validate([schema_g])
    assert conforms

    invalid_data = (
        base_data
        + """
:equip brick:hasLocation :point.

"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate([schema_g])
    assert not conforms


def test_type():
    invalid_data = (
        base_data
        + """
:loc a brick:Point.
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate([schema_g])
    assert not conforms


def test_point():
    invalid_data = (
        base_data
        + """
:point brick:hasLocation :loc.
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate([schema_g])
    assert not conforms


def test_meter_shapes():
    invalid_data = (
        base_data
        + """
:meter a brick:Meter .
:equip a brick:AHU ;
    brick:meters :meter .
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate([schema_g])
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
    conforms, _, _ = invalid_g.validate([schema_g])
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
    conforms, _, _ = valid_g.validate([schema_g])
    assert conforms

    invalid_data = (
        base_data
        + """
:meter a brick:Meter ;
    brick:isMeteredBy :equip .
:equip a brick:AHU .
"""
    )
    invalid_g = brickschema.Graph().parse(data=invalid_data, format="turtle")
    conforms, _, _ = invalid_g.validate([schema_g])
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
    conforms, _, _ = invalid_g.validate([schema_g])
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
    conforms, _, _ = valid_g.validate([schema_g])
    assert conforms
