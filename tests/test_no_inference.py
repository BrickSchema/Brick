# Set of tests to demonstrate use of Brick *without* the use of a reasoner
import brickschema
from rdflib import RDF, RDFS, OWL, Namespace
from .util import make_readable
import sys

sys.path.append("..")
from bricksrc.namespaces import BRICK, TAG, SKOS, A  # noqa: E402

BLDG = Namespace("https://brickschema.org/schema/ExampleBuilding#")

g = brickschema.Graph()
g.load_file("Brick.ttl")
g.bind("rdf", RDF)
g.bind("owl", OWL)
g.bind("rdfs", RDFS)
g.bind("skos", SKOS)
g.bind("brick", BRICK)
g.bind("tag", TAG)
g.bind("bldg", BLDG)

# Create instances
g.add((BLDG.Coil_1, A, BRICK.Heating_Coil))
g.add((BLDG.AHU1, A, BRICK.Air_Handler_Unit))
g.add((BLDG.VAV1, A, BRICK.Variable_Air_Volume_Box))
g.add((BLDG.CH1, A, BRICK.Chiller))

# locations
g.add((BLDG.Zone1, A, BRICK.HVAC_Zone))
g.add((BLDG.Room1, A, BRICK.Room))
g.add((BLDG.Room2, A, BRICK.Room))

# points
g.add((BLDG.TS1, A, BRICK.Air_Temperature_Sensor))
g.add((BLDG.TS2, A, BRICK.Air_Temperature_Sensor))
g.add((BLDG.AFS1, A, BRICK.Air_Flow_Sensor))
g.add((BLDG.co2s1, A, BRICK.CO2_Level_Sensor))

g.add((BLDG.AFSP1, A, BRICK.Air_Flow_Setpoint))

g.add((BLDG.MAFS1, A, BRICK.High_Setpoint_Limit))

# establishing some relationships
g.add((BLDG.CH1, BRICK.feeds, BLDG.AHU1))
g.add((BLDG.AHU1, BRICK.feeds, BLDG.VAV1))
g.add((BLDG.VAV1, BRICK.hasPoint, BLDG.TS2))
g.add((BLDG.VAV1, BRICK.hasPoint, BLDG.AFS1))
g.add((BLDG.VAV1, BRICK.hasPoint, BLDG.AFSP1))

g.add((BLDG.VAV1, BRICK.feeds, BLDG.Zone1))
g.add((BLDG.Zone1, BRICK.hasPart, BLDG.Room1))
g.add((BLDG.Zone1, BRICK.hasPart, BLDG.Room2))

g.add((BLDG.TS1, BRICK.hasLocation, BLDG.Room1))

# lets us use both relationships
g.expand(profile="owlrl")


def test_query_equipment():
    res = make_readable(
        g.query(
            """SELECT DISTINCT ?equip WHERE {
    ?equip rdf:type/rdfs:subClassOf* brick:Equipment .
    }"""
        )
    )
    assert len(res) == 4


def test_query_points():
    res = make_readable(
        g.query(
            """SELECT DISTINCT ?point WHERE {
    ?point rdf:type/rdfs:subClassOf* brick:Point .
    }"""
        )
    )
    assert len(res) == 6


def test_query_sensors():
    res = make_readable(
        g.query(
            """SELECT DISTINCT ?sensor WHERE {
    ?sensor rdf:type/rdfs:subClassOf* brick:Sensor .
    }"""
        )
    )
    assert len(res) == 4


def test_query_downstream_temperature():
    # temp sensors downstream of AHU1
    res = make_readable(
        g.query(
            """SELECT DISTINCT ?thing ?point WHERE {
    bldg:AHU1 (brick:feeds|brick:hasPart)* ?thing .
    ?thing (brick:hasPoint|brick:isLocationOf)  ?point .
    ?point rdf:type/rdfs:subClassOf* brick:Temperature_Sensor
    }"""
        )
    )
    assert len(res) == 2


def test_query_room_temp_sensors_ahu1():
    # temp sensors downstream of AHU1
    res = make_readable(
        g.query(
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
