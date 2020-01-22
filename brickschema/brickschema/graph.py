"""
The `graph` module provides a wrapper class + convenience methods for
building and querying a Brick graph
"""
import io
import pkgutil
import rdflib
from . import namespaces as ns


class Graph:
    def __init__(self, load_brick=False):
        """Wrapper class and convenience methods for handling Brick models
        and graphs.

        Args:
            load_brick (bool): if True, loads packaged Brick ontology
                into graph

        Returns:
            A Graph object
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

    def load_file(self, filename=None, source=None):
        """
        Imports the triples contained in the indicated file into the graph

        Args:
            filename (str): relative or absolute path to the file
            source (file): file-like object
        """
        if filename is not None:
            if filename.endswith('.ttl'):
                self.g.parse(filename, format='ttl')
            elif filename.endswith('.n3'):
                self.g.parse(filename, format='n3')
        elif source is not None:
            for fmt in ['ttl', 'n3']:
                try:
                    self.g.parse(source=source, format=fmt)
                    return
                except Exception as e:
                    print(f"could not load {filename} as {fmt}: {e}")
            raise Exception(f"unknown file format for {filename}")
        else:
            raise Exception("Must provide either a filename or file-like\
source to load_file")


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

        Args:
            *triples (list of rdflib.URIRef): list of 3-tuples
                constituting subject, predicate, object
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

    @property
    def triples(self):
        return list(self.g)

    def query(self, querystring):
        """
        Executes a SPARQL query against the underlying graph and returns
        the results

        Args:
            querystring (str): SPARQL query string to be executed

        Returns:
            results (list of list of rdflib.URIRef): query results
        """
        return list(self.g.query(querystring))

    def __len__(self):
        return len(self.g)


def _parse(graph, filename):
    """
    Determines the correct parse format to use from the file extension
    """
