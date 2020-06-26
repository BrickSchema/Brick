import csv
import json
import sys
import rdflib
import brickschema
from warnings import warn
from rdflib import RDF, RDFS, Namespace, BNode

sys.path.append("..")
from bricksrc.namespaces import BRICK, SKOS  # noqa: E402


g = rdflib.Graph()
g.parse("Brick.ttl", format="turtle")

g.bind("rdf", RDF)
g.bind("rdfs", RDFS)
g.bind("brick", BRICK)


def test_class_definitions():
    classes_without_definitions = g.query(
        """SELECT DISTINCT ?brick_class WHERE {
                              ?brick_class rdfs:subClassOf* brick:Class .
                              FILTER NOT EXISTS {
                                ?brick_class skos:definition ?definition .
                              }
                        }"""
    )
    with open("tests/test_no_definitions.json", "w") as fp:
        json.dump(
            [
                class_without_definition[0]
                for class_without_definition in classes_without_definitions
            ],
            fp,
            indent=2,
        )
    if classes_without_definitions:
        warn(
            UserWarning(
                f"No definitions specified for {len(classes_without_definitions)} "
                f"brick classes. For more information, see ./tests/test_no_definitions.json"
            )
        )


def test_non_class_definitions():
    definitions_without_classes = g.query(
        """SELECT DISTINCT ?brick_class WHERE {
                              ?brick_class skos:definition|rdfs:seeAlso ?definition .
                              FILTER NOT EXISTS {
                                ?brick_class rdfs:subClassOf* brick:Class .
                              }
                        }"""
    )
    with open("tests/obsolete_definitions.json", "w") as fp:
        json.dump(
            [
                definition_without_class[0]
                for definition_without_class in definitions_without_classes
            ],
            fp,
            indent=2,
        )
    assert (
        not definitions_without_classes
    ), f"{len(definitions_without_classes)} definitions found for deprecated classes. For more information, see ./tests/test_no_definitions.json"
