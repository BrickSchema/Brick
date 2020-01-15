import rdflib
from rdflib import RDF, OWL, RDFS, Namespace, BNode
from util.reasoner import reason_brick, make_readable, reason_owlrl
from collections import defaultdict

BRICK_VERSION = '1.1.0'
BRICK = Namespace("https://brickschema.org/schema/{0}/Brick#".format(BRICK_VERSION))
TAG = Namespace("https://brickschema.org/schema/{0}/BrickTag#".format(BRICK_VERSION))
BLDG = Namespace("https://brickschema.org/schema/ExampleBuilding#")

g = rdflib.Graph()
g.parse('Brick.ttl', format='turtle')


g.add((BLDG.Tmp1, RDF.type, BRICK.Air_Temperature_Sensor))

reason_owlrl(g)

res = g.query("""SELECT ?m ?class WHERE {
    ?class rdfs:subClassOf brick:Class .
    ?class owl:equivalentClass ?restrictions .
    ?restrictions owl:intersectionOf ?inter .
    ?inter rdf:rest*/rdf:first ?node .
    ?node owl:onProperty brick:measures .
    ?node owl:hasValue ?m
    }""")
measurable_mapping = defaultdict(set)
for row in res:
    m, c = row[0], row[1]
    if isinstance(c, BNode):
        continue
    measurable_mapping[c].add(m)
desired_inferences = {}
for c, measurables in measurable_mapping.items():
    print(f"{c} => {measurables}")
    inst = BLDG[f"test_inst_{c.split('#')[-1]}"]
    desired_inferences[inst] = c
    for m in measurables:
        g.add((inst, BRICK.measures, m))

reason_owlrl(g)

g.bind('rdf', RDF)
g.bind('owl', OWL)
g.bind('rdfs', RDFS)
g.bind('brick', BRICK)
g.bind('tag', TAG)
g.bind('bldg', BLDG)


# NOTE: currently removing these tests.
# Explanation: these tests verified that the quantities and substances that we
# are punning in Brick were explicitly defined. We now have reason to believe
# that *explicitly* instantiating these punned classes can cause issues with
# OWL-RL reasoning. The new test 'test_measurable_inference' tests that the use
# of the brick:measures relationship properly infers classes
#
# def test_quantity_instances():
#     quantities = make_readable(g.query("SELECT ?q WHERE { ?q a brick:Quantity}"))
#     quantity_classes = make_readable(g.query("SELECT ?q WHERE { ?q rdfs:subClassOf+ brick:Quantity}"))
#     assert(sorted(quantities) == sorted(quantity_classes))
#
#
# def test_substance_instances():
#     substances = make_readable(g.query("SELECT ?q WHERE { ?q a brick:Substance}"))
#     substance_classes = make_readable(g.query("SELECT ?q WHERE { ?q rdfs:subClassOf+ brick:Substance}"))
#     assert(sorted(substances) == sorted(substance_classes))

def test_measurables_defined():
    # test to make sure all objects of the brick:measures relationship are a Measurable
    measurable = make_readable(g.query("SELECT ?m WHERE { ?m a brick:Measurable }"))

    measured = make_readable(g.query("""SELECT ?m WHERE {
        ?class rdfs:subClassOf brick:Class .
        ?class owl:equivalentClass ?restrictions .
        ?restrictions owl:intersectionOf ?inter .
        ?inter rdf:rest*/rdf:first ?node .
        ?node owl:onProperty brick:measures .
        ?node owl:hasValue ?m
        }"""))
    for m in measured:
        assert m in measurable

def test_measurable_inference():
    for inst, klass in desired_inferences.items():
        res = g.query(f"SELECT ?class WHERE {{ <{inst}> rdf:type ?class }}")
        assert klass in [row[0] for row in res]
