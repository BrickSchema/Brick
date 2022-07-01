import rdflib
import json
from collections import defaultdict
from rdflib import Namespace, URIRef
import brickschema
import sys

sys.path.append("..")
from bricksrc.namespaces import BRICK  # noqa: E402
from bricksrc.substances import substances  # noqa: E402
from bricksrc.quantities import quantity_definitions  # noqa: E402

BLDG = Namespace("https://brickschema.org/schema/ExampleBuilding#")


def _get_subclasses(hierarchy):
    """
    Helper method to generate a list of pairwise
    subclass relationships denoted by a hierarchy definition in 'bricksrc'
    """
    for klass, defn in hierarchy.items():
        if "subclasses" not in defn:
            continue
        for subklass, subdefn in defn["subclasses"].items():
            yield (klass, subklass)
        for tup in _get_subclasses(defn["subclasses"]):
            yield tup


def test_measurable_hierarchy():
    """
    Checks to make sure the hierarchy is preserved when the
    ontology is serialized. All subclass relationships explicitly
    included in the substances + quantities hierarchies should
    be in the ontology
    """
    g = rdflib.Graph()
    g.parse("Brick.ttl", format="turtle")

    # check substance classes
    for klass, subklass in _get_subclasses(substances):
        query = f"SELECT ?x WHERE {{ <{BRICK[subklass]}> rdfs:subClassOf ?x }}"
        res = list(g.query(query))
        assert (BRICK[klass],) in res


def test_measures_infers():
    g = brickschema.Graph()
    g.load_file("Brick.ttl")

    qstr = """select ?class ?o where {
      ?class rdfs:subClassOf+ brick:Class.
      ?class owl:equivalentClass ?restrictions.
      ?restrictions owl:intersectionOf ?inter.
      ?inter rdf:rest*/rdf:first ?node.
      ?node owl:onProperty brick:measures .
      ?node owl:hasValue ?o.
    }
    """
    for row in g.query(qstr):
        klass = row[0]
        entity = klass + "_entity"  # Define an entity for the class
        g.add(
            (entity, BRICK.measures, row[1])
        )  # Associate the entity with measurement restrictions

    # Infer classes of the entities.
    # Apply reasoner
    g.expand(profile="shacl")

    qstr = """select ?instance ?class where {
        ?instance a ?class.
        ?class rdfs:subClassOf* brick:Class.
    }
    """
    inferred_klasses = defaultdict(set)
    for row in g.query(qstr):
        entity = row[0]
        klass = row[1]
        if BRICK in klass:  # Filter out non-Brick classes such as Restrictions
            inferred_klasses[entity].add(klass)

    over_inferences = {}  # Inferred Classes that are not supposed to be inferred.
    under_inferences = (
        {}
    )  # Classes that should have been inferred but not actually inferred.
    wrong_inferences = {}  # Other wrongly inferred Classes.
    for entity, inferred_parents in inferred_klasses.items():
        if entity[-7:] != "_entity":
            continue
        true_class = URIRef(
            entity[0:-7]
        )  # This is based on how the entity name is defined above.

        # Find the original classes through the hierarchy from the original graph.
        qstr = """select ?parent where {{
            {{
                <{0}> owl:equivalentClass*/rdfs:subClassOf*/owl:equivalentClass*/rdfs:subClassOf* ?parent .
            }} UNION {{
                ?other owl:equivalentClass* <{0}> .
                ?other rdfs:subClassOf*/owl:equivalentClass*/rdfs:subClassOf* ?parent .
            }}
            ?parent rdfs:subClassOf* brick:Class
        }}
        """.format(
            true_class
        )
        res = g.query(qstr)
        true_parents = [row[0] for row in res]
        true_parents = set(filter(lambda parent: BRICK in parent, true_parents))
        serialized = {
            "inferred_parents": list(inferred_parents),
            "true_parents": list(true_parents),
        }
        if inferred_parents > true_parents:
            over_inferences[entity] = serialized
        elif inferred_parents < true_parents:
            under_inferences[entity] = serialized
        elif inferred_parents != true_parents:
            wrong_inferences[entity] = serialized

    with open("tests/test_measures_inference.json", "w") as fp:
        json.dump(
            {
                "over_inferences": over_inferences,
                "under_inferences": under_inferences,
                "wrong_inferencers": wrong_inferences,
            },
            fp,
            indent=2,
        )
        fp.write("\n")

    assert not over_inferences, "There are {0} classes that are over-inferred".format(
        len(over_inferences)
    )
    assert not under_inferences, "There are {0} classes that are under-inferred".format(
        len(under_inferences)
    )
    assert (
        not wrong_inferences
    ), "There are {0} classes that are inferred incorrectly in other ways".format(
        len(wrong_inferences)
    )
