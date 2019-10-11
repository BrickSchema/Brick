from argparse import ArgumentParser
from rdflib import Graph, Namespace
from utils import find_conversions, convert, standardize_namespaces, bump_versions, create_output_file

parser = ArgumentParser(description='Update Brick models.')
parser.add_argument('models', metavar='model', type=str, nargs='+',
                    help='a turtle file with a brick model')
parser.add_argument('--source',
                    help='source version', required=True)
parser.add_argument('--target',
                    help='target version', required=True)

args = parser.parse_args()
versions_graph = Graph()
versions_graph.parse('./conversions/versions.ttl', format='turtle')
versions_graph.bind('version', Namespace("https:brickschema.org/version#"))
job = versions_graph.query("""ASK{
                    "%s" version:updatesTo+ "%s"
}""" % (args.source, args.target))


for doable in job:
    if doable:
        print("Conversion available!\n=====================")
        conversions = find_conversions(args.source, args.target, versions_graph)
        for model in args.models:
            print('\n\nUpdating {}...'.format(model))
            output = create_output_file(model, args.target)
            standardize_namespaces(output)
            for conversion in conversions:
                model_graph = Graph()
                model_graph.parse(output, format='turtle')
                print("Converting to v{}...".format(conversion[1]))
                convert(conversion, model_graph)
                model_graph.serialize(output, format='turtle')
                bump_versions(output, conversion[0], conversion[1])
            print('Output stored: {}'.format(output))
    else:
        print("No conversions available from {} to {}.".format(args.source, args.target))
