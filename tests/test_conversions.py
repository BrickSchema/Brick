import json
import os
import sys

from rdflib import Graph, Namespace

sys.path.append("..")

g = Graph()


def test_queries():
    conversion_scripts = {}
    malformed_queries = []

    path = os.path.join("tools", "convert", "conversions")

    # load conversion data
    for filename in os.listdir(path):
        if filename[-4:] == "json":
            filepath = os.path.join(path, filename)
            with open(filepath, "r") as f:
                conversion_scripts[filename[:-4]] = json.load(f)

    for filename, conversion_data in conversion_scripts.items():
        # initialize namespaces used in the queries
        namespaces = {}
        for prefix, namespace in conversion_data["namespaces"].items():
            namespaces[prefix] = Namespace(namespace)
            g.bind(prefix, Namespace(namespace), override=True)

        # execute queries
        for operation in conversion_data["operations"]:
            try:
                g.update(operation["query"], initNs=namespaces)
            except Exception as e:
                malformed_queries.append(f"{filename}: {operation['description']}")

    assert malformed_queries == []
