"""
Entity property definitions
"""
from collections import defaultdict
from rdflib import Literal
from .namespaces import BRICK, RDFS, SKOS, UNIT, XSD, SH, BSH, REF, QUDTQK

# these are the "relationship"/predicates/OWL properties that
# relate a Brick entity to a structured value.
# These are all instances of Brick.EntityProperty, which is
# a subclass of OWL.ObjectProperty
entity_properties = {
    BRICK.deprecation: {
        SKOS.definition: Literal("Marks a concept as deprecated"),
        "property_of": BRICK.Entity,
        SH.node: BSH.DeprecationShape,
        RDFS.label: Literal("Deprecation Notice", lang="en"),
    },
    BRICK.lastKnownValue: {
        SKOS.definition: Literal("The last known value of the Point entity"),
        "property_of": BRICK.Point,
        SH.node: BSH.LastKnownValueShape,
        RDFS.label: Literal("Last known value", lang="en"),
    },
    BRICK.area: {
        SKOS.definition: Literal("Entity has 2-dimensional area"),
        SH.node: BSH.AreaShape,
        "property_of": BRICK.Location,
        RDFS.label: Literal("Area", lang="en"),
        "subproperties": {
            BRICK.grossArea: {
                SKOS.definition: Literal("Entity has gross 2-dimensional area"),
                SH.node: BSH.AreaShape,
                "property_of": BRICK.Location,
                RDFS.label: Literal("Gross area", lang="en"),
            },
            BRICK.netArea: {
                SKOS.definition: Literal("Entity has net 2-dimensional area"),
                SH.node: BSH.AreaShape,
                "property_of": BRICK.Location,
                RDFS.label: Literal("Net area", lang="en"),
            },
            BRICK.panelArea: {
                SKOS.definition: Literal("Surface area of a panel, such as a PV panel"),
                "property_of": BRICK.Equipment,
                SH.node: BSH.AreaShape,
                RDFS.label: Literal("Panel area", lang="en"),
            },
        },
    },
    BRICK.volume: {
        SKOS.definition: Literal("Entity has 3-dimensional volume"),
        "property_of": [BRICK.Equipment, BRICK.Location],
        SH.node: BSH.VolumeShape,
        RDFS.label: Literal("Volume", lang="en"),
    },
    BRICK.azimuth: {
        SKOS.definition: Literal(
            "(Horizontal) angle between a projected vector and a reference vector (typically a compass bearing). The projected vector usually indicates the direction of a face or plane."
        ),
        SH.node: BSH.AzimuthShape,
        RDFS.label: Literal("Azimuth", lang="en"),
        "property_of": BRICK.Equipment,
    },
    BRICK.tilt: {
        SKOS.definition: Literal(
            "The direction an entity is facing in degrees above the horizon"
        ),
        SH.node: BSH.TiltShape,
        RDFS.label: Literal("Tilt", lang="en"),
        "property_of": BRICK.Equipment,
    },
    BRICK.coordinates: {
        SKOS.definition: Literal("The location of an entity in latitude/longitude"),
        SH.node: BSH.CoordinateShape,
        RDFS.label: Literal("Coordinates", lang="en"),
        "property_of": [BRICK.Equipment, BRICK.Location],
    },
    BRICK.resolution: {
        SKOS.definition: Literal(
            "The resolution of the entity specifing the smallest measurable or controllable increment"
            ),
        SH.node: BSH.ResolutionShape,
        RDFS.label: Literal("Resolution", lang="en"),
        "property_of": BRICK.Point,
    },
    # electrical properties
    BRICK.electricalComplexPower: {
        SKOS.definition: Literal("Associated electrical complexity with the entity"),
        SH.node: BSH.ElectricalComplexPowerShape,
        RDFS.label: Literal("electrical complex power type", lang="en"),
        "property_of": [BRICK.Equipment, BRICK.Point],
    },
    BRICK.electricalFlow: {
        SKOS.definition: Literal(
            "Entity has this electrical flow relative to the building'"
        ),
        SH.node: BSH.ElectricalFlowShape,
        RDFS.label: Literal("Electrical flow direction", lang="en"),
        "property_of": [BRICK.Equipment, BRICK.Point],
    },
    BRICK.electricalPhases: {
        SKOS.definition: Literal("Entity has these electrical AC phases"),
        SH.node: BSH.PhasesShape,
        RDFS.label: Literal("Electrical phases", lang="en"),
        "property_of": BRICK.Equipment,
    },
    BRICK.electricalPhaseCount: {
        SKOS.definition: Literal("Entity has these phases"),
        SH.node: BSH.PhaseCountShape,
        RDFS.label: Literal("Electrical phase count", lang="en"),
        "property_of": BRICK.Equipment,
    },
    BRICK.currentFlowType: {
        SKOS.definition: Literal("The current flow type of the entity"),
        SH.node: BSH.CurrentFlowTypeShape,
        RDFS.label: Literal("Current flow type", lang="en"),
        "property_of": BRICK.Equipment,
    },
    BRICK.ratedPowerOutput: {
        SKOS.definition: Literal("The nominal rated power output of the entity"),
        RDFS.label: Literal("Rated power output", lang="en"),
        SH.node: BSH.PowerQuantityShape,
        "property_of": BRICK.Equipment,
    },
    BRICK.measuredPowerOutput: {
        SKOS.definition: Literal("The nominal measured power output of the entity"),
        RDFS.label: Literal("Measured power output", lang="en"),
        SH.node: BSH.PowerQuantityShape,
        "property_of": BRICK.Equipment,
    },
    BRICK.ratedPowerInput: {
        SKOS.definition: Literal("The nominal rated power input of the entity"),
        RDFS.label: Literal("Rated power input", lang="en"),
        SH.node: BSH.PowerQuantityShape,
        "property_of": BRICK.Equipment,
    },
    BRICK.measuredPowerInput: {
        SKOS.definition: Literal("The nominal measured power input of the entity"),
        RDFS.label: Literal("Measured power input", lang="en"),
        SH.node: BSH.PowerQuantityShape,
        "property_of": BRICK.Equipment,
    },
    BRICK.ratedVoltageInput: {
        SKOS.definition: Literal("The nominal rated voltage input of the entity"),
        SH.node: BSH.VoltageQuantityShape,
        RDFS.label: Literal("Measured voltage input", lang="en"),
        "property_of": BRICK.Equipment,
        "subproperties": {
            BRICK.ratedMaximumVoltageInput: {
                RDFS.label: Literal("Rated maximum voltage input", lang="en"),
                SKOS.definition: Literal(
                    "The maximum voltage that can be input to the entity"
                ),
                SH.node: BSH.VoltageQuantityShape,
                "property_of": BRICK.Equipment,
            },
            BRICK.ratedMinimumVoltageInput: {
                RDFS.label: Literal("Rated minimum voltage input", lang="en"),
                SKOS.definition: Literal(
                    "The minimum voltage that can be input to the entity"
                ),
                "property_of": BRICK.Equipment,
                SH.node: BSH.VoltageQuantityShape,
            },
        },
    },
    BRICK.ratedVoltageOutput: {
        SKOS.definition: Literal("The nominal rated voltage output of the entity"),
        SH.node: BSH.VoltageQuantityShape,
        "property_of": BRICK.Equipment,
        RDFS.label: Literal("Rated voltage output", lang="en"),
        "subproperties": {
            BRICK.ratedMaximumVoltageOutput: {
                RDFS.label: Literal("Rated maximum voltage output", lang="en"),
                SKOS.definition: Literal(
                    "The maximum voltage that can be output by the entity"
                ),
                SH.node: BSH.VoltageQuantityShape,
                "property_of": BRICK.Equipment,
            },
            BRICK.ratedMinimumVoltageOutput: {
                RDFS.label: Literal("Rated minimum voltage output", lang="en"),
                SKOS.definition: Literal(
                    "The minimum voltage that can be output by the entity"
                ),
                SH.node: BSH.VoltageQuantityShape,
                "property_of": BRICK.Equipment,
            },
        },
    },
    BRICK.ratedCurrentInput: {
        SKOS.definition: Literal("The nominal rated current input of the entity"),
        SH.node: BSH.Electric_CurrentQuantityShape,
        RDFS.label: Literal("Rated current input", lang="en"),
        "property_of": BRICK.Equipment,
        "subproperties": {
            BRICK.ratedMaximumCurrentInput: {
                RDFS.label: Literal("Rated maximum current input", lang="en"),
                SKOS.definition: Literal(
                    "The maximum current that can be input to the entity"
                ),
                SH.node: BSH.Electric_CurrentQuantityShape,
                "property_of": BRICK.Equipment,
            },
            BRICK.ratedMinimumCurrentInput: {
                RDFS.label: Literal("Rated minimum current input", lang="en"),
                SKOS.definition: Literal(
                    "The minimum current that can be input to the entity"
                ),
                SH.node: BSH.Electric_CurrentQuantityShape,
                "property_of": BRICK.Equipment,
            },
        },
    },
    BRICK.ratedCurrentOutput: {
        SKOS.definition: Literal("The nominal rated current output of the entity"),
        SH.node: BSH.Electric_CurrentQuantityShape,
        RDFS.label: Literal("Rated current output", lang="en"),
        "property_of": BRICK.Equipment,
        "subproperties": {
            BRICK.ratedMaximumCurrentOutput: {
                RDFS.label: Literal("Rated maximum current output", lang="en"),
                SKOS.definition: Literal(
                    "The maximum current that can be output by the entity"
                ),
                SH.node: BSH.Electric_CurrentQuantityShape,
                "property_of": BRICK.Equipment,
            },
            BRICK.ratedMinimumCurrentOutput: {
                RDFS.label: Literal("Rated minimum current output", lang="en"),
                SKOS.definition: Literal(
                    "The minimum current that can be output by the entity"
                ),
                SH.node: BSH.Electric_CurrentQuantityShape,
                "property_of": BRICK.Equipment,
            },
        },
    },
    BRICK.temperatureCoefficientofPmax: {
        SKOS.definition: Literal(
            "The % change in power output for every degree celsius that the entity is hotter than 25 degrees celsius"
        ),
        SH.node: BSH.TemperatureCoefficientPerDegreeCelsiusShape,
        RDFS.label: Literal("Temperature coefficient", lang="en"),
        "property_of": BRICK.Equipment,
    },
    BRICK.conversionEfficiency: {
        SKOS.definition: Literal(
            "The percent efficiency of the conversion process (usually to power or energy) carried out by the entity"
        ),
        SH.node: BSH.EfficiencyShape,
        RDFS.label: Literal("Conversion efficiency", lang="en"),
        "property_of": BRICK.Equipment,
        "subproperties": {
            BRICK.ratedModuleConversionEfficiency: {
                SKOS.definition: Literal(
                    "The *rated* percentage of sunlight that is converted into usable power, as measured using Standard Test Conditions (STC): 1000 W/sqm irradiance, 25 degC panel temperature, no wind"
                ),
                "property_of": BRICK.PV_Panel,
                SH.node: BSH.EfficiencyShape,
                RDFS.label: Literal("Rated module conversion efficiency", lang="en"),
            },
            BRICK.measuredModuleConversionEfficiency: {
                SKOS.definition: Literal(
                    "The measured percentage of sunlight that is converted into usable power"
                ),
                "property_of": BRICK.PV_Panel,
                SH.node: BSH.EfficiencyShape,
                RDFS.label: Literal("Measured module conversion efficiency", lang="en"),
            },
        },
    },
    # equipment operation properties
    BRICK.operationalStage: {
        SKOS.definition: Literal("The associated operational stage"),
        SH.node: BSH.StageShape,
        RDFS.label: Literal("Operational stage", lang="en"),
        "property_of": BRICK.Equipment,
    },
    BRICK.operationalStageCount: {
        SKOS.definition: Literal(
            "The number of operational stages supported by this equipment"
        ),
        "property_of": BRICK.Equipment,
        SH.node: BSH.StageShape,
        RDFS.label: Literal("Operational stage count", lang="en"),
    },
    BRICK.coolingCapacity: {
        SKOS.definition: Literal(
            "Measurement of a chiller ability to remove heat (adopted from Project Haystack)"
        ),
        "property_of": BRICK.Chiller,
        SH.node: BSH.CoolingCapacityShape,
        RDFS.label: Literal("Cooling capacity", lang="en"),
        RDFS.seeAlso: Literal("https://project-haystack.org/tag/coolingCapacity"),
    },
    # building properties
    BRICK.buildingPrimaryFunction: {
        SKOS.definition: Literal(
            "Enumerated string applied to a site record to indicate the building's primary function. The list of primary functions is derived from the US Energy Star program (adopted from Project Haystack)"
        ),
        RDFS.seeAlso: Literal("https://project-haystack.org/tag/primaryFunction"),
        "property_of": BRICK.Building,
        SH.node: BSH.BuildingPrimaryFunctionShape,
        RDFS.label: Literal("Building primary function", lang="en"),
    },
    BRICK.yearBuilt: {
        SKOS.definition: Literal(
            "Four digit year that a building was first built. (adopted from Project Haystack)"
        ),
        "property_of": BRICK.Building,
        SH.node: BSH.YearBuiltShape,
        RDFS.seeAlso: Literal("https://project-haystack.org/tag/yearBuilt"),
        RDFS.label: Literal("Year built", lang="en"),
    },
    BRICK.thermalTransmittance: {
        SKOS.definition: Literal(
            "The area-weighted average heat transfer coefficient (commonly referred to as a U-value)"
        ),
        "property_of": BRICK.Location,
        SH.node: BSH.ThermalTransmittanceShape,
        RDFS.label: Literal("Thermal transmittance", lang="en"),
        RDFS.seeAlso: Literal(
            "https://www.iso.org/obp/ui/#iso:std:iso:13789:ed-3:v1:en"
        ),
        "subproperties": {
            BRICK.buildingThermalTransmittance: {
                "property_of": BRICK.Building,
                SH.node: BSH.ThermalTransmittanceShape,
                SKOS.definition: Literal(
                    "The area-weighted average heat transfer coefficient (commonly referred to as a U-value) for a building envelope"
                ),
                RDFS.seeAlso: Literal(
                    "https://www.iso.org/obp/ui/#iso:std:iso:13789:ed-3:v1:en"
                ),
                RDFS.label: Literal("Building thermal transmittance", lang="en"),
            },
        },
    },
    # special stuff
    BRICK.aggregate: {
        SKOS.definition: Literal(
            "Description of how the data for this point is aggregated"
        ),
        "property_of": BRICK.Point,
        SH.node: BSH.AggregationShape,
        RDFS.label: Literal("Aggregate", lang="en"),
    },
    BRICK.isVirtualMeter: {
        SKOS.definition: Literal(
            "True if the associated meter is 'virtual', i.e. a logical meter which includes or aggregates information from a variety of sources such as other submeters or equipment."
        ),
        "property_of": BRICK.Meter,
        SH.node: BSH.VirtualMeterShape,
        RDFS.label: Literal("is virtual meter", lang="en"),
    },
    BRICK.electricVehicleChargerType: {
        SKOS.definition: Literal(
            "Which type of EVSE charger this is, e.g. Level 1 (up to up to 2.5kW of AC power on 1 phase 120V input), Level 2 (direct AC power but can use higher voltage and up to 3 phases), or Level 3 (direct DC power)"
        ),
        "property_of": BRICK.Electric_Vehicle_Charging_Station,
        RDFS.label: Literal("has electric vehicle charger type", lang="en"),
        SH.node: BSH.ElectricVehicleChargingTypeShape,
    },
    BRICK.electricVehicleChargerDirectionality: {
        SKOS.definition: Literal(
            "Indicates if the EVSE charger supports bidirectional charging or just unidirectional charging of the EV battery"
        ),
        "property_of": [
            BRICK.Electric_Vehicle_Charging_Station,
            BRICK.Electric_Vehicle_Charging_Port,
        ],
        RDFS.label: Literal("has electric vehicle charger directionality", lang="en"),
        SH.node: BSH.ElectricVehicleChargingDirectionalityShape,
    },
    BRICK.electricVehicleConnectorType: {
        SKOS.definition: Literal(
            "Identifies which kind of connector the port has. This property helps identify the physical connection required between the vehicle and the charging equipment."
        ),
        "property_of": BRICK.Electric_Vehicle_Charging_Port,
        RDFS.label: Literal("has electric vehicle connector type", lang="en"),
        SH.node: BSH.ElectricVehicleConnectorTypeShape,
    },
}

