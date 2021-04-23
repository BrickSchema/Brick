from .namespaces import BRICK, TAG, OWL, RDFS, SKOS, UNIT, XSD
from rdflib import Namespace, Literal

# these are the "relationship"/predicates/OWL properties that
# relate a Brick entity to a structured value.
# These are all instances of Brick.EntityProperty, which is
# a subclass of OWL.ObjectProperty
entity_properties = {
    BRICK.area: {
        SKOS.definition: Literal("Entity has 2-dimensional area"),
        RDFS.range: BRICK.AreaShape,
        "subproperties": {
            BRICK.grossArea: {
                SKOS.definition: Literal("Entity has gross 2-dimensional area"),
                RDFS.range: BRICK.AreaShape,
            },
            BRICK.netArea: {
                SKOS.definition: Literal("Entity has net 2-dimensional area"),
                RDFS.range: BRICK.AreaShape,
            },
            BRICK.panelArea: {
                SKOS.definition: Literal("Surface area of a panel, such as a PV panel"),
                # TODO: needs to go on equipment; do we remove "domain" from the above?
                RDFS.range: BRICK.AreaShape,
            },
        },
    },
    BRICK.volume: {
        SKOS.definition: Literal("Entity has 3-dimensional volume"),
        RDFS.range: BRICK.VolumeShape,
    },
    BRICK.orientation: {
        SKOS.definition: Literal(
            "The direction an entity is facing, relative to some reference point (usually a 'compass' direction)"
        ),
        # TODO: for points + equipment? or just equipment?
        RDFS.range: BRICK.OrientationShape,
    },
    BRICK.tilt: {
        SKOS.definition: Literal(
            "The direction an entity is facing in degrees above the horizon"
        ),
        RDFS.range: BRICK.TiltShape,
    },
    BRICK.coordinates: {
        SKOS.definition: Literal("The location of an entity in latitude/longitude"),
        RDFS.range: BRICK.CoordinateShape,
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
    BRICK.CoordinateShape: {
        "properties": {
            BRICK.latitude: {"datatype": XSD.float},
            BRICK.longitude: {"datatype": XSD.float},
        },
    },
    BRICK.TiltShape: {"units": [UNIT.DEG], "datatype": XSD.float},
    BRICK.OrientationShape: {
        "units": [UNIT.DEG],
        "datatype": XSD.float,
        "properties": {
            BRICK.orientationRelativeTo: {"values": ["North", "South", "East", "West"]}
        },
    },
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
}
