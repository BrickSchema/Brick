import time
import owlrl
from rdflib import Graph, Namespace
from rdflib import RDF, RDFS, OWL
from collections import defaultdict
from tqdm import tqdm

BRICK_VERSION = '1.1.0'

BRICK = Namespace("https://brickschema.org/schema/{0}/Brick#".format(BRICK_VERSION))

def make_readable(res):
    return [[uri.split('#')[-1] for uri in row] for row in res]

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

def reason_inverse_edges(g):
    """
    Applies the 'classic' Brick reasoning. Just fills in any edges
    implied by inverse relationships
    """

    # inverse relationships
    query = """
    INSERT {
        ?o ?invprop ?s
    } WHERE {
        ?s ?prop ?o.
        ?prop owl:inverseOf ?invprop.
    }
    """
    g.update(query)

def reason_brick(g):
    """
    Basic hard-coded reasoning for Brick. Applies juuuust enough
    of the OWLRL rules that we can use most of the features we need.
    Almost certainly incomplete, and will be updated.

    TODO: We should replace this as soon as we have a performant
    OWLRL reasoner implementation

    - adds inverse edges
    - does a simple tag <--> class inference
    - does a simple substance <--> class inference
    - applies rdfs reasoning (adds in rdf:type edges)
    """
    reason_inverse_edges(g)

    # handle tags
    res = g.query("""
    select ?class ?p ?o where {
      ?class rdfs:subClassOf+ brick:Class.
      ?class owl:equivalentClass ?restrictions.
      ?restrictions owl:intersectionOf ?inter.
      ?inter rdf:rest*/rdf:first ?node.
      {
          BIND (brick:hasTag as ?p)
          ?node owl:onProperty ?p.
          ?node owl:hasValue ?o.
      } UNION {
          BIND (brick:measures as ?p)
          ?node owl:onProperty ?p.
          ?node owl:hasValue ?o.
      }
    }""")
    tag_properties = defaultdict(list)
    measures_properties = defaultdict(list)
    for (classname, prop, obj) in tqdm(res):
        if prop == BRICK.hasTag:
            tag_properties[classname].append(obj)
        elif prop == BRICK.measures:
            measures_properties[classname].append(obj)

    # tag inference
    for classname, tags in tag_properties.items():
        # find entities with tags and instantiate the class
        qstr = "select ?inst where {\n"
        for tag in tags:
            qstr += f"  ?inst brick:hasTag <{tag}> .\n"
        qstr +="}"
        for row in g.query(qstr):
            inst = row[0]
            g.add((inst, RDF.type, classname))

        # find entities of the class and add the tags
        qstr = f"select ?inst where {{ ?inst rdf:type/rdfs:subClassOf* <{classname}> }}"
        for row in g.query(qstr):
            inst = row[0]
            for tag in tags:
                g.add((inst, BRICK.hasTag, tag))

    # measures inference
    for classname, substances in measures_properties.items():
        # find entities with substances and instantiate the class
        qstr = "select ?inst where {\n"
        for substance in substances:
            qstr += f"  ?inst brick:measures <{substance}> .\n"
        qstr +="}"
        for row in g.query(qstr):
            inst = row[0]
            g.add((inst, RDF.type, classname))

        # find entities of the class and add the substances
        qstr = f"select ?inst where {{ ?inst rdf:type/rdfs:subClassOf* <{classname}> }}"
        for row in g.query(qstr):
            inst = row[0]
            for substance in substances:
                g.add((inst, BRICK.measures, substance))

    # apply RDFS reasoning
    reason_rdfs(g)

if __name__ == '__main__':
    g = Graph()
    g.parse('Brick.ttl', format='turtle')

    #reason_owlrl(g)
    reason_inverse_edges(g)

    s = g.serialize(format='ttl')
    with open('compiled_brick.ttl','wb') as f:
        f.write(s)
