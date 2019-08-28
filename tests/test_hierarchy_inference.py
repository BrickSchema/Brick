import argparse
import json
from copy import deepcopy
from collections import defaultdict

from tqdm import tqdm
import arrow
import owlrl
from rdflib import RDF, OWL, RDFS, Namespace, URIRef, Graph

parser = argparse.ArgumentParser()
parser.add_argument('--reuse-inference',
                    action='store_const',
                    default=False,
                    const=True,
                    dest='reuse_inference',
                    )
args = parser.parse_args()
inference_file = 'tests/test_hierarchy_inference.ttl'

def rereason_owlrl(G, dummy=None):
    start_time = arrow.get()
    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(G)
    end_time = arrow.get()
    print('{0} took for owlrl reasoning'.format(end_time - start_time))
    return G

BRICK_VERSION = '1.1.0'
BRICK = Namespace("https://brickschema.org/schema/{0}/Brick#".format(BRICK_VERSION))
TAG = Namespace("https://brickschema.org/schema/{0}/BrickTag#".format(BRICK_VERSION))
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
entity_postfix = '_0'

q_prefix = """
prefix brick: <https://brickschema.org/schema/1.1.0/Brick#>
prefix owl: <http://www.w3.org/2002/07/owl#>
"""

g = Graph()
g.parse('Brick.ttl', format='turtle')

qstr = q_prefix + """
select ?class where {
    ?class rdfs:subClassOf+ brick:Class.
}
"""

if args.reuse_inference:
    expanded_g = Graph()
    expanded_g.parse(inference_file, format='turtle')
else:
    # create instances and associate them with related Tags.
    qstr = q_prefix + """
    select ?class ?p ?o where {
      ?class rdfs:subClassOf+ brick:Class.
      ?class owl:equivalentClass ?restrictions.
      ?restrictions owl:intersectionOf ?inter.
      ?inter rdf:rest*/rdf:first ?node.
      {
          BIND (brick:hasTag as ?p)
          ?node owl:onProperty ?p.
          ?node owl:hasValue ?o.
      } UNION {
          BIND (brick:measures as ?p)
          ?node owl:onProperty ?p.
          ?node owl:hasValue ?o.
      }
    }
    """
    start_time = arrow.get()
    for row in tqdm(g.query(qstr)):
        klass = row[0]
        entity = klass + entity_postfix
        g.add((entity, row[1], row[2]))
    end_time = arrow.get()
    print('{0} seconds taken'.format(end_time - start_time))
    expanded_g = rereason_owlrl(g, 'tests/test_hierarchy_inference.n3')
    expanded_g.serialize('tests/test_hierarchy_inference.ttl', format='turtle')


# Find all instances and their parents from the inferred graph.
qstr = q_prefix + """
select ?instance ?class where {
    ?instance a ?class.
    ?class rdfs:subClassOf* brick:Class.
}
"""
inferred_klasses = defaultdict(set)
for row in tqdm(expanded_g.query(qstr)):
    klass = row[1]
    if BRICK in klass: # Filter out non-Brick classes such as Restrictions
        inferred_klasses[row[0]].add(row[1])

over_inferences = {}
under_inferences = {}
wrong_inferences = {}
for entity, parents in inferred_klasses.items():
    if entity[-2:] != entity_postfix:
        continue
    true_class = URIRef(entity[0:-2])
    qstr = q_prefix + """
    select ?parent where {{
        <{0}> rdfs:subClassOf* ?parent.
        ?parent rdfs:subClassOf* brick:Class.
    }}
    """.format(true_class)
    res = g.query(qstr)
    true_parents = [row[0] for row in res]
    true_parents = set(filter(lambda parent: BRICK in parent, true_parents))
    serialized = {
        'inferred_parents': list(parents),
        'true_parents': list(true_parents),
    }
    if parents > true_parents:
        over_inferences[entity] = serialized
    elif parents < true_parents:
        under_inferences[entity] = serialized
    elif parents != true_parents:
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
