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

for name, properties in property_definitions.items():

    for pred, obj in properties.items():
        sh_prop = BNode()
        if pred != SKOS.notation:
            continue

        # For now the shapes are generated with the guidance of RDFS.notation
        # For example: (extracted from ../bricksrc/properties.py)
        # SKOS.notation: [Literal("RDFS.domain: BRICK.Point"),
        #                Literal("RDFS.range: BRICK.Measurable")],
        # which dictates the subject and object types of the property.

        for elt in obj:
            if str(elt).startswith('RDFS.range'):
                (RDFS_range, range_elt) = str(elt).split()
                range_value = eval(range_elt)

                shapename = f"{name}RangeShape"
                G.add((BSH[shapename], SH['property'], sh_prop))
                G.add((BSH[shapename], A, SH.NodeShape))

                G.add((sh_prop, SH['nodeKind'], SH.IRI))
                G.add((sh_prop, SH['path'], BRICK[name]))
                G.add((sh_prop, SH['class'], range_value))
                G.add((BSH[shapename], SH.targetSubjectsOf, BRICK[name]))
                G.add((sh_prop, SH['message'],
                       Literal(f"Property {name} has object with incorrect type")))

            if str(elt).startswith('RDFS.domain'):
                (RDFS_domain, domain_elt) = str(elt).split()
                domain_value = eval(domain_elt)

                shapename = f"{name}DomainShape"
                G.add( (BSH[shapename], A, SH.NodeShape))
                G.add( (BSH[shapename], SH.targetSubjectsOf, BRICK[name]))
                G.add( (BSH[shapename], SH['class'], domain_value))
                G.add( (BSH[shapename], SH['message'],
                        Literal(f"Property {name} has subject with incorrect type")))

# subproperties
# TODO: explicitly coded for now, but we should generalize
substance_subproperties = {
    'feedsAir':  {
        'substance': BRICK.Air,
        'properties': [BRICK.regulates, BRICK.measures]
    },
}

for subprop, desc in substance_subproperties.items():
    for prop in desc['properties']:
        sh_prop = BNode()
        (prefix, name) = prop.split('#')
        shapename = f"feedsAir{name.capitalize()}Shape"
        G.add((BSH[shapename], SH['property'], sh_prop))
        G.add((BSH[shapename], A, SH.NodeShape))
        G.add((sh_prop, SH['nodeKind'], SH.IRI))
        G.add((sh_prop, SH['path'], prop))
        G.add((sh_prop, SH['class'], desc['substance']))
        G.add((sh_prop, SH['message'],
               Literal(f"Subject of property {subprop} has object with incorrect type")))

        G.add((BSH[shapename], SH.targetSubjectsOf, BRICK[subprop]))

with open('shacl_test.ttl', 'wb') as f:
    f.write(G.serialize(format='ttl'))
