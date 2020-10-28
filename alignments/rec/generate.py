import sys
from rdflib import Graph, Namespace, BNode
from rdflib.collection import Collection

if len(sys.argv) < 2:
    print("Usage: python generate.py <input file>")
    sys.exit(1)

graph = Graph()
file_format = sys.argv[1].split(".")[-1]
if file_format == "rdf":
    file_format = "xml"
graph.parse(sys.argv[1], format=file_format)

OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
BRICK = Namespace("https://brickschema.org/schema/1.1/Brick#")
REC_DEVICE = Namespace("https://w3id.org/rec/device/")
REC_CORE = Namespace("https://w3id.org/rec/core/")

mapping = {
    REC_DEVICE.Boiler: BRICK.Boiler,
    REC_DEVICE.AirHandlingUnit: BRICK.Air_Handler_Unit,
    REC_DEVICE.Thermostat: BRICK.Thermostat,
    REC_DEVICE.Chiller: BRICK.Chiller,
    REC_DEVICE.Coil: BRICK.Coil,
    REC_DEVICE.Valve: BRICK.Valve,
    REC_DEVICE.Damper: BRICK.Damper,
    REC_DEVICE.Pump: BRICK.Pump,
    REC_DEVICE.Condenser: BRICK.Condenser,
}

for device_type, brick_class in mapping.items():
    # define owl:Restriction
    restriction_class = BNode()
    graph.add((restriction_class, RDF.type, OWL.Restriction))
    graph.add((restriction_class, RDF.type, OWL.Class))
    graph.add((restriction_class, OWL.onProperty, REC_DEVICE.hasDeviceFunctionType))
    graph.add((restriction_class, OWL.hasValue, device_type))
    graph.add((device_type, RDF.type, OWL.NamedIndividual))

    # define list of classes for intersection
    intersection_classes = [REC_CORE.Device, restriction_class]
    intersection_list = BNode()
    Collection(graph, intersection_list, intersection_classes)

    # define equivalency to intersection of classes
    equivalent_class = BNode()
    graph.add((equivalent_class, OWL.intersectionOf, intersection_list))

    graph.add((brick_class, OWL.equivalentClass, equivalent_class))

graph.serialize("Brick-REC-alignment.ttl")
