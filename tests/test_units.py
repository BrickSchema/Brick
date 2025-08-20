from rdflib import Namespace
import re
import brickschema
from collections import defaultdict
import warnings
import sys

sys.path.append("..")
from bricksrc.namespaces import A, BRICK, QUDT  # noqa: E402

BLDG = Namespace("https://brickschema.org/schema/ExampleBuilding#")


def test_quantity_has_one_quantitykind(brick_with_imports):
    """
    In the current implementation, using brick:hasQUDTReference to align Quantity
    with QUDT QuantityKinds, we need to make sure that  a Brick Quantity
    does not end up with more than 1 QuantityKind
    """
    g = brick_with_imports
    g.compile()
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


def test_instances_measure_correct_units(brick_with_imports):
    """
    Ensures that, for every (Class, Quantity, Unit) where the Unit is applicable
    to the Quantity of that Class, we can create an instance of the Class with
    that Unit and it is recognized as having an applicable unit for at least one
    quantity of the class. Also guards that we created one instance per source row.
    """

    g = brick_with_imports

    classes_with_quantities = g.query(
        "SELECT distinct ?class ?quantity ?unit WHERE { \
             ?class rdfs:subClassOf* brick:Point .\
             ?class brick:hasQuantity ?quantity .\
             ?quantity qudt:applicableUnit ?unit . \
             FILTER NOT EXISTS { ?class brick:aliasOf ?alias } }"
    )

    triples = []
    for brickclass, quantity, unit in classes_with_quantities:
        class_name = re.split("/|#", brickclass)[-1]
        quantity_name = re.split("/|#", quantity)[-1]
        unit_name = re.split("/|#", unit)[-1]
        instance = BLDG[f"Instance_of_{class_name}_{quantity_name}_{unit_name}"]
        triples.append((instance, A, brickclass))
        triples.append((instance, BRICK.hasUnit, unit))

    if triples:
        g.add(*triples)
    g.compile()

    # Each created instance should be countable via the applicability join.
    instances = g.query(
        "SELECT DISTINCT ?inst WHERE { \
             ?inst rdf:type/rdfs:subClassOf* ?klass . \
             ?klass brick:hasQuantity ?quantity . \
             ?inst brick:hasUnit ?unit . \
             ?quantity qudt:applicableUnit ?unit . \
             FILTER NOT EXISTS { ?klass brick:aliasOf ?alias } }"
    )
    assert len(instances) == len(classes_with_quantities)

    # There should be no instance whose unit is not applicable to any quantity of its class.
    mismatches = list(
        g.query(
            "SELECT DISTINCT ?inst ?klass ?unit WHERE { \
                 ?inst a ?klass ; \
                       brick:hasUnit ?unit . \
                 ?klass rdfs:subClassOf* brick:Point . \
                 FILTER NOT EXISTS { \
                   ?klass rdfs:subClassOf* ?k . \
                   ?k brick:hasQuantity ?q . \
                   ?q qudt:applicableUnit ?unit . \
                 } \
                 FILTER NOT EXISTS { ?klass brick:aliasOf ?alias } \
            }"
        )
    )
    assert len(mismatches) == 0, f"Found {len(mismatches)} instances with non-applicable units, e.g. {mismatches[:5]}"


def test_quantity_units(brick_with_imports):
    g = brick_with_imports
    g.bind("qudt", QUDT)
    g.compile()

    # test the definitions by making sure that some quantities have applicable
    # units
    quantities_with_units = g.query(
        "SELECT ?q WHERE { \
             ?q rdf:type brick:Quantity .\
             ?q qudt:applicableUnit ?unit}"
    )
    assert len(quantities_with_units) > 0


def test_all_quantities_have_units(brick_with_imports):
    g = brick_with_imports
    g.compile()

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


# Deleting this test because it requires RDFS semantics, which we are no longer
# using.
# def test_points_hierarchy_units(brick_with_imports):
#     g = brick_with_imports
#     qstr = """
# SELECT ?class (GROUP_CONCAT(?class_unit) as ?class_units) ?parent (GROUP_CONCAT(?parent_unit) AS ?parent_units) WHERE {
#   ?class brick:hasQuantity ?class_quantity.
#   ?class_quantity qudt:applicableUnit ?class_unit.
#
#   ?class rdfs:subClassOf ?parent.
#
#   ?parent brick:hasQuantity ?parent_quantity.
#   ?parent_quantity qudt:applicableUnit ?parent_unit.
# } GROUP BY ?class ?parent
#     """
#
#     unfound_units = defaultdict(dict)
#     for row in g.query(qstr):
#         curr_units = set([unit.split("/")[-1] for unit in row[1].split()])
#         parent_units = set([unit.split("/")[-1] for unit in row[3].split()])
#         if not curr_units.issubset(parent_units):
#             print('---'*30)
#             print(f"{row[0]} with parent {row[2]}")
#             print(f"{curr_units=}")
#             print(f"{parent_units=}")
#             klass = row[0].split("#")[-1]
#             parent = row[2].split("#")[-1]
#             unfound_units[parent][klass] = curr_units - parent_units
#     assert not dict(unfound_units)
