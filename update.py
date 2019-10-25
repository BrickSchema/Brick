from argparse import ArgumentParser
from rdflib import Graph, Namespace
from utils import find_conversions, convert, standardize_namespaces, bump_versions, backup
from logging import getLogger


"""
Argument Parsing:
source: source version (for example '1.0.3')
target: target version (for example '1.1.0')
info: log operation description
"""
parser = ArgumentParser(description='Update Brick models.')
parser.add_argument('models', metavar='model', type=str, nargs='+',
                    help='a turtle file with a brick model')
parser.add_argument('--source',
                    help='source version', required=True)
parser.add_argument('--target',
                    help='target version', required=True)
parser.add_argument('--info',
                    help='get information related to ongoing operations', action='store_true')
args = parser.parse_args()


# set log level to INFO if required.
if args.info:
    getLogger().setLevel("INFO")


# Load the versions graph which has information about possible conversions.
versions_graph = Graph()
versions_graph.parse('./conversions/versions.ttl', format='turtle')
versions_graph.bind('version', Namespace("https:brickschema.org/version#"))

# Ask if the conversion is possible
job = versions_graph.query("""ASK{
                    "%s" version:convertsTo+ "%s"
}""" % (args.source, args.target))

# If yes, find the shortest path and convert
for doable in job:
    if doable:
        print("Conversion available!\n=====================")
        # Find the conversions to update the model in minimum number of version upgrades
        conversions = find_conversions(args.source, args.target, versions_graph)

        # Loop through all the input models
        for model in args.models:
            print('\n\nUpdating {}...'.format(model))

            # Create a model.bak
            backup(model)
            standardize_namespaces(model)

            # Execute all conversions
            for conversion in conversions:
                model_graph = Graph()
                model_graph.parse(model, format='turtle')
                print("Converting to {}...".format(conversion[1]))
                convert(conversion, model_graph)
                model_graph.serialize(model, format='turtle')
                bump_versions(model, conversion[0], conversion[1])
            print('Output stored: {}'.format(model))
    else:
        print("No conversions available from {} to {}.".format(args.source, args.target))
