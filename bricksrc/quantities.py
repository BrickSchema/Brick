from brickschema.graph import Graph
from rdflib import Literal, URIRef
from .namespaces import SKOS, OWL, RDFS, BRICK, QUDTQK, QUDTDV, QUDT, UNIT


g = Graph()
g.load_file("support/VOCAB_QUDT-QUANTITY-KINDS-ALL-v2.1.ttl")
g.load_file("support/VOCAB_QUDT-UNITS-ALL-v2.1.ttl")
g.bind("qudt", QUDT)
g.bind("qudtqk", QUDTQK)
g.expand(profile="brick")


def get_units(qudt_quantity):
    """
    Fetches the QUDT unit and symbol (as a Literal) from the QUDT ontology so
    in order to avoid having to pull the full QUDT ontology into Brick
    """
    return g.query(
        f"""SELECT ?unit ?symbol ?label WHERE {{
                    <{qudt_quantity}> qudt:applicableUnit ?unit .
                    OPTIONAL {{
                        ?unit qudt:symbol ?symbol .
                        FILTER(isLiteral(?symbol))
                    }} .
                    OPTIONAL {{
                        ?unit rdfs:label ?label .
                    }}
                    }}"""
    )


"""
Each is a qudt:QuantityKind
"""
quantity_definitions = {
    "Air_Quality": {
        SKOS.narrower: {
            "Ammonia_Concentration": {
                QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                SKOS.definition: Literal("The concentration of Ammonia in a medium"),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("AmmoniaConcentration"),
                SKOS.broader: QUDTQK.DimensionlessRatio,
            },
            "CO_Concentration": {
                QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                SKOS.definition: Literal(
                    "The concentration of carbon monoxide in a medium"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("COConcentration"),
                SKOS.broader: QUDTQK.DimensionlessRatio,
                SKOS.narrower: {
                    "Differential_CO_Concentration": {
                        QUDT.isDeltaQuantity: Literal(True),
                        QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB],
                        SKOS.definition: Literal(
                            "The difference in carbon monoxide concentration between two areas"
                        ),
                        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                        RDFS.label: Literal("ΔCOConcentration"),
                    },
                },
            },
            "CO2_Concentration": {
                QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                SKOS.definition: Literal(
                    "The concentration of carbon dioxide in a medium"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("CO2Concentration"),
                SKOS.broader: QUDTQK.DimensionlessRatio,
                SKOS.narrower: {
                    "Differential_CO2_Concentration": {
                        QUDT.isDeltaQuantity: Literal(True),
                        QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB],
                        SKOS.definition: Literal(
                            "The difference in carbon dioxide concentration between two areas"
                        ),
                        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                        RDFS.label: Literal("ΔCO2Concentration"),
                    },
                },
            },
            "Formaldehyde_Concentration": {
                QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                SKOS.definition: Literal(
                    "The concentration of formaldehyde in a medium"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("FormaldehydeConcentration"),
                SKOS.broader: QUDTQK.DimensionlessRatio,
            },
            "Ozone_Concentration": {
                QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                SKOS.definition: Literal("The concentration of ozone in a medium"),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("OzoneConcentration"),
                SKOS.broader: QUDTQK.DimensionlessRatio,
            },
            "Methane_Concentration": {
                QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                SKOS.definition: Literal("The concentration of methane in a medium"),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("MethaneConcentration"),
                SKOS.broader: QUDTQK.DimensionlessRatio,
            },
            "NO2_Concentration": {
                QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                SKOS.definition: Literal(
                    "The concentration of nitrogen dioxide in a medium"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("PM10Concentration"),
            },
            "PM10_Concentration": {
                QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB, UNIT["MicroGM-PER-M3"]],
                SKOS.definition: Literal(
                    "The concentration of particulates with diameter of 10 microns or less in air"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("PM10Concentration"),
            },
            "PM2.5_Concentration": {
                QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB, UNIT["MicroGM-PER-M3"]],
                SKOS.definition: Literal(
                    "The concentration of particulates with diameter of 2.5 microns or less in air"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("PM2.5Concentration"),
            },
            "PM1_Concentration": {
                QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB, UNIT["MicroGM-PER-M3"]],
                SKOS.definition: Literal(
                    "The concentration of particulates with diameter of 1 microns or less in air"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("PM1Concentration"),
            },
            "Radioactivity_Concentration": {
                SKOS.narrower: {
                    "Radon_Concentration": {
                        QUDT.applicableUnit: [UNIT["BQ-PER-M3"]],
                        QUDT.hasDimensionVector: QUDTDV["A0E0L-3I0M0H0T-1D0"],
                        SKOS.definition: Literal(
                            "The concentration of radioactivity due to Radon in a medium"
                        ),
                        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                        RDFS.label: Literal("RadonConcentration"),
                        SKOS.broader: QUDTQK.ActivityConcentration,
                    },
                },
            },
            "TVOC_Concentration": {
                QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB, UNIT["MicroGM-PER-M3"]],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                SKOS.definition: Literal(
                    "The concentration of total volatile organic compounds in air"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("TVOCConcentration"),
                SKOS.broader: QUDTQK.DimensionlessRatio,
            },
        },
    },
    "Angle": {BRICK.hasQUDTReference: QUDTQK["Angle"]},
    "Conductivity": {BRICK.hasQUDTReference: QUDTQK["Conductivity"]},
    "Capacity": {BRICK.hasQUDTReference: QUDTQK["Capacity"]},
    "Enthalpy": {
        SKOS.definition: Literal(
            "(also known as heat content), thermodynamic quantity equal to the sum of the internal energy of a system plus the product of the pressure volume work done on the system. H = E + pv, where H = enthalpy or total heat content, E = internal energy of the system, p = pressure, and v = volume. (Compare to [[specific enthalpy]].)"
        ),
        BRICK.hasQUDTReference: QUDTQK["Enthalpy"],
    },
    "Mass": {
        BRICK.hasQUDTReference: QUDTQK["Mass"],
        SKOS.narrower: {
            "GrainsOfMoisture": {
                QUDT.applicableUnit: UNIT.GRAIN,
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M1H0T0D0"],
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("GrainsOfMoisture"),
                SKOS.definition: Literal(
                    "Mass of moisture per pround of air, measured in grains of water"
                ),
                SKOS.broader: QUDTQK.Mass,
            }
        },
    },
    "Phasor": {
        SKOS.related: {
            "Phasor_Angle": {
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
                SKOS.definition: Literal("Angle component of a phasor"),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("PhasorAngle"),
                SKOS.broader: QUDTQK.PlaneAngle,
            },
            "Phasor_Magnitude": {
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
                SKOS.definition: Literal("Magnitude component of a phasor"),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("PhasorMagnitude"),
            },
        },
    },
    "Power": {
        BRICK.hasQUDTReference: QUDTQK["Power"],
        SKOS.narrower: {
            "Electric_Power": {
                BRICK.hasQUDTReference: QUDTQK["ElectricPower"],
                SKOS.narrower: {
                    "Apparent_Power": {BRICK.hasQUDTReference: QUDTQK["ApparentPower"]},
                    "Active_Power": {
                        OWL.sameAs: BRICK["Real_Power"],
                        BRICK.hasQUDTReference: QUDTQK["ActivePower"],
                    },
                    "Real_Power": {
                        OWL.sameAs: BRICK["Active_Power"],
                        BRICK.hasQUDTReference: QUDTQK["ActivePower"],
                    },
                    "Reactive_Power": {BRICK.hasQUDTReference: QUDTQK["ReactivePower"]},
                    "Complex_Power": {BRICK.hasQUDTReference: QUDTQK["ComplexPower"]},
                },
            },
            "Peak_Power": {
                SKOS.broader: QUDTQK.Power,
                QUDT.applicableUnit: [UNIT.KiloW, UNIT.MegaW, UNIT.MilliW, UNIT.W],
                QUDT.hasDimensionVector: QUDTDV["A0E0L2I0M1H0T-3D0"],
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("PeakPower"),
                SKOS.definition: Literal(
                    "Tracks the highest (peak) observed power in some interval"
                ),
            },
            "Thermal_Power": {
                QUDT.applicableUnit: [
                    UNIT.MilliW,
                    UNIT.W,
                    UNIT.KiloW,
                    UNIT.MegaW,
                    UNIT.BTU_IT,
                ],
                QUDT.hasDimensionVector: QUDTDV["A0E0L2I0M1H0T-3D0"],
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("ThermalPower"),
                SKOS.broader: QUDTQK.Power,
            },
        },
    },
    "Cloudage": {
        # TODO: define Okta?
        # QUDT.applicableUnit: [UNIT.Okta],
        SKOS.definition: Literal(
            "The fraction of the sky obscured by clouds when observed from a particular location"
        ),
        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
        RDFS.label: Literal("Cloudage"),
        SKOS.broader: QUDTQK.Dimensionless,
    },
    "Electric_Current": {
        BRICK.hasQUDTReference: QUDTQK["ElectricCurrent"],
        SKOS.related: {
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
                SKOS.definition: Literal("Angle of current phasor"),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("CurrentAngle"),
                SKOS.broader: BRICK.Phasor_Angle,
            },
            "Current_Imbalance": {
                SKOS.definition: Literal("The percent deviation from average current"),
                QUDT.applicableUnit: [UNIT.PERCENT],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("CurrentImbalance"),
                SKOS.broader: QUDTQK.Dimensionless,
            },
            "Current_Total_Harmonic_Distortion": {
                SKOS.definition: Literal(
                    "Measurement of harmonic distortion present in a signal defined as the sum of the powers of all harmonic components to the power of the fundamental frequency. (https://en.wikipedia.org/wiki/Total_harmonic_distortion)"
                ),
                QUDT.applicableUnit: [UNIT.PERCENT, UNIT.DeciB_M],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("CurrentTotalHarmonicDistortion"),
                SKOS.broader: QUDTQK.Dimensionless,
            },
            "Alternating_Current_Frequency": {
                QUDT.applicableUnit: [UNIT.GigaHZ, UNIT.MegaHZ, UNIT.KiloHZ, UNIT.HZ],
                SKOS.definition: Literal(
                    "The frequency of the oscillations of alternating current"
                ),
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T-1D0"],
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("Alternating_Current_Frequency"),
                SKOS.broader: QUDTQK.Frequency,
            },
        },
    },
    "Voltage": {
        BRICK.hasQUDTReference: QUDTQK["Voltage"],
        SKOS.related: {
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
                SKOS.definition: Literal("Angle of voltage phasor"),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("VoltageAngle"),
                SKOS.broader: BRICK.Phasor_Angle,
            },
            "Voltage_Imbalance": {
                SKOS.definition: Literal("The percent deviation from average voltage"),
                QUDT.applicableUnit: [UNIT.PERCENT],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("VoltageImbalance"),
                SKOS.broader: QUDTQK.Dimensionless,
            },
        },
    },
    "Dewpoint": {BRICK.hasQUDTReference: QUDTQK["DewPointTemperature"]},
    "Direction": {
        SKOS.narrower: {
            "Wind_Direction": {
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
                SKOS.definition: Literal("Direction of wind relative to North"),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("Wind_Direction"),
            }
        }
    },
    "Energy": {
        SKOS.narrower: {
            "Electric_Energy": {
                QUDT.applicableUnit: [
                    UNIT.J,
                    UNIT["W-HR"],
                    UNIT["KiloW-HR"],
                    UNIT["MegaW-HR"],
                    UNIT["V-A_Reactive-HR"],
                    UNIT["KiloV-A_Reactive-HR"],
                    UNIT["MegaV-A_Reactive-HR"],
                    UNIT["KiloV-A-HR"],
                    UNIT["V-A-HR"],
                    UNIT["MegaV-A-HR"],
                ],
                QUDT.hasDimensionVector: QUDTDV["A0E0L2I0M1H0T-2D0"],
                SKOS.definition: Literal(
                    "A form of energy resulting from the flow of electrical charge"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("ElectricEnergy"),
                SKOS.broader: QUDTQK["Energy"],
                SKOS.narrower: {
                    "Active_Energy": {
                        QUDT.applicableUnit: [
                            UNIT["W-HR"],
                            UNIT["KiloW-HR"],
                            UNIT["MegaW-HR"],
                        ],
                        SKOS.definition: Literal(
                            "The integral of the active power over a time interval"
                        ),
                        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                        RDFS.label: Literal("Active_Energy"),
                    },
                    "Reactive_Energy": {
                        QUDT.applicableUnit: [
                            UNIT["V-A_Reactive-HR"],
                            UNIT["KiloV-A_Reactive-HR"],
                            UNIT["MegaV-A_Reactive-HR"],
                        ],
                        SKOS.definition: Literal(
                            "The integral of the reactive power over a time interval"
                        ),
                        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                        RDFS.label: Literal("Reactive_Energy"),
                    },
                    "Apparent_Energy": {
                        QUDT.applicableUnit: [
                            UNIT["KiloV-A-HR"],
                            UNIT["V-A-HR"],
                            UNIT["MegaV-A-HR"],
                        ],
                        SKOS.definition: Literal(
                            "The integral of the apparent power over a time interval"
                        ),
                        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                        RDFS.label: Literal("Apparent_Energy"),
                    },
                },
            },
            "Thermal_Energy": {BRICK.hasQUDTReference: QUDTQK["ThermalEnergy"]},
        },
    },
    "Flow": {
        BRICK.hasQUDTReference: QUDTQK["VolumeFlowRate"],
        SKOS.narrower: {
            "Flow_Loss": {
                QUDT.applicableUnit: [UNIT["M3-PER-SEC"]],
                QUDT.hasDimensionVector: QUDTDV["A0E0L3I0M0H0T-1D0"],
                SKOS.definition: Literal(
                    "The amount of flow rate that is lost during distribution"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("FlowLoss"),
                SKOS.broader: BRICK.Flow,
            },
        },
    },
    "Frequency": {
        BRICK.hasQUDTReference: QUDTQK["Frequency"],
        SKOS.narrower: {"Alternating_Current_Frequency": {}},
    },
    "Humidity": {
        SKOS.narrower: {
            "Relative_Humidity": {BRICK.hasQUDTReference: QUDTQK["RelativeHumidity"]},
            "Absolute_Humidity": {BRICK.hasQUDTReference: QUDTQK["AbsoluteHumidity"]},
        }
    },
    "Illuminance": {BRICK.hasQUDTReference: QUDTQK["Illuminance"]},
    "Irradiance": {
        QUDT.applicableUnit: [
            UNIT["W-PER-M2"],
            UNIT["W-PER-IN2"],
            UNIT["W-PER-FT2"],
            UNIT["W-PER-CentiM2"],
        ],
        SKOS.definition: Literal(
            "The power per unit area of electromagnetic radiation incident on a surface"
        ),
        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
        RDFS.label: Literal("Irradiance"),
        SKOS.broader: QUDTQK.PowerPerArea,
        SKOS.narrower: {
            "Solar_Irradiance": {
                QUDT.applicableUnit: [
                    UNIT["W-PER-M2"],
                    UNIT["W-PER-IN2"],
                    UNIT["W-PER-FT2"],
                    UNIT["W-PER-CentiM2"],
                ],
                SKOS.definition: Literal(
                    "The power per unit area of solar electromagnetic radiation incident on a surface"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("SolarIrradiance"),
                SKOS.broader: BRICK.Irradiance,
            }
        },
    },
    "Level": {
        QUDT.applicableUnit: [
            UNIT["CentiM"],
            UNIT["DeciM"],
            UNIT["MilliM"],
            UNIT["MicroM"],
            UNIT["KiloM"],
            UNIT["M"],
            UNIT["IN"],
            UNIT["FT"],
            UNIT["YD"],
        ],
        QUDT.hasDimensionVector: QUDTDV["A0E0L1I0M0H0T0D0"],
        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
        RDFS.label: Literal("Level"),
        SKOS.definition: Literal(
            "Amount of substance in a container; typically measured in height"
        ),
        SKOS.broader: QUDTQK.Length,
        SKOS.narrower: {
            "Precipitation": {
                QUDT.applicableUnit: [
                    UNIT["CentiM"],
                    UNIT["DeciM"],
                    UNIT["MilliM"],
                    UNIT["MicroM"],
                    UNIT["KiloM"],
                    UNIT["M"],
                    UNIT["IN"],
                    UNIT["FT"],
                    UNIT["YD"],
                ],
                SKOS.definition: Literal(
                    "Amount of atmospheric water vapor fallen including rain, sleet, snow, and hail (https://project-haystack.dev/doc/lib-phScience/precipitation)"
                ),
                QUDT.hasDimensionVector: QUDTDV["A0E0L1I0M0H0T0D0"],
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("Precipitation"),
                SKOS.broader: QUDTQK.Length,
            },
        },
    },
    "Luminance": {
        BRICK.hasQUDTReference: QUDTQK["Luminance"],
        SKOS.narrower: {
            "Luminous_Flux": {BRICK.hasQUDTReference: QUDTQK["LuminousFlux"]},
            "Luminous_Intensity": {BRICK.hasQUDTReference: QUDTQK["LuminousIntensity"]},
        },
    },
    "Occupancy": {
        SKOS.narrower: {
            "Occupancy_Count": {
                # QUDT.applicableUnit: [UNIT["People"]],
                SKOS.definition: Literal("Number of people in an area"),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("Occupancy_Count"),
                SKOS.broader: QUDTQK.Dimensionless,
            },
            "Occupancy_Percentage": {
                QUDT.applicableUnit: [UNIT["PERCENT"]],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                SKOS.definition: Literal(
                    "Percent of total occupancy of space that is occupied"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("Occupancy_Percentage"),
                SKOS.broader: QUDTQK.Dimensionless,
            },
        }
    },
    "Position": {
        QUDT.applicableUnit: [UNIT["PERCENT"]],
        SKOS.definition: Literal("The fraction of the full range of motion"),
        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
        RDFS.label: Literal("Position"),
        SKOS.broader: QUDTQK.Dimensionless,
        QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
    },
    "Power_Factor": {BRICK.hasQUDTReference: QUDTQK["PowerFactor"]},
    "Pressure": {
        BRICK.hasQUDTReference: QUDTQK["Pressure"],
        SKOS.narrower: {
            "Atmospheric_Pressure": {
                BRICK.hasQUDTReference: QUDTQK["AtmosphericPressure"]
            },
            "Dynamic_Pressure": {},
            "Differential_Pressure": {
                QUDT.isDeltaQuantity: Literal(True),
                SKOS.narrower: {
                    "Differential_Static_Pressure": {
                        BRICK.hasQUDTReference: QUDTQK["StaticPressure"],
                        QUDT.isDeltaQuantity: Literal(True),
                    },
                    "Differential_Dynamic_Pressure": {
                        BRICK.hasQUDTReference: QUDTQK["DynamicPressure"],
                        QUDT.isDeltaQuantity: Literal(True),
                    },
                },
            },
            "Static_Pressure": {
                BRICK.hasQUDTReference: QUDTQK["StaticPressure"],
                SKOS.narrower: {
                    "Differential_Static_Pressure": {
                        BRICK.hasQUDTReference: QUDTQK["StaticPressure"],
                        QUDT.isDeltaQuantity: Literal(True),
                    },
                },
            },
            "Velocity_Pressure": {
                BRICK.hasQUDTReference: [
                    QUDTQK["DynamicPressure"],
                    BRICK["Dynamic_Pressure"],
                ],
                SKOS.narrower: {
                    "Differential_Dynamic_Pressure": {
                        BRICK.hasQUDTReference: QUDTQK["DynamicPressure"],
                        QUDT.isDeltaQuantity: Literal(True),
                    },
                },
            },
        },
    },
    "Radiance": {
        BRICK.hasQUDTReference: QUDTQK["Radiance"],
        SKOS.narrower: {
            "Solar_Radiance": {
                QUDT.applicableUnit: [UNIT["W-PER-M2-SR"]],
                SKOS.definition: Literal(
                    "The amount of light that passes through or is emitted from the sun and falls within a given solid angle in a specified direction",
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("Solar_Radiance"),
                SKOS.broader: QUDTQK.Radiance,
            }
        },
    },
    "Speed": {
        BRICK.hasQUDTReference: QUDTQK["Speed"],
        SKOS.narrower: {
            "Linear_Speed": {
                QUDT.applicableUnit: [
                    UNIT["M-PER-HR"],
                    UNIT["KiloM-PER-HR"],
                    UNIT["FT-PER-HR"],
                    UNIT["MI-PER-HR"],
                    UNIT["M-PER-SEC"],
                    UNIT["KiloM-PER-SEC"],
                    UNIT["FT-PER-SEC"],
                    UNIT["MI-PER-SEC"],
                ],
                SKOS.definition: Literal(
                    "Speed in one dimension (linear)",
                ),
                QUDT.hasDimensionVector: QUDTDV["A0E0L1I0M0H0T-1D0"],
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("Linear_Speed"),
                SKOS.broader: QUDTQK.Speed,
            },
            "Rotational_Speed": {
                QUDT.applicableUnit: [
                    UNIT["RAD-PER-HR"],
                    UNIT["RAD-PER-SEC"],
                    UNIT["RAD-PER-MIN"],
                    UNIT["DEG-PER-HR"],
                    UNIT["DEG-PER-MIN"],
                    UNIT["DEG-PER-SEC"],
                ],
                SKOS.definition: Literal(
                    "Rotational speed",
                ),
                QUDT.hasDimensionVector: QUDTDV["A0E0L1I0M0H0T-1D0"],
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("Rotational_Speed"),
                SKOS.broader: [QUDTQK.Speed, QUDTQK.Frequency],
            },
        },
    },
    "Temperature": {
        BRICK.hasQUDTReference: QUDTQK["Temperature"],
        SKOS.narrower: {
            "Differential_Temperature": {
                BRICK.hasQUDTReference: QUDTQK["Temperature"],
                QUDT.isDeltaQuantity: Literal(True),
            },
            "Operative_Temperature": {
                QUDT.applicableUnit: [UNIT["DEG_F"], UNIT["DEG_C"], UNIT["K"]],
                SKOS.definition: Literal(
                    "The uniform temperature of an imaginary black enclosure in which an occupant would exchange the same amount of heat by radiation plus convection as in the actual nonuniform environment (https://en.wikipedia.org/wiki/Operative_temperature)"
                ),
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H1T0D0"],
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("Operative_Temperature"),
                SKOS.broader: QUDTQK.Temperature,
            },
            "Radiant_Temperature": {
                QUDT.applicableUnit: [UNIT["DEG_F"], UNIT["DEG_C"], UNIT["K"]],
                SKOS.definition: Literal(
                    "the uniform temperature of an imaginary enclosure in which the radiant heat transfer from the human body is equal to the radiant heat transfer in the actual non-uniform enclosure. (https://en.wikipedia.org/wiki/Mean_radiant_temperature)"
                ),
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H1T0D0"],
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("Radiant_Temperature"),
                SKOS.broader: QUDTQK.Temperature,
            },
            "Dry_Bulb_Temperature": {
                QUDT.applicableUnit: [UNIT["DEG_F"], UNIT["DEG_C"], UNIT["K"]],
                SKOS.definition: Literal(
                    "The temperature of air measured by a thermometer freely exposed to the air, but shielded from radiation and moisture. (https://en.wikipedia.org/wiki/Dry-bulb_temperature)"
                ),
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H1T0D0"],
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("Dry_Bulb_Temperature"),
                SKOS.broader: QUDTQK.Temperature,
                SKOS.narrower: {
                    "Differential_Dry_Bulb_Temperature": {
                        BRICK.hasQUDTReference: QUDTQK["Dry_Bulb_Temperature"],
                        QUDT.isDeltaQuantity: Literal(True),
                    },
                },
            },
            "Wet_Bulb_Temperature": {
                QUDT.applicableUnit: [UNIT["DEG_F"], UNIT["DEG_C"], UNIT["K"]],
                SKOS.definition: Literal(
                    "The temperature read by a thermometer covered in water-soaked cloth (wet-bulb thermometer) over which air is passed. A wet-bulb thermometer indicates a temperature close to the true (thermodynamic) wet-bulb temperature. The wet-bulb temperature is the lowest temperature that can be reached under current ambient conditions by the evaporation of water only.  DBT is the temperature that is usually thought of as air temperature, and it is the true thermodynamic temperature. It indicates the amount of heat in the air and is directly proportional to the mean kinetic energy of the air molecule. (https://en.wikipedia.org/wiki/Wet-bulb_temperature)"
                ),
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H1T0D0"],
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                RDFS.label: Literal("Wet_Bulb_Temperature"),
                SKOS.broader: QUDTQK.Temperature,
            },
        },
    },
    "Time": {
        BRICK.hasQUDTReference: QUDTQK["Time"],
        # TODO: what are these?
        SKOS.narrower: {"Acceleration_Time": {}, "Deceleration_Time": {}},
    },
    "Torque": {BRICK.hasQUDTReference: QUDTQK["Torque"]},
    # TODO: https://ci.mines-stetienne.fr/seas/WeatherOntology-0.9#AirTemperature ?
    "Weather_Condition": {},
}
