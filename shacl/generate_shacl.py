from rdflib import Graph, Literal, BNode, URIRef
from rdflib.collection import Collection

import sys
sys.path.append('..')
from bricksrc.namespaces import RDF, RDFS, BRICK, BSH, SH, SKOS
from bricksrc.namespaces import bind_prefixes
# add SHACL shapes from properties
from bricksrc.properties import properties as property_definitions

G = Graph()
bind_prefixes(G)
A = RDF.type

substance_subproperties = {
    BRICK.feedsAir:  {
        'substance': BRICK.Air,
    },
}

def addExpectedDomainShape(propertyName, expectedType):
    sh_prop = BNode()
    shapename = f"{propertyName}DomainShape"
    G.add((BSH[shapename], A, SH.NodeShape))
    G.add((BSH[shapename], SH.targetSubjectsOf, BRICK[propertyName]))
    G.add((BSH[shapename], SH['class'], expectedType))
    G.add((BSH[shapename], SH['message'],
           Literal(f"Property {propertyName} has subject with incorrect type")))

def addExpectedRangeShape(propertyName, expectedType):
    sh_prop = BNode()
    shapename = f"{propertyName}RangeShape"
    G.add((BSH[shapename], SH['property'], sh_prop))
    G.add((BSH[shapename], A, SH.NodeShape))

    G.add((sh_prop, SH['path'], BRICK[propertyName]))
    G.add((sh_prop, SH['class'], expectedType))
    G.add((BSH[shapename], SH.targetSubjectsOf, BRICK[propertyName]))
    G.add((sh_prop, SH['message'],
           Literal(f"Property {propertyName} has object with incorrect type")))

for name, properties in property_definitions.items():

    for pred, obj in properties.items():
        sh_prop = BNode()

        # We are only concerned with properties that have RDFS.domain or .range
        # predicate.  The temporary replacements for those predicates are
        # brick:expectedDomain and :expectedRange.  See properties.py for
        # explanation.

        if pred == BRICK.expectedDomain:
            addExpectedDomainShape(name, obj)

        if pred == BRICK.expectedRange:
            addExpectedRangeShape(name, obj)

        '''
        if pred == "hasSubproperty":
            for subprop, desc in obj.items():
                for prop in desc['properties']:
                    sh_prop = BNode()
                    (prefix, name) = prop.split('#')
                    shapename = f"feedsAir{name.capitalize()}Shape"
                    G.add((BSH[shapename], SH['property'], sh_prop))
                    G.add((BSH[shapename], A, SH.NodeShape))
                    G.add((sh_prop, SH['path'], prop))
                    G.add((sh_prop, SH['class'], desc['substance']))
                    G.add((sh_prop, SH['message'],
                           Literal(f"Subject of property {subprop} has object with incorrect type")))

                    G.add((BSH[shapename], SH.targetSubjectsOf, BRICK[subprop]))
        '''

with open('shacl_test.ttl', 'wb') as f:
    f.write(G.serialize(format='ttl'))
