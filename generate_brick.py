from collections import defaultdict
from rdflib import Graph, Literal, BNode, URIRef
from rdflib.namespace import XSD
from rdflib.collection import Collection

from bricksrc.namespaces import BRICK, RDF, OWL, RDFS, TAG, SOSA
from bricksrc.namespaces import bind_prefixes

from bricksrc.setpoint import setpoint_definitions
from bricksrc.sensor import sensor_definitions
from bricksrc.alarm import alarm_definitions
from bricksrc.status import status_definitions
from bricksrc.command import command_definitions
from bricksrc.parameter import parameter_definitions
from bricksrc.location import location_subclasses
from bricksrc.equipment import equipment_subclasses, hvac_subclasses, valve_subclasses
from bricksrc.substances import substances
from bricksrc.quantities import quantity_definitions
from bricksrc.properties import properties
from bricksrc.tags import tags

G = Graph()
bind_prefixes(G)
A = RDF.type
tag_lookup = defaultdict(set)
intersection_classes = {}

# helps setup the restriction classes for having and not having tags
def make_tag_classes(G, tag):
    has_tag = BNode(f"has_{tag}")
    G.add((has_tag, A, OWL.Restriction))
    G.add((has_tag, RDFS.subClassOf, BRICK.Class))
    G.add((has_tag, OWL.hasValue, TAG[tag]))
    G.add((has_tag, OWL.onProperty, BRICK.hasTag))

    has_no_tag = BNode(f"has_no_{tag}")
    G.add((has_no_tag, RDFS.subClassOf, BRICK.Class))
    G.add((has_no_tag, OWL.complementOf, has_tag))
    return has_tag, has_no_tag

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
    all_restrictions = []
    equivalent_class = BNode()
    list_name = BNode()

    for tag in definition:
        G.add((BRICK[klass], BRICK.hasAssociatedTag, tag))

    for idnum, item in enumerate(definition):
        restriction = BNode(f"has_{item.split('#')[-1]}")
        all_restrictions.append(restriction)
        G.add((restriction, A, OWL.Restriction))
        G.add((restriction, OWL.onProperty, BRICK.hasTag))
        G.add((restriction, OWL.hasValue, item))
        G.add((item, A, BRICK.Tag)) # make sure the tag is declared as such
        G.add((item, RDFS.label, Literal(item.split('#')[-1]))) # make sure the tag is declared as such

    # tag index
    tagset = tuple(sorted([item.split('#')[-1] for item in definition]))
    tag_lookup[tagset].add(klass)

    # if we've already mapped this class, don't map it again
    if klass in intersection_classes:
        return
    if len(all_restrictions) == 1:
        G.add( (BRICK[klass], RDFS.subClassOf, all_restrictions[0]) )
    if len(all_restrictions) > 1:
        G.add( (BRICK[klass], RDFS.subClassOf, equivalent_class) )
        G.add( (equivalent_class, OWL.intersectionOf, list_name) )
        Collection(G, list_name, all_restrictions)
    intersection_classes[klass] = tuple(sorted(definition))

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
        G.add((superclass, A, OWL.Class))
        G.add((BRICK[subclass], A, OWL.Class))
        G.add((BRICK[subclass], RDFS.label, Literal(subclass.replace("_"," "))))
        G.add((BRICK[subclass], RDFS.subClassOf, superclass))
        for k, v in properties.items():
            if isinstance(v, list) and k == "tags":
                add_tags(subclass, v)
            elif isinstance(v, list) and k == "parents":
                for parent in v:
                    G.add( (BRICK[subclass], RDFS.subClassOf, parent) )
            elif isinstance(v, list) and k == "substances":
                add_restriction(subclass, v)
            elif not apply_prop(subclass, k, v):
                if isinstance(v, dict) and k == "subclasses":
                    define_subclasses(v, BRICK[subclass])

