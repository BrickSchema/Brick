from .namespaces import BRICK, TAG, OWL, QUDTQK

alarm_definitions = {
    "Alarm": {
        "tags": [TAG.Point, TAG.Alarm],
        "subclasses": {
            # intermediate classes introduced by the Brick 2.0 point attribute work
            "High_Alarm": {
                "tags": [TAG.Point, TAG.High, TAG.Alarm],
            },
            "Low_Alarm": {
                "tags": [TAG.Point, TAG.Low, TAG.Alarm],
            },
            "Max_Alarm": {
                "tags": [TAG.Point, TAG.Max, TAG.Alarm],
            },
            "Min_Alarm": {
                "tags": [TAG.Point, TAG.Min, TAG.Alarm],
            },
            "Loss_Alarm": {
                "tags": [TAG.Point, TAG.Loss, TAG.Alarm],
            },
            "Low_Battery_Alarm": {
                BRICK.ofEquipment: BRICK.Battery,
                "parents": [BRICK.Low_Alarm],
                "tags": [TAG.Point, TAG.Alarm, TAG.Low, TAG.Battery],
            },
            "Air_Alarm": {
                BRICK.hasSubstance: BRICK.Air,
                "tags": [TAG.Point, TAG.Air, TAG.Alarm],
                "subclasses": {
                    "Air_Flow_Alarm": {
                        BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                        BRICK.hasSubstance: BRICK.Air,
                        "tags": [TAG.Point, TAG.Air, TAG.Alarm, TAG.Flow],
                        "subclasses": {
                            "Air_Flow_Loss_Alarm": {
                                BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                BRICK.hasSubstance: BRICK.Air,
                                "parents": [BRICK.Loss_Alarm],
                                "tags": [
                                    TAG.Point,
                                    TAG.Air,
                                    TAG.Alarm,
                                    TAG.Flow,
                                    TAG.Loss,
                                ],
                            },
                            "High_Air_Flow_Alarm": {
                                BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                BRICK.hasSubstance: BRICK.Air,
                                "parents": [BRICK.High_Alarm],
                                "tags": [
                                    TAG.Point,
                                    TAG.Air,
                                    TAG.Alarm,
                                    TAG.Flow,
                                    TAG.High,
                                ],
                            },
                            "Low_Air_Flow_Alarm": {
                                BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                BRICK.hasSubstance: BRICK.Air,
                                "parents": [BRICK.Low_Alarm],
                                "tags": [
                                    TAG.Point,
                                    TAG.Air,
                                    TAG.Alarm,
                                    TAG.Flow,
                                    TAG.Low,
                                ],
                                "subclasses": {
                                    "Low_Supply_Air_Flow_Alarm": {
                                        BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                        BRICK.hasSubstance: BRICK.Supply_Air,
                                        "parents": [BRICK.Low_Alarm],
                                        "aliases": [
                                            BRICK["Low_Discharge_Air_Flow_Alarm"]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Air,
                                            TAG.Alarm,
                                            TAG.Flow,
                                            TAG.Low,
                                            TAG.Supply,
                                            TAG.Discharge,
                                        ],
                                    },
                                },
                            },
                        },
                    }
                },
            },
            "CO2_Alarm": {
                # TODO(Brick 2.0): BRICK.hasSubstance: BRICK.CO2,  # spreadsheet puts the measured constituent here; 1.x uses hasSubstance for the medium
                "tags": [TAG.Point, TAG.CO2, TAG.Alarm],
                "subclasses": {
                    "High_CO2_Alarm": {
                        # TODO(Brick 2.0): BRICK.hasSubstance: BRICK.CO2,  # spreadsheet puts the measured constituent here; 1.x uses hasSubstance for the medium
                        "parents": [BRICK.High_Alarm],
                        "tags": [TAG.Point, TAG.High, TAG.CO2, TAG.Alarm],
                    },
                },
            },
            "Voltage_Alarm": {
                BRICK.hasQuantity: QUDTQK.Voltage,
                "tags": [TAG.Point, TAG.Voltage, TAG.Alarm],
                "subclasses": {
                    "Low_Voltage_Alarm": {
                        BRICK.hasQuantity: QUDTQK.Voltage,
                        "parents": [BRICK.Low_Alarm],
                        "tags": [TAG.Point, TAG.Low, TAG.Voltage, TAG.Alarm],
                    },
                },
            },
            "Valve_Position_Alarm": {
                BRICK.ofEquipment: BRICK.Valve,
                "tags": [TAG.Point, TAG.Valve, TAG.Position, TAG.Alarm],
            },
            "Change_Filter_Alarm": {
                "tags": [TAG.Point, TAG.Change, TAG.Filter, TAG.Alarm],
            },
            "Communication_Loss_Alarm": {
                BRICK.hasEnumeration: BRICK["EnumerationKind-CommunicationState"],
                "parents": [BRICK.Loss_Alarm],
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
                    "Sensor_Failure_Alarm": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Failure, TAG.Alarm],
                    },
                },
            },
            "Humidity_Alarm": {
                BRICK.hasQuantity: QUDTQK.RelativeHumidity,
                "tags": [TAG.Point, TAG.Humidity, TAG.Alarm],
                "subclasses": {
                    "High_Humidity_Alarm": {
                        BRICK.hasQuantity: QUDTQK.RelativeHumidity,
                        "parents": [BRICK.High_Alarm],
                        "tags": [TAG.Point, TAG.High, TAG.Humidity, TAG.Alarm],
                    },
                    "Low_Humidity_Alarm": {
                        BRICK.hasQuantity: QUDTQK.RelativeHumidity,
                        "parents": [BRICK.Low_Alarm],
                        "tags": [TAG.Point, TAG.Low, TAG.Humidity, TAG.Alarm],
                    },
                },
            },
            "Leak_Alarm": {
                "tags": [TAG.Point, TAG.Leak, TAG.Alarm],
                "subclasses": {
                    "Condensate_Leak_Alarm": {
                        BRICK.hasSubstance: BRICK.Condensate,
                        "tags": [TAG.Point, TAG.Condensate, TAG.Leak, TAG.Alarm],
                    },
                },
            },
            "Liquid_Detection_Alarm": {
                BRICK.ofProcess: BRICK.Liquid_Detection,
                "tags": [TAG.Point, TAG.Liquid, TAG.Detection, TAG.Alarm],
            },
            "Luminance_Alarm": {
                BRICK.hasQuantity: QUDTQK.Luminance,
                "tags": [TAG.Point, TAG.Luminance, TAG.Alarm],
            },
            "Maintenance_Required_Alarm": {
                BRICK.hasEnumeration: BRICK["EnumerationKind-Maintenance_Required"],
                "tags": [TAG.Point, TAG.Maintenance, TAG.Required, TAG.Alarm],
            },
            "Overload_Alarm": {"tags": [TAG.Point, TAG.Overload, TAG.Alarm]},
            "Power_Alarm": {
                BRICK.hasQuantity: QUDTQK.Power,
                "tags": [TAG.Point, TAG.Power, TAG.Alarm],
                "subclasses": {
                    "Power_Loss_Alarm": {
                        BRICK.hasQuantity: QUDTQK.Power,
                        "parents": [BRICK.Loss_Alarm],
                        "tags": [TAG.Point, TAG.Power, TAG.Loss, TAG.Alarm],
                    },
                },
            },
            "Pressure_Alarm": {
                BRICK.hasQuantity: QUDTQK.Pressure,
                "tags": [TAG.Point, TAG.Pressure, TAG.Alarm],
                "subclasses": {
                    "High_Pressure_Alarm": {
                        "tags": [TAG.Point, TAG.High, TAG.Pressure, TAG.Alarm],
                    },
                    "Low_Pressure_Alarm": {
                        "tags": [TAG.Point, TAG.Low, TAG.Pressure, TAG.Alarm],
                    },
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
                BRICK.hasQuantity: QUDTQK.Temperature,
                "tags": [TAG.Point, TAG.Temperature, TAG.Alarm],
                "subclasses": {
                    "High_Temperature_Alarm": {
                        BRICK.hasQuantity: QUDTQK.Temperature,
                        "parents": [BRICK.High_Alarm],
                        "tags": [TAG.Point, TAG.High, TAG.Temperature, TAG.Alarm],
                    },
                    "Low_Temperature_Alarm": {
                        BRICK.hasQuantity: QUDTQK.Temperature,
                        "parents": [BRICK.Low_Alarm],
                        "tags": [TAG.Point, TAG.Low, TAG.Temperature, TAG.Alarm],
                    },
                    "Water_Temperature_Alarm": {
                        BRICK.hasQuantity: QUDTQK.Temperature,
                        BRICK.hasSubstance: BRICK.Water,
                        "tags": [TAG.Point, TAG.Water, TAG.Temperature, TAG.Alarm],
                        "parents": [BRICK.Water_Alarm],
                        "subclasses": {
                            "Entering_Water_Temperature_Alarm": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                BRICK.hasSubstance: BRICK.Entering_Water,
                                "tags": [
                                    TAG.Point,
                                    TAG.Entering,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Alarm,
                                ],
                            },
                            "Leaving_Water_Temperature_Alarm": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                BRICK.hasSubstance: BRICK.Leaving_Water,
                                "tags": [
                                    TAG.Point,
                                    TAG.Leaving,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Alarm,
                                ],
                            },
                        },
                    },
                    "Air_Temperature_Alarm": {
                        BRICK.hasQuantity: QUDTQK.Temperature,
                        BRICK.hasSubstance: BRICK.Air,
                        "tags": [TAG.Point, TAG.Air, TAG.Temperature, TAG.Alarm],
                        "parents": [BRICK.Air_Alarm],
                        "subclasses": {
                            "Supply_Air_Temperature_Alarm": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                BRICK.hasSubstance: BRICK.Supply_Air,
                                "aliases": [BRICK["Discharge_Air_Temperature_Alarm"]],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Alarm,
                                ],
                                "subclasses": {
                                    "High_Supply_Air_Temperature_Alarm": {
                                        BRICK.hasQuantity: QUDTQK.Temperature,
                                        BRICK.hasSubstance: BRICK.Supply_Air,
                                        "aliases": [
                                            BRICK[
                                                "High_Discharge_Air_Temperature_Alarm"
                                            ]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.High,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Alarm,
                                        ],
                                        "parents": [
                                            BRICK.High_Temperature_Alarm,
                                            BRICK.High_Alarm,
                                        ],
                                    },
                                    "Low_Supply_Air_Temperature_Alarm": {
                                        BRICK.hasQuantity: QUDTQK.Temperature,
                                        BRICK.hasSubstance: BRICK.Supply_Air,
                                        "aliases": [
                                            BRICK["Low_Discharge_Air_Temperature_Alarm"]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Low,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Alarm,
                                        ],
                                        "parents": [
                                            BRICK.Low_Temperature_Alarm,
                                            BRICK.Low_Alarm,
                                        ],
                                    },
                                },
                            },
                            "Return_Air_Temperature_Alarm": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                BRICK.hasSubstance: BRICK.Return_Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Return,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Alarm,
                                ],
                                "subclasses": {
                                    "High_Return_Air_Temperature_Alarm": {
                                        BRICK.hasQuantity: QUDTQK.Temperature,
                                        BRICK.hasSubstance: BRICK.Return_Air,
                                        "tags": [
                                            TAG.Point,
                                            TAG.High,
                                            TAG.Return,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Alarm,
                                        ],
                                        "parents": [
                                            BRICK.High_Temperature_Alarm,
                                            BRICK.High_Alarm,
                                        ],
                                    },
                                    "Low_Return_Air_Temperature_Alarm": {
                                        BRICK.hasQuantity: QUDTQK.Temperature,
                                        BRICK.hasSubstance: BRICK.Return_Air,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Low,
                                            TAG.Return,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Alarm,
                                        ],
                                        "parents": [
                                            BRICK.Low_Temperature_Alarm,
                                            BRICK.Low_Alarm,
                                        ],
                                    },
                                },
                            },
                        },
                    },
                },
            },
            "Smoke_Alarm": {
                BRICK.hasSubstance: BRICK.Smoke,
                "tags": [TAG.Point, TAG.Smoke, TAG.Alarm],
                "subclasses": {
                    "Smoke_Detection_Alarm": {
                        BRICK.ofProcess: BRICK.Smoke_Detection,
                        "tags": [TAG.Point, TAG.Smoke, TAG.Detection, TAG.Alarm],
                        "subclasses": {
                            "Supply_Air_Smoke_Detection_Alarm": {
                                BRICK.hasSubstance: BRICK.Supply_Air,
                                BRICK.ofProcess: BRICK.Smoke_Detection,
                                "aliases": [
                                    BRICK["Discharge_Air_Smoke_Detection_Alarm"]
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
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
                BRICK.hasSubstance: BRICK.Water,
                "tags": [TAG.Point, TAG.Water, TAG.Alarm],
                "subclasses": {
                    "Deionized_Water_Alarm": {
                        BRICK.hasSubstance: BRICK.Deionized_Water,
                        "tags": [TAG.Point, TAG.Deionized, TAG.Water, TAG.Alarm],
                    },
                    "No_Water_Alarm": {
                        "tags": [TAG.Point, TAG.No, TAG.Water, TAG.Alarm],
                    },
                    "Water_Loss_Alarm": {
                        BRICK.hasSubstance: BRICK.Water,
                        "parents": [BRICK.Loss_Alarm],
                        "tags": [TAG.Point, TAG.Loss, TAG.Water, TAG.Alarm],
                    },
                    "Water_Level_Alarm": {
                        BRICK.hasSubstance: BRICK.Water,
                        "tags": [TAG.Water, TAG.Level, TAG.Alarm, TAG.Point],
                        "subclasses": {
                            "Collection_Basin_Water_Level_Alarm": {
                                BRICK.hasSubstance: BRICK.Collection_Basin_Water,
                                "tags": [
                                    TAG.Collection,
                                    TAG.Basin,
                                    TAG.Water,
                                    TAG.Level,
                                    TAG.Alarm,
                                    TAG.Point,
                                ],
                            },
                            "Max_Water_Level_Alarm": {
                                BRICK.hasSubstance: BRICK.Water,
                                "parents": [BRICK.Max_Alarm],
                                "tags": [
                                    TAG.Point,
                                    TAG.Max,
                                    TAG.Water,
                                    TAG.Level,
                                    TAG.Alarm,
                                ],
                            },
                            "Min_Water_Level_Alarm": {
                                BRICK.hasSubstance: BRICK.Water,
                                "parents": [BRICK.Min_Alarm],
                                "tags": [
                                    TAG.Point,
                                    TAG.Min,
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
