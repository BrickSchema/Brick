import csv
import re
from rdflib import Graph, Namespace, Literal, BNode
from rdflib import RDF, RDFS, XSD, OWL
from rdflib.collection import Collection

graph = Graph()
BRICK = Namespace("https://brickschema.org/schema/Brick#")
SH = Namespace("http://www.w3.org/ns/shacl#")
VBIS = Namespace("https://brickschema.org/schema/Brick/alignments/vbis#")
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


def rewrite_vbis_pattern(pat):
    """
    If '*' is in the pattern or there are fewer than 3 '-' in the pattern, then
    we return a rewritten regex; else we return the pattern (which should be a
    fully-qualified VBIS tag).  The first returned value is True if the value
    is a pattern, and False otherwise.

    Rewrite VBIS patterns to match the format of regular expressions
    required by XML schema
    """
    if "*" in pat:
        newpat = "^" + re.sub(r"-?\*", ".*", pat.strip()) + "$"
        return True, newpat
    elif len(re.findall("-", pat)) < 3:
        # treat this as a prefix
        return True, "^" + pat.strip() + ".*$"
    return False, pat


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


# use a set to eliminate duplicate rows in the CSV file
finished_brick_classes = set()
with open("vbis-brick-v5.csv") as f:
    r = csv.reader(f)
    header = next(r)
    for row in r:
        d = dict(zip(header, row))
        bc = get_brick_class(d)
        if bc is None or bc in finished_brick_classes:
            continue
        finished_brick_classes.add(bc)
        tagsOrPatterns = get_vbis_tags(d)
        if len(tagsOrPatterns) == 0:
            continue
        print(f"Defining shapes for {bc}")
        # create a shape for each set of tags
        graph.add((VBIS[f"{bc}Shape"], RDF.type, SH.NodeShape))
        graph.add((VBIS[f"{bc}Shape"], SH.targetClass, BRICK[bc]))

        # patterns is the list of patterns that match this Brick class
        patterns = []
        # vbtags is the list of fully qualified VB tags that match this Brick class
        vbtags = []
        # loop through all of the tags and/or patterns we get and sort them into
        # the above two lsits
        for vb in tagsOrPatterns:
            isPattern, patOrValue = rewrite_vbis_pattern(vb)
            if isPattern:
                patterns.append(patOrValue)
            else:
                vbtags.append(patOrValue)
        print(f"{len(patterns)} patterns; {len(vbtags)} full tags")

        if len(patterns) > 0:
            # handle patterns; this is either a SH:pattern directly (if there is one)
            # or a SH:or of a set of patterns (if there is > 1)
            if len(patterns) == 1:
                shape = BNode()
                graph.add((VBIS[f"{bc}Shape"], SH.property, shape))
                graph.add((shape, RDF.type, SH.PropertyShape))
                graph.add((shape, SH.path, VBIS.hasVBISTag))
                graph.add((shape, SH.pattern, Literal(patterns[0])))
            else:
                shapeList = BNode()
                graph.add((VBIS[f"{bc}Shape"], SH["or"], shapeList))
                patternList = []
                for vbtag in patterns:
                    pattern = BNode()
                    patternList.append(pattern)
                    graph.add((pattern, RDF.type, SH.PropertyShape))
                    graph.add((pattern, SH.path, VBIS.hasVBISTag))
                    graph.add((pattern, SH.pattern, Literal(vbtag)))
                Collection(graph, shapeList, patternList)
        elif len(vbtags) > 0:
            # handle fully qualified tags. If there is one, then it is a mandatory
            # value. If there are multiple, then we must have one of them as a value
            shape = BNode()
            graph.add((VBIS[f"{bc}Shape"], SH.property, shape))
            graph.add((shape, RDF.type, SH.PropertyShape))
            graph.add((shape, SH.path, VBIS.hasVBISTag))
            if len(vbtags) == 1:
                graph.add((shape, SH.hasValue, Literal(vbtags[0])))
            else:
                valueList = BNode()
                graph.add((shape, SH["in"], valueList))
                Collection(graph, valueList, [Literal(x) for x in vbtags])

graph.serialize("Brick-VBIS-alignment.ttl", format="turtle")
