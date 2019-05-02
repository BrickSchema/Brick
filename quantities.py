from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.collection import Collection
from rdflib.extras.infixowl import Restriction

BRICK = Namespace("https://brickschema.org/schema/1.0.3/Brick#")
TAG = Namespace("https://brickschema.org/schema/1.0.3/BrickTag#")
BLDG = Namespace("https://brickschema.org/schema/1.0.3/ExampleBuilding#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
A = RDF.type

quantity_definitions = {
    "Quantity": {
        "subclasses": {
            "Air_Quality": {
                "subclasses": {
                    "CO2": {},
                    "PM10": {},
                    "PM25": {},
                    "TVOC": {},
                },
            },
            "Conductivity": {},
            "Capacity": {},
            "Enthalpy": {},
            "Grains": {},
            "Power": {
                "subclasses": {
                    "Electric_Power": {
                        "subclasses": {
                            "Apparent_Power": {},
                            "Active_Power": {
                                OWL.equivalentClass: "Real_Power",
                            },
                            "Reactive_Power": {},
                            "Complex_Power": {},
                        },
                    }
                },
            },
            "Cloudage": {},
            "Current": {
                "subclasses": {
                    "Electric_Current": {
                        "subclasses": {
                            "Current_Angle": {},
                            "Current_Magnitude": {},
                            "Current_Imbalance": {},
                            "Current_Total_Harmonic_Distortion": {},
                            "Alternating_Current_Frequency": {},
                        },
                    },
                },
            },
            "Voltage": {
                "subclasses": {
                    "Electric_Voltage": {
                        "subclasses": {
                            "Voltage_Magnitude": {},
                            "Voltage_Angle": {},
                            "Voltage_Imbalance": {},
                        },
                    },
                },
            },
            "Daytime": {},
            "Dewpoint": {},
            "Direction": {
                "subclasses": {
                    "Wind_Direction": {},
                },
            },
            "Energy": {
                "subclasses": {
                    "Electric_Energy": {},
                    "Thermal_Energy": {},
                },
            },
            "Flow": {},
            "Frequency": {
                "subclasses": {
                    "Alternating_Current_Frequency": {},
                },
            },
            "Humidity": {},
            "Illuminance": {},
            "Irradiance": {
                "subclasses": {
                    "Solar_Irradiance": {},
                },
            },
            "Level": {},
            "Luminance": {
                "subclasses": {
                    "Luminous_Flux": {},
                    "Luminous_Intensity": {},
                },
            },
            "Power_Factor": {},
            "Precipitation": {},
            "Pressure": {
                "subclasses": {
                    "Atmospheric_Pressure": {},
                },
            },
            "Speed": {
                "subclasses": {
                    "Wind_Speed": {},
                },
            },
            "Temperature": {
                "subclasses": {
                    "Operative_Temperature": {},
                    "Radiant_Temperature": {},
                    "Wet_Bulb_Temperature": {},
                },
            },
            "Weather_Condition": {
            },
        },
    },
}
