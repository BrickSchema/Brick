from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import XSD
from rdflib.collection import Collection
from rdflib.extras.infixowl import Restriction

BRICK = Namespace("https://brickschema.org/schema/1.0.3/Brick#")
TAG = Namespace("https://brickschema.org/schema/1.0.3/BrickTag#")
BLDG = Namespace("https://brickschema.org/schema/1.0.3/ExampleBuilding#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")

G = Graph()
G.bind('rdf', RDF)
G.bind('owl', OWL)
G.bind('rdfs', RDFS)
G.bind('skos', SKOS)
G.bind('brick', BRICK)
G.bind('tag', TAG)
G.bind('bldg', BLDG)

A = RDF.type

#syntax for protege: http://protegeproject.github.io/protege/class-expression-syntax/
def add_restriction(klass, definition):
    l = []
    equivalent_class = BNode()
    list_name = BNode()
    for idnum, item in enumerate(definition):
        restriction = BNode()
        l.append(restriction)
        G.add( (restriction, A, OWL.Restriction) )
        G.add( (restriction, OWL.onProperty, item[0]) )
        G.add( (restriction, OWL.hasValue, item[1]) )
    G.add( (BRICK[klass], OWL.equivalentClass, equivalent_class) )
    G.add( (equivalent_class, OWL.intersectionOf, list_name) )
    c = Collection(G, list_name, l)

def add_tags(klass, definition):
    l = []
    equivalent_class = BNode()
    list_name = BNode()
    for idnum, item in enumerate(definition):
        restriction = BNode()
        l.append(restriction)
        G.add( (restriction, A, OWL.Restriction) )
        G.add( (restriction, OWL.onProperty, BRICK.hasTag) )
        G.add( (restriction, OWL.hasValue, item) )
        G.add( (item, A, BRICK.Tag) ) # make sure the tag is declared as such
    G.add( (BRICK[klass], OWL.equivalentClass, equivalent_class) )
    G.add( (equivalent_class, OWL.intersectionOf, list_name) )
    c = Collection(G, list_name, l)

def add_class_restriction(klass, definition):
    l = []
    equivalent_class = BNode()
    list_name = BNode()
    for idnum, item in enumerate(definition):
        restriction = BNode()
        l.append(restriction)
        G.add( (restriction, A, OWL.Restriction) )
        G.add( (restriction, OWL.onProperty, item[0]) )
        G.add( (restriction, item[1], item[2]) )
        if len(item) == 5:
            G.add( (restriction, item[3], Literal('{0}'.format(item[4]), datatype=XSD.integer)) )
    G.add( (BRICK[klass], OWL.equivalentClass, equivalent_class) )
    G.add( (equivalent_class, OWL.intersectionOf, list_name) )
    c = Collection(G, list_name, l)

def define_subclasses(definitions, superclass):
    for subclass, properties in definitions.items():
        G.add( (BRICK[subclass], A, OWL.Class) )
        G.add( (BRICK[subclass], RDFS.subClassOf, superclass) )
        for k, v in properties.items():
            if isinstance(v, list) and k == "tagvalues":
                add_restriction(subclass, v)
            elif isinstance(v, list) and k == "tags":
                add_tags(subclass, v)
            elif isinstance(v, list) and k == "substances":
                add_restriction(subclass, v)
            elif not apply_prop(subclass, k, v):
                if isinstance(v, dict) and k == "subclasses":
                    define_subclasses(v, BRICK[subclass])

def define_rootclasses(definitions):
    for rootclass, properties in definitions.items():
        G.add( (BRICK[rootclass], A, OWL.Class) )
        for k, v in properties.items():
            if isinstance(v, list) and k == "tagvalues":
                add_restriction(rootclass, v)
            elif isinstance(v, list) and k == "tags":
                add_tags(rootclass, v)
            elif isinstance(v, list) and k == "substances":
                add_class_restriction(subclass, v)
            elif not apply_prop(rootclass, k, v):
                if isinstance(v, dict) and k == "subclasses":
                    define_subclasses(v, BRICK[rootclass])

