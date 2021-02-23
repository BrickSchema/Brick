from .namespaces import BRICK, TAG, OWL

alarm_definitions = {
    "Alarm": {
        "tags": [TAG.Point, TAG.Alarm],
        "subclasses": {
            "Air_Alarm": {
                "tags": [TAG.Point, TAG.Air, TAG.Alarm],
                "subclasses": {
                    "Air_Flow_Loss_Alarm": {
                        "tags": [TAG.Point, TAG.Air, TAG.Alarm, TAG.Flow, TAG.Loss],
                    }
                },
            },
            "CO2_Alarm": {
                "tags": [TAG.Point, TAG.CO2, TAG.Alarm],
                "subclasses": {
                    "High_CO2_Alarm": {
                        "tags": [TAG.Point, TAG.High, TAG.CO2, TAG.Alarm],
                    },
                },
            },
            "Change_Filter_Alarm": {
                "tags": [TAG.Point, TAG.Change, TAG.Filter, TAG.Alarm],
            },
            "Communication_Loss_Alarm": {
                "tags": [TAG.Point, TAG.Communication, TAG.Loss, TAG.Alarm],
            },
            "Cycle_Alarm": {
                "tags": [TAG.Point, TAG.Cycle, TAG.Alarm],
                "subclasses": {
                    "Short_Cycle_Alarm": {
                        "tags": [TAG.Point, TAG.Short, TAG.Cycle, TAG.Alarm],
                    },
                },
            },
            "Emergency_Alarm": {
                "tags": [TAG.Point, TAG.Emergency, TAG.Alarm],
                "subclasses": {
                    "Emergency_Generator_Alarm": {
                        "tags": [TAG.Point, TAG.Generator, TAG.Emergency, TAG.Alarm],
                    },
                },
            },
            "Failure_Alarm": {
                "tags": [TAG.Point, TAG.Failure, TAG.Alarm],
                "subclasses": {
                    "Unit_Failure_Alarm": {
                        "tags": [TAG.Point, TAG.Unit, TAG.Failure, TAG.Alarm],
                    },
                },
            },
            "Humidity_Alarm": {
                "tags": [TAG.Point, TAG.Humidity, TAG.Alarm],
                "subclasses": {
                    "High_Humidity_Alarm": {
                        "tags": [TAG.Point, TAG.High, TAG.Humidity, TAG.Alarm],
                    },
                    "Low_Humidity_Alarm": {
                        "tags": [TAG.Point, TAG.Low, TAG.Humidity, TAG.Alarm],
                    },
                },
            },
            "Leak_Alarm": {
                "tags": [TAG.Point, TAG.Leak, TAG.Alarm],
                "subclasses": {
                    "Condensate_Leak_Alarm": {
                        "tags": [TAG.Point, TAG.Condensate, TAG.Leak, TAG.Alarm],
                    },
                },
            },
            "Liquid_Detection_Alarm": {
                "tags": [TAG.Point, TAG.Liquid, TAG.Detection, TAG.Alarm],
            },
            "Luminance_Alarm": {"tags": [TAG.Point, TAG.Luminance, TAG.Alarm]},
            "Maintenance_Required_Alarm": {
                "tags": [TAG.Point, TAG.Maintenance, TAG.Required, TAG.Alarm],
            },
            "Overload_Alarm": {"tags": [TAG.Point, TAG.Overload, TAG.Alarm]},
            "Power_Alarm": {
                "tags": [TAG.Point, TAG.Power, TAG.Alarm],
                "subclasses": {
                    "Power_Loss_Alarm": {
                        "tags": [TAG.Point, TAG.Power, TAG.Loss, TAG.Alarm],
                    },
                },
            },
            "Pressure_Alarm": {
                "tags": [TAG.Point, TAG.Pressure, TAG.Alarm],
                "subclasses": {
                    "High_Head_Pressure_Alarm": {
                        "tags": [
                            TAG.Point,
                            TAG.High,
                            TAG.Head,
                            TAG.Pressure,
                            TAG.Alarm,
                        ],
                    },
                    "Low_Suction_Pressure_Alarm": {
                        "tags": [
                            TAG.Point,
                            TAG.Low,
                            TAG.Suction,
                            TAG.Pressure,
                            TAG.Alarm,
                        ],
                    },
                },
            },
            "Temperature_Alarm": {
                "tags": [TAG.Point, TAG.Temperature, TAG.Alarm],
                "subclasses": {
                    "High_Temperature_Alarm": {
                        "tags": [TAG.Point, TAG.High, TAG.Temperature, TAG.Alarm],
                    },
                    "Low_Temperature_Alarm": {
                        "tags": [TAG.Point, TAG.Low, TAG.Temperature, TAG.Alarm],
                    },
                    "Water_Temperature_Alarm": {
                        "tags": [TAG.Point, TAG.Water, TAG.Temperature, TAG.Alarm],
                        "parents": [BRICK.Water_Alarm],
                        "subclasses": {
                            "Discharge_Water_Temperature_Alarm": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Alarm,
                                ],
                            },
                            "Supply_Water_Temperature_Alarm": {
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Water_Temperature_Alarm"
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Alarm,
                                ],
                            },
                        },
                    },
                    "Air_Temperature_Alarm": {
                        "tags": [TAG.Point, TAG.Air, TAG.Temperature, TAG.Alarm],
                        "parents": [BRICK.Air_Alarm],
                        "subclasses": {
                            "Discharge_Air_Temperature_Alarm": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Alarm,
                                ],
                                "subclasses": {
                                    "High_Discharge_Air_Temperature_Alarm": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.High,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Alarm,
                                        ],
                                        "parents": [BRICK.High_Temperature_Alarm],
                                    },
                                },
                            },
                            "Supply_Air_Temperature_Alarm": {
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Air_Temperature_Alarm"
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Alarm,
                                ],
                            },
                            "Return_Air_Temperature_Alarm": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Return,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Alarm,
                                ],
                                "subclasses": {
                                    "High_Return_Air_Temperature_Alarm": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.High,
                                            TAG.Return,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Alarm,
                                        ],
                                        "parents": [BRICK.High_Temperature_Alarm],
                                    },
                                    "Low_Return_Air_Temperature_Alarm": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Low,
                                            TAG.Return,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Alarm,
                                        ],
                                        "parents": [BRICK.Low_Temperature_Alarm],
                                    },
                                },
                            },
                        },
                    },
                },
            },
            "Smoke_Alarm": {
                "tags": [TAG.Point, TAG.Smoke, TAG.Alarm],
                "subclasses": {
                    "Smoke_Detection_Alarm": {
                        "tags": [TAG.Point, TAG.Smoke, TAG.Detection, TAG.Alarm],
                        "subclasses": {
                            "Discharge_Air_Smoke_Detection_Alarm": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Smoke,
                                    TAG.Detection,
                                    TAG.Alarm,
                                ],
                                "parents": [BRICK.Air_Alarm],
                            },
                        },
                    },
                },
            },
            "Water_Alarm": {
                "tags": [TAG.Point, TAG.Water, TAG.Alarm],
                "subclasses": {
                    "Deionized_Water_Alarm": {
                        "tags": [TAG.Point, TAG.Deionized, TAG.Water, TAG.Alarm],
                    },
                    "No_Water_Alarm": {
                        "tags": [TAG.Point, TAG.No, TAG.Water, TAG.Alarm],
                    },
                    "Water_Loss_Alarm": {
                        "tags": [TAG.Point, TAG.Loss, TAG.Water, TAG.Alarm],
                    },
                    "Water_Level_Alarm": {
                        "tags": [TAG.Water, TAG.Level, TAG.Alarm, TAG.Point],
                        "subclasses": {
                            "Collection_Basin_Water_Level_Alarm": {
                                "tags": [
                                    TAG.Collection,
                                    TAG.Basin,
                                    TAG.Water,
                                    TAG.Level,
                                    TAG.Alarm,
                                    TAG.Point,
                                ]
                            },
                            "Min_Water_Level_Alarm": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Min,
                                    TAG.Water,
                                    TAG.Level,
                                    TAG.Alarm,
                                ]
                            },
                            "Max_Water_Level_Alarm": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Max,
                                    TAG.Water,
                                    TAG.Level,
                                    TAG.Alarm,
                                ],
                            },
                        },
                    },
                },
            },
        },
    },
}
