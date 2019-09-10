"""
Set of tests to demonstrate use of Brick *without* the use of a reasoner
"""

import rdflib
from rdflib import RDF, RDFS, OWL, Namespace

BRICK_VERSION = '1.1.0'

BRICK = Namespace("https://brickschema.org/schema/{0}/Brick#".format(BRICK_VERSION))
TAG = Namespace("https://brickschema.org/schema/{0}/BrickTag#".format(BRICK_VERSION))
BLDG = Namespace("https://brickschema.org/schema/{0}/ExampleBuilding#".format(BRICK_VERSION))
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
DCTERMS = Namespace("http://purl.org/dc/terms#")
SDO = Namespace("http://schema.org#")
A = RDF.type

G = rdflib.Graph()
G.parse('Brick.ttl', format='turtle')
G.bind('rdf', RDF)
G.bind('owl', OWL)
G.bind('rdfs', RDFS)
G.bind('skos', SKOS)
G.bind('brick', BRICK)
G.bind('tag', TAG)
G.bind('bldg', BLDG)

# Create instances
G.add( (BLDG.Coil_1, A, BRICK.Heating_Coil) )
G.add( (BLDG.AHU1, A, BRICK.Air_Handler_Unit) )
G.add( (BLDG.VAV1, A, BRICK.Variable_Air_Volume_Box) )
G.add( (BLDG.CH1, A, BRICK.Chiller) )

# locations
G.add( (BLDG.Zone1, A, BRICK.HVAC_Zone) )
G.add( (BLDG.Room1, A, BRICK.Room) )
G.add( (BLDG.Room2, A, BRICK.Room) )

# points
G.add( (BLDG.TS1, A, BRICK.Air_Temperature_Sensor) )
G.add( (BLDG.TS2, A, BRICK.Air_Temperature_Sensor) )
G.add( (BLDG.AFS1, A, BRICK.Air_Flow_Sensor) )
G.add( (BLDG.co2s1, A, BRICK.CO2_Level_Sensor) )

G.add( (BLDG.AFSP1, A, BRICK.Air_Flow_Setpoint) )

G.add( (BLDG.MAFS1, A, BRICK.Max_Air_Flow_Setpoint_Limit) )

# establishing some relationships
G.add( (BLDG.CH1, BRICK.feeds, BLDG.AHU1) )
G.add( (BLDG.AHU1, BRICK.feeds, BLDG.VAV1) )
G.add( (BLDG.VAV1, BRICK.hasPoint, BLDG.TS2) )
G.add( (BLDG.VAV1, BRICK.hasPoint, BLDG.AFS1) )
G.add( (BLDG.VAV1, BRICK.hasPoint, BLDG.AFSP1) )

G.add( (BLDG.VAV1, BRICK.feeds, BLDG.Zone1) )
G.add( (BLDG.Zone1, BRICK.hasPart, BLDG.Room1) )
G.add( (BLDG.Zone1, BRICK.hasPart, BLDG.Room2) )

G.add( (BLDG.TS1, BRICK.hasLocation, BLDG.Room1) )

# applies simple, cheap transformations
from util.reasoner import reason_classic
reason_classic(G)

def make_readable(res):
    return [[uri.split('#')[-1] for uri in row] for row in res]

def test_query_equipment():
    res = make_readable(G.query("""SELECT DISTINCT ?equip WHERE {
    ?equip rdf:type/rdfs:subClassOf* brick:Equipment .
    }"""))
    assert len(res) ==  4

def test_query_points():
    res = make_readable(G.query("""SELECT DISTINCT ?point WHERE {
    ?point rdf:type/rdfs:subClassOf* brick:Point .
    }"""))
    assert len(res) ==  6

def test_query_sensors():
    res = make_readable(G.query("""SELECT DISTINCT ?sensor WHERE {
    ?sensor rdf:type/rdfs:subClassOf* brick:Sensor .
    }"""))
    assert len(res) ==  4

def test_query_downstream_temperature():
    # temp sensors downstream of AHU1
    res = make_readable(G.query("""SELECT DISTINCT ?thing ?point WHERE {
    bldg:AHU1 (brick:feeds|brick:hasPart)* ?thing .
    ?thing (brick:hasPoint|brick:isLocationOf)  ?point .
    ?point rdf:type/rdfs:subClassOf* brick:Temperature_Sensor
    }"""))
    assert len(res) ==  2

def test_query_room_temp_sensors_ahu1():
    # temp sensors downstream of AHU1
    res = make_readable(G.query("""SELECT DISTINCT ?zone ?room ?sensor WHERE {
    bldg:AHU1 brick:feeds+ ?zone .
    ?zone brick:hasPart ?room .
    ?room rdf:type brick:Room .
    ?room brick:isLocationOf ?sensor .
    ?sensor rdf:type/rdfs:subClassOf* brick:Temperature_Sensor
    }"""))
    assert len(res) ==  1
