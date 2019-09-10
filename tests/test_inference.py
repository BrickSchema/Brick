import time
import sys
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

## Instances
G.add( (BLDG.Coil_1, A, BRICK.Heating_Coil) )

G.add( (BLDG.Coil_2, BRICK.hasTag, TAG.Coil) )
G.add( (BLDG.Coil_2, BRICK.hasTag, TAG.Heat) )

G.add( (BLDG.AHU1, A, BRICK.AHU) )
G.add( (BLDG.VAV1, A, BRICK.VAV) )
G.add( (BLDG.AHU1, BRICK.feedsAir, BLDG.VAV1) )
G.add( (BLDG.CH1, A, BRICK.Chiller) )

# This gets inferred as an air temperature sensor
G.add( (BLDG.TS1, A, BRICK.Temperature_Sensor) )
G.add( (BLDG.TS1, BRICK.measures, BRICK.Air) )
G.add( (BLDG.TS2, A, BRICK.Air_Temperature_Sensor) )

# add air flow setpoint
G.add( (BLDG.AFSP1, A, BRICK.Setpoint) )
G.add( (BLDG.AFSP1, BRICK.hasTag, TAG.Air) )
G.add( (BLDG.AFSP1, BRICK.hasTag, TAG.Flow) )
G.add( (BLDG.AFSP1, BRICK.hasTag, TAG.Setpoint) )

# add air flow setpoint limit
G.add( (BLDG.MAFS1, A, BRICK.Setpoint) )
G.add( (BLDG.MAFS1, BRICK.hasTag, TAG.Air) )
G.add( (BLDG.MAFS1, BRICK.hasTag, TAG.Flow) )
G.add( (BLDG.MAFS1, BRICK.hasTag, TAG.Setpoint) )
G.add( (BLDG.MAFS1, BRICK.hasTag, TAG.Limit) )
G.add( (BLDG.MAFS1, BRICK.hasTag, TAG.Max) )

G.add( (BLDG.AFS1, A, BRICK.Air_Flow_Sensor) )

G.add( (BLDG.co2s1, A, BRICK.CO2_Level_Sensor) )

G.add( (BLDG.standalone, A, BRICK.Temperature_Sensor) )

# Apply reasoner
from util.reasoner import reason_rdfs
reason_rdfs(G)

G.bind('rdf', RDF)
G.bind('owl', OWL)
G.bind('rdfs', RDFS)
G.bind('skos', SKOS)
G.bind('brick', BRICK)
G.bind('tag', TAG)
G.bind('bldg', BLDG)

s = G.serialize(format='ttl')
print('expanded:', len(G))

with open('Brick_expanded.ttl','wb') as f:
    f.write(s)

# now you can query!
# ipython -i generate_brick.py

def make_readable(res):
    return [[uri.split('#')[-1] for uri in row] for row in res]

def test_tag1():
    res1 = make_readable(G.query("SELECT DISTINCT ?co2tag WHERE { bldg:co2s1 brick:hasTag ?co2tag }"))
    assert len(res1) == 3

def test_sensors_measure_co2():
    # which sensors measure CO2?
    res2 = make_readable(G.query("SELECT DISTINCT ?sensor WHERE { ?sensor brick:measures brick:CO2 }"))
    assert len(res2) == 1

def test_sensors_measure_air():
    # measure air? use abbreviated form too
    res3 = make_readable(G.query("SELECT DISTINCT ?sensor WHERE { ?sensor brick:measures brick:Air }"))
    assert len(res3) == 4

def test_sensors_measure_air_temp():
    # sensors that measure air temperature
    res4 = make_readable(G.query("SELECT DISTINCT ?sensor WHERE { ?sensor brick:measures brick:Air . ?sensor rdf:type brick:Temperature_Sensor }"))
    assert len(res4) == 2

def test_air_flow_sensor():
    # air flow sensors
    res = make_readable(G.query("SELECT DISTINCT ?sensor WHERE { ?sensor rdf:type brick:Air_Flow_Sensor }"))
    assert len(res) == 1

def test_air_flow_sp():
    # air flow setpoints
    res = make_readable(G.query("SELECT DISTINCT ?sp WHERE { ?sp rdf:type brick:Air_Flow_Setpoint }"))
    assert len(res) == 2

def test_air_flow_sensor2():
    # air flow sensors
    res = make_readable(G.query("SELECT DISTINCT ?sensor WHERE { ?sensor brick:hasTag tag:Air . ?sensor brick:hasTag tag:Sensor . ?sensor brick:hasTag tag:Flow }"))
    assert len(res) == 1
