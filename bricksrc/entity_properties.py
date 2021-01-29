from .namespaces import BRICK, TAG, OWL, RDFS, SKOS, UNIT, PROP
from rdflib import Namespace, Literal


# define properties:
# prop:value

# for each entity property, what do we need? (these are shapes)
# - what kind of property (IdentityProperty, etc)
# - definition
# - seeAlso

# need value shapes:
# - units: (single value or enumeration)
# - datatype and/or enumeration
# - mincount / maxcaount?


entity_properties = {
    PROP.hasArea: {
        SKOS.definition: Literal("Entity has 2-dimensional area"),
        RDFS.range: PROP.AreaShape,
        "subproperties": {
            PROP.hasGrossArea: {
                SKOS.definition: Literal("Entity has gross 2-dimensional area"),
                RDFS.range: PROP.AreaShape,
            },
            PROP.hasNetArea: {
                SKOS.definition: Literal("Entity has net 2-dimensional area"),
                RDFS.range: PROP.AreaShape,
            },
        },
    },
    PROP.hasVolume: {
        SKOS.definition: Literal("Entity has 3-dimensional volume"),
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
}

shape_properties = {
    PROP.AreaShape: {"units": [UNIT.FT2, UNIT.M2]},
    PROP.VolumeShape: {"units": [UNIT.FT3, UNIT.M3]},
    PROP.PowerComplexityShape: {"values": ["real", "reactive", "apparent"]},
    PROP.PowerFlowShape: {"values": ["import", "export", "net", "absolute"]},
    PROP.PhasesShape: {"values": ["A", "B", "C", "AB", "BC", "AC", "ABC"]},
    PROP.PhaseCountShape: {"values": ["1", "2", "3", "Total"]},
    PROP.CurrentFlowTypeShape: {"values": ["AC", "DC"]},
}
