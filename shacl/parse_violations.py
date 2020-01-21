import argparse
from rdflib import Graph, Namespace, URIRef, Literal
from pyshacl import validate
from logging import getLogger
from os.path import dirname, splitext
import sys
import ntpath

import sys
sys.path.append('..')
from bricksrc.namespaces import RDF, RDFS, BRICK, BSH, SH, SKOS
from bricksrc.namespaces import bind_prefixes
# add SHACL shapes from properties
from bricksrc.properties import properties as property_definitions


parser = argparse.ArgumentParser(description='Run the pySHACL validator from the command line.')
parser.add_argument('data', metavar='DataGraph',
                    help='The file containing the Target Data Graph.')
parser.add_argument('-s', '--shacl', dest='shacl', action='store', nargs='?',
                    help='A file containing the SHACL Shapes Graph.')
parser.add_argument('-e', '--ont-graph', dest='ont', action='store', nargs='?',
                    help='A file path or URL to a docucument containing extra ontological information to mix into the data graph.')
parser.add_argument('-i', '--inference', dest='inference', action='store',
                    default='none', choices=('none', 'rdfs', 'owlrl', 'both'),
                    help='Choose a type of inferencing to run against the Data Graph before validating.')
parser.add_argument('-m', '--metashacl', dest='metashacl', action='store_true',
                    default=False, help='Validate the SHACL Shapes graph against the shacl-shacl '
                    'Shapes Graph before before validating the Data Graph.')
parser.add_argument('--imports', dest='imports', action='store_true',
                    default=False, help='Allow import of sub-graphs defined in statements with owl:import.')
parser.add_argument('-a', '--advanced', dest='advanced', action='store_true',
                    default=False, help='Enable features from the SHACL Advanced Features specification.')
parser.add_argument('--abort', dest='abort', action='store_true',
                    default=False, help='Abort on first error.')
parser.add_argument('-d', '--debug', dest='debug', action='store_true',
                    default=False, help='Output additional runtime messages.')
parser.add_argument('-f', '--format', dest='format', action='store',
                    help='Choose an output format. Default is \"human\".',
                    default='human', choices=('human', 'turtle', 'xml', 'json-ld', 'nt', 'n3'))
parser.add_argument('-df', '--data-file-format', dest='data_file_format', action='store',
                    help='Explicitly state the RDF File format of the input DataGraph file. Default=\"auto\".',
                    default='auto', choices=('auto', 'turtle', 'xml', 'json-ld', 'nt', 'n3'))
parser.add_argument('-sf', '--shacl-file-format', dest='shacl_file_format', action='store',
                    help='Explicitly state the RDF File format of the input SHACL file. Default=\"auto\".',
                    default='auto', choices=('auto', 'turtle', 'xml', 'json-ld', 'nt', 'n3'))
parser.add_argument('-ef', '--ont-file-format', dest='ont_file_format', action='store',
                    help='Explicitly state the RDF File format of the extra ontology file. Default=\"auto\".',
                    default='auto', choices=('auto', 'turtle', 'xml', 'json-ld', 'nt', 'n3'))
parser.add_argument('-o', '--output', dest='output', nargs='?', type=argparse.FileType('w'),
                    help='Send output to a file (defaults to stdout).',
                    default=sys.stdout)

args = parser.parse_args()
data_graph = Graph().parse(args.data, format='turtle')
shacl_graph = Graph().parse(args.shacl, format='turtle')

ont_graph = Graph().parse(args.ont, format='turtle')

r = validate(data_graph, shacl_graph=shacl_graph, ont_graph=ont_graph,
             inference='rdfs', abort_on_error=False, meta_shacl=True, debug=False)
conforms, results_graph, results_text = r
print(conforms, results_graph, results_text)

with open('results_text', 'w') as f:
    f.write(results_text)

with open('results_graph.ttl', 'wb') as f:
    f.write(results_graph.serialize(format='ttl'))

exit()


with open('results.ttl', 'wb') as f:
    f.write(results_graph.serialize(format='ttl'))

violation_dict = {}
for (s, p, o) in results_graph:
    if (o not in violation_dict) and (p == SH.result):
        print(s, p, o)
        violation_dict[o] = Graph()
        # violation_dict[o].add((s, p, o))

for (s, p, o) in results_graph:
    if s in violation_dict:
        violation_dict[s].add((s, p, o))

outfile = sys.stdout.buffer
for k in violation_dict:
    print(k, violation_dict[k])
    outfile.write(violation_dict[k].serialize(format='ttl'))



exit()

bind_prefixes(data_graph)
data_graph.bind('bldg', Namespace('http://example.com/mybuilding#'))

res = data_graph.query(
    """SELECT ?s ?p ?o
       WHERE {
          ?s brick:hasLocation ?o .
       }""",
    )

#res.bind('bldg', Namespace('http://example.com/mybuilding#'))
rg = Graph()
rg.bind('bldg', Namespace(f"http://example.com/mybuilding#"))
rg = Graph()
for (s, p, o) in res:
    print(s, p, o)
    rg.add((s, BRICK['hasLocation'], o))

#print(rg.serialize(format='ttl'))
with open('queryResult.ttl', 'wb') as f:
    f.write(rg.serialize(format='ttl'))
