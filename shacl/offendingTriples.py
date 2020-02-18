# This module is used by _pyshacl.py, a thin wrapper of pyshacl
# to find offending triples for each reported constraint violation.

from rdflib import Graph, Namespace, URIRef, BNode
from rdflib.plugins.sparql import prepareQuery

import sys
sys.path.append('..')
from bricksrc.namespaces import RDF, RDFS, BRICK, BSH, SH, SKOS
from bricksrc.namespaces import bind_prefixes

class OffendingTriples():

    # build accumulative namespace index from participating files
    # build list of violations, each is a graph
    def __init__(self, v_graph, d_file, output):
        self.results_graph = v_graph
        self.data_graph = Graph().parse(d_file, format='ttl')
        self.outFile = output

        self.namespaceDict = {}
        self.buildNamespaceDict(self.results_graph)
        self.buildNamespaceDict(self.data_graph)

        # results_graph from pyshacl.validate() is a list of graphs.
        # Some graphs are violation graphs each representing
        # a violation with the sh:result predicate.
        # There are also other graphs without sh:result and we
        # don't care about them.
        # To filter out the unwanted graphs, we
        # iterate the results_graph twice:
        # Round 1: Create a graph for each violation and index it.
        # Round 2: Add all triples belonging to a violation to proper entry.

        self.violationDict = {}
        for (s, p, o) in self.results_graph:
            if (o not in self.violationDict) and (p == SH.result):
                self.violationDict[o] = Graph()
                for n in self.namespaceDict:
                    self.violationDict[o].bind(n, self.namespaceDict[n])

        for (s, p, o) in self.results_graph:
            if s in self.violationDict:
                self.violationDict[s].add((s, p, o))
    # end of  __init__()

    # Load namespaces into a dictionary which is accumulative among
    # the shape graph and data graph.
    def buildNamespaceDict(self, g):
        for (prefix, path) in g.namespaces():
            assert (prefix not in self.namespaceDict) or \
                (Namespace(path) == self.namespaceDict[prefix]), \
                "Same prefix \'%s\' used for %s and %s" % \
                (prefix, self.namespaceDict[prefix], path)

            if prefix not in self.namespaceDict:
                self.namespaceDict[prefix] = Namespace(path)

    # Serialize and streamline (remove @prefix lines) a grpah and append to output
    def appendGraphToOutput(self, msg, g):
        if msg:
            self.outFile.write(msg)
        for n in self.namespaceDict:
            g.bind(n, self.namespaceDict[n])
        bind_prefixes(g)

        for b_line in g.serialize(format='ttl').splitlines():
            line = b_line.decode('utf-8')
            if (not line.startswith('@prefix')) and \
               ('offendingTriple' not in line) \
               and line.strip():
                self.outFile.write(line)
                self.outFile.write('\n')



    def appendViolationToOutput(self, msg, g):
        # first print the violation body
        self.appendGraphToOutput(msg, g)

        # tease out the triples with offendingTriple as predicate
        tripleGraphs = []
        for (s, p, o) in g:
            if p == BSH['offendingTriple']:
                tripleG = Graph()
                for (s1, p1, o1) in o:
                    tripleG.add((s1, p1, o1))
                tripleGraphs.append(tripleG)

        if len(tripleGraphs) == 0:
            self.outFile.write('Please add triple finder for the above violation!!!\n')
            return

        if len(tripleGraphs) == 1:
            self.outFile.write('Offending triple:\n')
        else:
            self.outFile.write('Potential offending triples:\n')
        for tripleG in tripleGraphs:
            self.appendGraphToOutput(None, tripleG)


    # Query data graph and return the list of resulting triples
    def queryDataGraph(self, s, p, o):
        q = prepareQuery('SELECT ?s ?p ?o WHERE {%s %s %s .}' %
                         (s if s else '?s',
                          p if p else '?p',
                          o if o else '?o'),
                         initNs=self.namespaceDict
                         )
        res = self.data_graph.query(q)
        assert len(res), \
            'Must have at lease one triple like \'%s %s %s\'' % (s, p, o)
        return res


    # Take one contraint violation (a graph) and a sh: predicate,
    # find the object which is a node in the data graph.
    # Return the object found or None.
    def violationPredicateObj(self, violation, predicate, mustFind=True):
        q = prepareQuery('SELECT ?s ?p ?o WHERE {?s %s ?o .}' % predicate,
                         initNs=self.namespaceDict
                        )
        res = violation.query(q)
        if mustFind:
            assert len(res) == 1, 'Must have predicate \'%s\'' % predicate
        if len(res):
            for (s, p, o) in res:
                return o
        return None  # Ok to miss certain predicate, such as sh:resultPath


    # Take one contraint violation (a graph) and find the potential offending
    # triples.  Return the triples in a list.
    def triplesForOneViolation(self, violation):
        resultPath = self.violationPredicateObj(violation,
                                                'sh:resultPath',
                                                mustFind=False)
        if resultPath:
            focusNode = self.violationPredicateObj(violation, 'sh:focusNode')
            valueNode = self.violationPredicateObj(violation, 'sh:value')

            # TODO: Although we haven't seen a violation with sh:resultPath where
            # focusNode and valueNode are the same, the case should be considered.
            # The triple probably should be queried using queryDataGraph() instead
            # of assuming focusNode is the subject here.

            g = Graph()
            g.add((focusNode, resultPath, valueNode))
            violation.add((BNode(), BSH['offendingTriple'], g))
            return

        # Without sh:resultPath in the violation. We are currently only concerned
        # with the RDFS.domain shape.
        sourceShape = self.violationPredicateObj(violation, 'sh:sourceShape')
        (bsh, shapeName) = sourceShape.split('#')

        if shapeName.endswith('DomainShape'):
            # For a brick property xyz with RDFS.domain predicate, the shape's name
            # is bsh:xyzDomainShape.  Here we tease out brick:xyz to make the query.
            path = 'brick:' + shapeName[:-len('DomainShape')]

            # The full name (http...) of the focusNode doesn't seem to work
            # in the query.  Therefore make a prefixed version for the query.
            focusNode = self.violationPredicateObj(violation, 'sh:focusNode')
            (ns, name) = focusNode.split('#')
            namespaces = [key  for (key, value) in self.namespaceDict.items() \
                          if Namespace(ns+'#') == value]
            assert len(namespaces), "Must find a prefix for %s" % focusNode
            res = self.queryDataGraph('%s:%s' % (namespaces[0], name), path, None)

            # Due to inherent ambiguity of this kind of shape,
            # multiple triples may be found.
            for (s, p, o) in res:
                g = Graph()
                bind_prefixes(g)
                g.add((focusNode, URIRef(path), o))
                violation.add((BNode(), BSH['offendingTriple'], g))

            return

        # When control reaches here, a handler is missing for the violation.
        return

    # end of triplesForOneViolation()


    # Called from _pyshacl.py to get offending triples for all violations.
    def findAndPrint(self):
        self.outFile.write('\nAdditional info (%d constraint violations with offending triples):\n' %
                      len(self.violationDict))

        # Print each violation graph, find and print the offending triple(s), too
        for k in self.violationDict:
            self.triplesForOneViolation(self.violationDict[k])
            self.appendViolationToOutput('\nConstraint violation:\n',
                                         self.violationDict[k])

# end of class OffendingTriples()
