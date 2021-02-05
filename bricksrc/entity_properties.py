from .namespaces import BRICK, TAG, OWL, RDFS, SKOS, UNIT, PROP, XSD
from rdflib import Namespace, Literal

# these are the "relationship"/predicates/OWL properties that
# relate a Brick entity to a structured value.
# These are all instances of Brick.EntityProperty, which is
# a subclass of OWL.ObjectProperty
entity_properties = {
    PROP.hasArea: {
        SKOS.definition: Literal("Entity has 2-dimensional area"),
        RDFS.domain: BRICK.Location,
        RDFS.range: PROP.AreaShape,
        "subproperties": {
            PROP.hasGrossArea: {
                SKOS.definition: Literal("Entity has gross 2-dimensional area"),
                RDFS.domain: BRICK.Location,
                RDFS.range: PROP.AreaShape,
            },
            PROP.hasNetArea: {
                SKOS.definition: Literal("Entity has net 2-dimensional area"),
                RDFS.domain: BRICK.Location,
                RDFS.range: PROP.AreaShape,
            },
        },
    },
    PROP.hasVolume: {
        SKOS.definition: Literal("Entity has 3-dimensional volume"),
        RDFS.domain: BRICK.Location,
        RDFS.range: PROP.VolumeShape,
    },
    # electrical properties
    PROP.hasComplexity: {
        SKOS.definition: Literal("Entity has this power complexity"),
        RDFS.range: PROP.PowerComplexityShape,
    },
    PROP.hasPowerFlow: {
        SKOS.definition: Literal(
            "Entity has this power flow relative to the building'"
        ),
        RDFS.range: PROP.PowerFlowShape,
    },
    PROP.hasPhases: {
        SKOS.definition: Literal("Entity has these electrical AC phases"),
        RDFS.range: PROP.PhasesShape,
    },
    PROP.hasPhaseCount: {
        SKOS.definition: Literal("Entity has these phases"),
        RDFS.range: PROP.PhaseCountShape,
    },
    PROP.hasCurrentFlowType: {
        SKOS.definition: Literal("The current flow type of the entity"),
        RDFS.range: PROP.CurrentFlowTypeShape,
    },
    # equipment operation properties
    PROP.hasStage: {
        SKOS.definition: Literal("The associated operational stage"),
        RDFS.range: PROP.StageShape,
    },
    PROP.hasStageCount: {
        SKOS.definition: Literal(
            "The number of operational stages supported by this eqiupment"
        ),
        RDFS.domain: BRICK.Equipment,
        RDFS.range: PROP.StageShape,
    },
    PROP.hasBuildingPrimaryFunction: {
        SKOS.definition: Literal(
            "Enumerated string applied to a site record to indicate the building's primary function. The list of primary functions is derived from the US Energy Star program (adopted from Project Haystack)"
        ),
        RDFS.seeAlso: Literal("https://project-haystack.org/tag/primaryFunction"),
        RDFS.domain: BRICK.Building,
        RDFS.range: PROP.BuildingPrimaryFunctionShape,
    },
    PROP.hasCoolingCapacity: {
        SKOS.definition: Literal(
            "Measurement of a chiller ability to remove heat (adopted from Project Haystack)"
        ),
        RDFS.domain: BRICK.Chiller,
        RDFS.range: PROP.CoolingCapacityShape,
        RDFS.seeAlso: Literal("https://project-haystack.org/tag/coolingCapacity"),
    },
    PROP.hasYearBuilt: {
        SKOS.definition: Literal(
            "Four digit year that a building was first built. (adopted from Project Haystack)"
        ),
        RDFS.domain: BRICK.Building,
        RDFS.range: PROP.YearBuiltShape,
        RDFS.seeAlso: Literal("https://project-haystack.org/tag/yearBuilt"),
    },
    # special stuff
    PROP.aggregate: {
        SKOS.definition: Literal(
            "Description of how the dta for this point is aggregated"
        ),
        RDFS.domain: BRICK.Point,
        RDFS.range: PROP.AggregationShape,
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
    PROP.AreaShape: {"units": [UNIT.FT2, UNIT.M2], "datatype": XSD.float},
    PROP.VolumeShape: {"units": [UNIT.FT3, UNIT.M3], "datatype": XSD.float},
    PROP.PowerComplexityShape: {"values": ["real", "reactive", "apparent"]},
    PROP.PowerFlowShape: {"values": ["import", "export", "net", "absolute"]},
    PROP.PhasesShape: {"values": ["A", "B", "C", "AB", "BC", "AC", "ABC"]},
    PROP.PhaseCountShape: {"values": ["1", "2", "3", "Total"]},
    PROP.CurrentFlowTypeShape: {"values": ["AC", "DC"]},
    PROP.StageShape: {"values": [1, 2, 3, 4]},
    PROP.BuildingPrimaryFunctionShape: {"values": building_primary_function_values},
    PROP.YearBuiltShape: {"datatype": XSD.integer},
    PROP.CoolingCapacityShape: {
        "datatype": XSD.float,
        "units": [UNIT.TON_FG, UNIT["BTU_IT-PER-HR"], UNIT["BTU_TH-PER-HR"], UNIT.W],
    },
    PROP.AggregationShape: {
        "properties": {
            PROP.aggregationFunction: {
                "values": ["max", "min", "count", "mean", "sum", "median", "mode"]
            },
            PROP.aggregationInterval: {
                SKOS.definition: Literal(
                    "Interval expressed in an ISO 8601 Duration string, e.g. RP1D"
                ),
                "datatype": XSD.string,
            },
        }
    },
}
