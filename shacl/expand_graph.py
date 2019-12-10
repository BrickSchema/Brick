#! /usr/bin/python3

import sys
sys.path.append('..')

from rdflib import Graph, Namespace
from bricksrc.namespaces import BRICK, RDF, OWL, DCTERMS, SDO, RDFS, SKOS, BRICK, TAG, SOSA, BSH, SH
from bricksrc.namespaces import bind_prefixes
from tests.util.reasoner import reason_brick

G = Graph()
bind_prefixes(G)
A = RDF.type
G.parse(sys.argv[1], format='ttl')
#G.parse('Brick.ttl', format='ttl')

reason_brick(G)

with open('output.ttl', 'wb') as f:
    f.write(G.serialize(format='ttl'))
