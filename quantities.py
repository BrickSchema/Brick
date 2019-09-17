from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.collection import Collection
from rdflib.extras.infixowl import Restriction

from namespaces import *


quantity_definitions = {
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
    "Enthalpy": {
        "tags": [TAG.Enthalpy],
        SKOS.definition: Literal("(also known as heat content), thermodynamic quantity equal to the sum of the internal energy of a system plus the product of the pressure volume work done on the system. H = E + pv, where H = enthalpy or total heat content, E = internal energy of the system, p = pressure, and v = volume. (Compare to [[specific enthalpy]].)"),
    },
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
            "Peak_Power": {
                SKOS.definition: Literal("Tracks the highest (peak) observed power in some interval"),
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
    "Humidity": {
        "subclasses": {
            "Relative_Humidity": {},
        },
    },
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
        "tags": [TAG.Luminance],
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
}
