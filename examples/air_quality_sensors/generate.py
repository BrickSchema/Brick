import brickschema
from brickschema.namespaces import A, OWL, BRICK, UNIT, XSD
from rdflib import Namespace, Literal

# our entities will live in this namespace
BLDG = Namespace("urn:example#")

# load brick into a graph so we can query it
brick = brickschema.Graph().load_file("../../Brick.ttl")

# create a graph for our model
g = brickschema.Graph()
g.bind("bldg", BLDG)


# we want to define a collection of air quality sensors that measure
# the air in a particular room on a floor of a building of our deployment
# site

# start by defining the locations

# The generated turtle file should look like this:
#   bldg:deployment_site  a brick:Site ;
#     brick:hasPart   bldg:building_1 .
#   bldg:building_1 a brick:Building ;
#     brick:hasPart   bldg:floor_1 .
#   bldg:floor_1  a brick:Floor ;
#       brick:hasPart bldg:room_1 .
#   bldg:room_1 a brick:Room .

g.add((BLDG["deployment_site"], A, BRICK["Site"]))
g.add((BLDG["building_1"], A, BRICK["Building"]))
g.add((BLDG["floor_1"], A, BRICK["Floor"]))
g.add((BLDG["room_1"], A, BRICK["Room"]))

g.add((BLDG["deployment_site"], BRICK.hasPart, BLDG["building_1"]))
g.add((BLDG["building_1"], BRICK.hasPart, BLDG["floor_1"]))
g.add((BLDG["floor_1"], BRICK.hasPart, BLDG["room_1"]))

# we can actually be more specific about the types of the rooms!
# Query Brick for available room types
results = list(
    brick.query("SELECT ?roomtype WHERE { ?roomtype rdfs:subClassOf+ brick:Room }")
)
print(f"Brick has {len(results)} room types defined. Here are 10 of them:")
for r in results[:10]:
    print(f"Room type: {r[0]}")

g.add((BLDG["room_1"], A, BRICK["Office_Kitchen"]))

# can add information about the sq area of the room and the floor
# this nifty syntax requires brickschema>=0.3.2a1
room_area = [
    (BRICK.value, Literal(40, datatype=XSD.double)),
    (BRICK.hasUnit, UNIT["M2"]),
]
g.add((BLDG["room_1"], BRICK.area, room_area))

floor_area = [
    (BRICK.value, Literal(1000, datatype=XSD.double)),
    (BRICK.hasUnit, UNIT["M2"]),
]
g.add((BLDG["floor_1"], BRICK.area, floor_area))

# now we can create the sensors! To avoid having to write out the "g.add()" calls by hand,
# can simplify the process by using a Python data structure and then iterating over it.

# each item in this list will have (sensor name, brick class, units, location)
sensors = [
    (BLDG["co_sensor"], BRICK["CO_Level_Sensor"], UNIT["PPM"], BLDG["room_1"]),
    (BLDG["co2_sensor"], BRICK["CO2_Level_Sensor"], UNIT["PPM"], BLDG["room_1"]),
    (
        BLDG["methane_sensor"],
        BRICK["Methane_Level_Sensor"],
        UNIT["PPM"],
        BLDG["room_1"],
    ),
    (
        BLDG["pm2.5_sensor"],
        BRICK["PM2.5_Sensor"],
        UNIT["MicroGM-PER-M3"],
        BLDG["room_1"],
    ),
    (
        BLDG["air_temp_sensor"],
        BRICK["Air_Temperature_Sensor"],
        UNIT["DEG_C"],
        BLDG["room_1"],
    ),
]
for (sensor, brick_type, units, location) in sensors:
    g.add((sensor, A, brick_type))
    g.add((sensor, BRICK.hasUnit, units))
    g.add((sensor, BRICK.isPointOf, location))

# save the file
g.serialize("air_quality_sensor_example.ttl", format="ttl")


# now we can load in Brick, "compile" it with a reasoner, and then run some interesting queries
g.load_file("../../Brick.ttl")
g.expand("brick")

print("What sensors in the graph measure air quality?")
q = """SELECT ?sensor ?location WHERE {
    ?sensor brick:measures brick:Air_Quality .
    ?sensor brick:hasLocation ?location .
}"""
for row in g.query(q):
    print(row)

print("What are other kinds of units that the PM2.5 sensor could have?")
q = """SELECT ?unit WHERE {
    ?sensor a   brick:PM2.5_Sensor .
    ?sensor brick:measures/qudt:applicableUnit ?unit
}"""
for row in g.query(q):
    print(row)
