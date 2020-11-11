from rdflib import Namespace, Graph
from brickschema.namespaces import BRICK, RDF, RDFS, A

"""
Define the graph that will hold all of the triples defining the apartment.
We define the 'apt' namespace to identify the entities that are part of the
apartment graph vs the entities/concepts that are part of Brick
"""
g = Graph()
APT = Namespace("apartment#")
g.bind("apt", APT)
g.bind("brick", BRICK)
g.bind("rdf", RDF)
g.bind("rdfs", RDFS)

"""
Brick doesn't currently have the notion of an Apartment yet, so we can define
it as a special kind of Space.
Create "my_apartment" as an instance of this new class.
"""
g.add((BRICK["Apartment"], RDFS.subClassOf, BRICK["Space"]))
g.add((APT["my_apartment"], A, BRICK["Apartment"]))

"""
Define the spatial elements of the apartment:
- 3 rooms (bedroom, kitchen, living room)
- 1 HVAC zone (all 3 rooms)
- 3 Lighting zones (1 per room)
"""
g.add((APT["thermostat_zone"], A, BRICK["HVAC_Zone"]))
g.add((APT["bedroom_lighting"], A, BRICK["Lighting_Zone"]))
g.add((APT["kitchen_lighting"], A, BRICK["Lighting_Zone"]))
g.add((APT["living_room_lighting"], A, BRICK["Lighting_Zone"]))

g.add((APT["bedroom"], A, BRICK["Room"]))
g.add((APT["bedroom"], BRICK.isPartOf, APT["my_apartment"]))
g.add((APT["bedroom"], BRICK.isPartOf, APT["thermostat_zone"]))
g.add((APT["bedroom"], BRICK.isPartOf, APT["bedroom_lighting"]))

g.add((APT["kitchen"], A, BRICK["Room"]))
g.add((APT["kitchen"], BRICK.isPartOf, APT["my_apartment"]))
g.add((APT["kitchen"], BRICK.isPartOf, APT["thermostat_zone"]))
g.add((APT["kitchen"], BRICK.isPartOf, APT["kitchen_lighting"]))

g.add((APT["living_room"], A, BRICK["Room"]))
g.add((APT["living_room"], BRICK.isPartOf, APT["my_apartment"]))
g.add((APT["living_room"], BRICK.isPartOf, APT["thermostat_zone"]))
g.add((APT["living_room"], BRICK.isPartOf, APT["living_room_lighting"]))

g.serialize("apartment.ttl", format="ttl")
