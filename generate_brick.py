from rdflib import Graph, Literal, BNode, URIRef
from rdflib.namespace import XSD
from rdflib.collection import Collection

from bricksrc.namespaces import BRICK, RDF, OWL, RDFS, TAG, SOSA
from bricksrc.namespaces import bind_prefixes

from collections import defaultdict

G = Graph()
bind_prefixes(G)
A = RDF.type

tag_lookup = defaultdict(set)


# syntax for protege:
# http://protegeproject.github.io/protege/class-expression-syntax/
def add_restriction(klass, definition):
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
    elements = []
    equivalent_class = BNode()
    list_name = BNode()

    for idnum, item in enumerate(definition):
        restriction = BNode()
        elements.append(restriction)
        G.add((restriction, A, OWL.Restriction))
        G.add((restriction, OWL.onProperty, BRICK.hasTag))
        G.add((restriction, OWL.hasValue, item))
        # make sure the tag is declared as such
        G.add((item, A, BRICK.Tag))
        # make sure the tag is declared as such
        G.add((item, RDFS.label, Literal(item.split('#')[-1])))

    # tag index
    tagset = tuple(sorted([item.split('#')[-1] for item in definition]))
    tag_lookup[tagset].add(klass)

    G.add((BRICK[klass], OWL.equivalentClass, equivalent_class))
    G.add((equivalent_class, OWL.intersectionOf, list_name))
    Collection(G, list_name, elements)


def lookup_tagset(s):
    s = set(map(lambda x: x.capitalize(), s))
    return [klass for tagset, klass in tag_lookup.items()
            if s.issubset(set(tagset))]


def add_class_restriction(klass, definition):
    elements = []
    equivalent_class = BNode()
    list_name = BNode()
    for idnum, item in enumerate(definition):
        restriction = BNode()
        elements.append(restriction)
        G.add((restriction, A, OWL.Restriction))
        G.add((restriction, OWL.onProperty, item[0]))
        G.add((restriction, item[1], item[2]))
        if len(item) == 5:
            G.add((restriction, item[3], Literal('{0}'.format(item[4]),
                  datatype=XSD.integer)))
    G.add((BRICK[klass], OWL.equivalentClass, equivalent_class))
    G.add((equivalent_class, OWL.intersectionOf, list_name))
    Collection(G, list_name, elements)


def define_subclasses(definitions, superclass):
    for subclass, definition in definitions.items():
        G.add((BRICK[subclass], A, OWL.Class))
        G.add((BRICK[subclass], RDFS.label,
              Literal(subclass.replace("_", " "))))
        G.add((BRICK[subclass], RDFS.subClassOf, superclass))
        for k, v in definition.items():
            if isinstance(v, list) and k == "tagvalues":
                add_restriction(subclass, v)
            elif isinstance(v, list) and k == "tags":
                add_tags(subclass, v)
            elif isinstance(v, list) and k == "parents":
                for parent in v:
                    G.add((BRICK[subclass], RDFS.subClassOf, parent))
            elif isinstance(v, list) and k == "substances":
                add_restriction(subclass, v)
            elif not apply_prop(subclass, k, v):
                if isinstance(v, dict) and k == "subclasses":
                    define_subclasses(v, BRICK[subclass])


def define_rootclasses(definitions):
    G.add((BRICK.Class, A, OWL.Class))
    G.add((BRICK.Tag, A, OWL.Class))
    for rootclass, definition in definitions.items():
        G.add((BRICK[rootclass], A, OWL.Class))
        G.add((BRICK[rootclass], RDFS.subClassOf, BRICK.Class))
        for k, v in definition.items():
            if isinstance(v, list) and k == "tagvalues":
                add_restriction(rootclass, v)
            elif isinstance(v, list) and k == "tags":
                add_tags(rootclass, v)
            elif isinstance(v, list) and k == "substances":
                add_class_restriction(rootclass, v)
            elif not apply_prop(rootclass, k, v):
                if isinstance(v, dict) and k == "subclasses":
                    define_subclasses(v, BRICK[rootclass])


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
    # "Tag": {},
    "Substance": {},
    "Quantity": {},
}
define_rootclasses(roots)

from bricksrc.setpoint import setpoint_definitions
define_subclasses(setpoint_definitions, BRICK.Point)

from bricksrc.sensor import sensor_definitions
define_subclasses(sensor_definitions, BRICK.Point)

from bricksrc.status import status_definitions
define_subclasses(status_definitions, BRICK.Point)

from bricksrc.command import command_definitions
define_subclasses(command_definitions, BRICK.Point)

from bricksrc.parameter import parameter_definitions
define_subclasses(parameter_definitions, BRICK.Point)

from bricksrc.location import location_subclasses
define_subclasses(location_subclasses, BRICK.Location)

from bricksrc.equipment import equipment_subclasses, \
                               hvac_subclasses, valve_subclasses
define_subclasses(equipment_subclasses, BRICK.Equipment)
define_subclasses(hvac_subclasses, BRICK.HVAC)
define_subclasses(valve_subclasses, BRICK.Valve)

from bricksrc.substances import substances
define_subclasses(substances, BRICK.Substance)

from bricksrc.quantities import quantity_definitions
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

from bricksrc.properties import properties
define_properties(properties)

from bricksrc.tags import tags
for tag, definition in tags.items():
    G.add((TAG[tag], A, BRICK.Tag))

print('base:', len(G))
G.serialize('Brick.ttl', format='turtle')
