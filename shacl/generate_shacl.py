from rdflib import Graph, Literal, BNode, URIRef, Namespace
from rdflib.collection import Collection
from rdflib.plugins.sparql import prepareQuery

import sys
sys.path.append('..')
from bricksrc.namespaces import RDF, RDFS, BRICK, BSH, SH, SKOS
from bricksrc.namespaces import bind_prefixes
# add SHACL shapes from properties
from bricksrc.properties import properties as property_definitions

G = Graph()
bind_prefixes(G)
A = RDF.type

domainShapeDict = {}
rangeShapeDict = {}
subpropertyDict = {}

# Make shape for expectedDomain property
def addDomainShape(propertyName, expectedType):
    domainShapeDict[propertyName] = expectedType
    sh_prop = BNode()
    shapename = f"{propertyName}DomainShape"
    G.add((BSH[shapename], A, SH.NodeShape))
    G.add((BSH[shapename], SH.targetSubjectsOf, BRICK[propertyName]))
    G.add((BSH[shapename], SH['class'], expectedType))
    G.add((BSH[shapename], SH['message'],
           Literal(f"Property {propertyName} has subject with incorrect type")))

# Make shape for expectedRange property
def addRangeShape(propertyName, expectedType):
    rangeShapeDict[propertyName] = expectedType
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
        # We are only concerned with properties that have RDFS.domain or .range
        # predicate.  The temporary replacements for those predicates are
        # brick:expectedDomain and :expectedRange.  See properties.py for
        # explanation.

        if pred == RDFS.domain:
            addDomainShape(name, obj)

        if pred == RDFS.range:
            addRangeShape(name, obj)

        # subproperties are considered after "domain" and "range" are counted for
        if pred == 'subproperties':
            for subprop, desc in obj.items():
                subpropertyDict[subprop] = desc

# TODO: A better way to describe the subproperties is probably
# using OWL restrictions while generateing Brick.ttl.  But
# that kind of schema change is beyond the scope for now.
substance_subproperties = {
    'feedsAir':  {
        'substanceType': BRICK.Air,
        'substanceSuperType': BRICK.Substance,
    },
}

# For each substance_subproperties element, such as Brick:feedsAir,
# the subject of the Brick:feedsAir predicate should satisfy triples like
# subject <property> Brick:Air ("substanceType") where a range shape can
# be found for a triple
# <property> RDFS.range Brick:Substance ("substanceSuperType").

for subprop, desc in subpropertyDict.items():
    subpropInfo = substance_subproperties[subprop]
    if not subpropInfo:  # subprop not in substance_subproperties
        continue

    for propertyName, expectedType in rangeShapeDict.items():
        if expectedType == subpropInfo['substanceSuperType']:
            sh_prop = BNode()
            capitalized = f"{propertyName[0].upper()}{propertyName[1:]}"
            shapename = f"feedsAir{capitalized}Shape"
            G.add((BSH[shapename], SH['property'], sh_prop))
            G.add((BSH[shapename], A, SH.NodeShape))
            G.add((sh_prop, SH['path'], BRICK[propertyName]))
            G.add((sh_prop, SH['class'], subpropInfo['substanceType']))
            G.add((sh_prop, SH['message'],
            Literal(f"Subject of property {subprop} has object with incorrect type")))
            G.add((BSH[shapename], SH.targetSubjectsOf, BRICK[subprop]))

with open('BrickShape.ttl', 'wb') as f:
    f.write(G.serialize(format='ttl'))
