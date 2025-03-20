import sys
from rdflib import RDF, OWL, RDFS, Namespace, BNode

sys.path.append("..")
from bricksrc.namespaces import (  # noqa: E402
    BRICK,
    TAG,
    SOSA,
    VCARD,
    SKOS,
    QUDT,
    XSD,
)


def test_subclasses(brick_with_imports):
    BLDG = Namespace("https://brickschema.org/schema/ExampleBuilding#")

    g = brick_with_imports
    g.expand("shacl", backend="topquadrant")

    g.bind("rdf", RDF)
    g.bind("owl", OWL)
    g.bind("rdfs", RDFS)
    g.bind("brick", BRICK)
    g.bind("tag", TAG)
    g.bind("bldg", BLDG)
    subclasses1 = g.query(
        "SELECT ?parent ?child WHERE {\
                                ?child rdfs:subClassOf ?parent . \
                                FILTER NOT EXISTS {?parent a sh:NodeShape} \
                          }"
    )
    subclasses2 = g.query(
        "SELECT ?parent ?child WHERE {\
                            ?child rdfs:subClassOf ?parent .\
                            ?child a owl:Class .\
                            ?parent a owl:Class\
                          }"
    )

    def _cond(x) -> bool:
        return (
            x[0] != x[1]
            and not isinstance(x[0], BNode)
            and not isinstance(x[1], BNode)
            and x[0].startswith(BRICK)
            and x[1].startswith(BRICK)
        )

    # filter out subclass of self (reflexive), BNodes, non-brick classes
    subclasses1 = list(filter(lambda x: _cond(x), subclasses1))
    subclasses2 = list(filter(lambda x: _cond(x), subclasses2))
    # get parents
    sc1 = [x[0] for x in subclasses1]
    sc2 = [x[0] for x in subclasses2]
    diff = set(sc1).difference(set(sc2))

    # there should only be these properties  outside of Brick *at this point
    # in time*. We check for a subset because depending on differences in
    # implementation details of reasoners, we may get some of these axiomatic
    # classes or not
    expected = set(
        [
            SOSA.FeatureOfInterest,
            SOSA.ObservableProperty,
            RDFS.Resource,
            RDFS.Class,
            RDF.Property,
            OWL.Class,
            OWL.ObjectProperty,
            VCARD.Address,
            SKOS.Concept,
            QUDT.Unit,
            QUDT.QuantityKind,
            XSD.string,
            BRICK.Relationship,
        ]
    )

    remaining = diff.difference(expected)
    assert diff.issubset(
        expected
    ), f"Got extra classes that may not be defined: \
                                      {remaining}"


def test_non_root_classes_are_subclasses(brick_with_imports):
    # find all owl:Class which are in the Brick namespace
    # and are not subclasses of any other class
    query = f"""
    SELECT ?class WHERE {{
        ?class a owl:Class .
        FILTER STRSTARTS(STR(?class), "{BRICK}") .
        FILTER NOT EXISTS {{
            ?class rdfs:subClassOf ?parent .
        }}
        FILTER ( ?class NOT IN (brick:Class, brick:Entity, brick:EntityPropertyValue, brick:EntityProperty, brick:Tag) )
    }}"""
    for result in brick_with_imports.query(query):
        assert False, f"Class {result} is not a subclass of any other class"
