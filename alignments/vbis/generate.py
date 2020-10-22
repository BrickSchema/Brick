import csv
from rdflib import Graph, Namespace, Literal, BNode
from rdflib import RDF, RDFS, XSD, OWL
from rdflib.collection import Collection

graph = Graph()
BRICK = Namespace("https://brickschema.org/schema/1.1/Brick#")
SH = Namespace("http://www.w3.org/ns/shacl#")
VBIS = Namespace("https://brickschema.org/schema/1.1/Brick/alignments/vbis#")
graph.bind("brick", BRICK)
graph.bind("sh", SH)
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
        # create a shape for each set of tags
        graph.add((BRICK[bc], RDF.type, SH.NodeShape))
        patterns = []
        if len(vbtags) == 1:
            shape = BNode()
            graph.add((BRICK[bc], SH.property, shape))
            graph.add((shape, RDF.type, SH.PropertyShape))
            graph.add((shape, SH.path, VBIS.hasVBISTag))
            graph.add((shape, SH.pattern, Literal(vbtags[0])))
        else:
            shapeList = BNode()
            graph.add((BRICK[bc], SH["or"], shapeList))
            for vb in vbtags:
                pattern = BNode()
                patterns.append(pattern)
                graph.add((pattern, RDF.type, SH.PropertyShape))
                graph.add((pattern, SH.path, VBIS.hasVBISTag))
                graph.add((pattern, SH.pattern, Literal(vb)))
            Collection(graph, shapeList, patterns)

graph.serialize("Brick-VBIS-alignment.ttl", format="turtle")
