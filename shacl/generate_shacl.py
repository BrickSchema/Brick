from rdflib import Graph, Literal, BNode
from rdflib.collection import Collection

import sys
sys.path.append('..')
from bricksrc.namespaces import RDF, RDFS, BRICK, BSH, SH
from bricksrc.namespaces import bind_prefixes
# add SHACL shapes from properties
from bricksrc.properties import properties as property_definitions

G = Graph()
bind_prefixes(G)
A = RDF.type
rootclasses = ["Equipment", "Location", "Point",
               "Substance", "Quantity"]

for name, properties in property_definitions.items():

    for pred, obj in properties.items():
        sh_prop = BNode()

        # TODO: currently just for rdfs:{domain, range}

        if pred == RDFS.range:
            shapename = f"{name}RangeShape"
            G.add((BSH[shapename], SH['property'], sh_prop))
            G.add((BSH[shapename], A, SH.NodeShape))

            G.add((sh_prop, SH['nodeKind'], SH.IRI))
            G.add((sh_prop, SH['path'], BRICK[name]))
            G.add((sh_prop, SH['class'], obj))
            G.add((BSH[shapename], SH.targetSubjectsOf, BRICK[name]))
            G.add((sh_prop, SH['message'],
                   Literal(f"Property {name} has object with incorrect type")))


        # TODO: broken SHACL for rdfs.domain
        #if pred == RDFS.domain:
        #    shapename = f"{name}DomainShape"
        #    G.add( (BSH[shapename], SH['property'], sh_prop))
        #    G.add( (BSH[shapename], A, SH.NodeShape))

        #    G.add( (sh_prop, SH['nodeKind'], SH.IRI))
        #    G.add( (sh_prop, SH['path'], BRICK[name]))
        #    qualifier = SH.targetClass
        #    G.add( (BSH[shapename], qualifier, obj))

        #    G.add( (sh_prop, SH['message'], Literal(f"Property {name} has subject with incorrect type")))

# make sure that root classes are disjoint, even if inference has generated
# some invalid properties (e.g. a subject of hasLocation will be inferred
# as a Location even if it is already an Equipment).
for rootclass1 in rootclasses:
    for rootclass2 in rootclasses:
        if rootclass1 == rootclass2:
            continue
        sh_prop = BNode()
        shapename = f"{rootclass1}CanNotBe{rootclass2}Shape"
        G.add((BSH[shapename], A, SH.NodeShape))
        G.add((BSH[shapename], SH.targetClass, BRICK[rootclass1]))
        G.add((BSH[shapename], SH["not"], sh_prop))
        G.add((sh_prop, SH["class"], BRICK[rootclass2]))
        G.add((sh_prop, SH["message"], Literal(f"Node cannot be both a \
               {BRICK[rootclass1]} and a {BRICK[rootclass2]}. Check the \
               properties it has")))

# subproperties
# TODO: explicitly coded for now, but we should generalize
substance_subproperties = {
    'feedsAir':  {
        'substance': BRICK.Air,
        'properties': [BRICK.regulates, BRICK.measures]
    },
}

for subprop, desc in substance_subproperties.items():
    shape = BSH[f"{subprop}SubstanceShape"]
    constraintlist = BNode()
    G.add((shape, A, SH.NodeShape))
    G.add((shape, SH.targetSubjectsOf, BRICK[subprop]))
    G.add((shape, SH['or'], constraintlist))

    constraints = []
    for prop in desc['properties']:
        constraint = BNode()
        definition = BNode()
        G.add( (constraint, SH['property'], definition))
        G.add( (definition, SH['path'], prop))
        G.add( (definition, SH['class'], desc['substance']))
        constraints.append(constraint)

    c = Collection(G, constraintlist, constraints)

with open('shacl_test.ttl', 'wb') as f:
    f.write(G.serialize(format='ttl'))
