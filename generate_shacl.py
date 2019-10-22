from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef, RDFS, OWL
from rdflib.namespace import XSD
from rdflib.collection import Collection

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
            G.add( (sh_prop, SH['class'], obj) )
            qualifier = SH.targetObjectsOf
            G.add( (BSH[shapename], qualifier, name) )

            G.add( (sh_prop, SH['message'], Literal("Property has object with incorrect type")) )

        if pred == RDFS.domain:
            shapename = f"{name}DomainShape"
            G.add( (BSH[shapename], SH['property'], sh_prop) )
            G.add( (BSH[shapename], A, SH.NodeShape) )

            G.add( (sh_prop, SH['nodeKind'], SH.IRI) )
            G.add( (sh_prop, SH['class'], obj) )
            qualifier = SH.targetSubjectsOf
            G.add( (BSH[shapename], qualifier, name) )

            G.add( (sh_prop, SH['message'], Literal("Property has subject with incorrect type")) )

with open('shacl_test.ttl', 'wb') as f:
    f.write(G.serialize(format='ttl'))
