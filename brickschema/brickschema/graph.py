# wrapper class and convenience methods for a Brick graph

import io
import pkgutil
import rdflib
from . import namespaces as ns


class Graph:
    def __init__(self, load_brick=False):
        """
        Wrapper class and convenience methods for handling Brick models
        and graphs.

        Keyword Args:
            load_brick (bool): if True, loads Brick ontology into graph

        Returns:
            graph (Graph): Graph object
        """
        self.g = rdflib.Graph()
        self.g.bind('rdf', ns.RDF)
        self.g.bind('owl', ns.OWL)
        self.g.bind('rdfs', ns.RDFS)
        self.g.bind('skos', ns.SKOS)
        self.g.bind('brick', ns.BRICK)
        self.g.bind('tag', ns.TAG)

        if load_brick:
            # get ontology data from package
            data = pkgutil.get_data(__name__, "ontologies/Brick.ttl").decode()
            # wrap in StringIO to make it file-like
            self.g.parse(source=io.StringIO(data), format='turtle')

    def add(self, *triples):
        """
        Adds triples to the graph. Triples should be 3-tuples of
        rdflib.URIRefs, e.g.

            from brickschema.graph import Graph
            from brickschema.namespaces import BRICK, RDF
            from rdflib import Namespace
            mygraph = Namespace("http://example.com/mybuilding#")

            g = Graph()
            g.add((mygraph["ts1"], RDF["type"], BRICK["Temperature_Sensor"]))
        """
        for triple in triples:
            assert len(triple) == 3
            self.g.add(triple)

    @property
    def nodes(self):
        """
        Returns all nodes in the graph

        Returns:
            nodes (list of rdflib.URIRef): nodes in the graph
        """
        return self.g.all_nodes()

    def query(self, querystring):
        """
        Executes a SPARQL query against the underlying graph and returns
        the results
        """
        return list(self.g.query(querystring))

    def __len__(self):
        return len(self.g)
