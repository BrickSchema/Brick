from rdflib import Namespace
import re
import brickschema
from collections import defaultdict
import warnings
import sys

sys.path.append("..")
from bricksrc.namespaces import A, BRICK, TAG, QUDT  # noqa: E402

BLDG = Namespace("https://brickschema.org/schema/ExampleBuilding#")


def test_quantity_has_one_quantitykind():
    """
    In the current implementation, using brick:hasQUDTReference to align Quantity
    with QUDT QuantityKinds, we need to make sure that  a Brick Quantity
    does not end up with more than 1 QuantityKind
    """
    g = brickschema.graph.Graph()
    g.load_file("Brick.ttl")
    g.bind("qudt", QUDT)
    g.expand(profile="shacl")
    quantity_qk = g.query(
        "SELECT ?quantity ?kind WHERE {\
            ?quantity   a   brick:Quantity .\
            ?quantity   brick:hasQUDTReference ?kind }"
    )
    assert len(quantity_qk) > 0
    seen = defaultdict(list)
    for quant, quantkind in quantity_qk:
        if quant == quantkind:
            continue
        if "Brick" in quant and "qudt" in quantkind:
            seen[quant].append(quantkind)
    for quant, kindlist in seen.items():
        assert (
            len(kindlist) == 1
        ), f"Quantity {quant} has more than one associated QuantityKind! {kindlist}"


def test_instances_measure_correct_units():
    """
    Tests that the units associated with instances are properly linked
    through the QuantityKinds

    Recall that the Brick unit model is such:

    Brick class --- hasQuantity ---> Brick quantity -- hasQUDTReference --> QuantityKind
        |                                                           |
        |                            +-----applicableUnit-----------+
        |                            |
        v                            v
     Instance --- hasUnit --->   QUDT unit

    We create an instance of each Brick class which 'hasQuantity ' a quantity
    and associate that instance with one of the applicable units as defined
    by QUDT. We then verify that all of those units are associated with the
    correct quantity
    """

    g = brickschema.graph.Graph()
    g.load_file("Brick.ttl")
    g.bind("qudt", QUDT)
    g.expand(profile="shacl")

    # test the definitions by making sure that some quantities have applicable
    # units
    classes_with_quantities = g.query(
        "SELECT distinct ?class ?quantity ?unit WHERE { \
             ?class rdfs:subClassOf* brick:Point .\
             ?class brick:hasQuantity ?quantity .\
             ?quantity qudt:applicableUnit ?unit }"
    )
    triples = []
    for brickclass, quantity, unit in classes_with_quantities:
        class_name = re.split("/|#", brickclass)[-1]
        unit_name = re.split("/|#", unit)[-1]
        instance = BLDG[f"Instance_of_{class_name}_{unit_name}"]
        triples.append((instance, A, brickclass))
        triples.append((instance, BRICK.hasUnit, unit))
    g.add(*triples)
    g.expand(profile="shacl")
    g.expand(profile="rdfs")

    instances = g.query(
        "SELECT distinct ?inst WHERE {\
             ?inst   rdf:type        brick:Point .\
             ?inst   rdf:type/brick:hasQuantity  ?quantity .\
             ?quantity    a   brick:Quantity .\
             ?inst   brick:hasUnit   ?unit .}"
    )
    assert len(instances) == len(classes_with_quantities)


def test_quantity_units():
    g = brickschema.graph.Graph()
    g.load_file("Brick.ttl")
    g.bind("qudt", QUDT)
    g.expand(profile="shacl")

    # test the definitions by making sure that some quantities have applicable
    # units
    quantities_with_units = g.query(
        "SELECT ?q WHERE { \
             ?q rdf:type brick:Quantity .\
             ?q qudt:applicableUnit ?unit}"
    )
    assert len(quantities_with_units) > 0


def test_all_quantities_have_units():
    g = brickschema.graph.Graph()
    g.load_file("Brick.ttl")
    g.bind("qudt", QUDT)
    g.expand(profile="shacl")

    # test the definitions by making sure that some quantities have applicable
    # units
    quantities_without_units = list(
        g.query(
            "SELECT ?q WHERE { \
             ?q rdf:type brick:Quantity .\
             FILTER NOT EXISTS {?q qudt:applicableUnit ?unit} }"
        )
    )
    if len(quantities_without_units) > 0:
        warnings.warn(
            f"The following quantities do not have associated units: {quantities_without_units}"
        )


def test_points_hierarchy_units():
    g = brickschema.graph.Graph()
    g.load_file("Brick.ttl")
    qstr = """
SELECT ?class (GROUP_CONCAT(?class_unit) as ?class_units) ?parent (GROUP_CONCAT(?parent_unit) AS ?parent_units) WHERE {
  ?class brick:hasQuantity ?class_quantity.
  ?class_quantity qudt:applicableUnit ?class_unit.

  ?class rdfs:subClassOf ?parent.

  ?parent brick:hasQuantity ?parent_quantity.
  ?parent_quantity qudt:applicableUnit ?parent_unit.
} GROUP BY ?class ?parent
    """

    unfound_units = defaultdict(dict)
    for row in g.query(qstr):
        curr_units = set([unit.split("/")[-1] for unit in row[1].split()])
        parent_units = set([unit.split("/")[-1] for unit in row[3].split()])
        if not curr_units.issubset(parent_units):
            klass = row[0].split("#")[-1]
            parent = row[2].split("#")[-1]
            unfound_units[parent][klass] = curr_units - parent_units
    assert not dict(unfound_units)
