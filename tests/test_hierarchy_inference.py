import json
from collections import defaultdict
import time
import brickschema

from tqdm import tqdm
from rdflib import Namespace, URIRef, Graph
from .util.reasoner import make_readable

"""
This script does the following:
(1) Create entities that are supposed to be instances of Classes. (Class == ``brick:Class``)
(2) Associate the entities with Tags defined for each Class.
(3) Infer each entity's classes (throughout the hierarchy) based only on its Tags.

If the schema is correctly designe, the following properties should be met
[1] Each of the entities should be an instance of the target Class defined in (2).
[2] Each of the entities should be instances of all the parent Classes of the target Class but nothing else. This is basically a super set of [1].

This test is a superset of ``test_inference.py``.
"""

inference_file = 'tests/test_hierarchy_inference.ttl'

BRICK_VERSION = '1.1.0'
BRICK = Namespace(f"https://brickschema.org/schema/{BRICK_VERSION}/Brick#")
TAG = Namespace(f"https://brickschema.org/schema/{BRICK_VERSION}/BrickTag#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
entity_postfix = '_0'

q_prefix = """
prefix brick: <https://brickschema.org/schema/1.1.0/Brick#>
prefix owl: <http://www.w3.org/2002/07/owl#>
"""


def test_hierarchyinference():

    # Load the schema
    g = Graph()
    g.parse('Brick.ttl', format='turtle')

    #if args.reuse_inference:  # Reuse previously inferred file if the flag is set.
    #    expanded_g = Graph()
    #    expanded_g.parse(inference_file, format='turtle')
    #else:  # create instances and associate them with related Tags.

    # Get all the Classes with their restrictions.
    qstr = q_prefix + """
    select ?class ?tag where {
      ?class rdfs:subClassOf+ brick:Class.
      ?class brick:hasAssociatedTag ?tag
    }
    """
    start_time = time.time()
    for row in tqdm(g.query(qstr)):
        klass = row[0]
        entity = klass + entity_postfix  # Define an entity for the class
        g.add((entity, BRICK.hasTag, row[1]))  # Associate the entity with restrictions (i.e., Tags)
    end_time = time.time()
    print('Instantiation took {0} seconds'.format(int(end_time-start_time)))

    # Infer classes of the entities.
    # Apply reasoner
    g.serialize('test.ttl', format='ttl')
    g = brickschema.inference.TagInferenceSession(approximate=False, load_brick=False).expand(g)
    g = brickschema.inference.OWLRLAllegroInferenceSession(load_brick=False).expand(g)
    g.serialize(inference_file, format='turtle')  # Store the inferred graph.


    # Find all instances and their parents from the inferred graph.
    qstr = q_prefix + """
    select ?instance ?class where {
        ?instance a ?class.
        ?class rdfs:subClassOf* brick:Class.
    }
    """
    inferred_klasses = defaultdict(set)
    for row in tqdm(g.query(qstr)):
        entity = row[0]
        klass = row[1]
        if BRICK in klass: # Filter out non-Brick classes such as Restrictions
            inferred_klasses[entity].add(klass)

    # get equivalent classes
    equivalent_classes = defaultdict(set)
    res = g.query(q_prefix+"""\nSELECT ?c1 ?c2 WHERE {
        ?c1 owl:equivalentClass ?c2
    }""")
    for (c1, c2) in res:
        equivalent_classes[c1].add(c2)
        equivalent_classes[c2].add(c1)

    over_inferences = {}  # Inferred Classes that are not supposed to be inferred.
    under_inferences = {}  # Classes that should have been inferred but not actually inferred.
    wrong_inferences = {}  # Other wrongly inferred Classes.
    for entity, inferred_parents in inferred_klasses.items():
        if entity[-2:] != entity_postfix:
            continue
        true_class = URIRef(entity[0:-2])  # This is based on how the entity name is defined above.

        # Find the original classes through the hierarchy from the original graph.
        qstr = q_prefix + """
        select ?parent where {{
            <{0}> rdfs:subClassOf* ?parent.
            ?parent rdfs:subClassOf* brick:Class.
        }}
        """.format(true_class)
        res = g.query(qstr)
        true_parents = [row[0] for row in res]
        for tp in true_parents[:]:
            true_parents.extend(equivalent_classes.get(tp, []))
        true_parents = set(filter(lambda parent: BRICK in parent, true_parents))
        # TODO: bug here where this does not consider equivalent classes
        serialized = {
            'inferred_parents': list(inferred_parents),
            'true_parents': list(true_parents),
        }
        if inferred_parents > true_parents:
            over_inferences[entity] = serialized
            diff = set(inferred_parents).difference(set(true_parents))
            print(f"Tags for {true_class.split('#')[-1]} imply extra classes: {make_readable([diff])}")
        elif inferred_parents < true_parents:
            under_inferences[entity] = serialized
            diff = set(true_parents).difference(set(inferred_parents))
            print(f"Tags for {true_class.split('#')[-1]} do not imply classes, but should: {make_readable([diff])}")
        elif inferred_parents != true_parents:
            wrong_inferences[entity] = serialized


    with open('tests/test_hierarchy_inference.json', 'w') as fp:
        json.dump({
            'over_inferences': over_inferences,
            'under_inferences': under_inferences,
            'wrong_inferencers': wrong_inferences,
        }, fp, indent=2)

    assert not over_inferences, 'There are {0} classes that are over-inferred'.format(len(over_inferences))
    assert not under_inferences, 'There are {0} classes that are under-inferred'.format(len(under_inferences))
    assert not wrong_inferences, 'There are {0} classes that are inferred incorrectly in other ways'.format(len(wrong_inferences))
