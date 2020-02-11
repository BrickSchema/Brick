import logging
from collections import defaultdict
from rdflib import Graph, Literal, BNode, URIRef
from rdflib.namespace import XSD
from rdflib.collection import Collection

from bricksrc.ontology import define_ontology

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

logging.basicConfig(
    format="%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.INFO,
)

G = Graph()
bind_prefixes(G)
A = RDF.type

tag_lookup = defaultdict(set)
intersection_classes = {}


def add_restriction(klass, definition):
    """
    Defines OWL.Restrictions linked to Brick classes
    through OWL.equivalentClass.

    This populates the property-object pairs (OWL.onProperty, 'property'),
    (OWL.hasValue, 'value'). The intersection of these properties is made to be
    equivalent to the given class.

    Args:
        klass: the URI of the Brick class to be modeled
        definition: a list of (property, value) pairs
    """
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
    G.add((klass, OWL.equivalentClass, equivalent_class))
    G.add((equivalent_class, OWL.intersectionOf, list_name))
    Collection(G, list_name, elements)


def add_tags(klass, definition):
    """
    Adds the definition of tags to the given class. This method adds two
    group of triples. The first group models the class as a subclass
    of entities that have all of the given tags (the 'OWL.intersectionOf'
    the OWL.Restriction classes modeled as entities that have a given tag).

    The second group of triples uses the BRICK.hasAssociatedTag property
    to associate the tags with this class. While this is duplicate information,
    it is much easier to query for.

    Args:
        klass: the URI of the Brick class to be modeled
        definition: a list of BRICK.Tag instances (e.g. TAG.Air)
    """
    if len(definition) == 0:
        return
    all_restrictions = []
    equivalent_class = BNode()
    list_name = BNode()

    for tag in definition:
        G.add((klass, BRICK.hasAssociatedTag, tag))

    for idnum, item in enumerate(definition):
        restriction = BNode(f"has_{item.split('#')[-1]}")
        all_restrictions.append(restriction)
        G.add((restriction, A, OWL.Restriction))
        G.add((restriction, OWL.onProperty, BRICK.hasTag))
        G.add((restriction, OWL.hasValue, item))
        G.add((item, A, BRICK.Tag))  # make sure the tag is declared as such
        G.add(
            (item, RDFS.label, Literal(item.split("#")[-1]))
        )  # make sure the tag is declared as such

    # tag index
    tagset = tuple(sorted([item.split("#")[-1] for item in definition]))
    tag_lookup[tagset].add(klass)

    # if we've already mapped this class, don't map it again
    if klass in intersection_classes:
        return
    if len(all_restrictions) == 1:
        G.add((klass, RDFS.subClassOf, all_restrictions[0]))
    if len(all_restrictions) > 1:
        G.add((klass, RDFS.subClassOf, equivalent_class))
        G.add((equivalent_class, OWL.intersectionOf, list_name))
        Collection(G, list_name, all_restrictions)
    intersection_classes[klass] = tuple(sorted(definition))


def define_classes(definitions, parent, pun_classes=False):
    """
    Generates triples for the hierarchy given by 'definitions', rooted
    at the class given by 'parent'
    - class hierarchy ('subclasses')
    - tag mappings
    - substance + quantity modeling

    If pun_classes is True, then create punned instances of the classes
    """
    for classname, defn in definitions.items():
        classname = BRICK[classname]
        # class is a owl:Class
        G.add((classname, A, OWL.Class))
        # subclass of parent
        G.add((classname, RDFS.subClassOf, parent))
        # add label
        class_label = classname.split("#")[-1].replace("_", " ")
        G.add((classname, RDFS.label, Literal(class_label)))
        if pun_classes:
            G.add((classname, A, classname))

        # define mapping to tags if it exists
        # "tags" property is a list of URIs naming Tags
        taglist = defn.get("tags", [])
        assert isinstance(taglist, list)
        if len(taglist) == 0:
            logging.warning(f"Property 'tags' not defined for {classname}")
        add_tags(classname, taglist)

        # define mapping to substances + quantities if it exists
        # "substances" property is a list of (predicate, object) pairs
        substancedef = defn.get("substances", [])
        assert isinstance(substancedef, list)
        add_restriction(classname, substancedef)

        # define class structure
        # this is a nested dictionary
        subclassdef = defn.get("subclasses", {})
        assert isinstance(subclassdef, dict)
        define_classes(subclassdef, classname, pun_classes=pun_classes)

        # handle 'parents' subclasses (links outside of tree-based hierarchy)
        parents = defn.get("parents", [])
        assert isinstance(parents, list)
        for _parent in parents:
            G.add((classname, RDFS.subClassOf, _parent))

        # all other key-value pairs in the definition are
        # property-object pairs
        expected_properties = ["parents", "tags", "substances", "subclasses"]
        other_properties = [
            prop for prop in defn.keys() if prop not in expected_properties
        ]
        for propname in other_properties:
            propval = defn[propname]
            G.add((classname, propname, propval))


