from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.collection import Collection
from rdflib.extras.infixowl import Restriction

from namespaces import *


quantity_definitions = {
    "Quantity": {
        "subclasses": {
            "Air_Quality": {
                "subclasses": {
                    "CO2_Level": {},
                    "PM10_Level": {},
                    "PM25_Level": {},
                    "TVOC_Level": {},
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
                    },
                    "Thermal_Power": {}
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
            "Level": {
                "subclasses": {
                    "CO2_Level": {},
                    "PM10_Level": {},
                    "PM25_Level": {},
                    "TVOC_Level": {},
                },
            },
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
                    "Static_Pressure": {},
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
                    "Dry_Bulb_Temperature": {},
                    "Wet_Bulb_Temperature": {},
                },
            },
            "Weather_Condition": {
            },
        },
    },
}
