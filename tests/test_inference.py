import owlready2
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

def rereason(G, filename):
    world = owlready2.World()
    with open(filename,'wb') as f:
        f.write(G.serialize(format='ntriples'))
    on = world.get_ontology(f"file://./{filename}").load()
    owlready2.sync_reasoner(world, infer_property_values =True)
    G = world.as_rdflib_graph()
    G.bind('rdf', RDF)
    G.bind('owl', OWL)
    G.bind('rdfs', RDFS)
    G.bind('skos', SKOS)
    G.bind('brick', BRICK)
    G.bind('tag', TAG)
    G.bind('bldg', BLDG)
    return G

# Apply reasoner
import time
import owlrl
t1 = time.time()
try:
    G = rereason(G, "Brick.n3")
except:
    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(G)
t2 = time.time()
print("Reasoning took {0}".format(t2-t1))
s = G.serialize(format='ttl')
print('expanded:', len(G))

with open('Brick_expanded.ttl','wb') as f:
    f.write(s)

# now you can query!
# ipython -i generate_brick.py

res1 = G.query("SELECT DISTINCT ?co2tag WHERE { bldg:co2s1 brick:hasTag ?co2tag }")
print(list(res1))
#assert len(res1) == 3

# which sensors measure CO2?
res2 = G.query("SELECT DISTINCT ?sensor WHERE { ?sensor brick:measures brick:CO2 }")
print('CO2 sensors: ', list(res2))

# measure air? use abbreviated form too
res3 = G.query("SELECT DISTINCT ?sensor WHERE { ?sensor brick:measures brick:Air }")
print('Air sensors: ', list(res3))

# sensors that measure air temperature
res4 = G.query("SELECT DISTINCT ?sensor WHERE { ?sensor brick:measures brick:Air . ?sensor rdf:type brick:Temperature_Sensor }")
print('Air temperature sensors: ', list(res4))

# air flow sensors
res4 = G.query("SELECT DISTINCT ?sensor WHERE { ?sensor rdf:type brick:Air_Flow_Sensor }")
print('Air flow sensors (using class): ', list(res4))

# air flow setpoints
res5 = G.query("SELECT DISTINCT ?sp WHERE { ?sp rdf:type brick:Air_Flow_Setpoint }")
print('Air flow setpoints (using class): ', list(res5))

# air flow sensors
res4 = G.query("SELECT DISTINCT ?sensor WHERE { ?sensor brick:hasTag tag:Air . ?sensor brick:hasTag tag:Sensor . ?sensor brick:hasTag tag:Flow }")
print('Air flow sensors (using tags): ', list(res4))

q1 = """SELECT ?sen WHERE {
  ?sen  rdf:type  brick:Temperature_Sensor
  FILTER NOT EXISTS {
     ?sen rdf:type ?c .
     ?c rdfs:subClassOf+ brick:Temperature_Sensor .
     FILTER (?c != brick:Temperature_Sensor) .
     FILTER  (!isBlank(?c))
  }
}
"""
res5 = G.query(q1)
print('Only temperature sensors: ', list(res5))
