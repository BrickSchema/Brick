import brickschema
from brickschema.namespaces import BRICK, RDFS
import sys

sys.path.append("..")
from bricksrc.properties import properties  # noqa:E402


def test_relationship_identification():
    g = brickschema.Graph()
    g.load_file("Brick.ttl")

    props = list(g.subjects(RDFS.subPropertyOf, BRICK.Relationship))
    assert len(props) == len(properties)
