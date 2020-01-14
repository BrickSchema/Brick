import time
import owlrl
from rdflib import Graph, Namespace
from rdflib import RDF, RDFS, OWL
from collections import defaultdict
from tqdm import tqdm

import io
import os
import sys
import tarfile
from pathlib import Path
import shutil
import docker

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
    return reason_agraph(g)
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
    select ?class ?p ?o ?restrictions where {
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
      } UNION {
          BIND (rdf:type as ?p)
          ?node owl:onProperty ?p.
          ?node owl:hasValue ?o.
      }
    }""")
    tag_properties = defaultdict(list)
    measures_properties = defaultdict(list)
    grouped_properties = defaultdict(list)

    for (classname, prop, obj, groupname) in tqdm(res):
        if prop == BRICK.hasTag:
            tag_properties[classname].append(obj)
        elif prop == BRICK.measures:
            measures_properties[classname].append(obj)

        #print(classname,groupname,prop,obj)
        grouped_properties[(classname,groupname)].append( (prop, obj) )

    # add properties based on classes
    for (classname, groupname), props in grouped_properties.items():
        q = "INSERT {\n"
        q += '\n'.join(
            [f"\t ?inst <{prop}> <{obj}> ." for prop,obj in props]
        )
        q += "\n} WHERE {\n"
        q += '\n'.join(
            [f"\t ?inst rdf:type <{classname}> ."]
        )
        q += "\n}"
        g.update(q)

    # add properties based on classes
    for (classname, groupname), props in grouped_properties.items():
        q = f"""INSERT {{
        ?inst rdf:type <{classname}>
        }} WHERE {{ \n"""
        q += '\n'.join(
            [f"\t ?inst <{prop}> <{obj}> ." for prop,obj in props]
        )
        q += "}\n"
        g.update(q)


    # tag inference
    for classname, tags in tag_properties.items():
        ## find entities with tags and instantiate the class
        #qstr = "select ?inst where {\n"
        #for tag in tags:
        #    qstr += f"  ?inst brick:hasTag <{tag}> .\n"
        #qstr +="}"
        #for row in g.query(qstr):
        #    inst = row[0]
        #    g.add((inst, RDF.type, classname))

        # find entities of the class and add the tags
        qstr = f"select ?inst where {{ ?inst rdf:type/rdfs:subClassOf* <{classname}> }}"
        for row in g.query(qstr):
            inst = row[0]
            for tag in tags:
                g.add((inst, BRICK.hasTag, tag))
#
#    # measures inference
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

def get_docker_client():
    client = docker.from_env()
    containers = client.containers.list(all=True)
    print(f"Checking {len(containers)} containers")
    for c in containers:
        if c.name != 'agraph':
            continue
        if c.status == 'running':
            print(f"Killing running agraph")
            c.kill()
        print(f"Removing old agraph")
        c.remove()
        break
    return client

def setup_input(g):
    """
    Add our serialized graph to an in-memory tar file that we can send to Docker
    """
    g.serialize('input.ttl', format='turtle')
    tarbytes = io.BytesIO()
    tar = tarfile.open(name='out.tar', mode='w', fileobj=tarbytes)
    tar.add('input.ttl', arcname='input.ttl')
    tar.close()
    # seek to beginning so our file is not empty when docker sees it
    tarbytes.seek(0)
    return tarbytes

def reason_agraph(g):
    def check_error(res):
        exit_code, message = res
        if exit_code > 0:
            print(f"Non-zero exit code {exit_code} with message {message}")
    # setup connection to docker
    client = get_docker_client()
    tar = setup_input(g)
    # TODO: temporary name so we can have more than one running?
    agraph = client.containers.run("franzinc/agraph", name="agraph", detach=True, shm_size='1G')
    if not agraph.put_archive('/opt', tar):
        print("Could not add input.ttl to docker container")
    check_error(agraph.exec_run("chown -R agraph /opt"))
    check_error(agraph.exec_run("/app/agraph/bin/agload test /opt/input.ttl", user='agraph'))
    check_error(agraph.exec_run("/app/agraph/bin/agmaterialize test --rule all", user='agraph'))
    check_error(agraph.exec_run("/app/agraph/bin/agexport -o turtle test /opt/output.ttl", user='agraph'))
    bits, stat = agraph.get_archive('/opt/output.ttl')
    with open('output.ttl.tar', 'wb') as f:
        for chunk in bits:
            f.write(chunk)
    tar = tarfile.open('output.ttl.tar')
    tar.extractall()
    tar.close()

    agraph.stop()
    agraph.remove()
    g.parse('output.ttl', format='ttl')

if __name__ == '__main__':
    g = Graph()
    g.parse('Brick.ttl', format='turtle')

    #reason_owlrl(g)
    reason_inverse_edges(g)

    s = g.serialize(format='ttl')
    with open('compiled_brick.ttl','wb') as f:
        f.write(s)
