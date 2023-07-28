import glob
import rdflib

# read the base Brick ontology
brick_graph = rdflib.Graph()
brick_graph.parse("Brick.ttl", format="ttl")
BRICK = rdflib.URIRef("https://brickschema.org/schema/1.3/Brick")

# add extension files to Brick graph
extension_files = glob.glob("extensions/*.ttl")
for filename in extension_files:
    brick_graph.parse(filename)

# remove duplicate ontology definitions and
# move prefixes onto Brick ontology definition
for pfx in brick_graph.objects(predicate=rdflib.SH.declare):
    brick_graph.remove((None, rdflib.SH.declare, pfx))
    brick_graph.add((BRICK, rdflib.SH.declare, pfx))

for ontology in brick_graph.subjects(predicate=rdflib.RDF.type, object=rdflib.OWL.Ontology):
    if ontology != BRICK:
        brick_graph.remove((ontology, rdflib.RDF.type, rdflib.OWL.Ontology))

# serialize Brick with all extensions added
with open("Brick+extensions.ttl", "w", encoding="utf-8") as fp:
    fp.write(brick_graph.serialize(format="turtle").rstrip())
    fp.write("\n")
