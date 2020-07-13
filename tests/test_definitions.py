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
                              ?brick_class (rdfs:subClassOf|a)+ brick:Class .
                              FILTER NOT EXISTS {
                                ?brick_class skos:definition ?definition .
                              }
                        }"""
    )
    with open("tests/classes_no_definitions.json", "w") as fp:
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
                f"brick class(es). For more information, see ./tests/classes_no_definitions.json"
            )
        )


def test_relationship_definitions():
    relationships_without_definitions = g.query(
        """SELECT DISTINCT ?brick_relationship WHERE {
                              ?brick_relationship (rdfs:subPropertyOf|a)+ ?some_property .
                              VALUES ?some_property {owl:AsymmetricProperty owl:IrreflexiveProperty owl:ObjectProperty} .
                              FILTER NOT EXISTS {
                                ?brick_relationship skos:definition ?definition .
                              }
                        }"""
    )
    with open("tests/relationships_no_definitions.json", "w") as fp:
        json.dump(
            [
                relationship_without_definition[0]
                for relationship_without_definition in relationships_without_definitions
            ],
            fp,
            indent=2,
        )
    if relationships_without_definitions:
        warn(
            UserWarning(
                f"No definitions specified for {len(relationships_without_definitions)} "
                f"brick relationship(s). For more information, see ./tests/relationships_no_definitions.json"
            )
        )


def test_obsolete_definitions():
    definitions_without_terms = g.query(
        """SELECT DISTINCT ?term WHERE {
                              ?term skos:definition|rdfs:seeAlso ?definition .
                              FILTER NOT EXISTS {
                                ?term (rdfs:subPropertyOf|rdfs:subClassOf|a)+ ?something .
                              }
                        }"""
    )
    with open("tests/obsolete_definitions.json", "w") as fp:
        json.dump(
            [
                definitions_without_term[0]
                for definitions_without_term in definitions_without_terms
            ],
            fp,
            indent=2,
        )
    assert (
        not definitions_without_terms
    ), f"{len(definitions_without_terms)} definitions found for deprecated term(s). For more information, see ./tests/obsolete_definitions.json"
