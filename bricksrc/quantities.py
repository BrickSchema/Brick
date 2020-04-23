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
    "Angle": {OWL.equivalentClass: QUDTQK["Angle"]},
    "Conductivity": {OWL.equivalentClass: QUDTQK["Conductivity"]},
    "Capacity": {OWL.equivalentClass: QUDTQK["Capacity"]},
    "Enthalpy": {
        SKOS.definition: Literal(
            "(also known as heat content), thermodynamic quantity equal to the sum of the internal energy of a system plus the product of the pressure volume work done on the system. H = E + pv, where H = enthalpy or total heat content, E = internal energy of the system, p = pressure, and v = volume. (Compare to [[specific enthalpy]].)"
        ),
        OWL.equivalentClass: QUDTQK["Enthalpy"],
    },
    "Grains": {},
    "Power": {
        OWL.equivalentClass: QUDTQK["Power"],
        "subclasses": {
            "Electric_Power": {
                OWL.equivalentClass: QUDTQK["ElectricPower"],
                "subclasses": {
                    "Apparent_Power": {OWL.equivalentClass: QUDTQK["ApparentPower"]},
                    "Active_Power": {
                        OWL.equivalentClass: [
                            QUDTQK["ActivePower"],
                            BRICK["Real_Power"],
                        ],
                    },
                    "Real_Power": {},
                    "Reactive_Power": {OWL.equivalentClass: QUDTQK["ReactivePower"]},
                    "Complex_Power": {OWL.equivalentClass: QUDTQK["ComplexPower"]},
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
                OWL.equivalentClass: QUDTQK["ElectricCurrent"],
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
        OWL.equivalentClass: QUDTQK["Voltage"],
        "subclasses": {
            "Voltage_Magnitude": {},
            "Voltage_Angle": {},
            "Voltage_Imbalance": {},
        },
    },
    "Daytime": {},
    "Dewpoint": {OWL.equivalentClass: QUDTQK["DewPointTemperature"]},
    "Direction": {"subclasses": {"Wind_Direction": {}}},
    "Energy": {
        "subclasses": {
            "Electric_Energy": {OWL.equivalentClass: QUDTQK["Energy"]},
            "Thermal_Energy": {OWL.equivalentClass: QUDTQK["ThermalEnergy"]},
        },
    },
    "Flow": {
        OWL.equivalentClass: QUDTQK["VolumeFlowRate"],
        "subclasses": {"Flow_Loss": {}},
    },
    "Frequency": {
        OWL.equivalentClass: QUDTQK["Frequency"],
        "subclasses": {"Alternating_Current_Frequency": {}},
    },
    "Humidity": {
        "subclasses": {
            "Relative_Humidity": {OWL.equivalentClass: QUDTQK["RelativeHumidity"]},
            "Absolute_Humidity": {OWL.equivalentClass: QUDTQK["AbsoluteHumidity"]},
        }
    },
    "Illuminance": {OWL.equivalentClass: QUDTQK["Illuminance"]},
    "Irradiance": {
        OWL.equivalentClass: QUDTQK["Irradiance"],
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
        OWL.equivalentClass: QUDTQK["Luminance"],
        "subclasses": {
            "Luminous_Flux": {OWL.equivalentClass: QUDTQK["LuminousFlux"]},
            "Luminous_Intensity": {OWL.equivalentClass: QUDTQK["LuminousIntensity"]},
        },
    },
    "Occupancy": {"subclasses": {"Occupancy_Count": {}, "Occupancy_Percentage": {}}},
    "Position": {},
    "Power_Factor": {OWL.equivalentClass: QUDTQK["PowerFactor"]},
    "Precipitation": {},
    "Pressure": {
        OWL.equivalentClass: QUDTQK["Pressure"],
        "subclasses": {
            "Atmospheric_Pressure": {
                OWL.equivalentClass: QUDTQK["AtmosphericPressure"]
            },
            "Dynamic_Pressure": {},
            "Static_Pressure": {OWL.equivalentClass: QUDTQK["StaticPressure"]},
            "Velocity_Pressure": {
                OWL.equivalentClass: [
                    QUDTQK["DynamicPressure"],
                    BRICK["Dynamic_Pressure"],
                ],
            },
        },
    },
    "Radiance": {
        OWL.equivalentClass: QUDTQK["Radiance"],
        "subclasses": {"Solar_Radiance": {}},
    },
    "Speed": {OWL.equivalentClass: QUDTQK["Speed"], "subclasses": {"Wind_Speed": {}}},
    "Temperature": {
        OWL.equivalentClass: QUDTQK["Temperature"],
        "subclasses": {
            "Operative_Temperature": {},
            "Radiant_Temperature": {},
            "Dry_Bulb_Temperature": {},
            "Wet_Bulb_Temperature": {},
        },
    },
    "Time": {
        OWL.equivalentClass: QUDTQK["Time"],
        "subclasses": {"Acceleration_Time": {}, "Deceleration_Time": {}},
    },
    "Torque": {OWL.equivalentClass: QUDTQK["Torque"]},
    "Weather_Condition": {},
}


def associate_units(outputG):
    g = brickschema.graph.Graph()
    g.g.bind("qudt", QUDT)
    for triple in outputG:
        g.add(triple)
    g.load_file("support/VOCAB_QUDT-QUANTITY-KINDS-ALL-v2.1.ttl")
    unit_map = g.query(
        "SELECT ?quant ?unit WHERE {\
        ?quant a brick:Quantity .\
        ?quant owl:equivalentClass/qudt:applicableUnit ?unit . }"
    )
    for brickquant, unit in unit_map:
        outputG.add((brickquant, QUDT.applicableUnit, unit))
