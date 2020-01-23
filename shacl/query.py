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

namespaceDict = {}

outFile = sys.stdout

# Load namespaces into a dictionary which is accumulative among
# the shape graph, data graph and ontology graph.
def buildNamespaceDict(g):
    for (prefix, path) in g.namespaces():
        assert (prefix not in namespaceDict) or (Namespace(path) == namespaceDict[prefix]), \
        "Same prefix \'%s\' used for %s and %s" % (prefix, namespaceDict[prefix], path)
        if prefix not in namespaceDict:
            namespaceDict[prefix] = Namespace(path)

# Serialize and streamline (remove @prefix lines) and append to output
def appendGraphToOutput(m, g, f):
    if m:
        f.write(m)
    for n in namespaceDict:
        g.bind(n, namespaceDict[n])

    for b_line in g.serialize(format='ttl').splitlines():
        line = b_line.decode('utf-8')
        if (not line.startswith('@prefix')) and line.strip():
            f.write(line)
            f.write('\n')

# Query data graph and return the list of resulting triples
def queryDataGraph(s, p, o):
    q = prepareQuery('SELECT ?s ?p ?o WHERE {%s %s %s .}' %
                     (s if s else '?s',
                      p if p else '?p',
                      o if o else '?o'),
                     initNs=namespaceDict
                     )
    res = data_graph.query(q)
    assert len(res), 'Must have at lease one triple like \'%s %s %s\'' % (s, p, o)
    return res

# Take one contraint violation (a graph) and a sh: predicate,
# find the object, a node in the data graph.
def getViolationPredicateObj(violation, predicate, mustFind=True):
    q = prepareQuery('SELECT ?s ?p ?o WHERE {?s %s ?o .}' % predicate,
                     initNs=namespaceDict
                    )
    res = violation.query(q)
    if mustFind:
        assert len(res) == 1, 'Must have predicate \'%s\'' % predicate

    if len(res):
        for (s, p, o) in res:
            return o
    return None  # Ok to miss certain predicate, such as sh:resultPath

# Take one contraint violation (a graph) and find the potential offending
# triples
def appendOffendingTriples(violation):
    resultPath = getViolationPredicateObj(violation, 'sh:resultPath', mustFind=False)
    if resultPath:
        focusNode = getViolationPredicateObj(violation, 'sh:focusNode')
        valueNode = getViolationPredicateObj(violation, 'sh:value')

        # TODO: Although we haven't see a violation with sh:resultPath where
        # focusNode and valueNode are the same, the case should be considered.
        # The triple probably should be queried using queryDataGraph() instead
        # of assuming focusNode is the subject here.

        g = Graph()
        g.add((focusNode, resultPath, valueNode))
        appendGraphToOutput('Offending triple:\n', g, outFile)
        return

    # No sh:resultPath in the violation, we are currently only concerned
    # with the RDFS.domain shape.
    sourceShape = getViolationPredicateObj(violation, 'sh:sourceShape')
    (bsh, shapeName) = sourceShape.split('#')
    if shapeName.endswith('DomainShape'):
        path = 'brick:' + shapeName[:-len('DomainShape')]
        focusNode = getViolationPredicateObj(violation, 'sh:focusNode')
        (ns, name) = focusNode.split('#')
        namespaces = [key  for (key, value) in namespaceDict.items() \
                      if Namespace(ns+'#') == value]
        assert len(namespaces), "Must find a prefix for %s" % focusNode
        res = queryDataGraph('%s:%s' % (namespaces[0], name), path, None)

        if len(res) > 1:
            outFile.write('Potential offending triples:\n')
        else:
            outFile.write('Offending triple:\n')
        for (s, p, o) in res:
            g = Graph()
            g.add((focusNode, URIRef(path), o))
            appendGraphToOutput(None, g, outFile)
        return

    # When control reaches here, our shapes generate violations whose offending
    # triples are not handled yes.  Give a warning.
    outFile.write('Please add triple finder for the above violation!!!\n')
    return
# end of appendOffendingTriples()

# Start of main

buildNamespaceDict(results_graph)
buildNamespaceDict(data_graph)

violationDict = {}

# The results_graph has violation graphs, each for a violation,
# and graphs of sh:sourceShape. Now we only consider the violation
# graphs that have sh:result predicate.
# Iterate the results_graph twice: Create a graph for each violation
# and index it in the first round.  In the second round add all triples
# belong to a violation to the right entry.
for (s, p, o) in results_graph:
    if (o not in violationDict) and (p == SH.result):
        violationDict[o] = Graph()
        for n in namespaceDict:
            violationDict[o].bind(n, namespaceDict[n])

for (s, p, o) in results_graph:
    if s in violationDict:
        violationDict[s].add((s, p, o))

# Print out the violation graphs, print out the offending triple(s), too
for k in violationDict:
    appendGraphToOutput('\nConstraint violation:\n', violationDict[k], outFile)
    appendOffendingTriples(violationDict[k])

exit()
