# wrapper class and convenience methods for a Brick graph

import io
import pkgutil
import rdflib
import brickschema.namespaces as ns


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

    def query(self, querystring):
        """
        Executes a SPARQL query against the underlying graph and returns
        the results
        """
        return list(self.g.query(querystring))
