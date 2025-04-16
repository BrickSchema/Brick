from brickschema.graph import Graph
from ontoenv import OntoEnv, Config
from rdflib import Literal, URIRef
from .namespaces import SKOS, RDFS, BRICK, QUDTQK, QUDTDV, QUDT, UNIT, XSD
from .env import env

g = Graph()
env.import_graph(g, "http://qudt.org/3.1.0/vocab/unit")
env.import_graph(g, "http://qudt.org/3.1.0/vocab/quantitykind")
g.bind("qudt", QUDT)
g.bind("qudtqk", QUDTQK)

env.import_dependencies(g)
g.expand("shacl", backend="topquadrant")


def get_units(qudt_quantity):
    """
    Fetches the QUDT unit and symbol (as a Literal) from the QUDT ontology so
    in order to avoid having to pull the full QUDT ontology into Brick
    """
    return [
        x[0]
        for x in g.query(
            f"""SELECT ?unit WHERE {{
                    <{qudt_quantity}> qudt:applicableUnit ?unit .
                }}"""
        )
    ]


def all_units():
    return g.query(
        """SELECT ?unit ?symbol ?label WHERE {
        ?unit a qudt:Unit .
        OPTIONAL { ?unit qudt:symbol ?symbol } .
        OPTIONAL { ?unit rdfs:label ?label} .
    }"""
    )


