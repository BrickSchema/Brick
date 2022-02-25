from rdflib import RDF, RDFS, OWL, Namespace, Graph

"""

A Brick model is a digital representation of the resources and relationships
inside a building described using the Brick schema.

A Brick model is maintained/query through the abstraction of a Graph. A Graph
consists of triples (subject, predicate, object). Subjects and objects can be
"classes" or "instances of classes" (sometimes called individuals, instances or
entities). Predicates are the "directed edges" in the graph and are sometimes
referred to as such

    +---------+        Predicate         +--------+
    | Subject |------------------------->| Object |
    +---------+                          +--------+

"""

g = Graph()

"""

Now that we have the graph object we have to decide what to put into it. At the
very least, we probably want to put in triples describing the "things" in our
building. In Brick, "things" have a name and a class, which tells us what kind
of thing they are.

The Brick schema defines a set of classes that are ready for you to use. Brick
classes includes HVAC equipment, lighting equipment, electrical equipment,
rooms and other spatial elements, zones, and points like sensors and setpoints.
You can find a list of the classes supported by Brick online:
https://brickschema.org/ontology

Before we start adding things to our Brick model, we need to define a namespace.
A "namespace" is a way of grouping information so that the names we choose for
things don't conflict with names in other Brick models (more on that later).

Namespaces are URLs; they do not have to actually point to a real web resource,
but it is of course helpful if they point to some documentation (try going to
https://brickschema.org/schema/Brick#Air_Handler_Unit as an example).

We will choose an arbitrary URL for our namespace and refer to it by the
nickname "bldg" for convenience. "bldg" is also called a "prefix".

"""

BLDG = Namespace("http://example.com/mybuilding#")
g.bind("bldg", BLDG)

"""

Here, we tell our graph what the Brick namespace is. This does *not* mean that
the contents of the Brick schema (which is a graph itself) get pulled in. It
simply allows us to refer to classes and relationships that are defined in the
Brick schema.

"""
BRICK = Namespace("https://brickschema.org/schema/Brick#")
g.bind("brick", BRICK)


"""

Now we can add instances to our Brick model (building graph). We use the RDF
namespace (imported above) in addition to the BRICK and BLDG namespaces.
"RDF.type" is the "type" predicate defined within the RDF graph. The RDF.type
predicate is how we create "instances" of Brick classes.

"""

# (subject, predicate, object)
g.add((BLDG.AHU1A, RDF.type, BRICK.Air_Handler_Unit))
# you can use "quotes" to name entities as well
g.add((BLDG["VAV2-3"], RDF.type, BRICK.Variable_Air_Volume_Box))


"""
We can also add relationships between entities in our Brick model. The
BRICK.feeds relationship indicates a sequence between two pieces of equipment
"""

g.add((BLDG.AHU1A, BRICK.feeds, BLDG["VAV2-3"]))

"""
Let's add a few more entities so the graph is more interesting. We will
implement the Brick model for the *blue* entities in the sample graph at
brickschema.org
"""

# declare entities first
g.add((BLDG["VAV2-4"], RDF.type, BRICK.Variable_Air_Volume_Box))
g.add((BLDG["VAV2-4.DPR"], RDF.type, BRICK.Damper))
g.add((BLDG["VAV2-4.DPRPOS"], RDF.type, BRICK.Damper_Position_Setpoint))
g.add((BLDG["VAV2-4.ZN_T"], RDF.type, BRICK.Supply_Air_Temperature_Sensor))
g.add((BLDG["VAV2-4.SUPFLOW"], RDF.type, BRICK.Supply_Air_Flow_Sensor))
g.add((BLDG["VAV2-4.SUPFLSP"], RDF.type, BRICK.Supply_Air_Flow_Setpoint))
g.add((BLDG["VAV2-3Zone"], RDF.type, BRICK.HVAC_Zone))
g.add((BLDG["Room-410"], RDF.type, BRICK.Room))
g.add((BLDG["Room-411"], RDF.type, BRICK.Room))
g.add((BLDG["Room-412"], RDF.type, BRICK.Room))

