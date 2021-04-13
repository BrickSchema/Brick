from .namespaces import BRICK, TAG, OWL, RDFS, SKOS, UNIT, XSD
from rdflib import Namespace, Literal

# these are the "relationship"/predicates/OWL properties that
# relate a Brick entity to a structured value.
# These are all instances of Brick.EntityProperty, which is
# a subclass of OWL.ObjectProperty
entity_properties = {
    BRICK.area: {
        SKOS.definition: Literal("Entity has 2-dimensional area"),
        RDFS.domain: BRICK.Location,
        RDFS.range: BRICK.AreaShape,
        "subproperties": {
            BRICK.grossArea: {
                SKOS.definition: Literal("Entity has gross 2-dimensional area"),
                RDFS.domain: BRICK.Location,
                RDFS.range: BRICK.AreaShape,
            },
            BRICK.netArea: {
                SKOS.definition: Literal("Entity has net 2-dimensional area"),
                RDFS.domain: BRICK.Location,
                RDFS.range: BRICK.AreaShape,
            },
        },
    },
    BRICK.volume: {
        SKOS.definition: Literal("Entity has 3-dimensional volume"),
        RDFS.domain: BRICK.Location,
        RDFS.range: BRICK.VolumeShape,
    },
    # electrical properties
    BRICK.powerComplexity: {
        SKOS.definition: Literal("Entity has this power complexity"),
        RDFS.range: BRICK.PowerComplexityShape,
    },
    BRICK.powerFlow: {
        SKOS.definition: Literal(
            "Entity has this power flow relative to the building'"
        ),
        RDFS.range: BRICK.PowerFlowShape,
    },
    BRICK.electricalPhases: {
        SKOS.definition: Literal("Entity has these electrical AC phases"),
        RDFS.range: BRICK.PhasesShape,
    },
    BRICK.electricalPhaseCount: {
        SKOS.definition: Literal("Entity has these phases"),
        RDFS.range: BRICK.PhaseCountShape,
    },
    BRICK.currentFlowType: {
        SKOS.definition: Literal("The current flow type of the entity"),
        RDFS.range: BRICK.CurrentFlowTypeShape,
    },
    # equipment operation properties
    BRICK.operationalStage: {
        SKOS.definition: Literal("The associated operational stage"),
        RDFS.range: BRICK.StageShape,
    },
    BRICK.operationalStageCount: {
        SKOS.definition: Literal(
            "The number of operational stages supported by this eqiupment"
        ),
        RDFS.domain: BRICK.Equipment,
        RDFS.range: BRICK.StageShape,
    },
    BRICK.coolingCapacity: {
        SKOS.definition: Literal(
            "Measurement of a chiller ability to remove heat (adopted from Project Haystack)"
        ),
        RDFS.domain: BRICK.Chiller,
        RDFS.range: BRICK.CoolingCapacityShape,
        RDFS.seeAlso: Literal("https://project-haystack.org/tag/coolingCapacity"),
    },
    # building properties
    BRICK.buildingPrimaryFunction: {
        SKOS.definition: Literal(
            "Enumerated string applied to a site record to indicate the building's primary function. The list of primary functions is derived from the US Energy Star program (adopted from Project Haystack)"
        ),
        RDFS.seeAlso: Literal("https://project-haystack.org/tag/primaryFunction"),
        RDFS.domain: BRICK.Building,
        RDFS.range: BRICK.BuildingPrimaryFunctionShape,
    },
    BRICK.yearBuilt: {
        SKOS.definition: Literal(
            "Four digit year that a building was first built. (adopted from Project Haystack)"
        ),
        RDFS.domain: BRICK.Building,
        RDFS.range: BRICK.YearBuiltShape,
        RDFS.seeAlso: Literal("https://project-haystack.org/tag/yearBuilt"),
    },
    BRICK.thermalTransmittence: {
        SKOS.definition: Literal(
            "The area-weighted average heat transfer coefficient (commonly referred to as a U-value)"
        ),
        RDFS.range: BRICK.ThermalTransmittenceShape,
        RDFS.seeAlso: Literal(
            "https://www.iso.org/obp/ui/#iso:std:iso:13789:ed-3:v1:en"
        ),
        "subproperties": {
            BRICK.buildingThermalTransmittence: {
                RDFS.domain: BRICK.Building,
                RDFS.range: BRICK.ThermalTransmittenceShape,
                SKOS.definition: Literal(
                    "The area-weighted average heat transfer coefficient (commonly referred to as a U-value) for a building envelope"
                ),
                RDFS.seeAlso: Literal(
                    "https://www.iso.org/obp/ui/#iso:std:iso:13789:ed-3:v1:en"
                ),
            },
        },
    },
    # heat pump properties
    BRICK.loadSideResource: {
        SKOS.definition: Literal(
            "The resource that is the target of some thermodynamic process, e.g. the air that is heated or cooled"
        ),
        RDFS.range: BRICK.ThermodynamicResourceShape,
    },
    BRICK.sourceSideResource: {
        SKOS.definition: Literal(
            "The resource that is the other side of some thermodynamic process -- i.e. not the load. For example, the chilled water that cools the air"
        ),
        RDFS.range: BRICK.ThermodynamicResourceShape,
    },
    BRICK.heatFlow: {
        SKOS.definition: Literal(
            "The direction of heat flow from the source-side to the load-side"
        ),
        RDFS.range: BRICK.HeatFlowShape,
    },
    BRICK.reversibleHeatFlow: {
        SKOS.definition: Literal(
            "Whether or not the heat flow operation is reversible"
        ),
        RDFS.range: BRICK.TrueFalseShape,
    },
    # special stuff
    BRICK.aggregate: {
        SKOS.definition: Literal(
            "Description of how the dta for this point is aggregated"
        ),
        RDFS.domain: BRICK.Point,
        RDFS.range: BRICK.AggregationShape,
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
    BRICK.AreaShape: {"units": [UNIT.FT2, UNIT.M2], "datatype": XSD.float},
    BRICK.VolumeShape: {"units": [UNIT.FT3, UNIT.M3], "datatype": XSD.float},
    BRICK.PowerComplexityShape: {"values": ["real", "reactive", "apparent"]},
    BRICK.PowerFlowShape: {"values": ["import", "export", "net", "absolute"]},
    BRICK.PhasesShape: {"values": ["A", "B", "C", "AB", "BC", "AC", "ABC"]},
    BRICK.PhaseCountShape: {"values": ["1", "2", "3", "Total"]},
    BRICK.CurrentFlowTypeShape: {"values": ["AC", "DC"]},
    BRICK.StageShape: {"values": [1, 2, 3, 4]},
    BRICK.BuildingPrimaryFunctionShape: {"values": building_primary_function_values},
    BRICK.YearBuiltShape: {"datatype": XSD.integer},
    BRICK.ThermalTransmittenceShape: {
        "datatype": XSD.float,
        "units": [UNIT.BTU_IT, UNIT["W-PER-M2-K"]],
    },
    BRICK.CoolingCapacityShape: {
        "datatype": XSD.float,
        "units": [UNIT.TON_FG, UNIT["BTU_IT-PER-HR"], UNIT["BTU_TH-PER-HR"], UNIT.W],
    },
    BRICK.AggregationShape: {
        "properties": {
            BRICK.aggregationFunction: {
                "values": ["max", "min", "count", "mean", "sum", "median", "mode"]
            },
            BRICK.aggregationInterval: {
                SKOS.definition: Literal(
                    "Interval expressed in an ISO 8601 Duration string, e.g. RP1D"
                ),
                "datatype": XSD.string,
            },
        }
    },
    BRICK.ThermodynamicResourceShape: {
        "values": [
            BRICK.Air,
            BRICK.Water,
            BRICK.Refrigerant,
            BRICK.Freon,
            BRICK.Puron,
            BRICK.Ground,
        ],
    },
    BRICK.HeatFlowShape: {"values": ["heat", "cool"]},
    BRICK.TrueFalseShape: {"values": ["true", "false"]},
}
