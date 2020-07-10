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
    In the current implementation, using owl:sameAs to align Quantity
    with QUDT QuantityKinds, we need to make sure that  a Brick Quantity
    does not end up with more than 1 QuantityKind
    """
    g = brickschema.graph.Graph()
    g.load_file("Brick.ttl")
    g.g.bind("qudt", QUDT)
    g = brickschema.inference.OWLRLInferenceSession(load_brick=False).expand(g)
    quantity_qk = g.query(
        "SELECT ?quantity ?kind WHERE {\
            ?quantity   a   brick:Quantity .\
            ?quantity   owl:sameAs ?kind }"
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

    Brick class ---measures---> Brick quantity -- sameAs --> QuantityKind
        |                                                           |
        |                            +-----applicableUnit-----------+
        |                            |
        v                            v
     Instance --- hasUnit --->   QUDT unit

    We create an instance of each Brick class which 'measures' a quantity
    and associate that instance with one of the applicable units as defined
    by QUDT. We then verify that all of those units are associated with the
    correct quantity
    """

    g = brickschema.graph.Graph()
    g.load_file("Brick.ttl")
    g.g.bind("qudt", QUDT)
    g = brickschema.inference.OWLRLInferenceSession(load_brick=False).expand(g)

    # test the definitions by making sure that some quantities have applicable
    # units
    classes_with_quantities = g.query(
        "SELECT ?class ?quantity ?unit WHERE { \
             ?class a   brick:Class .\
             ?class brick:measures ?quantity .\
             ?quantity qudt:applicableUnit ?unit }"
    )
    triples = []
    for brickclass, quantity, unit in classes_with_quantities:
        class_name = re.split("/|#", brickclass)[-1]
        unit_name = re.split("/|#", unit)[-1]
        instance_name = f"Instance_of_{class_name}_{unit_name}"
        triples.append((BLDG[instance_name], A, brickclass))
        triples.append((BLDG[instance_name], BRICK.hasUnit, unit))
    g.add(*triples)
    g = brickschema.inference.OWLRLInferenceSession(load_brick=False).expand(g)

    instances = g.query(
        "SELECT ?inst ?quantity ?unit WHERE {\
             ?inst   rdf:type        brick:Sensor .\
             ?inst   rdf:type/brick:measures  ?quantity .\
             ?quantity    a   brick:Quantity .\
             ?inst   brick:hasUnit   ?unit .}"
    )

    assert len(instances) == len(classes_with_quantities)


def test_quantity_units():
    g = brickschema.graph.Graph()
    g.load_file("Brick.ttl")
    g.g.bind("qudt", QUDT)
    g = brickschema.inference.OWLRLInferenceSession(load_brick=False).expand(g)

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
    g.g.bind("qudt", QUDT)
    g = brickschema.inference.OWLRLInferenceSession(load_brick=False).expand(g)

    # test the definitions by making sure that some quantities have applicable
    # units
    quantities_without_units = g.query(
        "SELECT ?q WHERE { \
             ?q rdf:type brick:Quantity .\
             FILTER NOT EXISTS {?q qudt:applicableUnit ?unit} }"
    )
    if len(quantities_without_units) > 0:
        warnings.warn(
            f"The following quantities do not have associated units: {quantities_without_units}"
        )
