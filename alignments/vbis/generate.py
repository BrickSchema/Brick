import csv
import json
import logging
from collections import defaultdict
from rdflib.collection import Collection
from rdflib import Namespace, Literal, BNode
import brickschema
from brickschema.namespaces import BRICK, SH, A, RDFS, SKOS, RDF

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)

g = brickschema.Graph().load_file("base.ttl")
brick = brickschema.Graph().load_file("../../Brick.ttl")

VBIS = Namespace("https://brickschema.org/schema/Brick/alignments/vbis#")
g.bind("vbis", VBIS)

# Brick Equipment -> {'tag': tag, 'pattern': pattern}
mapping = defaultdict(list)
vbistags = set()


def num_sections(tag):
    """Returns the number of VBIS sections in the tag"""
    return tag.count("-") + 1


def get_subclasses(brickclass):
    res = brick.query(f"SELECT ?sc WHERE {{ ?sc rdfs:subClassOf+ <{brickclass}> }}")
    return [row[0] for row in res]


def generate_vbis_to_brick_rule(brickclass, vbis_tag_list):
    rule = f"Generate{brickclass}FromVBIS"
    g.add((VBIS[rule], A, SH.NodeShape))
    g.add((VBIS[rule], SH.targetSubjectsOf, VBIS.hasTag))
    g.add(
        (
            VBIS[rule],
            SH.rule,
            [
                (A, SH.TripleRule),
                (SH.subject, SH.this),
                (SH.predicate, RDF.type),
                (SH.object, BRICK[brickclass]),
                (
                    SH.condition,
                    [
                        (
                            SH.property,
                            [(SH["path"], VBIS.hasTag), (SH["in"], vbis_tag_list)],
                        )
                    ],
                ),
            ],
        )
    )


def generate_brick_to_vbis_rule(brickclass, default_tag):
    rule = f"GenerateVBISFrom{brickclass}"
    g.add((VBIS[rule], A, SH.NodeShape))
    g.add((VBIS[rule], SH.targetClass, BRICK[brickclass]))
    g.add(
        (
            VBIS[rule],
            SH.rule,
            [
                (A, SH.TripleRule),
                (SH.subject, SH.this),
                (SH.predicate, VBIS.hasTag),
                (SH.object, VBIS[default_tag]),
                (
                    SH.condition,
                    [
                        (
                            SH.property,
                            [
                                (SH.minCount, Literal(0)),
                                (SH.maxCount, Literal(0)),
                                (SH.path, VBIS.hasTag),
                            ],
                        )
                    ],
                ),
            ],
        )
    )


logging.info("Reading VBIS-Brick mapping file")
with open("vbis-brick.csv") as f:
    r = csv.reader(f)
    for row in r:
        vbistag, brickclass = row
        brickclass = brickclass.replace("brick:", "")
        vbistags.add(vbistag)
        if brickclass != "":
            mapping[brickclass].append(vbistag)
        g.add((VBIS[vbistag], A, VBIS.VBISTag))
        g.add((VBIS[vbistag], RDFS.label, Literal(vbistag)))

print(json.dumps(mapping, indent=4))

logging.info("Generating RDF representation of VBIS tags")
# generate RDF representation for VBIS tags
for tagA in vbistags:
    for tagB in vbistags:
        if tagA == tagB:
            continue
        if tagA.startswith(tagB) and num_sections(tagA) == num_sections(tagB) + 1:
            g.add((VBIS[tagA], SKOS.broader, VBIS[tagB]))
        elif tagB.startswith(tagA) and num_sections(tagB) == num_sections(tagA) + 1:
            g.add((VBIS[tagA], SKOS.narrower, VBIS[tagB]))

logging.info("Using Brick class hiearchy to 'inherit' tags")
# use Brick class structure to 'inherit' tags from subclasses
for brickclass in mapping:
    for subclass in get_subclasses(BRICK[brickclass]):
        subclass_tags = mapping.get(subclass.split("#")[-1], [])
        mapping[brickclass].extend(subclass_tags)

logging.info("Generating SHACL shapes for Brick/VBIS alignment")
# generate SHACL shapes for Brick/VBIS alignment
for brickclass, vbistags in mapping.items():
    shape = f"{brickclass}TagShape"

    # figure out the "default" VBIS tags for each Brick class.
    # A "default" tag is shortest, non-empty prefix from the set of tags
    # Multiple default tags may exist
    defaults = [vbistags[0]]
    for tag in vbistags[1:]:
        accounted_for = False
        for i, dt in enumerate(defaults):
            if dt.startswith(tag):
                defaults[i] = tag
                accounted_for = True
            elif tag.startswith(dt):
                accounted_for = True
                continue
        if not accounted_for and tag not in defaults:
            defaults.append(tag)
    if len(defaults) == 1:
        generate_brick_to_vbis_rule(brickclass, defaults[0])

    taglist = BNode()
    vbistags = [VBIS[tag] for tag in set(vbistags)]
    Collection(g, taglist, vbistags)

    generate_vbis_to_brick_rule(brickclass, taglist)

    g.add((VBIS[shape], A, SH.NodeShape))
    g.add((VBIS[shape], SH.targetClass, BRICK[brickclass]))
    g.add(
        (
            VBIS[shape],
            SH.property,
            [
                (
                    SH.message,
                    Literal(
                        f"Brick class brick:{brickclass} does not match the provided tag"
                    ),
                ),
                (SH["path"], VBIS.hasTag),
                (SH["in"], taglist),
                (SH["maxCount"], Literal(1)),
            ],
        )
    )

g.serialize("Brick-VBIS-alignment.ttl", format="ttl")
