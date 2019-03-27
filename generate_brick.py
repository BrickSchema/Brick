from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.collection import Collection
from rdflib.extras.infixowl import Restriction

BRICK = Namespace("https://brickschema.org/schema/1.0.3/Brick#")
BRICKTAG = Namespace("https://brickschema.org/schema/1.0.3/BrickTag#")
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
G.bind('bricktag', BRICKTAG)
G.bind('bldg', BLDG)

A = RDF.type

def define_subclasses(definitions, superclass):
    for subclass, properties in definitions.items():
        G.add( (BRICK[subclass], A, OWL.Class) )
        G.add( (BRICK[subclass], RDFS.subClassOf, superclass) )
        for k, v in properties.items():
            if not apply_prop(subclass, k, v):
                if isinstance(v, dict) and k == "subclasses":
                    define_subclasses(v, BRICK[subclass])

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
            if not apply_prop(prop, k, v):
                if isinstance(v, dict) and k == "subproperties":
                    define_properties(v, BRICK[prop])


"""
Declare root classes
"""
G.add( (BRICK.Equipment, A, OWL.Class) )
G.add( (BRICK.Location, A, OWL.Class) )
G.add( (BRICK.Point, A, OWL.Class) )
G.add( (BRICK.Tag, A, OWL.Class) )
G.add( (BRICK.Substance, A, OWL.Class) )

from point import point_definitions
define_subclasses(point_definitions, BRICK.Point)

from location import location_subclasses
define_subclasses(location_subclasses, BRICK.Location)

from equipment import equipment_subclasses, hvac_subclasses, valve_subclasses
define_subclasses(equipment_subclasses, BRICK.Equipment)
define_subclasses(hvac_subclasses, BRICK.HVAC)
define_subclasses(valve_subclasses, BRICK.Valve)

from substances import substances
define_subclasses(substances, BRICK.Substance)

from properties import properties
define_properties(properties)

tags = {
    "Coil": {},
    "Valve": {},

    "Heat": {},
    "Cool": {},

    # substance tags
    "Air": {},
    "Steam": {},
    "Ice": {},
}

for tag, definition in tags.items():
    G.add( (BRICKTAG[tag], A, BRICK.Tag) )

# trying our own restrictions
r = {
    "Coil": [
        [ BRICK.hasTag, BRICKTAG.Coil ],
    ],
    "Heating_Coil": [
        [ BRICK.hasTag, BRICKTAG.Coil ],
        [ BRICK.hasTag, BRICKTAG.Heat ],
    ],
    "Cooling_Coil": [
        [ BRICK.hasTag, BRICKTAG.Coil ],
        [ BRICK.hasTag, BRICKTAG.Cool ],
    ]
}
#TODO: for "and" need to use an owl intersection
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

for k, v in r.items():
    add_restriction(k, v)

#r = Restriction(BRICK.hasTag, graph=G, value=BRICK.Valve)
#r.serialize(graph=G)

## Instances
G.add( (BLDG.Coil_1, A, BRICK.Heating_Coil) )

G.add( (BLDG.Coil_2, BRICK.hasTag, BRICKTAG.Coil) )
G.add( (BLDG.Coil_2, BRICK.hasTag, BRICKTAG.Heat) )

s = G.serialize(format='ttl')
print(len(G))

with open('Brick.ttl','wb') as f:
    f.write(s)
