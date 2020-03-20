import sys
from rdflib import RDFS, Graph
from bricksrc.namespaces import A, OWL, RDFS, SKOS, BRICK, SH, BSH, bind_prefixes
from .util import make_readable

sys.path.append("..")
from bricksrc.properties import properties

g = Graph()
g.parse('shacl/BrickShape.ttl', format='turtle')
bind_prefixes(g)

def test_domainProperties():
    for (name, props) in properties.items():
        if RDFS.domain in props:
            q = f"""SELECT $shape WHERE {{
            ?shape a sh:NodeShape .
            ?shape sh:targetSubjectsOf brick:{name} .
            ?shape sh:class <{props[RDFS.domain]}> . }}
            """
            res = make_readable(
                g.query(q)
            )
            assert len(res) == 1, 'unexpected # of query results'
    return

def test_rangeProperties():
    for (name, props) in properties.items():
        if RDFS.range in props:
            q = f"""SELECT $shape WHERE {{
            ?shape a sh:NodeShape .
            ?shape sh:property [
            sh:class <{props[RDFS.range]}> ;
            sh:path brick:{name} ;
            ] }}
            """
            res = make_readable(
                g.query(q)
            )
            assert len(res) == 1, 'unexpected # of query results'
    return
