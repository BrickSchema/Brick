import logging
from itertools import chain
import os
import brickschema
import importlib
from pathlib import Path
import sys
import csv
import glob
import ontoenv
import pyshacl
from rdflib import Graph, Literal, BNode, URIRef
from rdflib.namespace import XSD
from rdflib.collection import Collection

from bricksrc.ontology import (
    define_ontology,
    ontology_imports,
    define_extension,
    BRICK_IRI_VERSION,
)
from bricksrc.env import env

from bricksrc.namespaces import (
    BRICK,
    BSH,
    REC,
    RDF,
    OWL,
    RDFS,
    TAG,
    SOSA,
    SKOS,
    QUDT,
    VCARD,
    SH,
    REF,
)
from bricksrc.namespaces import bind_prefixes

from bricksrc.setpoint import setpoint_definitions
from bricksrc.sensor import sensor_definitions
from bricksrc.alarm import alarm_definitions
from bricksrc.status import status_definitions
from bricksrc.command import command_definitions
from bricksrc.parameter import parameter_definitions
from bricksrc.collections import collection_classes
from bricksrc.location import location_subclasses
from bricksrc.equipment import (
    equipment_subclasses,
    hvac_subclasses,
    hvac_valve_subclasses,
    valve_subclasses,
    security_subclasses,
    safety_subclasses,
)
from bricksrc.substances import substances
from bricksrc.relationships import relationships
from bricksrc.quantities import quantity_definitions, get_units
from bricksrc.entity_properties import entity_properties, get_shapes
from bricksrc.deprecations import deprecations


