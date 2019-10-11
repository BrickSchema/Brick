from dijkstar import Graph, find_path
from rdflib import Namespace
import json
import logging


def find_conversions(source, target, versions_graph):
    graph = Graph()
    for source_version, target_version in versions_graph.query("""SELECT ?source_version ?target_version{
                        ?source_version version:updatesTo ?target_version .
    }"""):
        graph.add_edge(str(source_version), str(target_version), {'conversions': 1})
    res = find_path(graph, str(source), str(target), cost_func=lambda u, v, e, prev_e: e['conversions'])
    conversions = []
    print(' -> '.join(res.nodes), '\n')
    current = source
    for node in res.nodes:
        conversions.append((current, node))
        current = node
    return conversions[1:]


def convert(conversion, model_graph):
    with open('./conversions/{}-{}.json'.format(*conversion), 'r') as file:
        conversion_data = json.load(file)
    namespaces = {}
    for prefix, namespace in conversion_data['namespaces'].items():
        namespaces[prefix] = Namespace(namespace)
    for operation in conversion_data['operations']:
        logging.info(operation['description'])
        model_graph.update(operation['query'], initNs=namespaces)


def standardize_namespaces(filename):
    with open(filename) as f:
        standardized_turtle = f.read().replace('http://brickschema.org',
                                   'https://brickschema.org')
    with open(filename, "w") as f:
        f.write(standardized_turtle)


def bump_versions(filename, source, target):
    with open(filename) as f:
        updated_turtle = f.read().replace('https://brickschema.org/schema/{}/Brick'.format(source),
                                   'https://brickschema.org/schema/{}/Brick'.format(target))

    with open(filename, "w") as f:
        f.write(updated_turtle)