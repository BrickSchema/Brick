import argparse
from rdflib import Graph, Namespace
from utils import find_conversions, convert

parser = argparse.ArgumentParser(description='Update Brick models.')
parser.add_argument('models', metavar='model', type=str, nargs='+',
                    help='a turtle file with a brick model')
parser.add_argument('--source',
                    help='source version')
parser.add_argument('--target',
                    help='target version')

args = parser.parse_args()
versions_graph = Graph()
versions_graph.parse('versions.ttl', format='turtle')
versions_graph.bind('version', Namespace("https:brickschema.org/version#"))
job = versions_graph.query("""ASK{
                    "%s" version:updatesTo+ "%s"
}""" % (args.source, args.target))


for doable in job:
    if doable:
        print("Conversion available!")
        conversions = find_conversions(args.source, args.target, versions_graph)
        for model in args.models:
            print('Updating {}...'.format(model))
            model_graph = Graph()
            model_graph.parse(model, format='turtle')
            for conversion in conversions:
                print("Converting {} to {}...".format(model, conversion[1]))
                convert(conversion, model_graph)
            model_graph.serialize('{}-{}'.format(args.target, model), format='turtle')
