import rdflib
import brickschema
from rdflib import RDF, OWL, RDFS, Namespace, BNode
from .util.reasoner import make_readable

BRICK_VERSION = '1.1.0'
BRICK = Namespace(f"https://brickschema.org/schema/{BRICK_VERSION}/Brick#")
TAG = Namespace(f"https://brickschema.org/schema/{BRICK_VERSION}/BrickTag#")
BLDG = Namespace("https://brickschema.org/schema/ExampleBuilding#")
SOSA = Namespace("http://www.w3.org/ns/sosa#")

g = rdflib.Graph()
g.parse('Brick.ttl', format='turtle')

g = brickschema.inference.TagInferenceSession(approximate=False, load_brick=False).expand(g)
g = brickschema.inference.OWLRLAllegroInferenceSession(load_brick=False).expand(g)

g.bind('rdf', RDF)
g.bind('owl', OWL)
g.bind('rdfs', RDFS)
g.bind('brick', BRICK)
g.bind('tag', TAG)
g.bind('bldg', BLDG)

def test_subclasses():
    subclasses1 = g.query("SELECT ?parent ?child WHERE {\
                                ?child rdfs:subClassOf ?parent\
                          }")
    subclasses2 = g.query("SELECT ?parent ?child WHERE {\
                            ?child rdfs:subClassOf ?parent .\
                            ?child a owl:Class .\
                            ?parent a owl:Class\
                          }")
    # filter out subclass of self (reflexive)
    subclasses1 = list(filter(lambda x: x[0] != x[1], subclasses1))
    subclasses2 = list(filter(lambda x: x[0] != x[1], subclasses2))
    # filter out BNodes
    subclasses1 = list(filter(lambda x: not isinstance(x[0], BNode), subclasses1))
    subclasses2 = list(filter(lambda x: not isinstance(x[0], BNode), subclasses2))
    subclasses1 = list(filter(lambda x: not isinstance(x[1], BNode), subclasses1))
    subclasses2 = list(filter(lambda x: not isinstance(x[1], BNode), subclasses2))
    # get parents
    sc1 = [x[0] for x in subclasses1]
    sc2 = [x[0] for x in subclasses2]
    diff = set(sc1).difference(set(sc2))

    # there should only be these properties  outside of Brick *at this point
    # in time*. We check for a subset because depending on differences in
    # implementation details of reasoners, we may get some of these axiomatic
    # classes or not
    expected = set([
        SOSA.FeatureOfInterest,
        SOSA.ObservableProperty,
        RDFS.Resource,
        RDFS.Class,
        RDF.Property,
        OWL.Class
    ])

    assert diff.issubset(expected), f"Got extra classes that may not be defined: \
                                      {diff.difference(expected)}"
