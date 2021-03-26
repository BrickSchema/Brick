import sys
import brickschema
from bricksrc.namespaces import A, OWL, RDFS, SKOS, BRICK, SH, BSH, bind_prefixes
from .util import make_readable

sys.path.append("..")
from bricksrc.properties import properties  # noqa: E402

g = brickschema.Graph()
g.load_file("shacl/BrickShape.ttl")
bind_prefixes(g)
