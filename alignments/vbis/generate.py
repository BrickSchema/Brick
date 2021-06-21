import csv
import json
from collections import defaultdict
from rdflib.collection import Collection
from rdflib import Namespace, Literal, BNode
import brickschema
from brickschema.namespaces import BRICK, SH, A, RDFS, SKOS


g = brickschema.Graph().load_file("base.ttl")

VBIS = Namespace("https://brickschema.org/schema/Brick/alignments/vbis#")
g.bind("vbis", VBIS)

# Brick Equipment -> {'tag': tag, 'pattern': pattern}
mapping = defaultdict(list)
vbistags = set()


def num_sections(tag):
    """Returns the number of VBIS sections in the tag"""
    return tag.count("-") + 1


with open("vbis-brick.csv") as f:
    r = csv.reader(f)
    for row in r:
        vbistag, brickclass = row
        brickclass = brickclass.replace("brick:", "")
        vbistags.add(vbistag)
        mapping[brickclass].append(vbistag)
        g.add((VBIS[vbistag], A, VBIS.VBISTag))
        g.add((VBIS[vbistag], RDFS.label, Literal(vbistag)))

print(json.dumps(mapping, indent=4))

# generate RDF representation for VBIS tags
for tagA in vbistags:
    for tagB in vbistags:
        if tagA == tagB:
            continue
        if tagA.startswith(tagB) and num_sections(tagA) == num_sections(tagB) + 1:
            g.add((VBIS[tagA], SKOS.broader, VBIS[tagB]))
        elif tagB.startswith(tagA) and num_sections(tagB) == num_sections(tagA) + 1:
            g.add((VBIS[tagA], SKOS.narrower, VBIS[tagB]))

# generate SHACL shapes for Brick/VBIS alignment
for brickclass, vbistags in mapping.items():
    shape = f"{brickclass}TagShape"

    taglist = BNode()
    vbistags = [VBIS[tag] for tag in vbistags]
    Collection(g, taglist, vbistags)

    g.add((VBIS[shape], A, SH.NodeShape))
    g.add((VBIS[shape], SH.targetClass, BRICK[brickclass]))
    g.add(
        (
            VBIS[shape],
            SH.property,
            [
                (SH["path"], VBIS.hasTag),
                (SH["in"], taglist),
                (SH["maxCount"], Literal(1)),
            ],
        )
    )

g.serialize("Brick-VBIS-alignment.ttl", format="ttl")
