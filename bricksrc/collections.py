from .namespaces import TAG, OWL, BRICK

system_subclasses = {
    "Domestic_Hot_Water_System": {
        "tags": [TAG.Domestic, TAG.Water, TAG.Hot, TAG.System]
    },
    "Electrical_System": {
        "tags": [TAG.Electrical, TAG.System],
        "subclasses": {
            "Energy_System": {
                "tags": [TAG.Energy, TAG.System],
                "subclasses": {
                    "Energy_Generation_System": {
                        "tags": [TAG.Energy, TAG.Generation, TAG.System],
                        "subclasses": {"PV_Generation_System": {}},
                    },
                    "Energy_Storage_System": {
                        "tags": [TAG.Energy, TAG.Storage, TAG.System],
                        "subclasses": {
                            "Battery_Energy_Storage_System": {
                                "tags": [
                                    TAG.Battery,
                                    TAG.Energy,
                                    TAG.Storage,
                                    TAG.System,
                                ],
                            },
                        },
                    },
                },
            }
        },
    },
    "Gas_System": {"tags": [TAG.Gas, TAG.System]},
    "HVAC_System": {"tags": [TAG.HVAC, TAG.System]},
    "Heating_Ventilation_Air_Conditioning_System": {
        OWL.equivalentClass: BRICK["HVAC_System"],
        "tags": [TAG.Heat, TAG.Ventilation, TAG.Air, TAG.Conditioning, TAG.System],
        "subclasses": {
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

loop_subclasses = {
    "Air_Loop": {"tags": [TAG.Air, TAG.Loop]},
    "Hot_Water_Loop": {"tags": [TAG.Hot, TAG.Water, TAG.Loop]},
    "Chilled_Water_Loop": {"tags": [TAG.Chilled, TAG.Water, TAG.Loop]},
}

collection_classes = {
    "Portfolio": {
        "tags": [TAG.Collection, TAG.Portfolio],
        "constraints": {BRICK.hasPart: [BRICK.Site]},
    },
    "System": {
        "tags": [TAG.Collection, TAG.System],
        "subclasses": system_subclasses,
        "constraints": {BRICK.hasPart: [BRICK.Equipment, BRICK.Point, BRICK.Loop]},
    },
    "Loop": {
        "tags": [TAG.Collection, TAG.Loop],
        "subclasses": loop_subclasses,
        "constraints": {BRICK.hasPart: [BRICK.Equipment, BRICK.Point]},
    },
    "Photovoltaic_Array": {
        "tags": [TAG.Collection, TAG.Photovoltaic, TAG.Array],
        "constraints": {BRICK.hasPart: [BRICK.PV_Panel]},
    },
}