def define_measurable_subclasses(definitions, measurable_class):
    for subclass, properties in definitions.items():
        G.add((BRICK[subclass], A, OWL.Class))
        G.add((BRICK[subclass], A, BRICK[subclass]))
        G.add((BRICK[subclass], RDFS.label, Literal(subclass.replace("_"," "))))
        # first level: we are instances of the measurable_class
        G.add((BRICK[subclass], A, measurable_class))
        for k, v in properties.items():
            if isinstance(v, list) and k == "tags":
                add_tags(subclass, v)
            elif isinstance(v, list) and k == "parents":
                for parent in v:
                    G.add( (BRICK[subclass], RDFS.subClassOf, parent) )
            elif isinstance(v, list) and k == "substances":
                add_restriction(subclass, v)
            elif not apply_prop(subclass, k, v):
                if isinstance(v, dict) and k == "subclasses":
                    define_measurable_subclasses(v, BRICK[subclass])

def define_rootclasses(definitions):
    G.add( (BRICK.Class, A, OWL.Class) )
    G.add( (BRICK.Tag, A, OWL.Class) )
    for rootclass, properties in definitions.items():
        G.add( (BRICK[rootclass], A, OWL.Class) )
        G.add( (BRICK[rootclass], RDFS.subClassOf, BRICK.Class) )
        for k, v in properties.items():
            if isinstance(v, list) and k == "tags":
                add_tags(rootclass, v)
            elif isinstance(v, list) and k == "substances":
                add_class_restriction(rootclass, v)
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
from bricksrc.ontology import define_ontology
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
    "Measurable": {},
}
# define root classes
define_rootclasses(roots)

# define BRICK properties
define_properties(properties)

# define Point subclasses
define_subclasses(setpoint_definitions, BRICK.Point)
define_subclasses(sensor_definitions, BRICK.Point)
define_subclasses(alarm_definitions, BRICK.Point)
define_subclasses(status_definitions, BRICK.Point)
define_subclasses(command_definitions, BRICK.Point)
define_subclasses(parameter_definitions, BRICK.Point)
# make points disjoint
pointclasses = ['Alarm', 'Status', 'Command', 'Setpoint', 'Sensor', 'Parameter']
for pc in pointclasses:
    for o in filter(lambda x: x != pc, pointclasses):
        G.add((BRICK[pc], OWL.disjointWith, BRICK[o]))

# define other root class structures
define_subclasses(location_subclasses, BRICK.Location)
define_subclasses(equipment_subclasses, BRICK.Equipment)
define_subclasses(hvac_subclasses, BRICK.HVAC)
define_subclasses(valve_subclasses, BRICK.Valve)

G.add((BRICK.Measurable, RDFS.subClassOf, BRICK.Class))
# set up Quantity definition
G.add((BRICK.Quantity, RDFS.subClassOf, SOSA.ObservableProperty))
G.add((BRICK.Quantity, RDFS.subClassOf, BRICK.Measurable))
G.add((BRICK.Quantity, A, OWL.Class))
# set up Substance definition
G.add((BRICK.Substance, RDFS.subClassOf, SOSA.FeatureOfInterest))
G.add((BRICK.Substance, RDFS.subClassOf, BRICK.Measurable))
G.add((BRICK.Substance, A, OWL.Class))

# We make the punning explicit here. Any subclass of brick:Substance
# or brick:Quantity is itself a substance or quantity. There is one canonical
# instance of each class, which is indicated by referencing the class itself.
#
#    bldg:tmp1      a           brick:Air_Temperature_Sensor;
#               brick:measures  brick:Air ,
#                               brick:Temperature .
# This makes Substance and Quantity metaclasses.
define_measurable_subclasses(substances, BRICK.Substance)
define_measurable_subclasses(quantity_definitions, BRICK.Quantity)

different_tag_list = []
# define tags
for tag, definition in tags.items():
    different_tag_list.append(TAG[tag])
    G.add((TAG[tag], A, BRICK.Tag))

# declares that all tags are pairwise different; i.e. no two tags refer
# to the same tag
different_tag = BNode("tags_are_different")
G.add((BRICK.Tag, A, OWL.AllDifferent))
G.add((BRICK.Tag, OWL.distinctMembers, different_tag))
Collection(G, different_tag, different_tag_list)

# serialize to output
print('base:',len(G))
G.serialize('Brick.ttl', format='turtle')
