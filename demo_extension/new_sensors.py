import rdflib
from bricksrc.namespaces import BRICK, SKOS, SH, XSD, RDFS

DEMO = rdflib.Namespace("urn:demo_extension#")

class_parent = BRICK.Equipment
classes = {
    DEMO["Sensor_Platform"]: {},
    DEMO["PurpleAir_Weather_Station"]: {
        "parents": [BRICK.Weather_Station],
    },
}


entity_properties = {
    DEMO.manufacturer: {
        SKOS.definition: rdflib.Literal("the manufacturer"),
        SH.datatype: XSD.string,
        RDFS.label: rdflib.Literal("manufacturer"),
        "property_of": BRICK.Equipment,
    }
}
