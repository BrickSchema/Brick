from .namespaces import TAG, BRICK

meter_subclasses = {
    "Electrical_Meter": {
        "tags": [TAG.Electrical, TAG.Meter, TAG.Equipment],
        "subclasses": {
            "Building_Electrical_Meter": {
                "tags": [
                    TAG.Building,
                    TAG.Electrical,
                    TAG.Meter,
                    TAG.Equipment,
                ],
                "parents": [BRICK.Building_Meter],
            }
        },
    },
    "Waste_Meter": {"tags": [TAG.Waste, TAG.Meter]},
    "Gas_Meter": {
        "tags": [TAG.Meter, TAG.Equipment, TAG.Gas],
        "subclasses": {
            "Building_Gas_Meter": {
                "tags": [TAG.Building, TAG.Gas, TAG.Meter, TAG.Equipment],
                "parents": [BRICK.Building_Meter],
                BRICK.hasSubstance: BRICK.Natural_Gas,
            }
        },
        BRICK.hasSubstance: BRICK.Natural_Gas,
    },
    "Thermal_Power_Meter": {
        "tags": [TAG.Meter, TAG.Equipment, TAG.Thermal, TAG.Power],
    },
    "Water_Meter": {
        "tags": [TAG.Meter, TAG.Equipment, TAG.Water],
        BRICK.hasSubstance: BRICK.Water,
        "subclasses": {
            "Building_Water_Meter": {
                "tags": [TAG.Building, TAG.Water, TAG.Meter, TAG.Equipment],
                "parents": [BRICK.Building_Meter],
                BRICK.hasSubstance: BRICK.Water,
            },
            "Chilled_Water_Meter": {
                "tags": [TAG.Meter, TAG.Equipment, TAG.Water, TAG.Chilled],
                BRICK.hasSubstance: BRICK.Chilled_Water,
                "subclasses": {
                    "Building_Chilled_Water_Meter": {
                        BRICK.hasSubstance: BRICK.Chilled_Water,
                        "tags": [
                            TAG.Building,
                            TAG.Chilled,
                            TAG.Water,
                            TAG.Meter,
                            TAG.Equipment,
                        ],
                        "parents": [BRICK.Building_Meter],
                    },
                },
            },
            "Hot_Water_Meter": {
                BRICK.hasSubstance: BRICK.Hot_Water,
                "tags": [TAG.Meter, TAG.Equipment, TAG.Water, TAG.Hot],
                "subclasses": {
                    "Building_Hot_Water_Meter": {
                        BRICK.hasSubstance: BRICK.Hot_Water,
                        "tags": [
                            TAG.Building,
                            TAG.Hot,
                            TAG.Water,
                            TAG.Meter,
                            TAG.Equipment,
                        ],
                        "parents": [BRICK.Building_Meter],
                    },
                },
            },
        },
    },
    "Building_Meter": {
        "tags": [TAG.Meter, TAG.Equipment, TAG.Building],
        "constraints": {BRICK.meters: [BRICK.Building]},
    },
}
