import rdflib
from rdflib import RDF, OWL, RDFS, Namespace, BNode
import brickschema
from .util import make_readable
from collections import defaultdict
import sys

sys.path.append("..")
from bricksrc.namespaces import BRICK, TAG  # noqa: E402

BLDG = Namespace("https://brickschema.org/schema/ExampleBuilding#")

g = brickschema.Graph()
g.load_file("Brick.ttl")
g.expand(profile="shacl")

res = g.query(
    """SELECT ?m ?class WHERE {
    ?class rdfs:subClassOf brick:Class .
    ?class owl:equivalentClass ?restrictions .
    ?restrictions owl:intersectionOf ?inter .
    ?inter rdf:rest*/rdf:first ?node .
    ?node owl:onProperty brick:measures .
    ?node owl:hasValue ?m
    }"""
)
measurable_mapping = defaultdict(set)
for row in res:
    m, c = row[0], row[1]
    if isinstance(c, BNode):
        continue
    measurable_mapping[c].add(m)
desired_inferences = {}
for c, measurables in measurable_mapping.items():
    # print(f"{c} => {measurables}")
    inst = BLDG[f"test_inst_{c.split('#')[-1]}"]
    desired_inferences[inst] = c
    for m in measurables:
        g.add((inst, BRICK.measures, m))

g.expand(profile="shacl")

g.bind("rdf", RDF)
g.bind("owl", OWL)
g.bind("rdfs", RDFS)
g.bind("brick", BRICK)
g.bind("tag", TAG)
g.bind("bldg", BLDG)


# NOTE: currently removing these tests.
# Explanation: these tests verified that the quantities and substances that we
# are punning in Brick were explicitly defined. We now have reason to believe
# that *explicitly* instantiating these punned classes can cause issues with
# OWL-RL reasoning. The new test 'test_measurable_inference' tests that the use
# of the brick:measures relationship properly infers classes

# def test_quantity_instances():
#     quantities = g.query("SELECT ?q WHERE {\
#                           ?q a brick:Quantity\
#                           }")
#     quantity_classes = g.query("SELECT ?q WHERE {\
#                             ?q rdfs:subClassOf+ brick:Quantity}")
#     quantities = set(quantities)
#     quantity_classes = set(quantity_classes)
#     quantity_classes.remove((OWL.Nothing, ))
#     assert(set(quantities) == set(quantity_classes))
#
#
# def test_substance_instances():
#     substances = g.query("SELECT ?q WHERE {\
#                           ?q a brick:Substance\
#                           }")
#     substance_classes = g.query("SELECT ?q WHERE {\
#                             ?q rdfs:subClassOf+ brick:Substance}")
#     substances = set(substances)
#     substance_classes = set(substance_classes)
#     substance_classes.remove((OWL.Nothing, ))
#     assert(set(substances) == set(substance_classes))


def test_measurables_defined():
    # test to make sure all objects of the
    # brick:measures relationship are a Measurable
    measurable = make_readable(
        g.query(
            "SELECT ?m WHERE {\
                                        ?m a brick:Measurable\
                                        }"
        )
    )

    measured = make_readable(
        g.query(
            """SELECT ?m WHERE {
        ?class rdfs:subClassOf brick:Class .
        ?class owl:equivalentClass ?restrictions .
        ?restrictions owl:intersectionOf ?inter .
        ?inter rdf:rest*/rdf:first ?node .
        ?node owl:onProperty brick:measures .
        ?node owl:hasValue ?m
        }"""
        )
    )
    for m in measured:
        assert m in measurable


def test_measurable_inference():
    for inst, klass in desired_inferences.items():
        res = g.query(f"SELECT ?class WHERE {{ <{inst}> rdf:type ?class }}")
        assert klass in [row[0] for row in res]
