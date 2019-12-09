#! /usr/bin/python3

from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef, RDFS, OWL
from rdflib.namespace import XSD
from rdflib.collection import Collection

import sys
sys.path.append('..')

from bricksrc.namespaces import BRICK, RDF, OWL, DCTERMS, SDO, RDFS, SKOS, BRICK, TAG, SOSA, BSH, SH
from bricksrc.namespaces import bind_prefixes

G = Graph()
bind_prefixes(G)
A = RDF.type

# add SHACL shapes from properties
from bricksrc.properties import properties as property_definitions

for name, properties in property_definitions.items():

    for pred, obj in properties.items():
        sh_prop = BNode()

        # TODO: currently just for rdfs:{domain, range}

        if pred == RDFS.range:
            shapename = f"{name}RangeShape"
            G.add( (BSH[shapename], SH['property'], sh_prop) )
            G.add( (BSH[shapename], A, SH.NodeShape) )

            G.add( (sh_prop, SH['nodeKind'], SH.IRI) )
            G.add( (sh_prop, SH['path'], BRICK[name]) )
            G.add( (sh_prop, SH['class'], obj) )
            qualifier = SH.targetObjectsOf
            G.add( (BSH[shapename], qualifier, BRICK[name]) )

            G.add( (sh_prop, SH['message'], Literal(f"Property {name} has object with incorrect type")) )

        # TODO: broken SHACL for rdfs.domain
        if pred == RDFS.domain:
            shapename = f"{name}DomainShape"
            G.add( (BSH[shapename], SH['property'], sh_prop) )
            G.add( (BSH[shapename], A, SH.NodeShape) )

            G.add( (sh_prop, SH['nodeKind'], SH.IRI) )
            G.add( (sh_prop, SH['path'], BRICK[name]) )
            qualifier = SH.targetClass
            G.add( (BSH[shapename], qualifier, obj) )

            G.add( (sh_prop, SH['message'], Literal(f"Property {name} has subject with incorrect type")) )

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
    G.add((shape, SH['or'], constraintlist))

    constraints = []
    for prop in desc['properties']:
        constraint = BNode()
        definition = BNode()
        G.add( (constraint, SH['property'], definition) )
        G.add( (definition, SH['path'], prop) )
        G.add( (definition, SH['class'], desc['substance']) )
        constraints.append(constraint)

    c = Collection(G, constraintlist, constraints)

with open('shacl_test.ttl', 'wb') as f:
    f.write(G.serialize(format='ttl'))
