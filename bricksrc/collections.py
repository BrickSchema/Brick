from .namespaces import TAG, OWL, BRICK

system_subclasses = {
    "Automatic_Tint_Window_Array": {
        "tags": [TAG.System, TAG.Tint, TAG.Array, TAG.Shade]
    },
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
                        "subclasses": {
                            "PV_Generation_System": {
                                "tags": [TAG.Photovoltaic, TAG.Generation, TAG.System],
                            }
                        },
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
    "Heating_Ventilation_Air_Conditioning_System": {
        "tags": [
            TAG.Heat,
            TAG.Ventilation,
            TAG.Air,
            TAG.Conditioning,
            TAG.HVAC,
            TAG.System,
        ],
        "aliases": [BRICK["HVAC_System"]],
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
            "VRF_System": {"tags": [TAG.Variable, TAG.Refrigerant, TAG.Flow, TAG.System]},
            "Refrigeration_System": {"tags": [TAG.Refrigeration, TAG.System]},
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
    "Shading_System": {
        "tags": [TAG.Shade, TAG.System],
        "subclasses": {
            "Blind_Group": {"tags": [TAG.Shade, TAG.System, TAG.Blind, TAG.Group]},
        },
    },
}

loop_subclasses = {
    "Air_Loop": {"tags": [TAG.Air, TAG.Loop]},
    "Water_Loop": {
        "tags": [TAG.Water, TAG.Loop],
        "subclasses": {
            "Hot_Water_Loop": {"tags": [TAG.Hot, TAG.Water, TAG.Loop]},
            "Chilled_Water_Loop": {"tags": [TAG.Chilled, TAG.Water, TAG.Loop]},
            "Domestic_Water_Loop": {"tags": [TAG.Domestic, TAG.Water, TAG.Loop]},
            "Condenser_Water_Loop": {"tags": [TAG.Condenser, TAG.Water, TAG.Loop]},
        },
    },
}

collection_classes = {
    "Portfolio": {
        "tags": [TAG.Collection, TAG.Portfolio],
        "constraints": {BRICK.hasPart: [BRICK.Site]},
    },
    "System": {
        "tags": [TAG.Collection, TAG.System],
        "subclasses": system_subclasses,
        "constraints": {
            BRICK.hasPart: [
                BRICK.Equipment,
                BRICK.Point,
                BRICK.Loop,
                BRICK.System,
                BRICK.Location,
                BRICK.PV_Array,
            ]
        },
    },
    "Loop": {
        "tags": [TAG.Collection, TAG.Loop],
        "subclasses": loop_subclasses,
        "constraints": {BRICK.hasPart: [BRICK.Equipment, BRICK.Point, BRICK.Location]},
    },
    "Photovoltaic_Array": {
        "tags": [TAG.Collection, TAG.Photovoltaic, TAG.PV, TAG.Array],
        "aliases": [BRICK["PV_Array"]],
        "constraints": {BRICK.hasPart: [BRICK.PV_Panel]},
    },
    "Electric_Vehicle_Charging_Hub": {
        "tags": [TAG.Collection, TAG.Electric, TAG.Vehicle, TAG.Charging, TAG.Hub],
        "aliases": [BRICK["EV_Charging_Hub"]],
        "constraints": {BRICK.hasPart: [BRICK.Electric_Vehicle_Charging_Station]},
    },
}
