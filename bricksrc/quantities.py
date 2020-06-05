from brickschema.graph import Graph
from brickschema.inference import BrickInferenceSession
from rdflib import Literal, URIRef
from .namespaces import SKOS, OWL, RDFS, BRICK, QUDTQK, QUDTDV, QUDT, UNIT


g = Graph()
g.load_file("support/VOCAB_QUDT-QUANTITY-KINDS-ALL-v2.1.ttl")
g.load_file("support/VOCAB_QUDT-UNITS-ALL-v2.1.ttl")
g.g.bind("qudt", QUDT)
g.g.bind("qudtqk", QUDTQK)
sess = BrickInferenceSession()
g = sess.expand(g)


def get_units(brick_quantity):
    """
    Fetches the QUDT unit and symbol (as a Literal) from the QUDT ontology so
    in order to avoid having to pull the full QUDT ontology into Brick
    """
    res = g.query(
        f"""SELECT ?unit ?symbol WHERE {{
                    <{brick_quantity}> qudt:applicableUnit ?unit .
                    ?unit qudt:symbol ?symbol .
                    FILTER(isLiteral(?symbol))
                    }}"""
    )
    for r in res:
        yield r


"""
Each is a qudt:QuantityKind
"""
# TODO: define these on QUDTQK namespace
quantitykind_extensions = {
    "Concentration": {
        QUDT.applicableUnit: [UNIT.PPM],
        QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
        QUDT.plainTextDescription: Literal("The concentration ratio of some substance"),
        RDFS.isDefinedBy: URIRef(str(QUDTQK).strip("/")),
        RDFS.label: Literal("Concentration"),
        SKOS.broader: QUDTQK.Dimensionless,
    },
    "ThermalPower": {
        QUDT.applicableUnit: [UNIT.MilliW, UNIT.W, UNIT.KiloW, UNIT.MegaW],
        QUDT.hasDimensionVector: QUDTDV["A0E0L2I0M1H0T-3D0"],
        RDFS.isDefinedBy: URIRef(str(QUDTQK).strip("/")),
        RDFS.label: Literal("ThermalPower"),
    },
}


quantity_definitions = {
    "Air_Quality": {
        "subconcepts": {
            "CO2_Level": {OWL.sameAs: QUDTQK["Concentration"]},
            "PM10_Level": {OWL.sameAs: QUDTQK["Concentration"]},
            "PM25_Level": {OWL.sameAs: QUDTQK["Concentration"]},
            "TVOC_Level": {OWL.sameAs: QUDTQK["Concentration"]},
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
    "Mass": {
        OWL.sameAs: QUDTQK["Mass"],
        "subconcepts": {"Grains": {QUDT.applicableUnit: UNIT.GRAINS}},
    },
    "Power": {
        OWL.sameAs: QUDTQK["Power"],
        "subconcepts": {
            "Electric_Power": {
                OWL.sameAs: QUDTQK["ElectricPower"],
                "subconcepts": {
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
            "Thermal_Power": {OWL.sameAs: QUDTQK["ThermalPower"]},
        },
    },
    "Cloudage": {},
    "Current": {
        "subconcepts": {
            "Electric_Current": {
                OWL.sameAs: QUDTQK["ElectricCurrent"],
                "subconcepts": {
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
        "subconcepts": {
            "Voltage_Magnitude": {OWL.sameAs: QUDTQK["Voltage"]},
            "Voltage_Angle": {},
            "Voltage_Imbalance": {},
        },
    },
    "Daytime": {},
    "Dewpoint": {OWL.sameAs: QUDTQK["DewPointTemperature"]},
    "Direction": {"subconcepts": {"Wind_Direction": {}}},
    "Energy": {
        "subconcepts": {
            "Electric_Energy": {OWL.sameAs: QUDTQK["Energy"]},
            "Thermal_Energy": {OWL.sameAs: QUDTQK["ThermalEnergy"]},
        },
    },
    "Flow": {OWL.sameAs: QUDTQK["VolumeFlowRate"], "subconcepts": {"Flow_Loss": {}}},
    "Frequency": {
        OWL.sameAs: QUDTQK["Frequency"],
        "subconcepts": {"Alternating_Current_Frequency": {}},
    },
    "Humidity": {
        "subconcepts": {
            "Relative_Humidity": {OWL.sameAs: QUDTQK["RelativeHumidity"]},
            "Absolute_Humidity": {OWL.sameAs: QUDTQK["AbsoluteHumidity"]},
        }
    },
    "Illuminance": {OWL.sameAs: QUDTQK["Illuminance"]},
    "Irradiance": {
        OWL.sameAs: QUDTQK["Irradiance"],
        "subconcepts": {"Solar_Irradiance": {}},
    },
    "Level": {
        "subconcepts": {
            "CO2_Level": {},
            "PM10_Level": {},
            "PM25_Level": {},
            "TVOC_Level": {},
        },
    },
    "Luminance": {
        OWL.sameAs: QUDTQK["Luminance"],
        "subconcepts": {
            "Luminous_Flux": {OWL.sameAs: QUDTQK["LuminousFlux"]},
            "Luminous_Intensity": {OWL.sameAs: QUDTQK["LuminousIntensity"]},
        },
    },
    "Occupancy": {"subconcepts": {"Occupancy_Count": {}, "Occupancy_Percentage": {}}},
    "Position": {},
    "Power_Factor": {OWL.sameAs: QUDTQK["PowerFactor"]},
    "Precipitation": {},
    "Pressure": {
        OWL.sameAs: QUDTQK["Pressure"],
        "subconcepts": {
            "Atmospheric_Pressure": {OWL.sameAs: QUDTQK["AtmosphericPressure"]},
            "Dynamic_Pressure": {},
            "Static_Pressure": {OWL.sameAs: QUDTQK["StaticPressure"]},
            "Velocity_Pressure": {
                OWL.sameAs: [QUDTQK["DynamicPressure"], BRICK["Dynamic_Pressure"]],
            },
        },
    },
    "Radiance": {OWL.sameAs: QUDTQK["Radiance"], "subconcepts": {"Solar_Radiance": {}}},
    "Speed": {OWL.sameAs: QUDTQK["Speed"], "subconcepts": {"Wind_Speed": {}}},
    "Temperature": {
        OWL.sameAs: QUDTQK["ThermodynamicTemperature"],
        "subconcepts": {
            "Operative_Temperature": {},
            "Radiant_Temperature": {},
            "Dry_Bulb_Temperature": {},
            "Wet_Bulb_Temperature": {},
        },
    },
    "Time": {
        OWL.sameAs: QUDTQK["Time"],
        "subconcepts": {"Acceleration_Time": {}, "Deceleration_Time": {}},
    },
    "Torque": {OWL.sameAs: QUDTQK["Torque"]},
    "Weather_Condition": {},
}
