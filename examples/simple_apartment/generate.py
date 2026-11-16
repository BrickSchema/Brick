from rdflib import Namespace, Graph
from brickschema.namespaces import BRICK, REC, RDF, RDFS, A

"""
Define the graph that will hold all of the triples defining the apartment.
We define the 'apt' namespace to identify the entities that are part of the
apartment graph vs the entities/concepts that are part of Brick
"""
g = Graph()
APT = Namespace("http://example.com/apartment#")
g.bind("apt", APT)
g.bind("brick", BRICK)
g.bind("rec", REC)
g.bind("rdf", RDF)
g.bind("rdfs", RDFS)

"""
RealEstateCore defines an Apartment as a collection of rooms.
Create "my_apartment" as an instance of it.
"""
g.add((APT["my_apartment"], A, REC.Apartment))

"""
Define the spatial elements of the apartment:
- 3 rooms (bedroom, kitchen, living room)
- 1 HVAC zone (all 3 rooms)
- 3 Lighting zones (1 per room)
"""
g.add((APT["thermostat_zone"], A, REC.HVACZone))
g.add((APT["bedroom_lighting"], A, REC.Zone))
g.add((APT["kitchen_lighting"], A, REC.Zone))
g.add((APT["living_room_lighting"], A, REC.Zone))

g.add((APT["bedroom"], A, REC.Room))
g.add((APT["my_apartment"], REC.includes, APT["bedroom"]))
g.add((APT["bedroom"], BRICK.isPartOf, APT["thermostat_zone"]))
g.add((APT["bedroom"], BRICK.isPartOf, APT["bedroom_lighting"]))

g.add((APT["kitchen"], A, REC.Room))
g.add((APT["my_apartment"], REC.includes, APT["kitchen"]))
g.add((APT["kitchen"], BRICK.isPartOf, APT["thermostat_zone"]))
g.add((APT["kitchen"], BRICK.isPartOf, APT["kitchen_lighting"]))

g.add((APT["living_room"], A, REC.Room))
g.add((APT["my_apartment"], REC.includes, APT["living_room"]))
g.add((APT["living_room"], BRICK.isPartOf, APT["thermostat_zone"]))
g.add((APT["living_room"], BRICK.isPartOf, APT["living_room_lighting"]))

g.serialize("apartment.ttl", format="ttl")
