import argparse
from rdflib import Graph, Namespace, URIRef, Literal
from pyshacl import validate
from logging import getLogger
from os.path import dirname, splitext
from rdflib.plugins.sparql import prepareQuery
import sys
import ntpath

import sys
sys.path.append('..')
from bricksrc.namespaces import RDF, RDFS, BRICK, BSH, SH, SKOS
from bricksrc.namespaces import bind_prefixes
# add SHACL shapes from properties
from bricksrc.properties import properties as property_definitions


parser = argparse.ArgumentParser(description='pySHACL wrapper for better violation reporting.')
parser.add_argument('data', metavar='DataGraph',
                    help='The file containing the Target Data Graph.')

args = parser.parse_args()
data_graph = Graph().parse(args.data, format='turtle')

results_graph = Graph().parse('results_graph.ttl', format='ttl')

def getViolationPredicateObj(violation, predicate):
    # print ('SELECT ?s ?p ?o WHERE {?s %s ?o .}' % predicate)
    q = prepareQuery('SELECT ?s ?p ?o WHERE {?s %s ?o .}' % predicate,
                       initNs=dict(sh=Namespace('http://www.w3.org/ns/shacl#')))
    res = violation.query(q)

    if len(res):
        for (s, p, o) in res:
            return o
    return None

def findCulprit(violation):
    resultPath = getViolationPredicateObj(violation, 'sh:resultPath')
    if resultPath:
        print('resultPath', resultPath)
        focusNode = getViolationPredicateObj(violation, 'sh:focusNode')
        print('focusNode', focusNode)
        valueNode = getViolationPredicateObj(violation, 'sh:value')
        print('value', valueNode)
    '''
    resultPathRes = violation.query(
        """SELECT ?s ?p ?o
        WHERE {
        ?s sh:resultPath ?o .
        }""",
    )

    if len(resultPathRes):  # have resultPath property
        focusNodeRes = violation.query(
            """SELECT ?s ?p ?o
            WHERE {
            ?s sh:focusNode ?o .
            }""",
        )

        print(type(resultPathRes))
        for (s, p, o) in focusNodeRes:
            focusNode = o
        print(focusNode)
    '''
'''
        q = prepareQuery('SELECT ?s ?p ?o WHERE {%s %s %s .}' % (s, o
        WHERE {
        ?s sh:resultPath ?o .
        }""",



        tripleByPath = violation.query(
        """SELECT ?s ?p ?o
        WHERE {
        ?s sh:resultPath ?o .
        }""",
    )
'''

violation_dict = {}
for (s, p, o) in results_graph:
    if (o not in violation_dict) and (p == SH.result):
        print(s, p, o)
        violation_dict[o] = Graph()
        bind_prefixes(violation_dict[o])
        violation_dict[o].bind('bldg', Namespace(f"http://example.com/mybuilding#"))

for (s, p, o) in results_graph:
    if s in violation_dict:
        violation_dict[s].add((s, p, o))

outfile = sys.stdout.buffer
for k in violation_dict:
    for b_line in violation_dict[k].serialize(format='ttl').splitlines():
        line = b_line.decode('utf-8')
        if not line.startswith('@prefix'):
            print(line)

    findCulprit(violation_dict[k])

exit()

bind_prefixes(data_graph)
data_graph.bind('bldg', Namespace('http://example.com/mybuilding#'))

res = data_graph.query(
    """SELECT ?s ?p ?o
       WHERE {
          ?s brick:hasLocation ?o .
       }""",
    )

#res.bind('bldg', Namespace('http://example.com/mybuilding#'))
rg = Graph()
rg.bind('bldg', Namespace(f"http://example.com/mybuilding#"))
rg = Graph()
for (s, p, o) in res:
    print(s, p, o)
    rg.add((s, BRICK['hasLocation'], o))

#print(rg.serialize(format='ttl'))
with open('queryResult.ttl', 'wb') as f:
    f.write(rg.serialize(format='ttl'))
