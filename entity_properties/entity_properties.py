import brickschema
import pyshacl

g = brickschema.graph.Graph()
g.load_file("../Brick.ttl")
g.load_file("defns.ttl")
g.load_file("sample.ttl")

g = brickschema.inference.BrickInferenceSession(load_brick=False).expand(g)
g.g.serialize("output.ttl", format="ttl")

res = g.query(
    """SELECT DISTINCT ?loc ?area ?unit WHERE {
        ?loc    a   brick:Location .
        ?loc    prop:hasArea/prop:value ?area .
        ?loc    prop:hasArea/brick:hasUnit ?unit .
    }"""
)

for row in res:
    print(row)

a, b, c = pyshacl.validate(g.g, advanced=True)
