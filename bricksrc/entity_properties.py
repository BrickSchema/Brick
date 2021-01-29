from .namespaces import BRICK, TAG, OWL, RDFS, SKOS, UNIT, PROP, XSD
from rdflib import Namespace, Literal

# TODO: aggregation

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
    # special stuff
    PROP.aggregate: {
        SKOS.definition: Literal(
            "Description of how the dta for this point is aggregated"
        ),
        RDFS.domain: BRICK.Point,
        RDFS.range: PROP.AggregationShape,
    },
}

shape_properties = {
    PROP.AreaShape: {"units": [UNIT.FT2, UNIT.M2], "datatype": XSD.float},
    PROP.VolumeShape: {"units": [UNIT.FT3, UNIT.M3], "datatype": XSD.float},
    PROP.PowerComplexityShape: {"values": ["real", "reactive", "apparent"]},
    PROP.PowerFlowShape: {"values": ["import", "export", "net", "absolute"]},
    PROP.PhasesShape: {"values": ["A", "B", "C", "AB", "BC", "AC", "ABC"]},
    PROP.PhaseCountShape: {"values": ["1", "2", "3", "Total"]},
    PROP.CurrentFlowTypeShape: {"values": ["AC", "DC"]},
    PROP.StageShape: {"values": [1, 2, 3, 4]},
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