building_primary_function_values = [
    "Adult Education",
    "Ambulatory Surgical Center",
    "Aquarium",
    "Automobile Dealership",
    "Bank Branch",
    "Bar/Nightclub",
    "Barracks",
    "Bowling Alley",
    "Casino",
    "College/University",
    "Convenience Store with Gas Station",
    "Convenience Store without Gas Station",
    "Convention Center",
    "Courthouse",
    "Data Center",
    "Distribution Center",
    "Drinking Water Treatment & Distribution",
    "Enclosed Mall",
    "Energy/Power Station",
    "Fast Food Restaurant",
    "Financial Office",
    "Fire Station",
    "Fitness Center/Health Club/Gym",
    "Food Sales",
    "Food Service",
    "Hospital (General Medical & Surgical)",
    "Hotel",
    "Ice/Curling Rink",
    "Indoor Arena",
    "K-12 School",
    "Laboratory",
    "Library",
    "Lifestyle Center",
    "Mailing Center/Post Office",
    "Manufacturing/Industrial Plant",
    "Medical Office",
    "Mixed Use Property",
    "Movie Theater",
    "Multifamily Housing",
    "Museum",
    "Non-Refrigerated Warehouse",
    "Office",
    "Other - Education",
    "Other - Entertainment/Public Assembly",
    "Other - Lodging/Residential",
    "Other - Mall",
    "Other - Public Services",
    "Other - Recreation",
    "Other - Restaurant/Bar",
    "Other - Services",
    "Other - Stadium",
    "Other - Technology/Science",
    "Other - Utility",
    "Other",
    "Other/Specialty Hospital",
    "Outpatient Rehabilitation/Physical Therapy",
    "Parking",
    "Performing Arts",
    "Personal Services (Health/Beauty, Dry Cleaning, etc)",
    "Police Station",
    "Pre-school/Daycare",
    "Prison/Incarceration",
    "Race Track",
    "Refrigerated Warehouse",
    "Repair Services (Vehicle, Shoe, Locksmith, etc)",
    "Residence Hall/Dormitory",
    "Restaurant",
    "Retail Store",
    "Roller Rink",
    "Self-Storage Facility",
    "Senior Care Community",
    "Single Family Home",
    "Social/Meeting Hall",
    "Stadium (Closed)",
    "Stadium (Open)",
    "Strip Mall",
    "Supermarket/Grocery Store",
    "Swimming Pool",
    "Transportation Terminal/Station",
    "Urgent Care/Clinic/Other Outpatient",
    "Veterinary Office",
    "Vocational School",
    "Wastewater Treatment Plant",
    "Wholesale Club/Supercenter",
    "Worship Facility",
    "Zoo",
]

