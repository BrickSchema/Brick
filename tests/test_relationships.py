import sys

sys.path.append("..")
from bricksrc.namespaces import BRICK, RDF, RDFS, OWL, REC  # noqa: E402
from bricksrc.relationships import relationships  # noqa:E402


def test_relationship_identification(brick):
    """
    Tests that Brick only defines the relationships mentioned in the relationships list,
    and that all relationships in the relationships list are defined in Brick
    """
    relships = set(brick.subjects(RDFS.subPropertyOf, BRICK.Relationship))
    all_properties = set(brick.subjects(RDF.type, OWL.ObjectProperty))
    all_properties = all_properties.union(
        set(brick.subjects(RDF.type, OWL.DatatypeProperty))
    )
    # keep only properties in the Brick and REC namespaces
    all_properties = {
        p for p in all_properties if p.startswith(BRICK) or p.startswith(REC)
    }
    non_brick_properties = all_properties - relships

    assert (
        len(relships) + len(non_brick_properties) == len(relationships)
    ), "There are properties in the built ontology which do not appear in the relationships.py file. Make sure to add all properties to relationships.py."
