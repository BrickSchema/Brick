# This module is used by _pyshacl.py, a thin wrapper of pyshacl
# to find offending triples for each reported constraint violation.

import argparse
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.plugins.sparql import prepareQuery
import sys

sys.path.append('..')
from bricksrc.namespaces import RDF, RDFS, BRICK, BSH, SH, SKOS

global result_graph
global data_graph
global namespaceDict
global outFile

namespaceDict = {}
outFile = None
result_graph = None
data_graph = None

# Load namespaces into a dictionary which is accumulative among
# the shape graph and data graph.
def buildNamespaceDict(g):
    global namespaceDict

    for (prefix, path) in g.namespaces():
        assert (prefix not in namespaceDict) or (Namespace(path) == namespaceDict[prefix]), \
        "Same prefix \'%s\' used for %s and %s" % (prefix, namespaceDict[prefix], path)

        if prefix not in namespaceDict:
            namespaceDict[prefix] = Namespace(path)


# Serialize and streamline (remove @prefix lines) and append to output
def appendGraphToOutput(msg, g, f):
    if msg:
        f.write(msg)
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
# find the object which is a node in the data graph.
# Return the object found or None.
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
# triples.
def offendingTriplesForOneViolation(violation):
    resultPath = getViolationPredicateObj(violation, 'sh:resultPath', mustFind=False)
    if resultPath:
        focusNode = getViolationPredicateObj(violation, 'sh:focusNode')
        valueNode = getViolationPredicateObj(violation, 'sh:value')

        # TODO: Although we haven't seen a violation with sh:resultPath where
        # focusNode and valueNode are the same, the case should be considered.
        # The triple probably should be queried using queryDataGraph() instead
        # of assuming focusNode is the subject here.

        g = Graph()
        g.add((focusNode, resultPath, valueNode))
        appendGraphToOutput('Offending triple:\n', g, outFile)
        return

    # Without sh:resultPath in the violation. We are currently only concerned
    # with the RDFS.domain shape.
    sourceShape = getViolationPredicateObj(violation, 'sh:sourceShape')
    (bsh, shapeName) = sourceShape.split('#')

    if shapeName.endswith('DomainShape'):
        # For a brick property xyz with RDFS.domain predicate, the shape's name
        # is bsh:xyzDomainShape.  Here we tease out brick:xyz to make the query.
        path = 'brick:' + shapeName[:-len('DomainShape')]

        # The full name (http...) of the focusNode doesn't seem to work
        # in the query.  Therefore make a prefixed version for the query.
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

    # When control reaches here, we need to add handler for the violation.
    # Give a warning.
    outFile.write('Please add triple finder for the above violation!!!\n')
    return
# end of offendingTriplesForOneViolation()


# Called from _pyshacl.py to get offending triples for all violations.
def findOffendingTriples(v_graph, d_file, output):
    global result_graph
    global data_graph
    global namespaceDict
    global outFile

    outFile = output
    results_graph = v_graph
    data_graph = Graph().parse(d_file, format='ttl')
    buildNamespaceDict(results_graph)
    buildNamespaceDict(data_graph)

    # The results_graph contains a list of graphs.  Some graphs are violation graphs
    # each representing a violation with the sh:result predicate.
    # There are also other graphs without sh:result and we don't care about them.
    # To filter out the unwanted graphs, we
    # iterate the results_graph twice: Round 1: Create a graph for each violation
    # and index it.  Round 2: Add all triples belonging to a violation to proper entry.

    violationDict = {}
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
        offendingTriplesForOneViolation(violationDict[k])
