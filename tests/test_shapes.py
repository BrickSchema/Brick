import sys
from pdb import set_trace as bp
import rdflib
from bricksrc.namespaces import A, OWL, RDFS, SKOS, BRICK, SH, BSH, bind_prefixes
import pyshacl

schema_g = rdflib.Graph().parse('shacl/BrickShape.ttl', format='turtle')
bind_prefixes(schema_g)

prefixes = """
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix : <http://example.com#> .
"""

base_data = prefixes + """
:equip a brick:Equipment.
:point a brick:Point.
:loc a brick:Location.
"""

def test_no_relations():
    data = base_data
    data_g = rdflib.Graph().parse(data=data, format='turtle')
    conforms, _, _ = pyshacl.validate(
        data_g, shacl_graph=schema_g,
    )
    assert conforms

def test_equip():
    valid_data = base_data + """
:equip brick:hasLocation :loc.
"""
    valid_g = rdflib.Graph().parse(data=valid_data, format='turtle')
    conforms, _, _ = pyshacl.validate(
        valid_g, shacl_graph=schema_g
    )
    assert conforms

    invalid_data = base_data + """
:equip brick:hasLocation :point.

"""
    invalid_g = rdflib.Graph().parse(data=invalid_data, format='turtle')
    conforms, _, _= pyshacl.validate(
        invalid_g, shacl_graph=schema_g
    )
    assert not conforms


def test_type():
    invalid_data = base_data + """
:loc a brick:Point.
"""
    invalid_g = rdflib.Graph().parse(data=invalid_data, format='turtle')
    conforms, _, _= pyshacl.validate(
        invalid_g, shacl_graph=schema_g,
    )
    assert not conforms


def test_point():
    invalid_data = base_data + """
:point brick:hasLocation :loc.
"""
    invalid_g = rdflib.Graph().parse(data=invalid_data, format='turtle')
    conforms, _, _= pyshacl.validate(
        invalid_g, shacl_graph=schema_g
    )
    assert not conforms




