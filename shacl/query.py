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

outfile = sys.stdout.buffer

parser = argparse.ArgumentParser(description='pySHACL wrapper for better violation reporting.')
parser.add_argument('data', metavar='DataGraph',
                    help='The file containing the Target Data Graph.')

args = parser.parse_args()
data_graph = Graph().parse(args.data, format='turtle')

results_graph = Graph().parse('results_graph.ttl', format='ttl')

namespaceDict = {}

def buildNamespaceDict(g):
    for (prefix, path) in g.namespaces():
        assert (prefix not in namespaceDict) or (Namespace(path) == namespaceDict[prefix]), \
        "Same prefix \'%s\' used for %s and %s" % (prefix, namespaceDict[prefix], path)
        if prefix not in namespaceDict:
            namespaceDict[prefix] = Namespace(path)

# streamline (remove @prefix lines) and append to file
def appendGraphToFile(m, g, f):
    bind_prefixes(g)
    g.bind('bldg', Namespace(f"http://example.com/mybuilding#"))
    f.write(m)
    firstLine = True
    for b_line in g.serialize(format='ttl').splitlines():
        line = b_line.decode('utf-8')
        if not line.startswith('@prefix'):
            if not firstLine:
                f.write('\n')
            f.write(line)
            firstLine = False

def queryDataGraph(s, p, o):
    print('SELECT ?s ?p ?o WHERE {%s %s %s .}' %
          (s if s else '?s',
           p if p else '?p',
           o if o else '?o'))
    q = prepareQuery('SELECT * WHERE {%s %s %s .}' %
                     (s if s else '?s',
                      p if p else '?p',
                      o if o else '?o'),
                     initNs=namespaceDict
                     )

    res = data_graph.query(q)
    assert len(res), 'Must have at lease one triple like \'%s %s %s\'' % (s, p, o)
    return res

def getViolationPredicateObj(violation, predicate):
    q = prepareQuery('SELECT ?s ?p ?o WHERE {?s %s ?o .}' % predicate,
                     initNs=dict(sh=Namespace('http://www.w3.org/ns/shacl#'),
                                 brick=Namespace('https://brickschema.org/schema/1.1.0/Brick#'),
                                 bldg=Namespace("http://example.com/mybuilding#")))
    res = violation.query(q)
    if len(res):
        for (s, p, o) in res:
            return o
    return None

def findCulprit(violation):
    resultPath = getViolationPredicateObj(violation, 'sh:resultPath')
    if resultPath:
        focusNode = getViolationPredicateObj(violation, 'sh:focusNode')
        valueNode = getViolationPredicateObj(violation, 'sh:value')
        g = Graph()
        g.add((focusNode, resultPath, valueNode))
        appendGraphToFile('Offending triple:', g, sys.stdout)
        return

    sourceShape = getViolationPredicateObj(violation, 'sh:sourceShape')
    (bsh, shapeName) = sourceShape.split('#')
    if shapeName.endswith('DomainShape'):
        path = 'brick:' + shapeName[:-len('DomainShape')]
        focusNode = getViolationPredicateObj(violation, 'sh:focusNode')
        (ns, name) = focusNode.split('#')
        print(ns, name)
        namespaces = [key  for (key, value) in namespaceDict.items() \
                      if Namespace(ns+'#') == value]
        assert len(namespaces), "Must find a prefix for %s" % focusNode
        res = queryDataGraph('%s:%s' % (namespaces[0], name),
                             path, None)
        for o in res:
            print(name, path, o)

violation_dict = {}
for (s, p, o) in results_graph:
    if (o not in violation_dict) and (p == SH.result):
        violation_dict[o] = Graph()
        bind_prefixes(violation_dict[o])
        violation_dict[o].bind('bldg', Namespace('http://example.com/mybuilding#'))

for (s, p, o) in results_graph:
    if s in violation_dict:
        violation_dict[s].add((s, p, o))

buildNamespaceDict(results_graph)
buildNamespaceDict(data_graph)

res = data_graph.query(
    """ SELECT ?s ?p ?o
    WHERE {
    bldg:VAV2-4.DPR  brick:measures ?o .
    }""",
    initNs=namespaceDict
#    initNs=dict(bldg=Namespace('http://example.com/mybuilding#'),
#                brick=Namespace('https://brickschema.org/schema/1.1.0/Brick#'))
 )
if len(res):
    for (s, p, o) in res:
        print(s, p, o)


for k in violation_dict:
    appendGraphToFile('\nConstraint violation:', violation_dict[k], sys.stdout)
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
