import brickschema
from brickschema.namespaces import BRICK, RDFS
import sys

sys.path.append("..")
from bricksrc.relationships import relationships  # noqa:E402


def test_relationship_identification():
    g = brickschema.Graph()
    g.load_file("Brick.ttl")

    relships = list(g.subjects(RDFS.subPropertyOf, BRICK.Relationship))
    assert len(relships) == len(relationships)