"""
Each is a qudt:QuantityKind
"""
quantity_definitions = {
    "Air_Quality": {
        QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
        SKOS.narrower: {
            "Ammonia_Concentration": {
                QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                SKOS.definition: Literal("The concentration of Ammonia in a medium"),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                SKOS.broader: QUDTQK.DimensionlessRatio,
            },
            "CO_Concentration": {
                QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                SKOS.definition: Literal(
                    "The concentration of carbon monoxide in a medium"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                SKOS.broader: QUDTQK.DimensionlessRatio,
                SKOS.narrower: {
                    "Differential_CO_Concentration": {
                        QUDT.isDeltaQuantity: Literal(True),
                        QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                        QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB],
                        SKOS.definition: Literal(
                            "The difference in carbon monoxide concentration between two areas"
                        ),
                        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
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
                SKOS.broader: QUDTQK.DimensionlessRatio,
                SKOS.narrower: {
                    "Differential_CO2_Concentration": {
                        QUDT.isDeltaQuantity: Literal(True),
                        QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                        QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB],
                        SKOS.definition: Literal(
                            "The difference in carbon dioxide concentration between two areas"
                        ),
                        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
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
                SKOS.broader: QUDTQK.DimensionlessRatio,
            },
            "Ozone_Concentration": {
                QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                SKOS.definition: Literal("The concentration of ozone in a medium"),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                SKOS.broader: QUDTQK.DimensionlessRatio,
            },
            "Methane_Concentration": {
                QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                SKOS.definition: Literal("The concentration of methane in a medium"),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                SKOS.broader: QUDTQK.DimensionlessRatio,
            },
            "NO2_Concentration": {
                QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                SKOS.definition: Literal(
                    "The concentration of nitrogen dioxide in a medium"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
            },
            "PM10_Concentration": {
                QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB, UNIT["MicroGM-PER-M3"]],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                SKOS.definition: Literal(
                    "The concentration of particulates with diameter of 10 microns or less in air"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
            },
            "PM2.5_Concentration": {
                QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB, UNIT["MicroGM-PER-M3"]],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                SKOS.definition: Literal(
                    "The concentration of particulates with diameter of 2.5 microns or less in air"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
            },
            "PM1_Concentration": {
                QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB, UNIT["MicroGM-PER-M3"]],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                SKOS.definition: Literal(
                    "The concentration of particulates with diameter of 1 microns or less in air"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
            },
            "Radon_Concentration": {
                QUDT.applicableUnit: [UNIT["BQ-PER-M3"]],
                QUDT.hasDimensionVector: QUDTDV["A0E0L-3I0M0H0T-1D0"],
                SKOS.definition: Literal(
                    "The concentration of radioactivity due to Radon in a medium"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                SKOS.broader: QUDTQK.ActivityConcentration,
            },
            "TVOC_Concentration": {
                QUDT.applicableUnit: [UNIT.PPM, UNIT.PPB, UNIT["MicroGM-PER-M3"]],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                SKOS.definition: Literal(
                    "The concentration of total volatile organic compounds in air"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                SKOS.broader: QUDTQK.DimensionlessRatio,
            },
            "GrainsOfMoisture": {
                QUDT.applicableUnit: UNIT.GRAIN,
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M1H0T0D0"],
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                SKOS.definition: Literal(
                    "Mass of moisture per pround of air, measured in grains of water"
                ),
                SKOS.broader: QUDTQK.Mass,
            },
        },
    },
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
    },
    "Cloudage": {
        QUDT.applicableUnit: [UNIT.OKTA],
        QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
        SKOS.definition: Literal(
            "The fraction of the sky obscured by clouds when observed from a particular location"
        ),
        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
        SKOS.broader: QUDTQK.Dimensionless,
    },
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
        SKOS.broader: BRICK.Phasor_Angle,
    },
    "Current_Imbalance": {
        SKOS.definition: Literal("The percent deviation from average current"),
        QUDT.applicableUnit: [UNIT.PERCENT],
        QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
        SKOS.broader: QUDTQK.Dimensionless,
    },
    "Current_Total_Harmonic_Distortion": {
        SKOS.definition: Literal(
            "Measurement of harmonic distortion present in a signal defined as the sum of the powers of all harmonic components to the power of the fundamental frequency. (https://en.wikipedia.org/wiki/Total_harmonic_distortion)"
        ),
        QUDT.applicableUnit: [UNIT.PERCENT, UNIT.DeciB_M],
        QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
        SKOS.broader: QUDTQK.Dimensionless,
    },
    "Alternating_Current_Frequency": {
        QUDT.applicableUnit: [UNIT.GigaHZ, UNIT.MegaHZ, UNIT.KiloHZ, UNIT.HZ],
        SKOS.definition: Literal(
            "The frequency of the oscillations of alternating current"
        ),
        QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T-1D0"],
        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
        SKOS.broader: QUDTQK.Frequency,
    },
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
        SKOS.broader: BRICK.Phasor_Angle,
    },
    "Voltage_Imbalance": {
        SKOS.definition: Literal("The percent deviation from average voltage"),
        QUDT.applicableUnit: [UNIT.PERCENT],
        QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
        SKOS.broader: QUDTQK.Dimensionless,
    },
    "Direction": {
        QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
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
            }
        }
    },
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
        SKOS.broader: QUDTQK["Energy"],
        SKOS.narrower: {
            "Active_Energy": {
                QUDT.hasDimensionVector: QUDTDV["A0E0L2I0M1H0T-2D0"],
                QUDT.applicableUnit: [
                    UNIT["W-HR"],
                    UNIT["KiloW-HR"],
                    UNIT["MegaW-HR"],
                ],
                SKOS.definition: Literal(
                    "The integral of the active power over a time interval"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
            },
            "Reactive_Energy": {
                QUDT.hasDimensionVector: QUDTDV["A0E0L2I0M1H0T-2D0"],
                QUDT.applicableUnit: [
                    UNIT["V-A_Reactive-HR"],
                    UNIT["KiloV-A_Reactive-HR"],
                    UNIT["MegaV-A_Reactive-HR"],
                ],
                SKOS.definition: Literal(
                    "The integral of the reactive power over a time interval"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
            },
            "Apparent_Energy": {
                QUDT.hasDimensionVector: QUDTDV["A0E0L2I0M1H0T-2D0"],
                QUDT.applicableUnit: [
                    UNIT["KiloV-A-HR"],
                    UNIT["V-A-HR"],
                    UNIT["MegaV-A-HR"],
                ],
                SKOS.definition: Literal(
                    "The integral of the apparent power over a time interval"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
            },
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
                SKOS.broader: QUDTQK.Length,
            },
        },
    },
    "Occupancy": {
        QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
        SKOS.narrower: {
            "Occupancy_Count": {
                # QUDT.applicableUnit: [UNIT["People"]],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                SKOS.definition: Literal("Number of people in an area"),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                SKOS.broader: QUDTQK.Dimensionless,
            },
            "Occupancy_Percentage": {
                QUDT.applicableUnit: [UNIT["PERCENT"]],
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
                SKOS.definition: Literal(
                    "Percent of total occupancy of space that is occupied"
                ),
                RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
                SKOS.broader: QUDTQK.Dimensionless,
            },
        }
    },
    "Position": {
        QUDT.applicableUnit: [UNIT["PERCENT"]],
        SKOS.definition: Literal("The fraction of the full range of motion"),
        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
        SKOS.broader: QUDTQK.Dimensionless,
        QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H0T0D1"],
    },
    "Differential_Pressure": {
        QUDT.isDeltaQuantity: Literal(True),
        QUDT.hasDimensionVector: QUDTDV["A0E0L-1I0M1H0T-2D0"],
        SKOS.narrower: {
            "Differential_Static_Pressure": {
                BRICK.hasQUDTReference: QUDTQK["StaticPressure"],
                QUDT.hasDimensionVector: QUDTDV["A0E0L-1I0M1H0T-2D0"],
                QUDT.isDeltaQuantity: Literal(True),
            },
            "Differential_Dynamic_Pressure": {
                BRICK.hasQUDTReference: QUDTQK["DynamicPressure"],
                QUDT.hasDimensionVector: QUDTDV["A0E0L-1I0M1H0T-2D0"],
                QUDT.isDeltaQuantity: Literal(True),
            },
        },
    },
    "Solar_Radiance": {
        QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M1H0T-3D0"],
        QUDT.applicableUnit: [UNIT["W-PER-M2-SR"]],
        SKOS.definition: Literal(
            "The amount of light that passes through or is emitted from the sun and falls within a given solid angle in a specified direction",
        ),
        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
        SKOS.broader: QUDTQK.Radiance,
    },
    "Solar_Irradiance": {
        QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M1H0T-3D0"],
        QUDT.applicableUnit: [UNIT["W-PER-M2"]],
        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
        SKOS.broader: QUDTQK.Irradiance,
    },
    "Speed": {
        BRICK.hasQUDTReference: QUDTQK["Speed"],
        QUDT.hasDimensionVector: QUDTDV["A0E0L1I0M0H0T-1D0"],
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
                SKOS.broader: [QUDTQK.Speed, QUDTQK.Frequency],
            },
        },
    },
    "Differential_Temperature": {
        BRICK.hasQUDTReference: QUDTQK["Temperature"],
        QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H1T0D0"],
        QUDT.isDeltaQuantity: Literal(True),
    },
    "Operative_Temperature": {
        QUDT.applicableUnit: [UNIT["DEG_F"], UNIT["DEG_C"], UNIT["K"]],
        SKOS.definition: Literal(
            "The uniform temperature of an imaginary black enclosure in which an occupant would exchange the same amount of heat by radiation plus convection as in the actual nonuniform environment (https://en.wikipedia.org/wiki/Operative_temperature)"
        ),
        QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H1T0D0"],
        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
        SKOS.broader: QUDTQK.Temperature,
    },
    "Radiant_Temperature": {
        QUDT.applicableUnit: [UNIT["DEG_F"], UNIT["DEG_C"], UNIT["K"]],
        SKOS.definition: Literal(
            "the uniform temperature of an imaginary enclosure in which the radiant heat transfer from the human body is equal to the radiant heat transfer in the actual non-uniform enclosure. (https://en.wikipedia.org/wiki/Mean_radiant_temperature)"
        ),
        QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H1T0D0"],
        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
        SKOS.broader: QUDTQK.Temperature,
    },
    "Dry_Bulb_Temperature": {
        QUDT.applicableUnit: [UNIT["DEG_F"], UNIT["DEG_C"], UNIT["K"]],
        SKOS.definition: Literal(
            "The temperature of air measured by a thermometer freely exposed to the air, but shielded from radiation and moisture. (https://en.wikipedia.org/wiki/Dry-bulb_temperature)"
        ),
        QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H1T0D0"],
        RDFS.isDefinedBy: URIRef(str(BRICK).strip("#")),
        SKOS.broader: QUDTQK.Temperature,
        SKOS.narrower: {
            "Differential_Dry_Bulb_Temperature": {
                QUDT.hasDimensionVector: QUDTDV["A0E0L0I0M0H1T0D0"],
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
        SKOS.broader: QUDTQK.Temperature,
    },
    # TODO: https://ci.mines-stetienne.fr/seas/WeatherOntology-0.9#AirTemperature ?
    "Volume": {
        BRICK.hasQUDTReference: QUDTQK["Volume"],
        QUDT.applicableUnit: [UNIT["M3"], UNIT["FT3"], UNIT["IN3"], UNIT["YD3"]],
        QUDT.hasDimensionVector: QUDTDV["A0E0L3I0M0H0T0D0"],
    },
}
