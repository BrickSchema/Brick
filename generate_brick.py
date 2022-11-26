import sys
import csv
import glob
import logging
from collections import defaultdict
import pyshacl
from rdflib import Graph, Literal, BNode, URIRef
from rdflib.namespace import XSD
from rdflib.collection import Collection

from bricksrc.ontology import define_ontology

from bricksrc.namespaces import (
    BRICK,
    BSH,
    RDF,
    OWL,
    RDFS,
    TAG,
    SOSA,
    SKOS,
    QUDT,
    UNIT,
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
from bricksrc.quantities import quantity_definitions, get_units
from bricksrc.properties import properties
from bricksrc.entity_properties import shape_properties, entity_properties, get_shapes
from bricksrc.deprecations import deprecations

logging.basicConfig(
    format="%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.INFO,
)

G = Graph()
bind_prefixes(G)
A = RDF.type

shaclGraph = Graph()
bind_prefixes(shaclGraph)
intersection_classes = {}
has_tag_restriction_class = {}
shacl_tag_property_shapes = {}
has_exactly_n_tags_shapes = {}


def add_properties(item, propdefs):
    for propname, propval in propdefs.items():
        if isinstance(propval, list):
            for pv in propdefs:
                G.add((item, propname, pv))
        elif not isinstance(propval, dict):
            G.add((item, propname, propval))


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
    }}"""
    )
    return set(brick_units)


def units_for_quantity(quantity):
    """
    Given a Brick Quantity (the full URI), returns the list of applicable units
    """
    brick_units = set(G.objects(subject=quantity, predicate=QUDT.applicableUnit))
    qudt_units = set(get_units(quantity))
    return list(brick_units.union(qudt_units))


def has_label(concept):
    return len(list(G.objects(subject=concept, predicate=RDFS.label))) > 0


def add_tags(klass, definition):
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
        G.add((klass, BRICK.hasAssociatedTag, tag))
        G.add((tag, A, BRICK.Tag))  # make sure the tag is declared as such
        G.add(
            (tag, RDFS.label, Literal(tag.split("#")[-1]))
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
        G.add((klass, A, SH.NodeShape))
        G.add((klass, SH.rule, classrule))
        G.add((classrule, A, SH.TripleRule))
        G.add((classrule, SH.subject, SH.this))
        G.add((classrule, SH.predicate, BRICK.hasTag))
        G.add((classrule, SH.object, tag))
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
        concept = BRICK[concept]
        for typeclass in typeclasses:
            G.add((concept, A, typeclass))
        # mark broader concept if one exists
        if broader is not None:
            G.add((concept, SKOS.broader, broader))
        # mark related concept if one exists
        if related is not None:
            G.add((concept, SKOS.related, related))
        # add label
        label = defn.get(RDFS.label, concept.split("#")[-1].replace("_", " "))
        if not has_label(concept):
            G.add((concept, RDFS.label, Literal(label)))

        # define concept hierarchy
        # this is a nested dictionary
        narrower_defs = defn.get(SKOS.narrower, {})
        if narrower_defs is not None and isinstance(narrower_defs, dict):
            define_concept_hierarchy(narrower_defs, [BRICK.Quantity], broader=concept)
        related_defs = defn.get(SKOS.related, {})
        if related_defs is not None and isinstance(related_defs, dict):
            define_concept_hierarchy(related_defs, [BRICK.Quantity], related=concept)

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
        for propname in other_properties:
            propval = defn[propname]
            if isinstance(propval, list):
                for pv in propval:
                    G.add((concept, propname, pv))
            elif not isinstance(propval, dict):
                G.add((concept, propname, propval))


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

        if not has_label(classname):
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

        # add SHACL constraints to the class
        constraints = defn.get("constraints", {})
        assert isinstance(constraints, dict)
        define_constraints(constraints, classname)

        # all other key-value pairs in the definition are
        # property-object pairs
        expected_properties = [
            "parents",
            "tags",
            "substances",
            "subclasses",
            "constraints",
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


def define_constraints(constraints, classname):
    """
    Makes 'classname' a SHACL NodeShape and Class (implicitly targeting all
    instances of the class) and defines some PropertyShapes based on 'constraints'
    that apply to the nodeshape.
    """
    for property_name, property_values in constraints.items():
        pnode = BNode()
        onode = BNode()
        G.add((classname, A, SH.NodeShape))
        G.add((classname, SH.property, pnode))
        G.add((pnode, SH["path"], property_name))

        if isinstance(property_values, URIRef):
            G.add((pnode, SH["class"], property_values))
        elif isinstance(property_values, list):
            G.add((pnode, SH["or"], onode))
            possible_values = []
            for pv in property_values:
                pvnode = BNode()
                G.add((pvnode, SH["class"], pv))
                possible_values.append(pvnode)
            Collection(G, onode, possible_values)
        else:
            raise Exception("Do not know how to handle constraints for %s" % classname)


def define_entity_properties(definitions, superprop=None):
    """
    Defines the EntityProperty relationships and their subproperties.
    Like most other generation methods in this file, it can add additional
    properties to the EntityProperty instances (like SKOS.definition)
    """
    for entprop, defn in definitions.items():
        G.add((entprop, A, BRICK.EntityProperty))
        if superprop is not None:
            G.add((entprop, RDFS.subPropertyOf, superprop))
        if "subproperties" in defn:
            subproperties = defn.pop("subproperties")
            define_entity_properties(subproperties, entprop)

        for prop, values in defn.items():
            if isinstance(values, list):
                for pv in values:
                    G.add((entprop, prop, pv))
            else:
                G.add((entprop, prop, values))


def define_shape_property_property(shape_name, definitions):

    # shape_detection_rule = BNode(f"_rule_for_{shape_name.split('#')[-1]}")
    # G.add((shape_detection_rule, A, SH.TripleRule))
    # G.add((shape_detection_rule, SH.subject, SH.this))
    # G.add((shape_detection_rule, SH.predicate, RDF.type))
    # G.add((shape_detection_rule, SH.object, shape_name))
    # G.add((shape_detection_rule, SH.condition, shape_name))

    if "or" in definitions:
        or_list = []
        for or_node_defn in definitions.pop("or"):
            or_node_shape = BNode()
            or_list.append(or_node_shape)
            define_shape_property_property(or_node_shape, or_node_defn)
        or_list_name = BNode()
        G.add((shape_name, SH["or"], or_list_name))
        Collection(G, or_list_name, or_list)
    for prop_name, prop_defn in definitions.items():
        ps = BNode()
        G.add((shape_name, SH.property, ps))
        G.add((ps, A, SH.PropertyShape))
        G.add((ps, SH.path, prop_name))
        if "import_from" in prop_defn:
            fname = prop_defn.pop("import_from")
            tmpG = Graph()
            tmpG.parse(fname)
            res = tmpG.query(f"SELECT ?p ?o WHERE {{ <{prop_name}> ?p ?o }}")
            for p, o in res:
                G.add((prop_name, p, o))
        if "optional" in prop_defn:
            if not prop_defn.pop("optional"):
                G.add((ps, SH.minCount, Literal(1)))
        else:
            G.add((ps, SH.minCount, Literal(1)))

        if "datatype" in prop_defn:
            dtype = prop_defn.pop("datatype")
            G.add((prop_name, A, OWL.DatatypeProperty))
            if dtype == BSH.NumericValue:
                G.add((ps, SH["or"], BSH.NumericValue))
            else:
                G.add((ps, SH.datatype, dtype))
        elif "values" in prop_defn:
            enumeration = BNode()
            G.add((ps, SH["in"], enumeration))
            G.add((ps, SH.minCount, Literal(1)))
            Collection(G, enumeration, map(Literal, prop_defn.pop("values")))
            G.add((prop_name, A, OWL.ObjectProperty))
        else:
            G.add((prop_name, A, OWL.ObjectProperty))
        add_properties(ps, prop_defn)


def define_shape_properties(definitions):
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
        G.add((shape_name, A, SH.NodeShape))
        G.add((shape_name, A, OWL.Class))
        G.add((shape_name, RDFS.subClassOf, BSH.ValueShape))

        needs_value_properties = ["values", "units", "unitsFromQuantity", "datatype"]
        brick_value_shape = BNode()
        if any(k in defn for k in needs_value_properties):
            G.add((shape_name, SH.property, brick_value_shape))
            G.add((brick_value_shape, A, SH.PropertyShape))
            G.add((brick_value_shape, SH.path, BRICK.value))
            G.add((brick_value_shape, SH.minCount, Literal(1)))
            G.add((brick_value_shape, SH.maxCount, Literal(1)))

        v = BNode()
        # prop:value PropertyShape
        if "values" in defn:
            enumeration = BNode()
            G.add((shape_name, SH.property, brick_value_shape))
            G.add((brick_value_shape, A, SH.PropertyShape))
            G.add((brick_value_shape, SH.path, BRICK.value))
            G.add((brick_value_shape, SH["in"], enumeration))
            G.add((brick_value_shape, SH.minCount, Literal(1)))
            vals = defn.pop("values")
            if isinstance(vals[0], str):
                Collection(
                    G, enumeration, map(lambda x: Literal(x, datatype=XSD.string), vals)
                )
            elif isinstance(vals[0], int):
                Collection(
                    G,
                    enumeration,
                    map(lambda x: Literal(x, datatype=XSD.integer), vals),
                )
            elif isinstance(vals[0], float):
                Collection(
                    G,
                    enumeration,
                    map(lambda x: Literal(x, datatype=XSD.decimal), vals),
                )
            else:
                Collection(G, enumeration, map(Literal, vals))
        if "units" in defn:
            v = BNode()
            enumeration = BNode()
            G.add((shape_name, SH.property, v))
            G.add((v, A, SH.PropertyShape))
            G.add((v, SH.path, BRICK.hasUnit))
            G.add((v, SH["in"], enumeration))
            G.add((v, SH.minCount, Literal(1)))
            G.add((v, SH.maxCount, Literal(1)))
            Collection(G, enumeration, defn.pop("units"))
        if "unitsFromQuantity" in defn:
            v = BNode()
            enumeration = BNode()
            G.add((shape_name, SH.property, v))
            G.add((v, A, SH.PropertyShape))
            G.add((v, SH.path, BRICK.hasUnit))
            G.add((v, SH["in"], enumeration))
            G.add((v, SH.minCount, Literal(1)))
            G.add((v, SH.maxCount, Literal(1)))
            units = units_for_quantity(defn.pop("unitsFromQuantity"))
            assert len(units) > 0, f"Quantity shape {shape_name} has no units"
            Collection(G, enumeration, units)
        if "properties" in defn:
            prop_defns = defn.pop("properties")
            define_shape_property_property(shape_name, prop_defns)
        elif "datatype" in defn:
            G.add((shape_name, SH.property, brick_value_shape))
            G.add((brick_value_shape, A, SH.PropertyShape))
            G.add((brick_value_shape, SH.path, BRICK.value))
            dtype = defn.pop("datatype")
            if dtype == BSH.NumericValue:
                G.add((brick_value_shape, SH["or"], BSH.NumericValue))
            else:
                G.add((brick_value_shape, SH.datatype, dtype))
            G.add((brick_value_shape, SH.minCount, Literal(1)))
            if "range" in defn:
                for prop_name, prop_value in defn.pop("range").items():
                    if prop_name not in [
                        "minExclusive",
                        "minInclusive",
                        "maxExclusive",
                        "maxInclusive",
                    ]:
                        raise Exception(f"brick:value property {prop_name} not valid")
                    G.add((brick_value_shape, SH[prop_name], Literal(prop_value)))


def define_properties(definitions, superprop=None):
    """
    Define BRICK properties
    """
    if len(definitions) == 0:
        return

    for prop, propdefn in definitions.items():
        if isinstance(prop, str):
            prop = BRICK[prop]
        if superprop is not None:
            G.add((prop, RDFS.subPropertyOf, superprop))

        # define property types
        prop_types = propdefn.get(A, [])
        assert isinstance(prop_types, list)
        for prop_type in prop_types:
            G.add((prop, A, prop_type))

        # define any subproperties
        subproperties_def = propdefn.get("subproperties", {})
        assert isinstance(subproperties_def, dict)
        define_properties(subproperties_def, prop)

        # define range/domain using SHACL shapes
        if "range" in propdefn:
            defn = propdefn.pop("range")
            range_shape = BSH[f"range_shape_{prop.split('#')[-1]}"]
            G.add((range_shape, A, SH.NodeShape))
            G.add((range_shape, SH.targetSubjectsOf, prop))
            constraint = BNode()
            G.add((range_shape, SH.property, constraint))
            G.add((constraint, SH.path, prop))
            G.add((constraint, SH.minCount, Literal(1)))
            if isinstance(defn, (tuple, list)):
                enumeration = BNode()
                G.add((constraint, SH["or"], enumeration))
                constraints = []
                for cls in defn:
                    constraint = BNode()
                    G.add((constraint, SH["class"], cls))
                    constraints.append(constraint)
                Collection(G, enumeration, constraints)
            else:
                G.add((constraint, SH["class"], defn))
        if "domain" in propdefn:
            defn = propdefn.pop("domain")
            domain_shape = BSH[f"domain_shape_{prop.split('#')[-1]}"]
            G.add((domain_shape, A, SH.NodeShape))
            G.add((domain_shape, SH.targetSubjectsOf, prop))
            if isinstance(defn, (tuple, list)):
                enumeration = BNode()
                G.add((domain_shape, SH["or"], enumeration))
                constraints = []
                for cls in defn:
                    constraint = BNode()
                    G.add((constraint, SH["class"], cls))
                    constraints.append(constraint)
                Collection(G, enumeration, constraints)
            else:
                G.add((domain_shape, SH["class"], defn))

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
                if isinstance(propval, list):
                    for val in propval:
                        G.add((prop, propname, val))
                else:
                    G.add((prop, propname, propval))


def add_definitions():
    """
    Adds definitions for Brick subclasses through SKOS.definitions.

    This parses the definitions from ./bricksrc/definitions.csv and
    adds it to the graph. If available, adds the source information of
    through RDFS.seeAlso.
    """
    with open("./bricksrc/definitions.csv", encoding="utf-8") as dictionary_file:
        dictionary = csv.reader(dictionary_file)

        # skip the header
        next(dictionary)

        # add definitions, citations to the graph
        for definition in dictionary:
            term = URIRef(definition[0])
            if len(definition[1]):
                G.add((term, SKOS.definition, Literal(definition[1], lang="en")))
            if len(definition[2]):
                G.add((term, RDFS.seeAlso, URIRef(definition[2])))

    qstr = """
    select ?param where {
      ?param rdfs:subClassOf* brick:Limit.
    }
    """
    limit_def_template = "A parameter that places {direction} bound on the range of permitted values of a {setpoint}."
    params = [row["param"] for row in G.query(qstr)]
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
            logging.info(f"Inferred setpoint: {setpoint}")
        limit_def = limit_def_template.format(direction=direction, setpoint=setpoint)
        G.add((param, SKOS.definition, Literal(limit_def, lang="en")))
        class_exists = G.query(
            f"""select ?class where {{
            BIND(brick:{setpoint} as ?class)
            ?class rdfs:subClassOf* brick:Class.
        }}
        """
        ).bindings
        if not class_exists:
            logging.warning(f"WARNING: {setpoint} does not exist in Brick for {param}.")


def handle_deprecations():
    for deprecated_term, md in deprecations.items():
        deprecation = BNode()
        shape = BNode()
        rule = BNode()
        G.add((deprecated_term, A, OWL.Class))
        G.add((deprecated_term, OWL.deprecated, Literal(True)))
        label = deprecated_term.split("#")[-1].replace("_", " ")
        G.add(
            (deprecated_term, RDFS.label, Literal(label))
        )  # make sure the tag is declared as such
        subclasses = md.pop(RDFS.subClassOf)
        if subclasses is not None:
            if not isinstance(subclasses, list):
                subclasses = [subclasses]
            for subclass in subclasses:
                G.add((deprecated_term, RDFS.subClassOf, subclass))
        G.add((deprecated_term, BRICK.deprecation, deprecation))
        G.add((deprecation, BRICK.deprecatedInVersion, Literal(md["version"])))
        G.add(
            (
                deprecation,
                BRICK.deprecationMitigationMessage,
                Literal(md["mitigation_message"]),
            )
        )
        if "replace_with" in md:
            G.add((deprecation, BRICK.deprecationMigitationRule, shape))
            G.add((shape, A, SH.NodeShape))
            G.add((shape, SH.targetClass, deprecated_term))
            G.add((shape, SH.rule, rule))
            G.add((rule, A, SH.SPARQLRule))
            G.add(
                (
                    rule,
                    SH.construct,
                    Literal(
                        "CONSTRUCT {"
                        f"$this rdf:type {md['replace_with'].n3()} ."
                        "} WHERE {"
                        f"$this rdf:type {deprecated_term.n3()} . }}"
                    ),
                )
            )
            G.add((rule, SH.prefixes, URIRef(RDF)))
            G.add((rule, SH.prefixes, URIRef(BRICK)))


logging.info("Beginning BRICK Ontology compilation")
# handle ontology definition
define_ontology(G)

# Declare root classes

# we keep the definition of brick:Class, which was the root
# class of Brick prior to v1.3.0, in order to maintain backwards
# compatibility with older Brick models. Both brick:Class and
# brick:Entity are root classes
G.add((BRICK.Class, A, OWL.Class))  # < Brick v1.3.0
G.add((BRICK.Entity, A, OWL.Class))  # >= Brick v1.3.0
G.add((BRICK.Tag, A, OWL.Class))

roots = {
    "Equipment": {"tags": [TAG.Equipment]},
    "Location": {"tags": [TAG.Location]},
    "Point": {"tags": [TAG.Point]},
    "Measurable": {},
    "Collection": {"tags": [TAG.Collection]},
}
define_classes(roots, BRICK.Class)  # <= Brick v1.3.0
define_classes(roots, BRICK.Entity)  # >= Brick v1.3.0

logging.info("Defining properties")
# define BRICK properties
define_properties(properties)
# add types to some external properties
G.add((VCARD.hasAddress, A, OWL.ObjectProperty))
G.add((VCARD.Address, A, OWL.Class))

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

logging.info("Defining Equipment, System and Location subclasses")
# define other root class structures
define_classes(location_subclasses, BRICK.Location)
define_classes(equipment_subclasses, BRICK.Equipment)
define_classes(collection_classes, BRICK.Collection)
define_classes(hvac_subclasses, BRICK.HVAC_Equipment)
define_classes(hvac_valve_subclasses, BRICK.HVAC_Equipment)
define_classes(valve_subclasses, BRICK.Equipment)
define_classes(security_subclasses, BRICK.Security_Equipment)
define_classes(safety_subclasses, BRICK.Safety_Equipment)

logging.info("Defining Measurable hierarchy")
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
G.add((BRICK.Quantity, RDFS.label, Literal("Quantity")))
G.add((BRICK.Quantity, RDFS.subClassOf, SKOS.Concept))
# set up Substance definition
G.add((BRICK.Substance, RDFS.subClassOf, SOSA.FeatureOfInterest))
G.add(
    (SOSA.FeatureOfInterest, A, OWL.Class)
)  # needs the type declaration to satisfy some checkers
G.add((BRICK.Substance, RDFS.subClassOf, BRICK.Measurable))
G.add((BRICK.Substance, A, OWL.Class))
G.add((BRICK.Substance, RDFS.label, Literal("Substance")))

# We make the punning explicit here. Any subclass of brick:Substance
# is itself a substance or quantity. There is one canonical instance of
# each class, which is indicated by referencing the class itself.
#
#    bldg:tmp1      a           brick:Air_Temperature_Sensor;
#               brick:measures  brick:Air ,
#                               brick:Temperature .
#
# This makes Substance metaclasses.
define_classes(substances, BRICK.Substance, pun_classes=True)

# this defines the SKOS-based concept hierarchy for BRICK Quantities
define_concept_hierarchy(quantity_definitions, [BRICK.Quantity])

# for all Quantities, copy part of the QUDT unit definitions over
res = G.query(
    """SELECT ?quantity ?qudtquant WHERE {
                ?quantity rdf:type brick:Quantity .
                ?quantity brick:hasQUDTReference ?qudtquant
                }"""
)

# this requires two passes to associate the applicable units with
# each of the quantities. The first pass associates Brick quantities
# with QUDT units via the "hasQUDTReference" property; the second pass
# traverses the SKOS broader/narrower hierarchy to inherit associated units
# "up" into the broader concepts.
for r in res:
    brick_quant, qudt_quant = r
    for unit, symb, label in get_units(qudt_quant):
        G.add((brick_quant, QUDT.applicableUnit, unit))
        G.add((unit, A, QUDT.Unit))
        if symb is not None:
            G.add((unit, QUDT.symbol, symb))
        if label is not None and not has_label(unit):
            G.add((unit, RDFS.label, label))
for r in res:
    brick_quant, qudt_quant = r
    # the symbols, units, and labels are already defined in the previous pass
    for unit, symb, label in get_units_brick(brick_quant):
        G.add((brick_quant, QUDT.applicableUnit, unit))


# entity property definitions (must happen after units are defined)
G.add((BRICK.value, A, OWL.DatatypeProperty))
G.add((BRICK.value, SKOS.definition, Literal("The basic value of an entity property")))
G.add((BRICK.EntityProperty, RDFS.subClassOf, OWL.ObjectProperty))
G.add((BRICK.EntityProperty, A, OWL.Class))
G.add((BSH.ValueShape, A, OWL.Class))
define_shape_properties(get_shapes(G))
define_entity_properties(entity_properties)

handle_deprecations()

logging.info("Adding class definitions")
add_definitions()

# add all TTL files in bricksrc
for ttlfile in glob.glob("bricksrc/*.ttl"):
    G.parse(ttlfile, format="turtle")

# add ref-schema definitions
G.parse("support/ref-schema.ttl", format="turtle")
ref_schema_uri = URIRef(REF.strip("#"))
for triple in G.cbd(ref_schema_uri):
    G.remove(triple)

logging.info(f"Brick ontology compilation finished! Generated {len(G)} triples")

extension_graphs = {"shacl_tag_inference": shaclGraph}

# serialize extensions to output
for name, graph in extension_graphs.items():
    with open(f"extensions/brick_extension_{name}.ttl", "w", encoding="utf-8") as fp:
        # need to write this manually; turtle serializer doesn't always add
        fp.write("@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n")
        fp.write(graph.serialize(format="turtle").rstrip())
        fp.write("\n")

# add SHACL shapes to graph
G.parse("shacl/BrickEntityShapeBase.ttl", format="ttl")

# validate Brick
valid, _, report = pyshacl.validate(data_graph=G, advanced=True, allow_warnings=True)
if not valid:
    print(report)
    sys.exit(1)


# serialize Brick to output
with open("Brick.ttl", "w", encoding="utf-8") as fp:
    fp.write(G.serialize(format="turtle").rstrip())
    fp.write("\n")

# serialize Brick + extensions
for graph in extension_graphs.values():
    G += graph
with open("Brick+extensions.ttl", "w", encoding="utf-8") as fp:
    fp.write(G.serialize(format="turtle").rstrip())
    fp.write("\n")
