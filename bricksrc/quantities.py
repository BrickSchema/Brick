from brickschema.graph import Graph
from brickschema.inference import BrickInferenceSession
from rdflib import Literal
from .namespaces import SKOS, OWL, RDFS, BRICK, QUDTQK, QUDT


g = Graph()
g.load_file("support/VOCAB_QUDT-QUANTITY-KINDS-ALL-v2.1.ttl")
g.load_file("support/VOCAB_QUDT-UNITS-ALL-v2.1.ttl")
g.g.bind("qudt", QUDT)
g.g.bind("qudtqk", QUDTQK)
sess = BrickInferenceSession()
g = sess.expand(g)


def get_units(brick_quantity):
    res = g.query(
        f"""SELECT ?unit ?symbol WHERE {{
                    <{brick_quantity}> qudt:applicableUnit ?unit .
                    ?unit qudt:symbol ?symbol .
                    FILTER(isLiteral(?symbol))
                    }}"""
    )
    for r in res:
        yield r


quantity_definitions = {
    "Air_Quality": {
        "subclasses": {
            "CO2_Level": {},
            "PM10_Level": {},
            "PM25_Level": {},
            "TVOC_Level": {},
        },
    },
    "Angle": {OWL.sameAs: QUDTQK["Angle"]},
    "Conductivity": {OWL.sameAs: QUDTQK["Conductivity"]},
    "Capacity": {OWL.sameAs: QUDTQK["Capacity"]},
    "Enthalpy": {
        SKOS.definition: Literal(
            "(also known as heat content), thermodynamic quantity equal to the sum of the internal energy of a system plus the product of the pressure volume work done on the system. H = E + pv, where H = enthalpy or total heat content, E = internal energy of the system, p = pressure, and v = volume. (Compare to [[specific enthalpy]].)"
        ),
        OWL.sameAs: QUDTQK["Enthalpy"],
    },
    "Grains": {},
    "Power": {
        OWL.sameAs: QUDTQK["Power"],
        "subclasses": {
            "Electric_Power": {
                OWL.sameAs: QUDTQK["ElectricPower"],
                "subclasses": {
                    "Apparent_Power": {OWL.sameAs: QUDTQK["ApparentPower"]},
                    "Active_Power": {
                        OWL.sameAs: [QUDTQK["ActivePower"], BRICK["Real_Power"]],
                    },
                    "Real_Power": {},
                    "Reactive_Power": {OWL.sameAs: QUDTQK["ReactivePower"]},
                    "Complex_Power": {OWL.sameAs: QUDTQK["ComplexPower"]},
                },
            },
            "Peak_Power": {
                OWL.sameAs: QUDTQK["ElectricPower"],
                SKOS.definition: Literal(
                    "Tracks the highest (peak) observed power in some interval"
                ),
            },
            "Thermal_Power": {},
        },
    },
    "Cloudage": {},
    "Current": {
        "subclasses": {
            "Electric_Current": {
                OWL.sameAs: QUDTQK["ElectricCurrent"],
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
            "Voltage_Magnitude": {OWL.sameAs: QUDTQK["Voltage"]},
            "Voltage_Angle": {},
            "Voltage_Imbalance": {},
        },
    },
    "Daytime": {},
    "Dewpoint": {OWL.sameAs: QUDTQK["DewPointTemperature"]},
    "Direction": {"subclasses": {"Wind_Direction": {}}},
    "Energy": {
        "subclasses": {
            "Electric_Energy": {OWL.sameAs: QUDTQK["Energy"]},
            "Thermal_Energy": {OWL.sameAs: QUDTQK["ThermalEnergy"]},
        },
    },
    "Flow": {OWL.sameAs: QUDTQK["VolumeFlowRate"], "subclasses": {"Flow_Loss": {}}},
    "Frequency": {
        OWL.sameAs: QUDTQK["Frequency"],
        "subclasses": {"Alternating_Current_Frequency": {}},
    },
    "Humidity": {
        "subclasses": {
            "Relative_Humidity": {OWL.sameAs: QUDTQK["RelativeHumidity"]},
            "Absolute_Humidity": {OWL.sameAs: QUDTQK["AbsoluteHumidity"]},
        }
    },
    "Illuminance": {OWL.sameAs: QUDTQK["Illuminance"]},
    "Irradiance": {
        OWL.sameAs: QUDTQK["Irradiance"],
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
        OWL.sameAs: QUDTQK["Luminance"],
        "subclasses": {
            "Luminous_Flux": {OWL.sameAs: QUDTQK["LuminousFlux"]},
            "Luminous_Intensity": {OWL.sameAs: QUDTQK["LuminousIntensity"]},
        },
    },
    "Occupancy": {"subclasses": {"Occupancy_Count": {}, "Occupancy_Percentage": {}}},
    "Position": {},
    "Power_Factor": {OWL.sameAs: QUDTQK["PowerFactor"]},
    "Precipitation": {},
    "Pressure": {
        OWL.sameAs: QUDTQK["Pressure"],
        "subclasses": {
            "Atmospheric_Pressure": {OWL.sameAs: QUDTQK["AtmosphericPressure"]},
            "Dynamic_Pressure": {},
            "Static_Pressure": {OWL.sameAs: QUDTQK["StaticPressure"]},
            "Velocity_Pressure": {
                OWL.sameAs: [QUDTQK["DynamicPressure"], BRICK["Dynamic_Pressure"]],
            },
        },
    },
    "Radiance": {OWL.sameAs: QUDTQK["Radiance"], "subclasses": {"Solar_Radiance": {}}},
    "Speed": {OWL.sameAs: QUDTQK["Speed"], "subclasses": {"Wind_Speed": {}}},
    "Temperature": {
        OWL.sameAs: QUDTQK["ThermodynamicTemperature"],
        "subclasses": {
            "Operative_Temperature": {},
            "Radiant_Temperature": {},
            "Dry_Bulb_Temperature": {},
            "Wet_Bulb_Temperature": {},
        },
    },
    "Time": {
        OWL.sameAs: QUDTQK["Time"],
        "subclasses": {"Acceleration_Time": {}, "Deceleration_Time": {}},
    },
    "Torque": {OWL.sameAs: QUDTQK["Torque"]},
    "Weather_Condition": {},
}
