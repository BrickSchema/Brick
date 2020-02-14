import sys
from argparse import ArgumentParser
from logging import getLogger
from os.path import dirname

from rdflib import Graph, Namespace
from utils import (
    find_conversions,
    execute_conversions,
    standardize_namespaces,
    get_output_filename,
)

"""
Argument Parsing:
source: source version (for example '1.0.3')
target: target version (for example '1.1')
info: log operation description
"""
parser = ArgumentParser(description="Update Brick models.")
parser.add_argument(
    "models",
    metavar="model",
    type=str,
    nargs="+",
    help="a turtle file with a brick model",
)
parser.add_argument("--source", help="source version", required=True)
parser.add_argument("--target", help="target version", required=True)
parser.add_argument(
    "--info", help="get information related to ongoing operations", action="store_true"
)
args = parser.parse_args()


# set log level to INFO if required.
if args.info:
    getLogger().setLevel("INFO")


def convert(source, target, models):
    # Load the versions graph which has information about possible conversions.
    versions_graph = Graph()
    directory = dirname(sys.argv[0]) or "."
    versions_graph.parse(directory + "/conversions/versions.ttl", format="turtle")
    versions_graph.bind("version", Namespace("https://brickschema.org/version#"))

    # Ask if the conversion is possible
    job = versions_graph.query(
        """ASK{
                        "%s" version:convertsTo+ "%s"
    }"""
        % (source, target)
    )

    # If yes, find the shortest path and convert
    for doable in job:
        if doable:
            print("Conversion available!\n=====================")
            # Find the conversions to update the model in minimum number of version upgrades
            conversions = find_conversions(source, target, versions_graph)

            # Loop through all the input models
            for model in models:
                print("\n\nUpdating {}...".format(model))

                standardize_namespaces(model)

                # Execute all conversions
                for conversion in conversions:
                    model_graph = Graph()
                    model_graph.parse(model, format="turtle")
                    print("Converting to {}...".format(conversion[1]))
                    execute_conversions(conversion, model_graph)
                    output = get_output_filename(model, conversion[1])
                    model_graph.serialize(output, format="turtle")
                print("Output stored: {}".format(output))
        else:
            print("No conversions available from {} to {}.".format(source, target))


convert(args.source, args.target, args.models)
