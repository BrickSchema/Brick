import sys
from rdflib import RDFS, Graph

sys.path.append("..")
from bricksrc.namespaces import BRICK  # noqa: E402

g = Graph()
g.parse("Brick.ttl", format="turtle")

g.bind("rdfs", RDFS)
g.bind("brick", BRICK)


def minify(node):
    return node.split("#")[-1]


def test_cycles():
    # Find all the classes that make the hierarchy cyclic.
    classes_in_cycles = []
    res1 = g.query(
        "SELECT ?brick_class WHERE { ?brick_class rdfs:subClassOf+ ?brick_class .}"
    )
    for row in res1:
        classes_in_cycles.append(row[0])

    # Find all the triples involved.
    loops = set()
    for brick_class in classes_in_cycles:
        res2 = g.query(
            """SELECT DISTINCT ?s ?o WHERE {
                              ?s rdfs:subClassOf ?o .
                              brick:%s rdfs:subClassOf+ ?s .
                              ?o rdfs:subClassOf+ brick:%s .
                        }"""
            % (minify(brick_class), minify(brick_class))
        )
        for s, o in res2:
            loops.add("%s -> subClassOf -> %s" % (minify(s), minify(o)))
    assert len(loops) == 0, f"Loops found in the class hierarchy! {loops}"
