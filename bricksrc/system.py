from rdflib import Literal
from .namespaces import BRICK, TAG, OWL, RDFS

system_subclasses = {
    "Domestic_Hot_Water_System": {
        "tags": [TAG.Domestic, TAG.Water, TAG.Hot, TAG.System]
    },
    "Electrical_System": {"tags": [TAG.Electrical, TAG.System]},
    "Gas_System": {"tags": [TAG.Gas, TAG.System]},
    "HVAC_System": {"tags": [TAG.HVAC, TAG.System]},
    "Heating_Ventilation_Air_Conditioning_System": {
        OWL.equivalentClass: BRICK["HVAC_System"],
        "tags": [TAG.Heat, TAG.Ventilation, TAG.Air, TAG.Conditioning, TAG.System],
        "subclasses": {
            "Air_System": {
                "tags": [TAG.Air, TAG.System],
                "subclasses": {
                    "Ventilation_Air_System": {
                        "tags": [
                            TAG.Ventilation,
                            TAG.Air,
                            TAG.System,
                        ]
                    },
                },
            },
            "Steam_System": {"tags": [TAG.Steam, TAG.System]},
            "Water_System": {
                "tags": [TAG.Water, TAG.System],
                "subclasses": {
                    "Chilled_Water_System": {
                        "tags": [TAG.Water, TAG.Chilled, TAG.System],
                    },
                    "Hot_Water_System": {
                        "tags": [TAG.Water, TAG.Hot, TAG.System],
                        "subclasses": {
                            "Preheat_Hot_Water_System": {
                                "tags": [
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.System,
                                    TAG.Preheat,
                                    TAG.System,
                                ]
                            },
                            "Reheat_Hot_Water_System": {
                                "tags": [
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.System,
                                    TAG.Reheat,
                                    TAG.System,
                                ]
                            },
                            "Radiation_Hot_Water_System": {
                                "tags": [
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.System,
                                    TAG.Radiation,
                                    TAG.System,
                                ]
                            },
                            "Heat_Recovery_Hot_Water_System": {
                                "tags": [
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.System,
                                    TAG.Heat,
                                    TAG.Recovery,
                                    TAG.System,
                                ]
                            },
                        },
                    },
                    "Condenser_Water_System": {
                        "tags": [TAG.Condenser, TAG.Water, TAG.System]
                    },
                },
            },
        },
    },
    "Lighting_System": {"tags": [TAG.Lighting, TAG.System]},
    "Safety_System": {
        "tags": [TAG.Safety, TAG.System],
        "subclasses": {
            "Fire_Safety_System": {"tags": [TAG.Fire, TAG.Safety, TAG.System]},
            "Emergency_Power_Off_System": {
                "tags": [TAG.Emergency, TAG.Power, TAG.Off, TAG.System],
            },
            "Emergency_Air_Flow_System": {
                "tags": [TAG.Emergency, TAG.Air, TAG.Flow, TAG.System],
            },
        },
    },
    "Shading_System": {"tags": [TAG.Shade, TAG.System]},
}
