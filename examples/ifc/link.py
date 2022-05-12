import brickschema
from brickschema.namespaces import Namespace, BRICK, REF, A
from rdflib import Literal

BLDG = Namespace("urn:example#")

g = brickschema.Graph()
g.load_file("ifc.ttl")  # our example file

# get project
project = list(g.query("SELECT ?proj WHERE { ?proj a ref:ifcProject }"))[0][0]

link = {
    "brick": BLDG["space3"],
    "ifc": "abc123",
}

g.add(
    (
        link["brick"],
        REF.hasExternalReference,
        [
            (A, REF.IFCReference),
            (REF.hasIfcProjectReference, project),
            (REF.ifcGlobalID, Literal(link["ifc"])),
        ],
    )
)

g.serialize("ifc-with-new-reference.ttl", format="turtle")
