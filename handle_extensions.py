import glob
import rdflib

# read the base Brick ontology
brick_graph = rdflib.Graph()
brick_graph.parse("Brick.ttl", format="ttl")

# add extension files to Brick graph
extension_files = glob.glob("extensions/*.ttl")
for filename in extension_files:
    brick_graph.parse(filename)

# serialize Brick with all extensions added
with open("Brick+extensions.ttl", "w", encoding="utf-8") as fp:
    fp.write(brick_graph.serialize(format="turtle").rstrip())
    fp.write("\n")
