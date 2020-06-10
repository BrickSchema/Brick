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
quantity_definitions = {
    "Air_Quality": {
        "subconcepts": {
            "CO2_Level": {
                QUDT.applicableUnit: [UNIT.PPM],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                QUDT.plainTextDescription: Literal(
                    "The concentration ratio of some substance"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("Concentration"),
                SKOS.broader: QUDTQK.Dimensionless,
            },
            "PM10_Level": {
                QUDT.applicableUnit: [UNIT.PPM],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                QUDT.plainTextDescription: Literal(
                    "The concentration ratio of some substance"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("Concentration"),
                SKOS.broader: QUDTQK.Dimensionless,
            },
            "PM25_Level": {
                QUDT.applicableUnit: [UNIT.PPM],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                QUDT.plainTextDescription: Literal(
                    "The concentration ratio of some substance"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("Concentration"),
                SKOS.broader: QUDTQK.Dimensionless,
            },
            "TVOC_Level": {
                QUDT.applicableUnit: [UNIT.PPM],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                QUDT.plainTextDescription: Literal(
                    "The concentration ratio of some substance"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("Concentration"),
                SKOS.broader: QUDTQK.Dimensionless,
            },
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
    "Phasor": {
        "subconcepts": {
            "PhasorAngle": {
                QUDT.applicableUnit: [
                    UNIT.ARCMIN,
                    UNIT.ARCSEC,
                    UNIT.DEG,
                    UNIT.GON,
                    UNIT.GRAD,
                    UNIT.MIL,
                    UNIT.RAD,
                    UNIT.MicroRAD,
                    UNIT.MilliRAD,
                    UNIT.MilliARCSEC,
                    UNIT.REV,
                ],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                QUDT.plainTextDescription: Literal("Angle component of a phasor"),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("PhasorAngle"),
                SKOS.broader: QUDTQK.PlaneAngle,
            },
            "PhasorMagnitude": {
                QUDT.applicableUnit: [
                    UNIT.ARCMIN,
                    UNIT.ARCSEC,
                    UNIT.DEG,
                    UNIT.GON,
                    UNIT.GRAD,
                    UNIT.MIL,
                    UNIT.RAD,
                    UNIT.MicroRAD,
                    UNIT.MilliRAD,
                    UNIT.MilliARCSEC,
                    UNIT.REV,
                ],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                QUDT.plainTextDescription: Literal("Magnitude component of a phasor"),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("PhasorMagnitude"),
                # TODO: finish
            },
        },
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
            "Thermal_Power": {
                QUDT.applicableUnit: [UNIT.MilliW, UNIT.W, UNIT.KiloW, UNIT.MegaW],
                QUDT.hasDimensionVector: QUDTDV["A0E0L2I0M1H0T-3D0"],
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("ThermalPower"),
                SKOS.broader: QUDTQK.Power,
            },
        },
    },
    "Cloudage": {
        QUDT.applicableUnit: [UNIT.Okta],
        QUDT.plainTextDescription: Literal(
            "The fraction of the sky obscured by clouds when observed from a particular location"
        ),
        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
        RDFS.label: Literal("Cloudage"),
        SKOS.broader: QUDTQK.Dimensionless,
    },
    "Current": {
        "subconcepts": {
            "Electric_Current": {
                OWL.sameAs: QUDTQK["ElectricCurrent"],
                "subconcepts": {
                    "Current_Angle": {
                        SKOS.definition: Literal(
                            "The angle of the phasor representing a measurement of electric current"
                        ),
                        QUDT.applicableUnit: [
                            UNIT.ARCMIN,
                            UNIT.ARCSEC,
                            UNIT.DEG,
                            UNIT.GON,
                            UNIT.GRAD,
                            UNIT.MIL,
                            UNIT.RAD,
                            UNIT.MicroRAD,
                            UNIT.MilliRAD,
                            UNIT.MilliARCSEC,
                            UNIT.REV,
                        ],
                        QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                        QUDT.plainTextDescription: Literal("Angle of current phasor"),
                        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                        RDFS.label: Literal("CurrentAngle"),
                        SKOS.broader: BRICK.PhasorAngle,
                    },
                    "Current_Magnitude": {
                        SKOS.definition: Literal(
                            "The magnitude of the phasor representing a measurement of electric current"
                        ),
                        QUDT.applicableUnit: [
                            UNIT.A,
                            UNIT.MilliA,
                            UNIT.MicroA,
                            UNIT.KiloA,
                        ],
                        QUDT.plainTextDescription: Literal(
                            "Magnitude of current phasor"
                        ),
                        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                        RDFS.label: Literal("CurrentMagnitude"),
                        SKOS.broader: BRICK.PhasorMagnitude,
                    },
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
            "Voltage_Angle": {
                SKOS.definition: Literal(
                    "The angle of the phasor representing a measurement of electric voltage"
                ),
                QUDT.applicableUnit: [
                    UNIT.ARCMIN,
                    UNIT.ARCSEC,
                    UNIT.DEG,
                    UNIT.GON,
                    UNIT.GRAD,
                    UNIT.MIL,
                    UNIT.RAD,
                    UNIT.MicroRAD,
                    UNIT.MilliRAD,
                    UNIT.MilliARCSEC,
                    UNIT.REV,
                ],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                QUDT.plainTextDescription: Literal("Angle of voltage phasor"),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("VoltageAngle"),
                SKOS.broader: BRICK.PhasorAngle,
                # TODO: units?
            },
            "Voltage_Imbalance": {},
        },
    },
    "Daytime": {},
    "Dewpoint": {OWL.sameAs: QUDTQK["DewPointTemperature"]},
    "Direction": {
        "subconcepts": {"Wind_Direction": {OWL.sameAs: QUDTQK["PlaneAngle"]}}
    },
    "Energy": {
        "subconcepts": {
            "Electric_Energy": {OWL.sameAs: QUDTQK["Energy"]},
            "Thermal_Energy": {OWL.sameAs: QUDTQK["ThermalEnergy"]},
        },
    },
    # define hydralic flow loss? https://en.wikipedia.org/wiki/Friction_loss
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
        QUDT.applicableUnit: [
            UNIT["W-PER-M2"],
            UNIT["W-PER-IN2"],
            UNIT["W-PER-FT2"],
            UNIT["W-PER-CeniM2"],
        ],
        QUDT.plainTextDescription: Literal(
            "The power per unit area of electromagnetic radiation incident on a surface"
        ),
        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
        RDFS.label: Literal("Irradiance"),
        SKOS.broader: QUDTQK.PowerPerArea,
        "subconcepts": {
            "Solar_Irradiance": {
                QUDT.applicableUnit: [
                    UNIT["W-PER-M2"],
                    UNIT["W-PER-IN2"],
                    UNIT["W-PER-FT2"],
                    UNIT["W-PER-CeniM2"],
                ],
                QUDT.plainTextDescription: Literal(
                    "The power per unit area of solar electromagnetic radiation incident on a surface"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("SolarIrradiance"),
                SKOS.broader: BRICK.Irradiance,
            }
        },
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
    "Position": {
        QUDT.applicableUnit: [UNIT["PERCENT"]],
        QUDT.plainTextDescription: Literal("The fraction of the full range of motion"),
        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
        RDFS.label: Literal("Position"),
        SKOS.broader: QUDTQK.DimensionlessRatio,
    },
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
