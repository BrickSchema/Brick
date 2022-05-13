import brickschema


def get_graph(filename):
    g = brickschema.Graph()
    # load local Brick file
    g.load_file("../../Brick.ttl")
    g.load_file(filename)
    g.expand("shacl")
    return g


FILES = [
    "main-and-submeter.ttl",
    "multiple-submeters.ttl",
    "single-meter.ttl",
]

"""
Gets all meters with an electrical power sensor which measure
max power and returns their uuid
"""
all_meter_query = """SELECT DISTINCT * WHERE {
    ?meter rdf:type/rdfs:subClassOf* brick:Meter .
    ?meter brick:hasPoint ?point .
    ?point rdf:type brick:Electric_Power_Sensor ;
           brick:aggregate [ brick:aggregationFunction "max" ] ;
           brick:timeseries [ brick:hasTimeseriesId ?uuid ] .
}
"""

for file in FILES:
    g = get_graph(file)
    g.serialize("/tmp/test.ttl", format="turtle")
    print(f"All Meter Query for {file}")
    for row in g.query(all_meter_query):
        print(row)
    print("-" * 80)

"""
Gets the building meter and its peak (max) power sensor
"""
building_meter_query = """SELECT DISTINCT * WHERE {
    ?meter rdf:type/rdfs:subClassOf* brick:Meter .
    ?meter brick:meters/rdf:type/rdfs:subClassOf* brick:Building .
    ?meter brick:hasPoint ?point .
    ?point rdf:type brick:Electric_Power_Sensor ;
           brick:aggregate [ brick:aggregationFunction "max" ] ;
           brick:timeseries [ brick:hasTimeseriesId ?uuid ] .
}
"""
for file in FILES:
    g = get_graph(file)
    g.serialize("/tmp/test.ttl", format="turtle")
    print(f"Building Meter Query for {file}")
    for row in g.query(building_meter_query):
        print(row)
    print("-" * 80)

"""
Gets all meters that aren't submeters; add these to get total of all metered consumption
"""
total_meter_query = """SELECT DISTINCT * WHERE {
    ?meter rdf:type/rdfs:subClassOf* brick:Meter .
    ?meter brick:hasPoint ?point .
    ?point rdf:type brick:Electric_Power_Sensor ;
           brick:aggregate [ brick:aggregationFunction "max" ] ;
           brick:timeseries [ brick:hasTimeseriesId ?uuid ] .
    FILTER NOT EXISTS { ?meter brick:isSubMeterOf ?parent }
}
"""
for file in FILES:
    g = get_graph(file)
    g.serialize("/tmp/test.ttl", format="turtle")
    print(f"Total Meter Query for {file}")
    for row in g.query(total_meter_query):
        print(row)
    print("-" * 80)