# declare edges
g.add((BLDG["AHU1A"], BRICK.feeds, BLDG["VAV2-4"]))
g.add((BLDG["VAV2-4"], BRICK.hasPart, BLDG["VAV2-4.DPR"]))
g.add((BLDG["VAV2-4.DPR"], BRICK.hasPoint, BLDG["VAV2-4.DPRPOS"]))
g.add((BLDG["VAV2-4"], BRICK.hasPoint, BLDG["VAV2-4.SUPFLOW"]))
g.add((BLDG["VAV2-4"], BRICK.hasPoint, BLDG["VAV2-4.SUPFLSP"]))
g.add((BLDG["VAV2-3"], BRICK.feeds, BLDG["VAV2-3Zone"]))
g.add((BLDG["VAV2-3Zone"], BRICK.hasPart, BLDG["Room-410"]))
g.add((BLDG["VAV2-3Zone"], BRICK.hasPart, BLDG["Room-411"]))
g.add((BLDG["VAV2-3Zone"], BRICK.hasPart, BLDG["Room-412"]))

"""
We can "serialize" this model to a file if we want to load it into another program.
"""
with open("example.ttl", "w") as f:
    # the Turtle format strikes a balance beteween being compact and easy to read
    f.write(g.serialize(format="ttl"))


"""
Curiously enough, we haven't actually made use of the Brick schema definition
yet. The Brick schema definition contains a set of rules and definitions. These
can help with:

- ensuring that classes and relationships are being used correctly
- allowing applications and users to query the Brick schema to better
  understand a class or relationship
- providing textual definitions of classes and relationships
- inferring classes from sets of tags (like Haystack) or from behavioral
  annotations (like "sensors that measure air temperature")

To understand what the Brick schema definition can give us, lets try finding
what kinds of air temperature sensors we have in our Brick model.
"""
sensors = g.query(
    """SELECT ?sensor WHERE {
    ?sensor rdf:type/rdfs:subClassOf* brick:Air_Temperature_Sensor
}"""
)

"""
This query uses the definition of the Brick class structure to find what
instances of Air_Temperature_Sensor exist as well as instances of any
*subclasses* of Air_Temperature_Sensor.  This kind of behavior is usually referred
to as "subtype polymorphism" and is analogous to what you'd find in Java.

*However*, our query returns no results because our Brick model doesn't know
what the Brick class hierarchy is yet.
"""

assert len(sensors) == 0

"""
If we want to make use of the Brick schema definition, we need to "import" it.
You need a file called "Brick.ttl" on your computer (this can be obtained from
https://brickschema.org/resources/ or at https://github.com/BrickSchema/Brick/releases)

Assuming Brick.ttl is in the root directory of this repo, you can load it with the following.
"""

g.parse("../../Brick.ttl", format="ttl")

"""
Now our query should execute and return one result (BLDG.VAV2-4.ZN-T)
"""

sensors = g.query(
    """SELECT ?sensor WHERE {
    ?sensor rdf:type brick:Supply_Air_Temperature_Sensor
}"""
)
assert len(sensors) == 1


"""

We can also expand Brick to add additional classes. Eventually, these suggestions should
be pushed upstream and contributed back to the community (see the Contribution guidelines at
https://github.com/BrickSchema/Brick/blob/master/CONTRIBUTING.md)

For now, lets define a new kind of zone called a Fire Zone. It is good practice when defining
new classes to "attach" them to existing classes in the Brick class structure through the
RDFS.subClassOf relationship. Here's the triples we need to define a new class:
"""

g.add((BRICK.Fire_Zone, RDF.type, OWL.Class))
# We can make Fire Zone a subclass of the more generic "Location" class.
# It is easy to change this later.
g.add((BRICK.Fire_Zone, RDFS.subClassOf, BRICK.Location))

# now we can use our new class
g.add((BLDG.FZ1, RDF.type, BRICK.Fire_Zone))
g.add((BLDG.FZ1, BRICK.hasPart, BLDG["Room-410"]))
