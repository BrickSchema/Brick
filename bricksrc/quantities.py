import brickschema
from rdflib import Literal
from .namespaces import SKOS, OWL, RDFS, BRICK, QUDTQK, QUDT


quantity_definitions = {
    "Air_Quality": {
        "subclasses": {
            "CO2_Level": {},
            "PM10_Level": {},
            "PM25_Level": {},
            "TVOC_Level": {},
        },
    },
    "Angle": {BRICK.associatedQuantityKind: QUDTQK["Angle"]},
    "Conductivity": {BRICK.associatedQuantityKind: QUDTQK["Conductivity"]},
    "Capacity": {BRICK.associatedQuantityKind: QUDTQK["Capacity"]},
    "Enthalpy": {
        SKOS.definition: Literal(
            "(also known as heat content), thermodynamic quantity equal to the sum of the internal energy of a system plus the product of the pressure volume work done on the system. H = E + pv, where H = enthalpy or total heat content, E = internal energy of the system, p = pressure, and v = volume. (Compare to [[specific enthalpy]].)"
        ),
        BRICK.associatedQuantityKind: QUDTQK["Enthalpy"],
    },
    "Grains": {},
    "Power": {
        BRICK.associatedQuantityKind: QUDTQK["Power"],
        "subclasses": {
            "Electric_Power": {
                BRICK.associatedQuantityKind: QUDTQK["ElectricPower"],
                "subclasses": {
                    "Apparent_Power": {
                        BRICK.associatedQuantityKind: QUDTQK["ApparentPower"]
                    },
                    "Active_Power": {
                        OWL.equivalentClass: BRICK["Real_Power"],
                        BRICK.associatedQuantityKind: QUDTQK["ActivePower"],
                    },
                    "Real_Power": {},
                    "Reactive_Power": {
                        BRICK.associatedQuantityKind: QUDTQK["ReactivePower"]
                    },
                    "Complex_Power": {
                        BRICK.associatedQuantityKind: QUDTQK["ComplexPower"]
                    },
                },
            },
            "Peak_Power": {
                SKOS.definition: Literal(
                    "Tracks the highest (peak) observed power in some interval"
                )
            },
            "Thermal_Power": {},
        },
    },
    "Cloudage": {},
    "Current": {
        "subclasses": {
            "Electric_Current": {
                BRICK.associatedQuantityKind: QUDTQK["ElectricCurrent"],
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
        BRICK.associatedQuantityKind: QUDTQK["Voltage"],
        "subclasses": {
            "Voltage_Magnitude": {},
            "Voltage_Angle": {},
            "Voltage_Imbalance": {},
        },
    },
    "Daytime": {},
    "Dewpoint": {BRICK.associatedQuantityKind: QUDTQK["DewPointTemperature"]},
    "Direction": {"subclasses": {"Wind_Direction": {}}},
    "Energy": {
        "subclasses": {
            "Electric_Energy": {BRICK.associatedQuantityKind: QUDTQK["Energy"]},
            "Thermal_Energy": {BRICK.associatedQuantityKind: QUDTQK["ThermalEnergy"]},
        },
    },
    "Flow": {
        BRICK.associatedQuantityKind: QUDTQK["VolumeFlowRate"],
        "subclasses": {"Flow_Loss": {}},
    },
    "Frequency": {
        BRICK.associatedQuantityKind: QUDTQK["Frequency"],
        "subclasses": {"Alternating_Current_Frequency": {}},
    },
    "Humidity": {
        "subclasses": {
            "Relative_Humidity": {
                BRICK.associatedQuantityKind: QUDTQK["RelativeHumidity"]
            },
            "Absolute_Humidity": {
                BRICK.associatedQuantityKind: QUDTQK["AbsoluteHumidity"]
            },
        }
    },
    "Illuminance": {BRICK.associatedQuantityKind: QUDTQK["Illuminance"]},
    "Irradiance": {
        BRICK.associatedQuantityKind: QUDTQK["Irradiance"],
        "subclasses": {"Solar_Irradiance": {}},
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
        BRICK.associatedQuantityKind: QUDTQK["Luminance"],
        "subclasses": {
            "Luminous_Flux": {BRICK.associatedQuantityKind: QUDTQK["LuminousFlux"]},
            "Luminous_Intensity": {
                BRICK.associatedQuantityKind: QUDTQK["LuminousIntensity"]
            },
        },
    },
    "Occupancy": {"subclasses": {"Occupancy_Count": {}, "Occupancy_Percentage": {}}},
    "Position": {},
    "Power_Factor": {BRICK.associatedQuantityKind: QUDTQK["PowerFactor"]},
    "Precipitation": {},
    "Pressure": {
        BRICK.associatedQuantityKind: QUDTQK["Pressure"],
        "subclasses": {
            "Atmospheric_Pressure": {
                BRICK.associatedQuantityKind: QUDTQK["AtmosphericPressure"]
            },
            "Dynamic_Pressure": {},
            "Static_Pressure": {BRICK.associatedQuantityKind: QUDTQK["StaticPressure"]},
            "Velocity_Pressure": {
                OWL.equivalentClass: BRICK["Dynamic_Pressure"],
                BRICK.associatedQuantityKind: QUDTQK["DynamicPressure"],
            },
        },
    },
    "Radiance": {
        BRICK.associatedQuantityKind: QUDTQK["Radiance"],
        "subclasses": {"Solar_Radiance": {}},
    },
    "Speed": {
        BRICK.associatedQuantityKind: QUDTQK["Speed"],
        "subclasses": {"Wind_Speed": {}},
    },
    "Temperature": {
        BRICK.associatedQuantityKind: QUDTQK["Temperature"],
        "subclasses": {
            "Operative_Temperature": {},
            "Radiant_Temperature": {},
            "Dry_Bulb_Temperature": {},
            "Wet_Bulb_Temperature": {},
        },
    },
    "Time": {
        BRICK.associatedQuantityKind: QUDTQK["Time"],
        "subclasses": {"Acceleration_Time": {}, "Deceleration_Time": {}},
    },
    "Torque": {BRICK.associatedQuantityKind: QUDTQK["Torque"]},
    "Weather_Condition": {},
}


def associate_units(outputG):
    g = brickschema.graph.Graph()
    g.g.bind("qudt", QUDT)
    for triple in outputG:
        g.add(triple)
    g.load_file("support/VOCAB_QUDT-QUANTITY-KINDS-ALL-v2.1.ttl")
    g = brickschema.inference.OWLRLInferenceSession(load_brick=False).expand(g)
    unit_map = g.query(
        "SELECT ?quant ?unit WHERE {\
        ?quant a brick:Quantity .\
        ?quant brick:associatedQuantityKind/qudt:applicableUnit ?unit . }"
    )
    for brickquant, unit in unit_map:
        outputG.add((brickquant, QUDT.applicableUnit, unit))
