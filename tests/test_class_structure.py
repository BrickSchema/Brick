import rdflib
from rdflib import RDF, OWL, RDFS, Namespace
from util.reasoner import reason_brick, make_readable

BRICK_VERSION = '1.1.0'
BRICK = Namespace("https://brickschema.org/schema/{0}/Brick#".format(BRICK_VERSION))
TAG = Namespace("https://brickschema.org/schema/{0}/BrickTag#".format(BRICK_VERSION))
BLDG = Namespace("https://brickschema.org/schema/ExampleBuilding#")
SOSA = Namespace("http://www.w3.org/ns/sosa#")

g = rdflib.Graph()
g.parse('Brick.ttl', format='turtle')

reason_brick(g)

g.bind('rdf', RDF)
g.bind('owl', OWL)
g.bind('rdfs', RDFS)
g.bind('brick', BRICK)
g.bind('tag', TAG)
g.bind('bldg', BLDG)

def test_subclasses():
    subclasses1 = g.query("SELECT ?parent ?child WHERE { ?child rdfs:subClassOf ?parent }")
    subclasses2 = g.query("SELECT ?parent ?child WHERE { ?child rdfs:subClassOf ?parent . ?child a owl:Class . ?parent a owl:Class }")
    sc1 = [x[0] for x in subclasses1]
    sc2 = [x[0] for x in subclasses2]
    diff = set(sc1).difference(set(sc2))

    # there should only be these two SOSA properties outside of Brick *at this point in time*
    expected = set([
        SOSA.FeatureOfInterest,
        SOSA.ObservableProperty
    ])
    assert expected == diff, f"Got extra classes that may not be defined: {diff.difference(expected)}"