def define_properties(definitions, superprop=None):
    """
    Define BRICK properties
    """
    if len(definitions) == 0:
        return

    for prop, propdefn in definitions.items():
        G.add((BRICK[prop], A, OWL.ObjectProperty))
        if superprop is not None:
            G.add((BRICK[prop], RDFS.subPropertyOf, superprop))

        # define property types
        prop_types = propdefn.get(A, [])
        assert isinstance(prop_types, list)
        for prop_type in prop_types:
            G.add((BRICK[prop], A, prop_type))

        # define any subproperties
        subproperties_def = propdefn.get("subproperties", {})
        assert isinstance(subproperties_def, dict)
        define_properties(subproperties_def, BRICK[prop])

        # define other properties of the Brick property
        for propname, propval in propdefn.items():
            # all other key-value pairs in the definition are
            # property-object pairs
            expected_properties = ["subproperties", A]
            other_properties = [
                prop for prop in propdefn.keys() if prop not in expected_properties
            ]

            for propname in other_properties:
                propval = propdefn[propname]
                G.add((BRICK[prop], propname, propval))


logging.info("Beginning BRICK Ontology compilation")
# handle ontology definition
define_ontology(G)

# Declare root classes

G.add((BRICK.Class, A, OWL.Class))
G.add((BRICK.Tag, A, OWL.Class))

roots = {
    "Equipment": {"tags": [TAG.Equipment]},
    "Location": {"tags": [TAG.Location]},
    "Point": {"tags": [TAG.Point]},
    "Measurable": {},
}
define_classes(roots, BRICK.Class)

logging.info("Defining properties")
# define BRICK properties
define_properties(properties)

logging.info("Defining Point subclasses")
# define Point subclasses
define_classes(setpoint_definitions, BRICK.Point)
define_classes(sensor_definitions, BRICK.Point)
define_classes(alarm_definitions, BRICK.Point)
define_classes(status_definitions, BRICK.Point)
define_classes(command_definitions, BRICK.Point)
define_classes(parameter_definitions, BRICK.Point)

# make points disjoint
pointclasses = ["Alarm", "Status", "Command", "Setpoint", "Sensor", "Parameter"]
for pc in pointclasses:
    for o in filter(lambda x: x != pc, pointclasses):
        G.add((BRICK[pc], OWL.disjointWith, BRICK[o]))

logging.info("Defining Equipment, Location subclasses")
# define other root class structures
define_classes(location_subclasses, BRICK.Location)
define_classes(equipment_subclasses, BRICK.Equipment)
define_classes(hvac_subclasses, BRICK.HVAC)
define_classes(valve_subclasses, BRICK.Valve)

logging.info("Defining Measurable hierarchy")
# define measurable hierarchy
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
define_classes(substances, BRICK.Substance, pun_classes=True)
define_classes(quantity_definitions, BRICK.Quantity, pun_classes=True)

logging.info("Finishing Tag definitions")
# declares that all tags are pairwise different; i.e. no two tags refer
# to the same tag
different_tag_list = []
for tag, definition in tags.items():
    different_tag_list.append(TAG[tag])
    G.add((TAG[tag], A, BRICK.Tag))
different_tag = BNode("tags_are_different")
G.add((BRICK.Tag, A, OWL.AllDifferent))
G.add((BRICK.Tag, OWL.distinctMembers, different_tag))
Collection(G, different_tag, different_tag_list)

logging.info(f"Brick ontology compilation finished! Generated {len(G)} triples")
# serialize to output
G.serialize("Brick.ttl", format="turtle")
