import json
import sys
import rdflib
from warnings import warn
from collections import Counter

sys.path.append("..")
from bricksrc.namespaces import BRICK, RDFS  # noqa: E402


def test_class_definitions(brick_with_imports):
    g = brick_with_imports
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


def test_relationship_definitions(brick_with_imports):
    g = brick_with_imports
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


def test_obsolete_definitions(brick_with_imports):
    g = brick_with_imports
    obsolete_definitions = g.query(
        """SELECT DISTINCT ?term WHERE {
                              ?term skos:definition|rdfs:seeAlso ?definition .
                              FILTER NOT EXISTS {
                                ?term (rdfs:subPropertyOf|rdfs:subClassOf|a)+ ?something .
                              }
                        }"""
    )
    with open("tests/obsolete_definitions.json", "w") as fp:
        json.dump(
            [str(obsolete_term[0]) for obsolete_term in obsolete_definitions],
            fp,
            indent=2,
        )
    error_message = (
        f"{len(obsolete_definitions)} obsolete definition(s) found. "
        f"Terms needing removal: "
        f"{', '.join(str(term[0]) for term in obsolete_definitions)}. "
        "See ./tests/obsolete_definitions.json for more information."
    )
    assert not obsolete_definitions, error_message


def test_valid_definition_encoding(brick_with_imports):
    g = brick_with_imports
    definitions = g.query(
        """SELECT ?term ?definition ?seealso WHERE { ?term skos:definition ?definition . OPTIONAL { ?term rdfs:seeAlso ?seealso } }"""
    )
    for term, defn, seealso in definitions:
        assert isinstance(defn, rdflib.Literal), (
            "Definition %s should be a Literal" % defn
        )
        assert (
            seealso is None
            or isinstance(seealso, rdflib.URIRef)
            or isinstance(seealso, rdflib.Literal)
        ), ("SeeAlso %s should be a URI or Literal or None" % seealso)


def test_rdfs_labels(brick_with_imports):
    g = brick_with_imports
    labels = g.subject_objects(predicate=RDFS.label)
    # double check that rdfs:label on Brick entity only has one value for 'en'
    c = Counter(
        [
            s
            for s, l in labels
            if (l.language is None or l.language == "en") and s.startswith(BRICK)
        ]
    )
    for entity, count in c.items():
        assert count == 1, f"Entity {entity} has {count} labels, which is more than 1"

    res = g.query(
        """ SELECT ?class WHERE {
        ?class rdfs:subClassOf+ brick:Entity .
        FILTER NOT EXISTS { ?class rdfs:label ?label }
    }"""
    )
    for row in res:
        assert False, "Class %s has no label" % row[0]