logging.basicConfig(
    format="%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


G = brickschema.Graph()
bind_prefixes(G)
A = RDF.type

shaclGraph = Graph()
bind_prefixes(shaclGraph)
intersection_classes = {}
has_tag_restriction_class = {}
shacl_tag_property_shapes = {}
has_exactly_n_tags_shapes = {}


def add_relationships(item, propdefs, graph=G):
    for propname, propval in propdefs.items():
        if isinstance(propval, list):
            for pv in propval:
                graph.add((item, propname, pv))
        elif not isinstance(propval, dict):
            graph.add((item, propname, propval))


def get_units_brick(brick_quantity):
    brick_units = G.query(
        f"""SELECT ?unit ?symbol ?label WHERE {{
        ?subquant skos:broader+ <{brick_quantity}> .
        ?subquant qudt:applicableUnit ?unit .
        OPTIONAL {{
            ?unit qudt:symbol ?symbol .
            FILTER(isLiteral(?symbol))
        }} .
        OPTIONAL {{
            ?unit rdfs:label ?label .
        }}
    }}"""  # noqa
    )
    return set(brick_units)


def units_for_quantity(quantity):
    """
    Given a Brick Quantity (the full URI), returns the list of applicable units
    """
    brick_units = set(G.objects(subject=quantity, predicate=QUDT.applicableUnit))
    qudt_units = set(get_units(quantity))
    return list(brick_units.union(qudt_units))


def has_label(concept, graph=G):
    return len(list(graph.objects(subject=concept, predicate=RDFS.label))) > 0


def add_tags(klass, definition, graph=G):
    """
    Adds the definition of tags to the given class. This method adds two
    groups of triples.

    The first group of triples uses the BRICK.hasAssociatedTag property
    to associate the tags with this class. While this is duplicate information,
    it is much easier to query for.

    The second group of triples uses SHACL-AF rules to generate the appropriate
    Brick class from a set of tags. Strict equality of the tag set is required:
    if two classes which are *not* related by a subclass relationship exist, but
    one class's tags are a strict subset of the other, then under this regime
    the subsumed class will *not* be inferred for instances of the class with more
    tags.

    Args:
        klass: the URI of the Brick class to be modeled
        definition: a list of BRICK.Tag instances (e.g. TAG.Air)
    """
    if len(definition) == 0:
        return
    for tag in definition:
        graph.add((klass, BRICK.hasAssociatedTag, tag))
        graph.add((tag, A, BRICK.Tag))  # make sure the tag is declared as such
        if not has_label(tag):
            graph.add(
                (tag, RDFS.label, Literal(tag.split("#")[-1], lang="en"))
            )  # make sure the tag is declared as such

    # add SHACL shape
    sc = BSH[klass.split("#")[-1] + "_TagShape"]
    shaclGraph.add((sc, A, SH.NodeShape))
    # G.add((sc, SH.targetSubjectsOf, BRICK.hasTag))
    rule = BNode(str(klass) + "TagInferenceRule")
    shaclGraph.add((sc, SH.rule, rule))

    # define rule
    shaclGraph.add((rule, A, SH.TripleRule))
    shaclGraph.add((rule, SH.subject, SH.this))
    shaclGraph.add((rule, SH.predicate, RDF.type))
    shaclGraph.add((rule, SH.object, klass))
    # conditions
    for tag in definition:
        classrule = BNode(f"add_{tag.split('#')[-1]}_to_{klass.split('#')[-1]}")
        graph.add((klass, A, SH.NodeShape))
        graph.add((klass, SH.rule, classrule))
        graph.add((classrule, A, SH.TripleRule))
        graph.add((classrule, SH.subject, SH.this))
        graph.add((classrule, SH.predicate, BRICK.hasTag))
        graph.add((classrule, SH.object, tag))
        if tag not in shacl_tag_property_shapes:
            cond = BNode(f"has_{tag.split('#')[-1]}_condition")
            prop = BNode(f"has_{tag.split('#')[-1]}_tag")
            tagshape = BNode()
            shaclGraph.add((rule, SH.condition, cond))
            shaclGraph.add((cond, SH.property, prop))
            shaclGraph.add((prop, SH.path, BRICK.hasTag))
            shaclGraph.add((prop, SH.qualifiedValueShape, tagshape))
            shaclGraph.add((tagshape, SH.hasValue, tag))
            shaclGraph.add(
                (prop, SH.qualifiedMinCount, Literal(1, datatype=XSD.integer))
            )

            # probably don't need the Max count here; addition of duplicate tags should be idempotent
            # shaclGraph.add((prop, SH.qualifiedMaxCount, Literal(1)))
            shacl_tag_property_shapes[tag] = cond
        shaclGraph.add((rule, SH.condition, shacl_tag_property_shapes[tag]))
    num_tags = len(definition)
    if len(definition) not in has_exactly_n_tags_shapes:
        # tag count condition
        cond = BSH[f"has_exactly_{num_tags}_tags_condition"]
        prop = BNode(f"has_exactly_{num_tags}_tags")
        shaclGraph.add((cond, A, OWL.Class))
        shaclGraph.add((cond, A, SH.NodeShape))
        shaclGraph.add((cond, SH.property, prop))
        shaclGraph.add((prop, SH.path, BRICK.hasTag))
        shaclGraph.add((prop, SH.minCount, Literal(len(definition))))
        shaclGraph.add((prop, SH.maxCount, Literal(len(definition))))
        has_exactly_n_tags_shapes[len(definition)] = cond

        # generate inference rule
        rule = BSH[f"has_exactly_{num_tags}_tags_rule"]
        body = BNode(f"has_{num_tags}_tags_body")
        shaclGraph.add((rule, A, SH.NodeShape))
        shaclGraph.add((rule, SH.targetSubjectsOf, BRICK.hasTag))
        shaclGraph.add((rule, SH.rule, body))
        shaclGraph.add((body, A, SH.TripleRule))
        shaclGraph.add((body, SH.subject, SH.this))
        shaclGraph.add((body, SH.predicate, RDF.type))
        shaclGraph.add((body, SH.object, cond))
        shaclGraph.add((body, SH.condition, cond))
    # shaclGraph.add((rule, SH.condition, has_exactly_n_tags_shapes[len(definition)]))

    shaclGraph.add((sc, SH.targetClass, has_exactly_n_tags_shapes[len(definition)]))

    # ensure that the rule applies to at least one of the base tags that should be on
    # most Brick classes
    # base_tags = [TAG.Equipment, TAG.Point, TAG.Location, TAG.System, TAG.Solid, TAG.Fluid]
    # target_class_tag = [t for t in base_tags if t in definition]
    # assert len(target_class_tag) > 0, klass
    # shaclGraph.add((sc, SH.targetClass, has_tag_restriction_class[target_class_tag[0]]))
    # shaclGraph.add((sc, SH.targetSubjectsOf, BRICK.hasTag))


def define_concept_hierarchy(definitions, typeclasses, broader=None, related=None):
    """
    Generates triples to define the SKOS hierarchy of concepts given by
    'definitions', which are all instances of the class given by 'typeclass'.
    'broader', if provided, is the skos:broader concept
    'related', if provided, is the skos:related concept

    Currently this is used for Brick Quantities
    """
    for concept, defn in definitions.items():
        label = concept.split("#")[-1].replace("_", " ")
        concept = BRICK[concept]
        if not has_label(concept):
            G.add((concept, RDFS.label, Literal(label, lang="en")))
        for typeclass in typeclasses:
            G.add((concept, A, typeclass))
        # mark broader concept if one exists
        if broader is not None:
            G.add((concept, SKOS.broader, broader))
            G.add((broader, SKOS.narrower, concept))
        # mark related concept if one exists
        if related is not None:
            G.add((concept, SKOS.related, related))
            G.add((related, SKOS.related, concept))

        # define concept hierarchy
        # this is a nested dictionary
        narrower_defs = defn.get(SKOS.narrower, {})
        if narrower_defs is not None and isinstance(narrower_defs, dict):
            define_concept_hierarchy(narrower_defs, typeclasses, broader=concept)
        related_defs = defn.get(SKOS.related, {})
        if related_defs is not None and isinstance(related_defs, dict):
            define_concept_hierarchy(related_defs, typeclasses, related=concept)

        # handle 'parents' subconcepts (links outside of tree-based hierarchy)
        parents = defn.get("parents", [])
        assert isinstance(parents, list)
        for _parent in parents:
            G.add((concept, SKOS.broader, _parent))

        # all other key-value pairs in the definition are
        # property-object pairs
        expected_properties = ["parents", "tags", "substances"]
        other_properties = [
            prop for prop in defn.keys() if prop not in expected_properties
        ]
        add_relationships(concept, {k: defn[k] for k in other_properties})


def inherit_has_quantity(definitions, parent_quantity=None):
    """
    Recursively ensures that the BRICK.hasQuantity annotation is inherited down the
    subclass tree unless a subclass already specifies a BRICK.hasQuantity.
    """
    for classname, defn in definitions.items():
        # Inherit BRICK.hasQuantity from parent if not defined in the current class
        if BRICK.hasQuantity not in defn and parent_quantity is not None:
            defn[BRICK.hasQuantity] = parent_quantity

        # Recursively apply to subclasses
        subclassdef = defn.get("subclasses", {})
        assert isinstance(subclassdef, dict)
        inherit_has_quantity(subclassdef, defn.get(BRICK.hasQuantity, parent_quantity))


def define_classes(definitions, parent, pun_classes=False, graph=G):
    """
    Generates triples for the hierarchy given by 'definitions', rooted
    at the class given by 'parent'
    - class hierarchy ('subclasses')
    - tag mappings
    - substance + quantity modeling

    If pun_classes is True, then create punned instances of the classes
    """
    for classname, defn in definitions.items():
        classname = BRICK[classname] if not isinstance(classname, URIRef) else classname
        # class is a owl:Class
        graph.add((classname, A, OWL.Class))
        graph.add((classname, A, SH.NodeShape))
        # subclass of parent
        graph.add((classname, RDFS.subClassOf, parent))
        # add label
        class_label = classname.split("#")[-1].replace("_", " ")

        if pun_classes:
            graph.add((classname, A, classname))

        # define mapping to tags if it exists
        # "tags" property is a list of URIs naming Tags
        taglist = defn.get("tags", [])
        assert isinstance(taglist, list)
        if len(taglist) == 0:
            logging.warning(f"Property 'tags' not defined for {classname}")
        add_tags(classname, taglist, graph=graph)

        # define class structure
        # this is a nested dictionary
        subclassdef = defn.get("subclasses", {})
        assert isinstance(subclassdef, dict)
        define_classes(subclassdef, classname, graph=graph)

        # handle 'parents' subclasses (links outside of tree-based hierarchy)
        parents = defn.get("parents", [])
        assert isinstance(parents, list)
        for _parent in parents:
            graph.add((classname, RDFS.subClassOf, _parent))

        # add SHACL constraints to the class
        constraints = defn.get("constraints", {})
        assert isinstance(constraints, dict)
        define_constraints(constraints, classname, graph=graph)

        aliases = defn.get("aliases", [])
        assert isinstance(aliases, list)
        for alias in aliases:
            graph.add((classname, OWL.equivalentClass, alias))
            graph.add((alias, A, OWL.Class))
            graph.add((alias, A, SH.NodeShape))
            graph.add((alias, OWL.equivalentClass, classname))
            # find parent class of what the alias is equivalent to, add the RDFS subClassOf properties
            parent_classes = list(graph.objects(subject=classname, predicate=RDFS.subClassOf))
            for pc in parent_classes:
                graph.add((alias, RDFS.subClassOf, pc))
            graph.add((alias, BRICK.aliasOf, classname))

        # all other key-value pairs in the definition are
        # property-object pairs
        expected_properties = [
            "parents",
            "tags",
            "substances",
            "subclasses",
            "constraints",
            "aliases",
        ]
        other_properties = [
            prop for prop in defn.keys() if prop not in expected_properties
        ]
        for propname in other_properties:
            propval = defn[propname]
            if isinstance(propval, list):
                for pv in propval:
                    G.add((classname, propname, pv))
            else:
                G.add((classname, propname, propval))


def define_constraints(constraints, classname, graph=G):
    """
    Makes 'classname' a SHACL NodeShape and Class (implicitly targeting all
    instances of the class) and defines some PropertyShapes based on 'constraints'
    that apply to the nodeshape.
    """
    for property_name, property_values in constraints.items():
        pnode = BNode()
        onode = BNode()
        graph.add((classname, A, SH.NodeShape))
        graph.add((classname, SH.property, pnode))
        graph.add((pnode, SH["path"], property_name))

        if isinstance(property_values, URIRef):
            graph.add((pnode, SH["class"], property_values))
        elif isinstance(property_values, list):
            if len(property_values) > 1:
                graph.add((pnode, SH["or"], onode))
                possible_values = []
                for pv in property_values:
                    pvnode = BNode()
                    graph.add((pvnode, SH["class"], pv))
                    possible_values.append(pvnode)
                Collection(graph, onode, possible_values)
            elif len(property_values) == 1:
                graph.add((pnode, SH["class"], property_values[0]))
        else:
            raise Exception("Do not know how to handle constraints for %s" % classname)


def define_entity_properties(definitions, superprop=None, graph=G):
    """
    Defines the EntityProperty relationships and their subproperties.
    Like most other generation methods in this file, it can add additional
    properties to the EntityProperty instances (like SKOS.definition)
    """
    _allowed_annotations = {SH.node, SH.datatype, SH.hasValue, SH["class"]}
    for entprop, defn in definitions.items():
        assert (
            "property_of" in defn
        ), f"{entprop} missing a 'property_of' annotation so Brick doesn't know where this property can be used"
        assert _allowed_annotations.intersection(
            defn.keys()
        ), f"{entprop} missing at least one of {_allowed_annotations} so Brick doesn't know what the values of this property can be"
        graph.add((entprop, A, BRICK.EntityProperty))
        graph.add((entprop, A, OWL.ObjectProperty))
        if superprop is not None:
            graph.add((entprop, RDFS.subPropertyOf, superprop))
        if "subproperties" in defn:
            subproperties = defn.pop("subproperties")
            define_entity_properties(subproperties, entprop, graph=graph)

        pshape = BSH[f"has{entprop.split('#')[-1]}Shape"]
        graph.add((pshape, A, SH.PropertyShape))
        graph.add((pshape, SH.path, entprop))
        # add the SH annotations above
        for annotation in _allowed_annotations:
            val = defn.get(annotation)
            if val is not None:
                val = defn.pop(annotation)
                graph.add((pshape, annotation, val))
        if not has_label(pshape):
            graph.add((pshape, RDFS.label, Literal(f"has {defn.get(RDFS.label)} property", lang="en")))

        # add the entity property as a sh:property on all of the
        # other Nodeshapes indicated by "property_of"
        shapes = defn.pop("property_of")
        if not isinstance(shapes, list):
            shapes = [shapes]
        for shape in shapes:
            graph.add((shape, SH.property, pshape))

        for prop, values in defn.items():
            if isinstance(values, list):
                for pv in values:
                    graph.add((entprop, prop, pv))
            else:
                graph.add((entprop, prop, values))


def define_shape_property_property(shape_name, definitions, graph=G):
    if "or" in definitions:
        or_list = []
        for or_node_defn in definitions.pop("or"):
            or_node_shape = BNode()
            or_list.append(or_node_shape)
            define_shape_property_property(or_node_shape, or_node_defn, graph=graph)
        or_list_name = BNode()
        graph.add((shape_name, SH["or"], or_list_name))
        Collection(graph, or_list_name, or_list)
    for prop_name, prop_defn in definitions.items():
        # check if there is already a property shape for this.
        # Only do this is if (a) the property is optional for this shape, and
        # (b) there are no further requirements; the existing property shapes
        # don't have any min/max counts or additional requirements
        if prop_defn.get("optional", False) and len(prop_defn.keys()) == 1:
            prop_exists = list(
                graph.query(
                    f"""SELECT ?x {{ ?p sh:property ?p .
                        ?p sh:path {prop_name.n3()} .
                        FILTER NOT EXISTS {{ ?p sh:minCount ?mc }}
                        FILTER NOT EXISTS {{ ?p sh:maxCount ?mc }}
                    }}"""  # noqa
                )
            )
            if len(prop_exists) > 0:
                graph.add((shape_name, SH.property, prop_exists[0][0]))
                continue  # continue to next property

        ps = BNode()
        graph.add((shape_name, SH.property, ps))
        graph.add((ps, A, SH.PropertyShape))
        graph.add((ps, SH.path, prop_name))
        if "import_from" in prop_defn:
            fname = prop_defn.pop("import_from")
            tmpG = Graph()
            tmpG.parse(fname)
            res = tmpG.query(f"SELECT ?p ?o WHERE {{ <{prop_name}> ?p ?o }}")  # noqa
            for p, o in res:
                graph.add((prop_name, p, o))
        if "optional" in prop_defn:
            if not prop_defn.pop("optional"):
                graph.add((ps, SH.minCount, Literal(1)))
        else:
            graph.add((ps, SH.minCount, Literal(1)))

        if "datatype" in prop_defn:
            dtype = prop_defn.pop("datatype")
            graph.add((prop_name, A, OWL.DatatypeProperty))
            if dtype == BSH.NumericValue:
                graph.add((ps, SH["or"], BSH.NumericValue))
            else:
                graph.add((ps, SH.datatype, dtype))
        elif "values" in prop_defn:
            enumeration = BNode()
            graph.add((ps, SH["in"], enumeration))
            graph.add((ps, SH.minCount, Literal(1)))
            Collection(graph, enumeration, map(Literal, prop_defn.pop("values")))
            graph.add((prop_name, A, OWL.DatatypeProperty))
        else:
            graph.add((prop_name, A, OWL.ObjectProperty))
        add_relationships(ps, prop_defn, graph=graph)


def define_shape_properties(definitions, graph=G):
    """
    Defines the NodeShapes that govern what the values of
    EntityProperty relationships should look like. The important
    keys are:
    - values: defines the set of possible values of this property as an enumeration
    - units: verifies that the units of the value are one of the given enumeration.
    - unitsFromQuantity: verifies that the units of the value are compatible with the units
                for the given Brick quantity
    - datatype: specifies the expected kind of data type of prop:value
    - properties: defines other epected properties of the Shape. These properties can have
                'datatype' or 'values', in addition to other standard properties like
                SKOS.definition

    Some other usage notes:
    - 'units' and 'datatype' should be used together
    - 'values' should not be used with units or datatype
    """
    for shape_name, defn in definitions.items():
        graph.add((shape_name, A, SH.NodeShape))
        graph.add((shape_name, A, OWL.Class))
        graph.add((shape_name, A, BRICK.EntityPropertyValue))
        graph.add((shape_name, RDFS.subClassOf, BSH.ValueShape))

        needs_value_properties = ["values", "units", "unitsFromQuantity", "datatype"]
        brick_value_shape = BNode()
        if any(k in defn for k in needs_value_properties):
            graph.add((shape_name, SH.property, brick_value_shape))
            graph.add((brick_value_shape, A, SH.PropertyShape))
            graph.add((brick_value_shape, SH.path, BRICK.value))
            graph.add((brick_value_shape, SH.minCount, Literal(1)))
            graph.add((brick_value_shape, SH.maxCount, Literal(1)))

        v = BNode()
        # prop:value PropertyShape
        if "values" in defn:
            enumeration = BNode()
            graph.add((shape_name, SH.property, brick_value_shape))
            graph.add((brick_value_shape, A, SH.PropertyShape))
            graph.add((brick_value_shape, SH.path, BRICK.value))
            graph.add((brick_value_shape, SH["in"], enumeration))
            graph.add((brick_value_shape, SH.minCount, Literal(1)))
            vals = defn.pop("values")
            if all(map(lambda v: isinstance(v, str), vals)):
                Collection(
                    graph,
                    enumeration,
                    map(lambda x: Literal(x, datatype=XSD.string), vals),
                )
            if all(map(lambda v: isinstance(v, int), vals)):
                Collection(
                    graph,
                    enumeration,
                    map(lambda x: Literal(x, datatype=XSD.integer), vals),
                )
            if all(map(lambda v: isinstance(v, float), vals)):
                Collection(
                    graph,
                    enumeration,
                    map(lambda x: Literal(x, datatype=XSD.decimal), vals),
                )
            else:
                Collection(graph, enumeration, map(Literal, vals))
        if "units" in defn:
            v = BNode()
            enumeration = BNode()
            graph.add((shape_name, SH.property, v))
            graph.add((v, A, SH.PropertyShape))
            graph.add((v, SH.path, BRICK.hasUnit))
            graph.add((v, SH["in"], enumeration))
            graph.add((v, SH.minCount, Literal(1)))
            graph.add((v, SH.maxCount, Literal(1)))
            Collection(graph, enumeration, defn.pop("units"))
        if "unitsFromQuantity" in defn:
            v = BNode()
            enumeration = BNode()
            graph.add((shape_name, SH.property, v))
            graph.add((v, A, SH.PropertyShape))
            graph.add((v, SH.path, BRICK.hasUnit))
            graph.add((v, SH["in"], enumeration))
            graph.add((v, SH.minCount, Literal(1)))
            graph.add((v, SH.maxCount, Literal(1)))
            units = units_for_quantity(defn.pop("unitsFromQuantity"))
            assert len(units) > 0, f"Quantity shape {shape_name} has no units"
            Collection(graph, enumeration, units)
        if "properties" in defn:
            prop_defns = defn.pop("properties")
            define_shape_property_property(shape_name, prop_defns, graph=graph)
        elif "datatype" in defn:
            graph.add((shape_name, SH.property, brick_value_shape))
            graph.add((brick_value_shape, A, SH.PropertyShape))
            graph.add((brick_value_shape, SH.path, BRICK.value))
            dtype = defn.pop("datatype")
            if dtype == BSH.NumericValue:
                graph.add((brick_value_shape, SH["or"], BSH.NumericValue))
            else:
                graph.add((brick_value_shape, SH.datatype, dtype))
            graph.add((brick_value_shape, SH.minCount, Literal(1)))
            if "range" in defn:
                for prop_name, prop_value in defn.pop("range").items():
                    if prop_name not in [
                        "minExclusive",
                        "minInclusive",
                        "maxExclusive",
                        "maxInclusive",
                    ]:
                        raise Exception(
                            f"brick:value property {prop_name} not valid"  # noqa
                        )
                    graph.add((brick_value_shape, SH[prop_name], Literal(prop_value)))


def define_relationships(definitions, superprop=None, graph=G):
    """
    Define BRICK relationships
    """
    if len(definitions) == 0:
        return

    for prop, propdefn in definitions.items():
        if not isinstance(prop, URIRef):
            prop = BRICK[prop]
        if superprop is not None:
            graph.add((prop, RDFS.subPropertyOf, superprop))

        if prop.startswith(BRICK):
            graph.add((prop, A, BRICK.Relationship))

        # define property types
        prop_types = propdefn.get(A, [])
        assert isinstance(prop_types, list)
        for prop_type in prop_types:
            graph.add((prop, A, prop_type))

        # define any subproperties
        subproperties_def = propdefn.get("subproperties", {})
        assert isinstance(subproperties_def, dict)
        define_relationships(subproperties_def, prop, graph=graph)

        # generate a SHACL Property Shape for this relationship if it is a Brick property
        if prop.startswith(BRICK):
            propshape = BSH[f"{prop[len(BRICK):]}Shape"]
            graph.add((propshape, A, SH.PropertyShape))
            graph.add((propshape, SH.path, prop))
        if "range" in propdefn.keys():
            range_defn = propdefn.pop("range")
            if isinstance(range_defn, (tuple, list)):
                enumeration = BNode()
                graph.add((propshape, SH["or"], enumeration))
                constraints = []
                for cls in range_defn:
                    constraint = BNode()
                    graph.add((constraint, SH["class"], cls))
                    constraints.append(constraint)
                Collection(graph, enumeration, constraints)
            elif range_defn is not None:
                graph.add((propshape, SH["class"], range_defn))

        if "datatype" in propdefn.keys():
            dtype_defn = propdefn.pop("datatype")
            if dtype_defn == BSH.NumericValue:
                graph.add((propshape, SH["or"], BSH.NumericValue))
            else:
                graph.add((propshape, SH.datatype, dtype_defn))

        if "domain" in propdefn.keys():
            # associate the PropertyShape with all possible subject classes
            domains = propdefn.pop("domain")
            if not isinstance(domains, list):
                domains = [domains]
            for domain in domains:
                graph.add((domain, SH.property, propshape))

        # define other properties of the Brick property
        expected_properties = ["subproperties", A]
        other_properties = [
            prop for prop in propdefn.keys() if prop not in expected_properties
        ]
        add_relationships(prop, {k: propdefn[k] for k in other_properties}, graph=graph)


def add_definitions(graph=G):
    """
    Adds definitions for Brick subclasses through SKOS.definitions.

    This parses the definitions from ./bricksrc/definitions.csv and
    adds it to the graph. If available, adds the source information of
    through RDFS.seeAlso.
    """
    with open("./bricksrc/definitions.csv", encoding="utf-8") as dictionary_file:
        dictionary = csv.reader(dictionary_file)

        header = next(dictionary)

        # add definitions, citations to the graph
        for definition in dictionary:
            term = URIRef(definition[0])
            if len(definition) > len(header):
                raise ValueError(
                    f"The term '{term}' has more elements than expected. Please check the format."
                )
            if len(definition[1]):
                graph.add((term, SKOS.definition, Literal(definition[1], lang="en")))
            if len(definition) > 2 and definition[2]:
                try:
                    graph.add((term, RDFS.seeAlso, URIRef(definition[2])))
                except Exception as e:
                    print(
                        f"Error processing 'seeAlso' for term '{term}': {e}. The definition provided is: '{definition}'."
                    )

    qstr = """
    select ?param where {
      ?param rdfs:subClassOf* brick:Limit.
    }
    """
    limit_def_template = "A parameter that places {direction} bound on the range of permitted values of a {setpoint}."
    params = [row["param"] for row in graph.query(qstr)]
    for param in params:
        words = param.split("#")[-1].split("_")
        prefix = words[0]

        # define "direction" component of Limit definition
        if prefix == "Min":
            direction = "a lower"
        elif prefix == "Max":
            direction = "an upper"
        else:
            prefix = None
            direction = "a lower or upper"

        # define the "setpoint" component of a Limit definition
        if param.split("#")[-1] in ["Max_Limit", "Min_Limit", "Limit"]:
            setpoint = "Setpoint"
        else:
            if prefix:
                setpoint = "_".join(words[1:-1])
            else:
                setpoint = "_".join(words[:-1])

        if setpoint.split("_")[-1] != "Setpoint":
            # While Limits are a boundary of a Setpoint, the associated
            # Setpoint names are not explicit in class's names. Thus needs
            # to be explicily added for the definition text.
            setpoint = setpoint + "_Setpoint"
            logger.info(f"Inferred setpoint: {setpoint}")
        limit_def = limit_def_template.format(direction=direction, setpoint=setpoint)
        if param != BRICK.Limit:  # definition already exists for Limit
            graph.add((param, SKOS.definition, Literal(limit_def, lang="en")))
        class_exists = graph.query(
            f"""select ?class where {{
            BIND(brick:{setpoint} as ?class)
            ?class rdfs:subClassOf* brick:Class.
        }}
        """  # noqa
        ).bindings
        if not class_exists:
            logging.warning(
                f"WARNING: {setpoint} does not exist in Brick for {param}."  # noqa
            )


def handle_deprecations():
    for deprecated_term, md in deprecations.items():
        term_type = md.get(A)
        if term_type:
            G.add((deprecated_term, A, term_type))

        G.add((deprecated_term, OWL.deprecated, Literal(True)))

        # handle subclasses or skos. Only add it as an owl:Class if
        # the use of rdfs:subClassOf exists, implying this is a Class
        if RDFS.subClassOf in md:
            G.add((deprecated_term, A, OWL.Class))
            subclasses = md.pop(RDFS.subClassOf)
            if subclasses is not None:
                if not isinstance(subclasses, list):
                    subclasses = [subclasses]
                for subclass in subclasses:
                    G.add((deprecated_term, RDFS.subClassOf, subclass))
        elif SKOS.narrower in md:
            subconcepts = md.pop(SKOS.narrower)
            if subconcepts is not None:
                if not isinstance(subconcepts, list):
                    subconcepts = [subconcepts]
                for subclass in subconcepts:
                    G.add((deprecated_term, SKOS.narrower, subclass))
        elif SKOS.broader in md:
            subconcepts = md.pop(SKOS.broader)
            if subconcepts is not None:
                if not isinstance(subconcepts, list):
                    subconcepts = [subconcepts]
                for subclass in subconcepts:
                    G.add((deprecated_term, SKOS.broader, subclass))
        G.add((deprecated_term, BRICK.deprecatedInVersion, Literal(md["version"])))
        G.add(
            (
                deprecated_term,
                BRICK.deprecationMitigationMessage,
                Literal(md["mitigation_message"]),
            )
        )
        G.add((deprecated_term, BRICK.isReplacedBy, md["replace_with"]))


def handle_concept_labels():
    """
    Adds labels to all concepts in the Brick namespace, unless they already have one.
    Brick concepts are all subclasses of Brick.Entity and subproperties of Brick.Relationship.
    If there are two or more labels for a concept, choose one and raise a Warning
    """
    concepts = chain(
            G.transitive_subjects(RDFS.subClassOf, BRICK.Entity),
            G.subjects(A, BRICK.Entity),
            G.subjects(A, OWL.ObjectProperty),
            G.subjects(A, OWL.DatatypeProperty),
            )
    for s in concepts:
        labels = list(G.objects(s, RDFS.label))
        if len(labels) == 0:
            G.add((s, RDFS.label, Literal(s.split("#")[-1].replace("_", " "), lang="en")))
        elif len(labels) > 1:
            logging.warning(f"Multiple labels for {s}: {labels}")
            # choose one and remove the others
            for to_remove in labels[1:]:
                G.remove((s, RDFS.label, to_remove))



logger.info("Beginning BRICK Ontology compilation")
# handle ontology definition
define_ontology(G)

logger.info("Inheriting annotations down the subclass trees")
inherit_has_quantity(setpoint_definitions)
inherit_has_quantity(sensor_definitions)
inherit_has_quantity(alarm_definitions)
inherit_has_quantity(status_definitions)
inherit_has_quantity(command_definitions)
inherit_has_quantity(parameter_definitions)

# Declare root classes

# we keep the definition of brick:Class, which was the root
# class of Brick prior to v1.3.0, in order to maintain backwards
# compatibility with older Brick models. Both brick:Class and
# brick:Entity are root classes
G.add((BRICK.Entity, A, OWL.Class))  # >= Brick v1.3.0
G.add((BRICK.Entity, A, SH.NodeShape))  # >= Brick v1.3.0
G.add((BRICK.Class, A, OWL.Class))  # < Brick v1.3.0
G.add((BRICK.Class, A, SH.NodeShape))  # < Brick v1.3.0
G.add((BRICK.Class, RDFS.subClassOf, BRICK.Entity))  # < Brick v1.3.0
G.add((BRICK.Tag, A, OWL.Class))
G.add((BRICK.Tag, A, SH.NodeShape))
G.add((BRICK.Tag, RDFS.subClassOf, BRICK.Entity))

roots = {
    "Equipment": {
        "tags": [TAG.Equipment],
    },
    "Location": {
        "tags": [TAG.Location],
    },
    "Point": {"tags": [TAG.Point]},
    "Measurable": {"tags": [TAG.Measurable]},
    "Collection": {"tags": [TAG.Collection]},
}
define_classes(roots, BRICK.Class)  # <= Brick v1.3.0
define_classes(roots, BRICK.Entity)  # >= Brick v1.3.0

logger.info("Defining properties")
# define BRICK properties
G.add((BRICK.Relationship, RDFS.subClassOf, RDF.Property))
G.add((BRICK.Relationship, A, BRICK.Relationship))
G.add((BRICK.Relationship, RDFS.label, Literal("Relationship", lang="en")))
G.add(
    (
        BRICK.Relationship,
        SKOS.definition,
        Literal(
            "Super-property of all Brick relationships between entities (Equipment, Location, Point)"
        ),
    )
)
define_relationships(relationships)

logger.info("Defining Point subclasses")
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

logger.info("Defining Equipment, System and Location subclasses")
# define other root class structures
define_classes(location_subclasses, BRICK.Location)
define_classes(equipment_subclasses, BRICK.Equipment)
define_classes(collection_classes, BRICK.Collection)
define_classes(hvac_subclasses, BRICK.HVAC_Equipment)
define_classes(hvac_valve_subclasses, BRICK.HVAC_Equipment)
define_classes(valve_subclasses, BRICK.Equipment)
define_classes(security_subclasses, BRICK.Security_Equipment)
define_classes(safety_subclasses, BRICK.Safety_Equipment)

logger.info("Defining Measurable hierarchy")
# define measurable hierarchy
G.add((BRICK.Measurable, RDFS.subClassOf, BRICK.Entity))
# set up Quantity definition
G.add((BRICK.Quantity, RDFS.subClassOf, SOSA.ObservableProperty))
G.add((BRICK.Quantity, RDFS.subClassOf, QUDT.QuantityKind))
G.add(
    (SOSA.ObservableProperty, A, OWL.Class)
)  # needs the type declaration to satisfy some checkers
G.add((BRICK.Quantity, RDFS.subClassOf, BRICK.Measurable))
G.add((BRICK.Quantity, A, OWL.Class))
G.add((BRICK.Quantity, A, SH.NodeShape))
G.add((BRICK.Quantity, RDFS.label, Literal("Quantity", lang="en")))
G.add((BRICK.Quantity, RDFS.subClassOf, SKOS.Concept))
# set up Substance definition
G.add((BRICK.Substance, RDFS.subClassOf, SOSA.FeatureOfInterest))
G.add(
    (SOSA.FeatureOfInterest, A, OWL.Class)
)  # needs the type declaration to satisfy some checkers
G.add((BRICK.Substance, RDFS.subClassOf, BRICK.Measurable))
G.add((BRICK.Substance, A, OWL.Class))
G.add((BRICK.Substance, A, SH.NodeShape))
G.add((BRICK.Substance, RDFS.label, Literal("Substance", lang="en")))

# We make the punning explicit here. Any subclass of brick:Substance
# is itself a substance or quantity. There is one canonical instance of
# each class, which is indicated by referencing the class itself.
#
#    bldg:tmp1      a           brick:Air_Temperature_Sensor;
#               brick:measures  brick:Air ,
#                               brick:Temperature .
#
# This makes Substance metaclasses.
define_concept_hierarchy(substances, [BRICK.Substance])

# this defines the SKOS-based concept hierarchy for BRICK Quantities
define_concept_hierarchy(quantity_definitions, [BRICK.Quantity])

# add any missing skos:narrower implied by skos:broader where the subject
# is defined by the Brick ontology
G.query(
    """CONSTRUCT {
    ?narrower skos:broader ?broader .
} WHERE {
    ?broader skos:narrower ?narrower .
    ?narrower rdf:type/rdfs:subClassOf* brick:Entity
}"""
)
# add any missing skos:broader implied by skos:narrower where the subject
# is defined by the Brick ontology
G.query(
    """CONSTRUCT {
    ?broader skos:narrower ?narrower .
} WHERE {
    ?narrower skos:broader ?broader .
    ?broader rdf:type/rdfs:subClassOf* brick:Entity
}"""
)

# for all Quantities, copy part of the QUDT unit definitions over
res = G.query(
    """SELECT ?quantity ?qudtquant WHERE {
                ?quantity rdf:type brick:Quantity .
                ?quantity brick:hasQUDTReference ?qudtquant
                }"""
)

logger.info("Adding applicable units")
# this requires two passes to associate the applicable units with
# each of the quantities. The first pass associates Brick quantities
# with QUDT units via the "hasQUDTReference" property; the second pass
# traverses the SKOS broader/narrower hierarchy to inherit associated units
# "up" into the broader concepts.
for r in res:
    brick_quant, qudt_quant = r
    for unit in get_units(qudt_quant):
        G.add((brick_quant, QUDT.applicableUnit, unit))
    # the symbols, units, and labels are already defined in the previous pass
    for unit, symb, label in get_units_brick(brick_quant):
        G.add((brick_quant, QUDT.applicableUnit, unit))
# all QUDT units
# for unit, symb, label in all_units():
#    G.add((unit, A, QUDT.Unit))
#    if symb is not None:
#        G.add((unit, QUDT.symbol, symb))
#    if label is not None and not has_label(unit):
#        G.add((unit, RDFS.label, label))


logger.info("Defining entity properties")
# entity property definitions (must happen after units are defined)
G.add((BRICK.value, SKOS.definition, Literal("The basic value of an entity property")))
G.add((BRICK.EntityProperty, A, RDF.Property))
G.add((BRICK.EntityProperty, RDFS.subClassOf, BRICK.Relationship))
G.add((BRICK.EntityPropertyValue, A, OWL.Class))
G.add((BRICK.EntityPropertyValue, A, SH.NodeShape))
G.add((BRICK.EntityPropertyValue, RDFS.label, Literal("EntityPropertyValue", lang="en")))
G.add((BRICK.EntityPropertyValue, RDFS.subClassOf, BRICK.Entity))
G.add((BSH.ValueShape, A, OWL.Class))
define_entity_properties(entity_properties)
define_shape_properties(get_shapes(G))

G.remove((BRICK.value, A, OWL.ObjectProperty))

logger.info("Adding deprecations")
# handle class deprecations
handle_deprecations()
# non-class deprecations handled in bricksrc/deprecations.ttl, which is added below

logger.info("Adding class definitions")
add_definitions()

logger.info("Adding other .ttl files")
# add all TTL files in bricksrc
for ttlfile in glob.glob("bricksrc/*.ttl"):
    G.parse(ttlfile, format="turtle")

# add ref-schema definitions
G.parse("support/ref-schema.ttl", format="turtle")
ref_schema_uri = URIRef(REF.strip("#"))
for triple in G.cbd(ref_schema_uri):
    G.remove(triple)

logger.info("Cleaning up ontology prefixes")
# remove duplicate ontology definitions and
# move prefixes onto Brick ontology definition
for ontology, pfx in G.subject_objects(predicate=SH.declare):
    if ontology == BRICK_IRI_VERSION:
        continue
    G.remove((None, SH.declare, pfx))
    G.add((BRICK_IRI_VERSION, SH.declare, pfx))

# reassign where rules find their prefixees
for rule, pfxs in G.subject_objects(predicate=SH.prefixes):
    G.remove((rule, SH.prefixes, pfxs))
    G.add((rule, SH.prefixes, BRICK_IRI_VERSION))

# remove ontology declarations
for ontology in G.subjects(predicate=RDF.type, object=OWL.Ontology):
    if ontology != BRICK_IRI_VERSION:
        G.remove((ontology, RDF.type, OWL.Ontology))
        G.remove((ontology, OWL.imports, None))
        G.remove((ontology, OWL.versionInfo, None))


# adding in any entity properties or classes defined
for filename in sys.argv[1:]:
    extension_graph = Graph()
    # TODO: add ontology definition
    print(f"Reading in entity properties and/or class definitions from {filename}")
    mod = importlib.import_module(filename)
    if hasattr(mod, "entity_properties"):
        define_entity_properties(mod.entity_properties, graph=extension_graph)
    if hasattr(mod, "classes"):
        for parent, tree in mod.classes.items():
            define_classes(tree, parent, graph=extension_graph)
    if hasattr(mod, "property_value_shapes"):
        define_shape_properties(mod.property_value_shapes, graph=extension_graph)
    if hasattr(mod, "ontology_definition"):
        define_extension(extension_graph, mod.ontology_definition)

    parts = Path("/".join(filename.split(".")))
    dest = Path("extensions") / parts.with_suffix(".ttl")
    os.makedirs(dest.parent, exist_ok=True)
    print(f"Writing extension graph to {dest}")
    extension_graph.serialize(dest, format="ttl")


logger.info(f"Brick ontology compilation finished! Generated {len(G)} triples")

extension_graphs = {"shacl_tag_inference": shaclGraph}

# serialize extensions to output
for name, graph in extension_graphs.items():
    with open(f"extensions/brick_extension_{name}.ttl", "w", encoding="utf-8") as fp:
        # need to write this manually; turtle serializer doesn't always add
        fp.write("@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n")
        fp.write(graph.serialize(format="turtle").rstrip())
        fp.write("\n")

# serialize Brick-only to output
with open("Brick-only.ttl", "w", encoding="utf-8") as fp:
    fp.write(G.serialize(format="turtle").rstrip())
    fp.write("\n")

# add rec stuff
env.import_graph(G, "https://w3id.org/rec")
# remove the REC import
G.remove((None, OWL.imports, URIRef("https://w3id.org/rec")))

# add inferred information to Brick
# logger.info("Adding inferred information to Brick")
# G.expand('shacl', backend='topquadrant')

# add labels to all concepts
handle_concept_labels()

# serialize Brick to output
with open("Brick.ttl", "w", encoding="utf-8") as fp:
    fp.write(G.serialize(format="turtle").rstrip())
    fp.write("\n")

# remove extensions file before computing imports
if os.path.exists("Brick+extensions.ttl"):
    os.remove("Brick+extensions.ttl")


# create new directory for storing imports
os.makedirs("imports", exist_ok=True)
for name, uri in ontology_imports.items():
    graph = env.get_graph(uri)
    graph.serialize(f"imports/{name}.ttl", format="turtle")
    env.import_graph(G, uri)

# add new Brick to ontology environment
env.add("Brick.ttl")
env.refresh()

# add the validation shapes (not for Brick distribution)
G.parse("validation.ttl")

# validate Brick
valid, _, report = G.validate(engine="topquadrant")
if not valid:
    print(report)
    sys.exit(1)

# serialize Brick+imports to output
with open("Brick+imports.ttl", "w", encoding="utf-8") as fp:
    fp.write(G.serialize(format="turtle").rstrip())
    fp.write("\n")