# These are the shapes that govern what values of Entity Properties should look like
shape_properties = {
    BSH.AreaShape: {"units": [UNIT.FT2, UNIT.M2], "datatype": BSH.NumericValue},
    BSH.LastKnownValueShape: {
        "properties": {
            BRICK.timestamp: {"datatype": XSD.dateTime},
            BRICK.value: {SH.minCount: Literal(1), SH.maxCount: Literal(1)},
        },
    },
    BSH.VolumeShape: {"units": [UNIT.FT3, UNIT.M3], "datatype": BSH.NumericValue},
    BSH.ElectricalComplexPowerShape: {"values": ["real", "reactive", "apparent"]},
    BSH.ElectricalFlowShape: {"values": ["import", "export", "net", "absolute"]},
    BSH.PhasesShape: {"values": ["A", "B", "C", "AB", "BC", "AC", "ABC"]},
    BSH.PhaseCountShape: {"values": [1, 2, 3, "Total"]},
    BSH.CurrentFlowTypeShape: {"values": ["AC", "DC"]},
    BSH.StageShape: {"values": [1, 2, 3, 4]},
    BSH.BuildingPrimaryFunctionShape: {"values": building_primary_function_values},
    BSH.CoordinateShape: {
        "properties": {
            BRICK.latitude: {"datatype": BSH.NumericValue},
            BRICK.longitude: {"datatype": BSH.NumericValue},
        },
    },
    BSH.TiltShape: {"unitsFromQuantity": QUDTQK.Angle, "datatype": BSH.NumericValue},
    BSH.TemperatureShape: {
        "unitsFromQuantity": QUDTQK.Temperature,
        "datatype": BSH.NumericValue,
    },
    BSH.TemperatureCoefficientPerDegreeCelsiusShape: {
        "units": [UNIT.PERCENT],
        "datatype": BSH.NumericValue,
    },
    BSH.AzimuthShape: {
        "unitsFromQuantity": QUDTQK.Angle,
        "datatype": BSH.NumericValue,
        "rotationalDirection": {"values": ["clockwise", "counterclockwise"]},
        "referenceDirection": {"values": ["North", "South", "East", "West"]},
        "range": {"minInclusive": 0, "maxInclusive": 360},
    },
    BSH.YearBuiltShape: {"datatype": XSD.nonNegativeInteger},
    BSH.ThermalTransmittanceShape: {
        "datatype": BSH.NumericValue,
        "units": [UNIT.BTU_IT, UNIT["W-PER-M2-K"]],
    },
    BSH.EfficiencyShape: {
        "datatype": BSH.NumericValue,
        "units": [UNIT.PERCENT],
        "range": {"minInclusive": 0},
    },
    BSH.ResolutionShape: {
        "datatype": BSH.NumericValue,
        "range": {"minExclusive": 0},
    },
    BSH.CoolingCapacityShape: {
        "datatype": BSH.NumericValue,
        "units": [UNIT.TON_FG, UNIT["BTU_IT-PER-HR"], UNIT["BTU_TH-PER-HR"], UNIT.W],
    },
    BSH.VirtualMeterShape: {
        "datatype": XSD.boolean,
    },
    BSH.AggregationShape: {
        "properties": {
            BRICK.aggregationFunction: {
                SKOS.definition: Literal(
                    "The aggregation function applied to data in the interval which produces the value"
                ),
                "values": ["max", "min", "count", "mean", "sum", "median", "mode"],
            },
            BRICK.aggregationInterval: {
                SKOS.definition: Literal(
                    "Interval expressed in an ISO 8601 Duration string, e.g. RP1D"
                ),
                "datatype": XSD.string,
            },
        }
    },
    BSH.DeprecationShape: {
        "properties": {
            BRICK.deprecatedInVersion: {
                SKOS.definition: Literal(
                    "The version in which the entity was deprecated"
                ),
                "datatype": XSD.string,
            },
            BRICK.deprecationMitigationMessage: {
                SKOS.definition: Literal(
                    "A message describing how to mitigate or address the deprecation"
                ),
                "datatype": XSD.string,
            },
            BRICK.deprecationMitigationRule: {
                SKOS.definition: Literal(
                    "A SHACL rule which will mitigate the deprecation"
                ),
                SH["class"]: SH.NodeShape,
                "optional": True,
            },
        },
    },
    BSH.ElectricVehicleChargingTypeShape: {
        "values": ["Level 1", "Level 2", "Level 3"]
    },
    BSH.ElectricVehicleChargingDirectionalityShape: {
        "values": ["unidirectional", "bidirectional"]
    },
    BSH.ElectricVehicleConnectorTypeShape: {
        "values": [
            "Type 1 (CSS)",
            "Type 2 (CSS)",
            "GB/T",
            "Type 1 (SAE J1772)",
            "Type 2 (IEC 62196)",
            "CHAdeMO",
            "CCS (Combined Charging System)",
            "Tesla Supercharger",
            "Wireless",
        ]
    },
}


