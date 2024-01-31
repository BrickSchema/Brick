# Set of tests to demonstrate use of Brick *without* the use of a reasoner
from .util import make_readable


def test_query_equipment(simple_brick_model):
    res = make_readable(
        simple_brick_model.query(
            """SELECT DISTINCT ?equip WHERE {
    ?equip rdf:type/rdfs:subClassOf* brick:Equipment .
    }"""
        )
    )
    assert len(res) == 4


def test_query_points(simple_brick_model):
    res = make_readable(
        simple_brick_model.query(
            """SELECT DISTINCT ?point WHERE {
    ?point rdf:type/rdfs:subClassOf* brick:Point .
    }"""
        )
    )
    assert len(res) == 6


def test_query_sensors(simple_brick_model):
    res = make_readable(
        simple_brick_model.query(
            """SELECT DISTINCT ?sensor WHERE {
    ?sensor rdf:type/rdfs:subClassOf* brick:Sensor .
    }"""
        )
    )
    assert len(res) == 4


def test_query_downstream_temperature(simple_brick_model):
    # temp sensors downstream of AHU1
    res = make_readable(
        simple_brick_model.query(
            """SELECT DISTINCT ?thing ?point WHERE {
    bldg:AHU1 (brick:feeds|brick:hasPart)* ?thing .
    ?thing (brick:hasPoint|brick:isLocationOf)  ?point .
    ?point rdf:type/rdfs:subClassOf* brick:Temperature_Sensor
    }"""
        )
    )
    assert len(res) == 2


def test_query_room_temp_sensors_ahu1(simple_brick_model):
    # temp sensors downstream of AHU1
    res = make_readable(
        simple_brick_model.query(
            """SELECT DISTINCT ?zone ?room ?sensor WHERE {
    bldg:AHU1 brick:feeds+ ?zone .
    ?zone brick:hasPart ?room .
    ?room rdf:type brick:Room .
    ?room brick:isLocationOf ?sensor .
    ?sensor rdf:type/rdfs:subClassOf* brick:Temperature_Sensor
    }"""
        )
    )
    assert len(res) == 1
