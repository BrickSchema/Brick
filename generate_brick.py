import logging
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

logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
        level=logging.DEBUG)

G = Graph()
bind_prefixes(G)
A = RDF.type

tag_lookup = defaultdict(set)
intersection_classes = {}


def add_restriction(klass, definition):
    if len(definition) == 0:
        return
    elements = []
    equivalent_class = BNode()
    list_name = BNode()
    for idnum, item in enumerate(definition):
        restriction = BNode()
        elements.append(restriction)
        G.add((restriction, A, OWL.Restriction))
        G.add((restriction, OWL.onProperty, item[0]))
        G.add((restriction, OWL.hasValue, item[1]))
    G.add((BRICK[klass], OWL.equivalentClass, equivalent_class))
    G.add((equivalent_class, OWL.intersectionOf, list_name))
    Collection(G, list_name, elements)


def has_tags(tagset, definition):
    return all([t in definition for t in tagset])


def add_tags(klass, definition):
    if len(definition) == 0:
        return
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
    return [klass for tagset, klass in tag_lookup.items()
            if s.issubset(set(tagset))]


def define_measurable_subclasses(definitions, measurable_class):
    for subclass, properties in definitions.items():
        G.add((BRICK[subclass], A, OWL.Class))
        G.add((BRICK[subclass], A, BRICK[subclass]))
        G.add((BRICK[subclass], RDFS.label, Literal(subclass.replace("_"," "))))
        # first level: we are instances of the measurable_class
        G.add((BRICK[subclass], A, measurable_class))
        G.add((BRICK[subclass], RDFS.subClassOf, measurable_class))
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


def define_classes(definitions, parent):
    """
    Generates triples for the hierarchy given by 'definitions', rooted
    at the class given by 'parent'
    - class hierarchy ('subclasses')
    - tag mappings
    - substance + quantity modeling
    """
    for classname, defn in definitions.items():
        classname = BRICK[classname]
        # class is a owl:Class
        G.add((classname, A, OWL.Class))
        # subclass of parent
        G.add((classname, RDFS.subClassOf, parent))

        # define mapping to tags if it exists
        # "tags" property is a list of URIs naming Tags
        taglist = defn.get('tags', [])
        assert isinstance(taglist, list)
        if len(taglist) == 0:
            logging.warning(f"Property 'tags' not defined for {classname}")
        add_tags(classname, taglist)

        # define mapping to substances + quantities if it exists
        # "substances" property is a list of (predicate, object) pairs
        substancedef = defn.get('substances', [])
        assert isinstance(substancedef, list)
        add_restriction(classname, substancedef)

        # define class structure
        # this is a nested dictionary
        subclassdef = defn.get('subclasses', {})
        assert isinstance(subclassdef, dict)
        define_classes(subclassdef, classname)

        # handle 'parents' subclasses (links outside of tree-based hierarchy)
        parents = defn.get('parents', [])
        assert isinstance(parents, list)
        for parent in parents:
            G.add((classname, RDFS.subClassOf, parent))

        # all other key-value pairs in the definition are
        # property-object pairs
        expected_properties = ['parents', 'tags', 'substances', 'subclasses']
        other_properties = [prop for prop in defn.keys()
                            if prop not in expected_properties]
        for propname in other_properties:
            propval = defn[propname]
            if isinstance(propval, str):
                propval = Brick[propval]
            G.add((classname, propname, propval))


def apply_prop(prop, pred, obj):
    if isinstance(obj, Literal):
        G.add((BRICK[prop], pred, obj))
        return True
    elif isinstance(obj, URIRef):
        G.add((BRICK[prop], pred, obj))
        return True
    elif isinstance(obj, str):
        G.add((BRICK[prop], pred, BRICK[obj]))
        return True
    elif isinstance(obj, list):
        for l in obj:
            apply_prop(prop, pred, l)
        return True
    return False


def define_properties(definitions, superprop=None):
    for prop, propdef in definitions.items():
        G.add((BRICK[prop], A, OWL.ObjectProperty))
        if superprop is not None:
            G.add((BRICK[prop], RDFS.subPropertyOf, superprop))
        for k, v in propdef.items():
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
        # "tags": [TAG.Point],
    },
    "Measurable": {},
}
G.add((BRICK.Class, A, OWL.Class))
G.add((BRICK.Tag, A, OWL.Class))

# define root classes
define_classes(roots, BRICK.Class)

# define BRICK properties
define_properties(properties)

# define Point subclasses
define_classes(setpoint_definitions, BRICK.Point)
define_classes(sensor_definitions, BRICK.Point)
define_classes(alarm_definitions, BRICK.Point)
define_classes(status_definitions, BRICK.Point)
define_classes(command_definitions, BRICK.Point)
define_classes(parameter_definitions, BRICK.Point)
# make points disjoint
pointclasses = ['Alarm', 'Status', 'Command', 'Setpoint', 'Sensor', 'Parameter']
for pc in pointclasses:
    for o in filter(lambda x: x != pc, pointclasses):
        G.add((BRICK[pc], OWL.disjointWith, BRICK[o]))

# define other root class structures
define_classes(location_subclasses, BRICK.Location)
define_classes(equipment_subclasses, BRICK.Equipment)
define_classes(hvac_subclasses, BRICK.HVAC)
define_classes(valve_subclasses, BRICK.Valve)

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