def get_shapes(G):
    shape_properties.update(generate_quantity_shapes(G))
    return shape_properties


# this generates shapes of the form BSH.<quantity name>QuantityShape
def generate_quantity_shapes(G):
    quantities = G.query(
        "SELECT ?q WHERE { ?q a brick:Quantity . ?q qudt:applicableUnit ?unit }"
    )
    d = defaultdict(dict)
    # some additional properties for some quantities
    d[BSH.PowerQuantityShape] = {
        "properties": {
            BRICK.ambientTemperatureOfMeasurement: {
                "optional": True,
                SKOS.definition: Literal(
                    "The ambient temperature at which the power input was measured"
                ),
                SH["class"]: BSH.TemperatureShape,
            },
        },
    }
    d[BSH.VoltageQuantityShape] = {
        "properties": {
            BRICK.ambientTemperatureOfMeasurement: {
                "optional": True,
                SKOS.definition: Literal(
                    "The ambient temperature at which the voltage was measured"
                ),
                SH["class"]: BSH.TemperatureShape,
            },
        },
    }
    d[BSH.Electric_CurrentQuantityShape] = {
        "properties": {
            BRICK.ambientTemperatureOfMeasurement: {
                "optional": True,
                SKOS.definition: Literal(
                    "The ambient temperature at which the current input was measured"
                ),
                SH["class"]: BSH.TemperatureShape,
            },
        },
    }

    for (quantity,) in quantities:
        shape = BSH[f"{quantity.split('#')[-1]}QuantityShape"]
        d[shape].update(
            {
                "unitsFromQuantity": quantity,
                "datatype": BSH.NumericValue,
            }
        )
    return d
