import time
import owlrl
from rdflib import Graph

def reason_owlrl(g):
    """
    Applies full OWL RL Reasoning. WARNING: takes a few hours.

    Lets us use:
    - tags <--> classes
    - measures properties
    - transitive properties
    - inverse properties
    - class hierarchy (rdf:type, not rdf:type/rdfs:subClassOf*)
    """
    start_time = time.time()
    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(g)
    end_time = time.time()
    print('owlrl reasoning took {0} seconds.'.format(int(end_time - start_time)))

def reason_rdfs(g):
    """
    Applies RDFS reasoning. Takes a few seconds.

    Lets us use:
    - class hierarchy (rdf:type, not rdf:type/rdfs:subClassOf*)
    """
    start_time = time.time()
    owlrl.DeductiveClosure(owlrl.RDFS_Semantics).expand(g)
    end_time = time.time()
    print('owlrl reasoning took {0} seconds.'.format(int(end_time - start_time)))
    
def reason_classic(g):
    """
    Applies the 'classic' Brick reasoning. Just fills in any edges
    implied by inverse relationships
    """
    res = g.query("""SELECT ?prop ?invprop WHERE {
    ?prop rdf:type owl:ObjectProperty .
    ?prop owl:inverseOf ?invprop
    }""")

    for prop, invprop in res:
        forward_edges = g.query(f"""SELECT ?subject ?object WHERE {{
        ?subject <{prop}> ?object
        }}""")
        backward_edges = g.query(f"""SELECT ?subject ?object WHERE {{
        ?subject <{invprop}> ?object
        }}""")
        for s, o in forward_edges:
            g.add((o, invprop, s))
        for s, o in backward_edges:
            g.add((o, prop, s))

if __name__ == '__main__':
    g = Graph()
    g.parse('Brick.ttl', format='turtle')

    #reason_owlrl(g)
    #reason_simple(g)
    reason_classic(g)

    s = g.serialize(format='ttl')
    with open('compiled_brick.ttl','wb') as f:
        f.write(s)
