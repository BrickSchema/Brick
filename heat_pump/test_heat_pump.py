import brickschema

g = brickschema.Graph().load_file("../Brick.ttl").load_file("heatpump.ttl")
g.expand("brick")

print("-" * 10, "brick:Air_Source_Heat_Pump")
q = "SELECT DISTINCT ?x WHERE { ?x a brick:Air_Source_Heat_Pump }"
for row in g.query(q):
    print(row)

print("-" * 10, "brick:Air_To_Air_Heat_Pump")

q = "SELECT DISTINCT ?x WHERE { ?x a brick:Air_To_Air_Heat_Pump }"
for row in g.query(q):
    print(row)

print("-" * 10, "source-side resource is air")

q = "SELECT DISTINCT ?x WHERE { ?x brick:sourceSideResource/brick:value brick:Air }"
for row in g.query(q):
    print(row)

print("-" * 10, "load-side resource is air")

q = "SELECT DISTINCT ?x WHERE { ?x brick:loadSideResource/brick:value brick:Air }"
for row in g.query(q):
    print(row)
