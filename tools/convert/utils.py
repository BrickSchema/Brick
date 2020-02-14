import sys
from json import load
from logging import info
from os.path import dirname

from dijkstar import Graph, find_path
from rdflib import Namespace
from tqdm import tqdm


def find_conversions(source, target, versions_graph):
    """
    This finds the minimum number of version upgrades required to reach the target version.
    :param source: source version
    :param target: target version
    :param versions_graph: graph to fetch update path from
    :return: list of conversions in order of execution
    """
    graph = Graph()
    for source_version, target_version in versions_graph.query(
        """SELECT ?source_version ?target_version{
                        ?source_version version:convertsTo ?target_version .
    }"""
    ):
        graph.add_edge(str(source_version), str(target_version), {"conversions": 1})

    # Find the shortest path
    res = find_path(
        graph,
        str(source),
        str(target),
        cost_func=lambda u, v, e, prev_e: e["conversions"],
    )

    # Create and return the conversions
    conversions = []
    print(" -> ".join(res.nodes))
    current = source
    for node in res.nodes:
        conversions.append((current, node))
        current = node
    return conversions[1:]


def execute_conversions(conversion, model_graph):
    """
    This function coverts the model graph from one version to another
    :param conversion: a tuple (from_version, to_version)
    :param model_graph: the model to update
    """

    # Load conversion scripts
    directory = dirname(sys.argv[0]) or "."
    with open(directory + "/conversions/{}-{}.json".format(*conversion), "r") as file:
        conversion_data = load(file)

    # Add query namespaces
    namespaces = {}
    for prefix, namespace in conversion_data["namespaces"].items():
        namespaces[prefix] = Namespace(namespace)
        model_graph.bind(prefix, Namespace(namespace), override=True)
    with tqdm(conversion_data["operations"], bar_format="{l_bar}{bar}") as operations:
        for operation in operations:
            info(operation["description"])
            model_graph.update(operation["query"], initNs=namespaces)


def standardize_namespaces(filename):
    # This function standardises https on all brick namespaces
    with open(filename) as f:
        standardized_turtle = f.read().replace(
            "http://brickschema.org", "https://brickschema.org"
        )
    with open(filename, "w") as f:
        f.write(standardized_turtle)


def get_output_filename(filename, version):
    # This function returns an output filename
    if (len(filename) > 2) and filename[-4:].lower() == ".ttl":
        return filename[:-4] + "(v%s)" % version + filename[-4:]
    else:
        return filename + "v%s" % version + ".ttl"
