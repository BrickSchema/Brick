import rdflib
from rdflib import RDF, OWL, RDFS, Namespace
from util.reasoner import reason_brick, make_readable

BRICK_VERSION = '1.1.0'
BRICK = Namespace("https://brickschema.org/schema/{0}/Brick#".format(BRICK_VERSION))
TAG = Namespace("https://brickschema.org/schema/{0}/BrickTag#".format(BRICK_VERSION))
BLDG = Namespace("https://brickschema.org/schema/ExampleBuilding#")

g = rdflib.Graph()
g.parse('Brick.ttl', format='turtle')


g.add((BLDG.Tmp1, RDF.type, BRICK.Air_Temperature_Sensor))

reason_brick(g)

g.bind('rdf', RDF)
g.bind('owl', OWL)
g.bind('rdfs', RDFS)
g.bind('brick', BRICK)
g.bind('tag', TAG)
g.bind('bldg', BLDG)

def test_quantity_instances():
    quantities = make_readable(g.query("SELECT ?q WHERE { ?q a brick:Quantity}"))
    quantity_classes = make_readable(g.query("SELECT ?q WHERE { ?q rdfs:subClassOf+ brick:Quantity}"))
    assert(sorted(quantities) == sorted(quantity_classes))


def test_substance_instances():
    substances = make_readable(g.query("SELECT ?q WHERE { ?q a brick:Substance}"))
    substance_classes = make_readable(g.query("SELECT ?q WHERE { ?q rdfs:subClassOf+ brick:Substance}"))
    assert(sorted(substances) == sorted(substance_classes))

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