def apply_prop(prop, pred, obj):
    if isinstance(obj, Literal):
        G.add( (BRICK[prop], pred, obj) )
        return True
    elif isinstance(obj, URIRef):
        G.add( (BRICK[prop], pred, obj) )
        return True
    elif isinstance(obj, str):
        G.add( (BRICK[prop], pred, BRICK[obj]) )
        return True
    elif isinstance(obj, list):
        for l in obj:
            apply_prop(prop, pred, l)
        return True
    return False

def define_properties(definitions, superprop=None):
    for prop, properties in definitions.items():
        G.add( (BRICK[prop], A, OWL.ObjectProperty) )
        if superprop is not None:
            G.add( (BRICK[prop], RDFS.subPropertyOf, superprop) )
        for k, v in properties.items():
            #if k == "domain_value_prop":
            #    assert isinstance(v, list)
            #    domain_class = BNode()
            #    print("domain", prop, v, domain_class)
            #    add_restriction(domain_class, v)
            #    G.add( (BRICK[prop], RDFS.domain, domain_class) )
            #elif k == "range_value_prop":
            #    assert isinstance(v, list)
            #    range_class = BNode()
            #    add_restriction(range_class, v)
            #    G.add( (BRICK[prop], RDFS.range, range_class) )
            if not apply_prop(prop, k, v):
                if isinstance(v, dict) and k == "subproperties":
                    define_properties(v, BRICK[prop])


"""
Declare root classes
"""
roots = {
    "Equipment": {
        "tagvalues": [
            [BRICK.hasTag, TAG.Equip],
        ],
    },
    "Location": {
        "tagvalues": [
            [BRICK.hasTag, TAG.Loc],
        ],
    },
    "Point": {
        "tagvalues": [
            [BRICK.hasTag, TAG.Point],
        ],
    },
    "Tag": {},
    "Substance": {},
    "Quantity": {},
}
define_rootclasses(roots)

from point import point_definitions
define_subclasses(point_definitions, BRICK.Point)

from sensor import sensor_definitions
define_subclasses(sensor_definitions, BRICK.Point)

from status import status_definitions
define_subclasses(status_definitions, BRICK.Point)

from limit import limit_definitions
define_subclasses(limit_definitions, BRICK.Point)

from location import location_subclasses
define_subclasses(location_subclasses, BRICK.Location)

from equipment import equipment_subclasses, hvac_subclasses, valve_subclasses
define_subclasses(equipment_subclasses, BRICK.Equipment)
define_subclasses(hvac_subclasses, BRICK.HVAC)
define_subclasses(valve_subclasses, BRICK.Valve)

from substances import substances
define_subclasses(substances, BRICK.Substance)

from quantities import quantity_definitions
define_subclasses(quantity_definitions, BRICK.Quantity)

from properties import properties
define_properties(properties)

from tags import tags
for tag, definition in tags.items():
    G.add( (TAG[tag], A, BRICK.Tag) )

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


G.add( (BLDG.AFS1, A, BRICK.Air_Flow_Sensor) )

G.add( (BLDG.co2s1, A, BRICK.CO2_Level_Sensor) )

G.add( (BLDG.standalone, A, BRICK.Temperature_Sensor) )


s = G.serialize(format='ttl')
print(len(G))

with open('Brick.ttl','wb') as f:
    f.write(s)

# Apply reasoner
import time
import owlrl
t1 = time.time()
owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(G)
t2 = time.time()
print("Reasoning took {0}".format(t2-t1))

# now you can query!
# ipython -i generate_brick.py

res1 = G.query("SELECT DISTINCT ?co2tag WHERE { bldg:co2s1 brick:hasTag ?co2tag }")
assert len(res1) == 3

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
