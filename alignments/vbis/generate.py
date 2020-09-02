import csv
from rdflib import Graph, Namespace, Literal
from rdflib import RDF, RDFS, XSD, OWL

graph = Graph()
BRICK = Namespace("https://brickschema.org/schema/1.1/Brick#")
VBIS = Namespace("https://brickschema.org/schema/1.1/Brick/alignments/vbis/v3#")
graph.bind("brick", BRICK)
graph.bind("vbisalign", VBIS)

# define mapping property
graph.add((VBIS.hasVBISTag, RDF.type, OWL.DatatypeProperty))
graph.add((VBIS.hasVBISTag, RDFS.range, XSD.String))
graph.add((VBIS.hasVBISTag, RDFS.domain, BRICK.Class))


def get_brick_class(d):
    for key in ["1", "2", "3", "4", "5"]:
        key = f"Brick Class {key}"
        if d.get(key) and len(d.get(key)) > 0:
            return d.get(key).replace(" ", "_")


def get_vbis_tags(d):
    vbis_tags = []
    for key in [
        "VBIS Tag",
        "Other VBIS Asset Types #1",
        "Other VBIS Asset Types #2",
        "Other VBIS Asset Types #3",
    ]:
        if d.get(key) and len(d.get(key)) > 0:
            vbis_tags.append(d.get(key))
    return vbis_tags


with open("vbis-brick.csv") as f:
    r = csv.reader(f)
    header = next(r)
    for row in r:
        d = dict(zip(header, row))
        bc = get_brick_class(d)
        if bc is None:
            continue
        vbtags = get_vbis_tags(d)
        if len(vbtags) == 0:
            continue
        for vb in vbtags:
            graph.add((BRICK[bc], VBIS.hasVBISTag, Literal(vb)))

graph.serialize("Brick-VBIS-alignment.ttl", format="turtle")
