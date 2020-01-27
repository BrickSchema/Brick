import sys
sys.path.append('..')
from bricksrc.namespaces import BRICK, TAG, A, SKOS
from rdflib import RDF, RDFS, OWL, Namespace, Graph
import brickschema

BLDG = Namespace(f"https://brickschema.org/schema/ExampleBuilding#")

g = Graph()
g.parse('Brick.ttl', format='turtle')

# Instances
g.add((BLDG.Coil_1, A, BRICK.Heating_Coil))

g.add((BLDG.Coil_2, BRICK.hasTag, TAG.Coil))
g.add((BLDG.Coil_2, BRICK.hasTag, TAG.Heat))

g.add((BLDG.AHU1, A, BRICK.AHU))
g.add((BLDG.VAV1, A, BRICK.VAV))
g.add((BLDG.AHU1, BRICK.feedsAir, BLDG.VAV1))
g.add((BLDG.CH1, A, BRICK.Chiller))

# This gets inferred as an air temperature sensor
g.add((BLDG.TS1, A, BRICK.Temperature_Sensor))
g.add((BLDG.TS1, BRICK.measures, BRICK.Air))
g.add((BLDG.TS2, A, BRICK.Air_Temperature_Sensor))

# add air flow sensor
g.add((BLDG.AFS1, BRICK.hasTag, TAG.Air))
g.add((BLDG.AFS1, BRICK.hasTag, TAG.Flow))
g.add((BLDG.AFS1, BRICK.hasTag, TAG.Sensor))

g.add((BLDG.S1, BRICK.hasTag, TAG.Sensor))

# add air flow setpoint
# g.add((BLDG.AFSP1, A, BRICK.Setpoint))
g.add((BLDG.AFSP1, BRICK.hasTag, TAG.Air))
g.add((BLDG.AFSP1, BRICK.hasTag, TAG.Flow))
g.add((BLDG.AFSP1, BRICK.hasTag, TAG.Setpoint))

# add air flow setpoint limit
g.add((BLDG.MAFS1, BRICK.hasTag, TAG.Max))
g.add((BLDG.MAFS1, BRICK.hasTag, TAG.Air))
g.add((BLDG.MAFS1, BRICK.hasTag, TAG.Flow))
g.add((BLDG.MAFS1, BRICK.hasTag, TAG.Setpoint))
g.add((BLDG.MAFS1, BRICK.hasTag, TAG.Limit))
g.add((BLDG.MAFS1, BRICK.hasTag, TAG.Parameter))

g.add((BLDG.AFS2, A, BRICK.Air_Flow_Sensor))

g.add((BLDG.co2s1, A, BRICK.CO2_Level_Sensor))

g.add((BLDG.standalone, A, BRICK.Temperature_Sensor))

# Apply reasoner
g = brickschema.inference.TagInferenceSession(load_brick=False, approximate=False).expand(g)
g = brickschema.inference.OWLRLAllegroInferenceSession(load_brick=False).expand(g)

g.bind('rdf', RDF)
g.bind('owl', OWL)
g.bind('rdfs', RDFS)
g.bind('skos', SKOS)
g.bind('brick', BRICK)
g.bind('tag', TAG)
g.bind('bldg', BLDG)

s = g.serialize('output.ttl', format='ttl')
print('expanded:', len(g))

def make_readable(res):
    return [[uri.split('#')[-1] for uri in row] for row in res]

def test_tag1():
    res1 = make_readable(g.query("SELECT DISTINCT ?co2tag WHERE {\
                                   bldg:co2s1 brick:hasTag ?co2tag\
                                  }"))
    assert len(res1) == 3


def test_sensors_measure_co2():
    # which sensors measure CO2?
    res2 = make_readable(g.query("SELECT DISTINCT ?sensor WHERE {\
                                    ?sensor brick:measures brick:CO2\
                                  }"))
    assert len(res2) == 1


def test_sensors_measure_air():
    # measure air? use abbreviated form too
    res3 = make_readable(g.query("SELECT DISTINCT ?sensor WHERE {\
                                    ?sensor brick:measures brick:Air\
                                  }"))
    assert len(res3) == 5


def test_sensors_measure_air_temp():
    # sensors that measure air temperature
    res4 = make_readable(g.query("SELECT DISTINCT ?sensor WHERE {\
                                    ?sensor brick:measures brick:Air .\
                                    ?sensor rdf:type brick:Temperature_Sensor\
                                  }"))
    assert len(res4) == 2


def test_air_flow_sensor():
    # air flow sensors
    res = make_readable(g.query("SELECT DISTINCT ?sensor WHERE {\
                                    ?sensor rdf:type brick:Air_Flow_Sensor\
                                 }"))
    assert len(res) == 2


def test_air_flow_sp():
    # air flow setpoints
    res = make_readable(g.query("SELECT DISTINCT ?sp WHERE {\
                                    ?sp rdf:type brick:Air_Flow_Setpoint\
                                 }"))
    assert len(res) == 1

def test_sp():
    # setpoints
    res = make_readable(g.query("SELECT DISTINCT ?sp WHERE {\
                                    ?sp rdf:type brick:Setpoint\
                                 }"))
    assert len(res) == 1

def test_max_air_flow_sp():
    # air flow setpoints
    res = make_readable(g.query("SELECT DISTINCT ?sp WHERE {\
                                    ?sp rdf:type brick:Max_Air_Flow_Setpoint_Limit\
                                 }"))
    assert len(res) == 1

def test_air_flow_sensor2():
    # air flow sensors
    res = make_readable(g.query("SELECT DISTINCT ?sensor WHERE {\
                                    ?sensor brick:hasTag tag:Air .\
                                    ?sensor brick:hasTag tag:Sensor .\
                                    ?sensor brick:hasTag tag:Flow\
                                 }"))
    assert len(res) == 2
