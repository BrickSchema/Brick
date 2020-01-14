from .namespaces import TAG, BRICK

alarm_definitions = {
    "Alarm": {
        "tags": [TAG.Alarm],
        "subclasses": {
            "Air_Alarm": {
                "tags": [TAG.Air, TAG.Alarm],
            },
            "CO2_Alarm": {
                "tags": [TAG.CO2, TAG.Alarm],
                "subclasses": {
                    "High_CO2_Alarm": {
                        "tags": [TAG.High, TAG.CO2, TAG.Alarm],
                    },
                },
            },
            "Change_Filter_Alarm": {
                "tags": [TAG.Change, TAG.Filter, TAG.Alarm],
            },
            "Communication_Loss_Alarm": {
                "tags": [TAG.Communication, TAG.Loss, TAG.Alarm],
            },
            "Cycle_Alarm": {
                "tags": [TAG.Cycle, TAG.Alarm],
                "subclasses": {
                    "Short_Cycle_Alarm": {
                        "tags": [TAG.Short, TAG.Cycle, TAG.Alarm],
                    },
                },
            },
            "Emergency_Alarm": {
                "tags": [TAG.Emergency, TAG.Alarm],
                "subclasses": {
                    "Emergency_Generator_Alarm": {
                        "tags": [TAG.Generator, TAG.Emergency, TAG.Alarm],
                    },
                    "Emergency_Power_Loss_Alarm": {
                        "tags": [TAG.Power, TAG.Loss, TAG.Emergency, TAG.Alarm],
                        "parents": [BRICK.Power_Loss_Alarm],
                    },
                },
            },
            "Failure_Alarm": {
                "tags": [TAG.Failure, TAG.Alarm],
                "subclasses": {
                    "Unit_Failure_Alarm": {
                        "tags": [TAG.Unit, TAG.Failure, TAG.Alarm],
                    },
                },
            },
            "Humidity_Alarm": {
                "tags": [TAG.Humidity, TAG.Alarm],
                "subclasses": {
                    "High_Humidity_Alarm": {
                        "tags": [TAG.High, TAG.Humidity, TAG.Alarm],
                    },
                    "Low_Humidity_Alarm": {
                        "tags": [TAG.Low, TAG.Humidity, TAG.Alarm],
                    },
                },
            },
            "Leak_Alarm": {
                "tags": [TAG.Leak, TAG.Alarm],
                "subclasses": {
                    "Condensate_Leak_Alarm": {
                        "tags": [TAG.Condensate, TAG.Leak, TAG.Alarm],
                    },
                },
            },
            "Liquid_Detected_Alarm": {
                "tags": [TAG.Liquid, TAG.Detected, TAG.Alarm],
            },
            "Luminance_Alarm": {
                "tags": [TAG.Luminance, TAG.Alarm],
            },
            "Maintenance_Required_Alarm": {
                "tags": [TAG.Maintenance, TAG.Required, TAG.Alarm],
            },
            "Overload_Alarm": {
                "tags": [TAG.Overload, TAG.Alarm],
            },
            "Power_Alarm": {
                "tags": [TAG.Power, TAG.Alarm],
                "subclasses": {
                    "Power_Loss_Alarm": {
                        "tags": [TAG.Power, TAG.Loss, TAG.Alarm],
                    },
                },
            },
            "Pressure_Alarm": {
                "tags": [TAG.Pressure, TAG.Alarm],
                "subclasses": {
                    "High_Head_Pressure_Alarm": {},
                    "Low_Suction_Pressure_Alarm": {},
                },
            },
            "Temperature_Alarm": {
                "tags": [TAG.Temperature, TAG.Alarm],
                "subclasses": {
                    "High_Temperature_Alarm": {
                        "tags": [TAG.High, TAG.Temperature, TAG.Alarm],
                    },
                    "Low_Temperature_Alarm": {
                        "tags": [TAG.Low, TAG.Temperature, TAG.Alarm],
                    },
                    "Water_Temperature_Alarm": {
                        "tags": [TAG.Water, TAG.Temperature, TAG.Alarm],
                        "parents": [BRICK.Water_Alarm],
                        "subclasses": {
                            "Discharge_Water_Temperature_Alarm": {
                                "tags": [TAG.Discharge, TAG.Water,
                                         TAG.Temperature, TAG.Alarm],
                            },
                            "Supply_Water_Temperature_Alarm": {
                                "tags": [TAG.Supply, TAG.Water,
                                         TAG.Temperature, TAG.Alarm],
                            },
                        },
                    },
                    "Air_Temperature_Alarm": {
                        "tags": [TAG.Air, TAG.Temperature, TAG.Alarm],
                        "parents": [BRICK.Air_Alarm],
                        "subclasses": {
                            "Discharge_Air_Temperature_Alarm": {
                                "tags": [TAG.Discharge, TAG.Air,
                                         TAG.Temperature, TAG.Alarm],
                                "subclasses": {
                                    "High_Discharge_Air_Temperature_Alarm": {
                                        "tags": [TAG.High, TAG.Discharge,
                                                 TAG.Air, TAG.Temperature,
                                                 TAG.Alarm],
                                        "parents": [BRICK.High_Temperature_Alarm],
                                    },
                                },
                            },
                            "Supply_Air_Temperature_Alarm": {
                                "tags": [TAG.Supply, TAG.Air,
                                         TAG.Temperature, TAG.Alarm],
                            },
                            "Return_Air_Temperature_Alarm": {
                                "tags": [TAG.Return, TAG.Air, TAG.Temperature, TAG.Alarm],
                                "subclasses": {
                                    "High_Return_Air_Temperature_Alarm": {
                                        "tags": [TAG.High, TAG.Return, TAG.Air, TAG.Temperature, TAG.Alarm],
                                        "parents": [BRICK.High_Temperature_Alarm],
                                    },
                                    "Low_Return_Air_Temperature_Alarm": {
                                        "tags": [TAG.Low, TAG.Return, TAG.Air, TAG.Temperature, TAG.Alarm],
                                        "parents": [BRICK.Low_Temperature_Alarm],
                                    },
                                },
                            },
                        },
                    },
                }
            },
            "Smoke_Alarm": {
                "tags": [TAG.Smoke, TAG.Alarm],
                "subclasses": {
                    "Smoke_Detected_Alarm": {
                        "tags": [TAG.Smoke, TAG.Detected, TAG.Alarm],
                        "subclasses": {
                            "Discharge_Air_Smoke_Detected_Alarm": {
                                "tags": [TAG.Discharge, TAG.Air, TAG.Smoke, TAG.Detected, TAG.Alarm],
                                "parents": [BRICK.Air_Alarm],
                            },
                        },
                    },
                },
            },
            "Water_Alarm": {
                "tags": [TAG.Water, TAG.Alarm],
                "subclasses": {
                    "Deionized_Water_Alarm": {
                        "tags": [TAG.Deionized, TAG.Water, TAG.Alarm],
                    },
                    "No_Water_Alarm": {
                        "tags": [TAG.No, TAG.Water, TAG.Alarm],
                    },
                    "Water_Loss_Alarm": {
                        "tags": [TAG.Loss, TAG.Water, TAG.Alarm],
                    },
                },
            },
        },
    },
}
