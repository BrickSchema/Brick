from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef, RDFS, OWL
from rdflib.namespace import XSD
from rdflib.collection import Collection
from rdflib.extras.infixowl import Restriction

from namespaces import BRICK, RDF, OWL, DCTERMS, SDO, RDFS, SKOS, BRICK, TAG, SOSA
from namespaces import bind_prefixes

G = Graph()
bind_prefixes(G)
A = RDF.type

from collections import defaultdict
tag_lookup = defaultdict(set)

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

def has_tags(tagset, definition):
    return all([t in definition for t in tagset])

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
        G.add( (item, RDFS.label, Literal(item.split('#')[-1])) ) # make sure the tag is declared as such

    # tag index
    tagset = tuple(sorted([item.split('#')[-1] for item in definition]))
    tag_lookup[tagset].add(klass)

    G.add( (BRICK[klass], OWL.equivalentClass, equivalent_class) )
    G.add( (equivalent_class, OWL.intersectionOf, list_name) )
    c = Collection(G, list_name, l)

def lookup_tagset(s):
    s = set(map(lambda x: x.capitalize(), s))
    return [klass for tagset, klass in tag_lookup.items() if s.issubset(set(tagset))]

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
        G.add( (BRICK[subclass], RDFS.label, Literal(subclass.replace("_"," "))) )
        G.add( (BRICK[subclass], RDFS.subClassOf, superclass) )
        for k, v in properties.items():
            if isinstance(v, list) and k == "tagvalues":
                add_restriction(subclass, v)
            elif isinstance(v, list) and k == "tags":
                add_tags(subclass, v)
            elif isinstance(v, list) and k == "parents":
                for parent in v:
                    G.add( (BRICK[subclass], RDFS.subClassOf, parent) )
            elif isinstance(v, list) and k == "substances":
                add_restriction(subclass, v)
            elif not apply_prop(subclass, k, v):
                if isinstance(v, dict) and k == "subclasses":
                    define_subclasses(v, BRICK[subclass])

def define_rootclasses(definitions):
    G.add( (BRICK.Class, A, OWL.Class) )
    G.add( (BRICK.Tag, A, OWL.Class) )
    for rootclass, properties in definitions.items():
        G.add( (BRICK[rootclass], A, OWL.Class) )
        G.add( (BRICK[rootclass], RDFS.subClassOf, BRICK.Class) )
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


# handle ontology definition
from ontology import define_ontology
define_ontology(G)

"""
Declare root classes
"""
roots = {
    "Equipment": {
        "tags": [TAG.Equipment],
    },
    "Location": {
        "tags": [TAG.Location],
    },
    "Point": {
        #"tags": [TAG.Point],
    },
    #"Tag": {},
    "Substance": {},
    "Quantity": {},
}
define_rootclasses(roots)

from setpoint import setpoint_definitions
define_subclasses(setpoint_definitions, BRICK.Point)

from sensor import sensor_definitions
define_subclasses(sensor_definitions, BRICK.Point)

from status import status_definitions
define_subclasses(status_definitions, BRICK.Point)

from command import command_definitions
define_subclasses(command_definitions, BRICK.Point)

from parameter import parameter_definitions
define_subclasses(parameter_definitions, BRICK.Point)

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

G.add((BRICK.Measurable, A, OWL.Class))
G.add((BRICK.Quantity, RDFS.subClassOf, SOSA.ObservableProperty))
G.add((BRICK.Substance, RDFS.subClassOf, SOSA.FeatureOfInterest))
G.add((BRICK.Substance, RDFS.subClassOf, BRICK.Measurable))
G.add((BRICK.Quantity, RDFS.subClassOf, BRICK.Measurable))

# We make the punning explicit here. Any subclass of brick:Substance
# or brick:Quantity is itself a substance or quantity. There is one canonical
# instance of each class, which is indicated by referencing the class itself.
#
#    bldg:tmp1      a           brick:Air_Temperature_Sensor;
#               brick:measures  brick:Air ,
#                               brick:Temperature .
#
# In the above example, brick:Air and brick:Temperature are both instances.
G.update("""INSERT { ?sc rdf:type brick:Substance }
            WHERE { ?sc rdfs:subClassOf+ brick:Substance }""")
G.update("""INSERT { ?qc rdf:type brick:Quantity }
            WHERE { ?qc rdfs:subClassOf+ brick:Quantity }""")

from properties import properties
define_properties(properties)

from tags import tags
for tag, definition in tags.items():
    G.add( (TAG[tag], A, BRICK.Tag) )

print('base:',len(G))
G.serialize('Brick.ttl', format='turtle')
