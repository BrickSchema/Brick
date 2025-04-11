from .namespaces import TAG, BRICK, RDFS, QUDTQK
from rdflib import Literal

setpoint_definitions = {
    "Setpoint": {
        RDFS.seeAlso: Literal(
            "https://xp20.ashrae.org/terminology/index.php?term=setpoint"
        ),
        "tags": [TAG.Point, TAG.Setpoint],
        "subclasses": {
            "Current_Ratio_Setpoint": {
                BRICK.hasQuantity: QUDTQK.ElectricCurrent,
                "tags": [TAG.Point, TAG.Setpoint, TAG.Current, TAG.Electric, TAG.Ratio],
            },
            "Voltage_Ratio_Setpoint": {
                BRICK.hasQuantity: QUDTQK.Voltage,
                "tags": [TAG.Point, TAG.Setpoint, TAG.Voltage, TAG.Electric, TAG.Ratio],
            },
            "Frequency_Setpoint": {
                "tags": [TAG.Point, TAG.Setpoint, TAG.Frequency],
                BRICK.hasQuantity: QUDTQK.Frequency,
            },
            "Illuminance_Setpoint": {
                BRICK.hasQuantity: QUDTQK.Illuminance,
                "tags": [TAG.Point, TAG.Setpoint, TAG.Illuminance],
            },
            "Enthalpy_Setpoint": {
                BRICK.hasQuantity: QUDTQK.Enthalpy,
                "tags": [TAG.Point, TAG.Setpoint, TAG.Enthalpy],
            },
            "Dewpoint_Setpoint": {
                BRICK.hasQuantity: QUDTQK.DewPointTemperature,
                "tags": [TAG.Point, TAG.Dewpoint, TAG.Setpoint],
            },
            "Demand_Setpoint": {
                "tags": [TAG.Point, TAG.Demand, TAG.Setpoint],
                BRICK.hasQuantity: QUDTQK.Power,
                "subclasses": {
                    "Cooling_Demand_Setpoint": {
                        "tags": [TAG.Point, TAG.Cool, TAG.Demand, TAG.Setpoint],
                    },
                    "Heating_Demand_Setpoint": {
                        "tags": [TAG.Point, TAG.Heat, TAG.Demand, TAG.Setpoint],
                    },
                    "Preheat_Demand_Setpoint": {
                        "tags": [TAG.Point, TAG.Preheat, TAG.Demand, TAG.Setpoint],
                    },
                    "Air_Flow_Demand_Setpoint": {
                        BRICK.hasSubstance: BRICK.Air,
                        BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                        "tags": [
                            TAG.Point,
                            TAG.Air,
                            TAG.Flow,
                            TAG.Demand,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Supply_Air_Flow_Demand_Setpoint": {
                                BRICK.hasSubstance: [
                                    BRICK.Supply_Air,
                                    BRICK.Discharge_Air,
                                ],
                                BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                "aliases": [
                                    BRICK["Discharge_Air_Flow_Demand_Setpoint"]
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Demand,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                },
            },
            "Damper_Position_Setpoint": {
                BRICK.hasQuantity: BRICK.Position,
                "tags": [TAG.Point, TAG.Damper, TAG.Position, TAG.Setpoint],
            },
            "Deadband_Setpoint": {
                "tags": [TAG.Point, TAG.Deadband, TAG.Setpoint],
                BRICK.hasQuantity: QUDTQK.Dimensionless,
                "subclasses": {
                    "Humidity_Deadband_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.RelativeHumidity,
                        "tags": [TAG.Point, TAG.Deadband, TAG.Setpoint, TAG.Humidity],
                    },
                    "Temperature_Deadband_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.Temperature,
                        "subclasses": {
                            "Occupied_Cooling_Temperature_Deadband_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                "tags": [
                                    TAG.Point,
                                    TAG.Occupied,
                                    TAG.Cool,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Cooling_Temperature_Setpoint],
                            },
                            "Occupied_Heating_Temperature_Deadband_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                "tags": [
                                    TAG.Point,
                                    TAG.Occupied,
                                    TAG.Heat,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Heating_Temperature_Setpoint],
                            },
                            "Unoccupied_Cooling_Temperature_Deadband_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Unoccupied,
                                    TAG.Cool,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Cooling_Temperature_Setpoint],
                            },
                            "Unoccupied_Heating_Temperature_Deadband_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Unoccupied,
                                    TAG.Heat,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Heating_Temperature_Setpoint],
                            },
                            "Supply_Air_Temperature_Deadband_Setpoint": {
                                BRICK.hasSubstance: [
                                    BRICK.Supply_Air,
                                    BRICK.Discharge_Air,
                                ],
                                BRICK.hasSubstance: [
                                    BRICK.Supply_Air,
                                    BRICK.Discharge_Air,
                                ],
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                "aliases": [
                                    BRICK["Discharge_Air_Temperature_Deadband_Setpoint"]
                                ],
                                "subclasses": {
                                    "Heating_Supply_Air_Temperature_Deadband_Setpoint": {
                                        "aliases": [
                                            BRICK[
                                                "Heating_Discharge_Air_Temperature_Deadband_Setpoint"
                                            ]
                                        ],
                                        BRICK.hasQuantity: QUDTQK.Temperature,
                                        BRICK.hasSubstance: BRICK.Discharge_Air,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Heat,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Deadband,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Discharge_Air_Temperature_Heating_Setpoint,
                                            BRICK.Heating_Temperature_Setpoint,
                                        ],
                                    },
                                    "Cooling_Supply_Air_Temperature_Deadband_Setpoint": {
                                        "aliases": [
                                            BRICK[
                                                "Cooling_Discharge_Air_Temperature_Deadband_Setpoint"
                                            ]
                                        ],
                                        BRICK.hasQuantity: QUDTQK.Temperature,
                                        BRICK.hasSubstance: BRICK.Discharge_Air,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Cool,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Deadband,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Discharge_Air_Temperature_Cooling_Setpoint,
                                            BRICK.Cooling_Temperature_Setpoint,
                                        ],
                                    },
                                },
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [
                                    BRICK.Discharge_Air_Temperature_Setpoint,
                                    BRICK.Air_Temperature_Setpoint,
                                ],
                            },
                            "Entering_Water_Temperature_Deadband_Setpoint": {
                                BRICK.hasSubstance: BRICK.Entering_Water,
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                "tags": [
                                    TAG.Point,
                                    TAG.Entering,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Entering_Water_Temperature_Setpoint],
                            },
                            "Leaving_Water_Temperature_Deadband_Setpoint": {
                                BRICK.hasSubstance: BRICK.Leaving_Water,
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                "tags": [
                                    TAG.Point,
                                    TAG.Leaving,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Leaving_Water_Temperature_Setpoint],
                            },
                        },
                        "tags": [
                            TAG.Point,
                            TAG.Temperature,
                            TAG.Deadband,
                            TAG.Setpoint,
                        ],
                        "parents": [BRICK.Temperature_Setpoint],
                    },
                    "Air_Flow_Deadband_Setpoint": {
                        BRICK.hasSubstance: BRICK.Air,
                        BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                        "subclasses": {
                            "Exhaust_Air_Stack_Flow_Deadband_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Exhaust,
                                    TAG.Air,
                                    TAG.Stack,
                                    TAG.Flow,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Exhaust_Air_Stack_Flow_Setpoint],
                            }
                        },
                        "tags": [
                            TAG.Point,
                            TAG.Air,
                            TAG.Flow,
                            TAG.Deadband,
                            TAG.Setpoint,
                        ],
                        "parents": [BRICK.Air_Flow_Setpoint],
                    },
                    "Static_Pressure_Deadband_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.StaticPressure,
                        "tags": [
                            TAG.Point,
                            TAG.Static,
                            TAG.Pressure,
                            TAG.Deadband,
                            TAG.Setpoint,
                        ],
                        "parents": [BRICK.Static_Pressure_Setpoint],
                        "subclasses": {
                            "Supply_Air_Static_Pressure_Deadband_Setpoint": {
                                BRICK.hasSubstance: [
                                    BRICK.Supply_Air,
                                    BRICK.Discharge_Air,
                                ],
                                BRICK.hasQuantity: QUDTQK.StaticPressure,
                                "aliases": [
                                    BRICK[
                                        "Discharge_Air_Static_Pressure_Deadband_Setpoint"
                                    ]
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [
                                    BRICK.Discharge_Air_Static_Pressure_Setpoint,
                                    BRICK.Supply_Air_Static_Pressure_Setpoint,
                                ],
                            },
                        },
                    },
                },
            },
            "Flow_Setpoint": {
                BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                "tags": [TAG.Point, TAG.Flow, TAG.Setpoint],
                "subclasses": {
                    "Air_Flow_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                        BRICK.hasSubstance: BRICK.Air,
                        "tags": [TAG.Point, TAG.Air, TAG.Flow, TAG.Setpoint],
                        "subclasses": {
                            "Air_Flow_Demand_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Demand,
                                    TAG.Setpoint,
                                ],
                            },
                            "Exhaust_Air_Flow_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                BRICK.hasSubstance: BRICK.Exhaust_Air,
                                "subclasses": {
                                    "Exhaust_Air_Stack_Flow_Setpoint": {
                                        BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Exhaust,
                                            TAG.Air,
                                            TAG.Stack,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    }
                                },
                                "tags": [
                                    TAG.Point,
                                    TAG.Exhaust,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                            },
                            "Outside_Air_Flow_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                BRICK.hasSubstance: BRICK.Outside_Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Outside,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                            },
                            "Supply_Air_Flow_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                BRICK.hasSubstance: [
                                    BRICK.Supply_Air,
                                    BRICK.Discharge_Air,
                                ],
                                "aliases": [BRICK["Discharge_Air_Flow_Setpoint"]],
                                "subclasses": {
                                    "Supply_Air_Flow_Demand_Setpoint": {
                                        "aliases": [
                                            BRICK["Discharge_Air_Flow_Demand_Setpoint"]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Demand,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Occupied_Supply_Air_Flow_Setpoint": {
                                        "aliases": [
                                            BRICK[
                                                "Occupied_Discharge_Air_Flow_Setpoint"
                                            ]
                                        ],
                                        "subclasses": {
                                            "Occupied_Cooling_Supply_Air_Flow_Setpoint": {
                                                "aliases": [
                                                    BRICK[
                                                        "Occupied_Cooling_Discharge_Air_Flow_Setpoint"
                                                    ]
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Occupied,
                                                    TAG.Cool,
                                                    TAG.Supply,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Cooling_Discharge_Air_Flow_Setpoint,
                                                    BRICK.Cooling_Supply_Air_Flow_Setpoint,
                                                ],
                                            },
                                            "Occupied_Heating_Supply_Air_Flow_Setpoint": {
                                                "aliases": [
                                                    BRICK[
                                                        "Occupied_Heating_Discharge_Air_Flow_Setpoint"
                                                    ]
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Occupied,
                                                    TAG.Heat,
                                                    TAG.Supply,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Heating_Discharge_Air_Flow_Setpoint,
                                                    BRICK.Heating_Supply_Air_Flow_Setpoint,
                                                ],
                                            },
                                        },
                                        "tags": [
                                            TAG.Point,
                                            TAG.Occupied,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Unoccupied_Supply_Air_Flow_Setpoint": {
                                        "aliases": [
                                            BRICK[
                                                "Unoccupied_Discharge_Air_Flow_Setpoint"
                                            ]
                                        ],
                                        "subclasses": {
                                            "Unoccupied_Cooling_Supply_Air_Flow_Setpoint": {
                                                "aliases": [
                                                    BRICK[
                                                        "Unoccupied_Cooling_Discharge_Air_Flow_Setpoint"
                                                    ]
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Unoccupied,
                                                    TAG.Cool,
                                                    TAG.Supply,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Cooling_Discharge_Air_Flow_Setpoint,
                                                    BRICK.Cooling_Supply_Air_Flow_Setpoint,
                                                ],
                                            },
                                            "Unoccupied_Heating_Supply_Air_Flow_Setpoint": {
                                                "aliases": [
                                                    BRICK[
                                                        "Unoccupied_Heating_Discharge_Air_Flow_Setpoint"
                                                    ]
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Unoccupied,
                                                    TAG.Heat,
                                                    TAG.Supply,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Heating_Discharge_Air_Flow_Setpoint,
                                                    BRICK.Heating_Supply_Air_Flow_Setpoint,
                                                ],
                                            },
                                        },
                                        "tags": [
                                            TAG.Point,
                                            TAG.Unoccupied,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Cooling_Supply_Air_Flow_Setpoint": {
                                        "aliases": [
                                            BRICK["Cooling_Discharge_Air_Flow_Setpoint"]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Cool,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Heating_Supply_Air_Flow_Setpoint": {
                                        "aliases": [
                                            BRICK["Heating_Discharge_Air_Flow_Setpoint"]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Heat,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                    "Water_Flow_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                        BRICK.hasSubstance: BRICK.Water,
                        "tags": [
                            TAG.Point,
                            TAG.Water,
                            TAG.Flow,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Condenser_Water_Flow_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                BRICK.hasSubstance: BRICK.Condenser_Water,
                                "tags": [
                                    TAG.Point,
                                    TAG.Condenser,
                                    TAG.Water,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                            },
                            "Entering_Water_Flow_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                BRICK.hasSubstance: BRICK.Entering_Water,
                                "tags": [
                                    TAG.Point,
                                    TAG.Entering,
                                    TAG.Water,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Entering_Chilled_Water_Flow_Setpoint": {
                                        BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                        BRICK.hasSubstance: BRICK.Entering_Chilled_Water,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Entering,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Chilled_Water_Flow_Setpoint],
                                    },
                                    "Entering_Hot_Water_Flow_Setpoint": {
                                        BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                        BRICK.hasSubstance: BRICK.Entering_Hot_Water,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Entering,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Hot_Water_Flow_Setpoint],
                                    },
                                },
                            },
                            "Leaving_Water_Flow_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                BRICK.hasSubstance: BRICK.Leaving_Water,
                                "tags": [
                                    TAG.Point,
                                    TAG.Leaving,
                                    TAG.Water,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Leaving_Chilled_Water_Flow_Setpoint": {
                                        BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                        BRICK.hasSubstance: BRICK.Leaving_Chilled_Water,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Leaving,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Chilled_Water_Flow_Setpoint],
                                    },
                                    "Leaving_Hot_Water_Flow_Setpoint": {
                                        BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                        BRICK.hasSubstance: BRICK.Leaving_Hot_Water,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Leaving,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Hot_Water_Flow_Setpoint],
                                    },
                                },
                            },
                            "Hot_Water_Flow_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                BRICK.hasSubstance: BRICK.Hot_Water,
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                            },
                            "Chilled_Water_Flow_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                BRICK.hasSubstance: BRICK.Chilled_Water,
                                "tags": [
                                    TAG.Point,
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                            },
                            "Bypass_Water_Flow_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                BRICK.hasSubstance: BRICK.Bypass_Water,
                                "tags": [
                                    TAG.Point,
                                    TAG.Bypass,
                                    TAG.Water,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                },
            },
            "Humidity_Setpoint": {
                "tags": [TAG.Point, TAG.Humidity, TAG.Setpoint],
                BRICK.hasQuantity: QUDTQK.PressureRatio,
                "subclasses": {
                    "Unoccupied_Humidity_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.RelativeHumidity,
                        "tags": [TAG.Point, TAG.Humidity, TAG.Setpoint, TAG.Unoccupied],
                    },
                    "Occupied_Humidity_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.RelativeHumidity,
                        "tags": [TAG.Point, TAG.Humidity, TAG.Setpoint, TAG.Occupied],
                    },
                    "Bypass_Air_Humidity_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.RelativeHumidity,
                        BRICK.hasSubstance: BRICK.Bypass_Air,
                        "tags": [
                            TAG.Point,
                            TAG.Humidity,
                            TAG.Setpoint,
                            TAG.Air,
                            TAG.Bypass,
                        ],
                    },
                    "Outside_Air_Humidity_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.RelativeHumidity,
                        BRICK.hasSubstance: BRICK.Outside_Air,
                        "tags": [
                            TAG.Point,
                            TAG.Humidity,
                            TAG.Setpoint,
                            TAG.Air,
                            TAG.Outside,
                        ],
                    },
                    "Zone_Air_Humidity_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.RelativeHumidity,
                        BRICK.hasSubstance: BRICK.Zone_Air,
                        "tags": [
                            TAG.Point,
                            TAG.Humidity,
                            TAG.Setpoint,
                            TAG.Air,
                            TAG.Zone,
                        ],
                    },
                    "Building_Air_Humidity_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.RelativeHumidity,
                        BRICK.hasSubstance: BRICK.Building_Air,
                        "tags": [
                            TAG.Point,
                            TAG.Humidity,
                            TAG.Setpoint,
                            TAG.Air,
                            TAG.Building,
                        ],
                    },
                    "Mixed_Air_Humidity_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.RelativeHumidity,
                        BRICK.hasSubstance: BRICK.Mixed_Air,
                        "tags": [
                            TAG.Point,
                            TAG.Humidity,
                            TAG.Setpoint,
                            TAG.Air,
                            TAG.Mixed,
                        ],
                    },
                    "Return_Air_Humidity_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.RelativeHumidity,
                        BRICK.hasSubstance: BRICK.Return_Air,
                        "tags": [
                            TAG.Point,
                            TAG.Humidity,
                            TAG.Setpoint,
                            TAG.Air,
                            TAG.Return,
                        ],
                    },
                    "Exhaust_Air_Humidity_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.RelativeHumidity,
                        BRICK.hasSubstance: BRICK.Exhaust_Air,
                        "tags": [
                            TAG.Point,
                            TAG.Humidity,
                            TAG.Setpoint,
                            TAG.Air,
                            TAG.Exhaust,
                        ],
                    },
                    "Supply_Air_Humidity_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.RelativeHumidity,
                        BRICK.hasSubstance: [BRICK.Supply_Air, BRICK.Discharge_Air],
                        "aliases": [BRICK["Discharge_Air_Humidity_Setpoint"]],
                        "tags": [
                            TAG.Point,
                            TAG.Humidity,
                            TAG.Setpoint,
                            TAG.Air,
                            TAG.Supply,
                            TAG.Discharge,
                        ],
                    },
                },
            },
            "Load_Setpoint": {
                BRICK.hasQuantity: QUDTQK.Power,
                "subclasses": {
                    "Load_Shed_Setpoint": {
                        "tags": [TAG.Point, TAG.Shed, TAG.Load, TAG.Setpoint],
                        "subclasses": {
                            "Leaving_Medium_Temperature_Hot_Water_Temperature_Load_Shed_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Medium,
                                    TAG.Temperature,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Leaving,
                                    TAG.Pressure,
                                    TAG.Shed,
                                    TAG.Load,
                                    TAG.Setpoint,
                                ],
                            },
                            "Entering_Medium_Temperature_Hot_Water_Temperature_Load_Shed_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Medium,
                                    TAG.Temperature,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Entering,
                                    TAG.Pressure,
                                    TAG.Shed,
                                    TAG.Load,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                },
                "tags": [TAG.Point, TAG.Load, TAG.Setpoint],
            },
            "Luminance_Setpoint": {
                "tags": [TAG.Point, TAG.Luminance, TAG.Setpoint],
                BRICK.hasQuantity: QUDTQK.Luminance,
            },
            "Pressure_Setpoint": {
                BRICK.hasQuantity: QUDTQK.Pressure,
                "subclasses": {
                    "Air_Pressure_Setpoint": {
                        "tags": [TAG.Setpoint, TAG.Pressure, TAG.Setpoint, TAG.Air],
                        BRICK.hasQuantity: QUDTQK.Pressure,
                    },
                    "Water_Pressure_Setpoint": {
                        "tags": [TAG.Setpoint, TAG.Pressure, TAG.Setpoint, TAG.Water],
                        BRICK.hasQuantity: QUDTQK.Pressure,
                    },
                    "Static_Pressure_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.StaticPressure,
                        "subclasses": {
                            "Building_Air_Static_Pressure_Setpoint": {
                                "parents": [BRICK["Air_Pressure_Setpoint"]],
                                BRICK.hasSubstance: BRICK.Building_Air,
                                BRICK.hasQuantity: QUDTQK.StaticPressure,
                                "tags": [
                                    TAG.Point,
                                    TAG.Building,
                                    TAG.Air,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                            },
                            "Chilled_Water_Static_Pressure_Setpoint": {
                                BRICK.hasSubstance: BRICK.Chilled_Water,
                                BRICK.hasQuantity: QUDTQK.StaticPressure,
                                "tags": [
                                    TAG.Point,
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                            },
                            "Duct_Air_Static_Pressure_Setpoint": {
                                BRICK.hasSubstance: BRICK.Air,
                                BRICK.hasQuantity: QUDTQK.StaticPressure,
                                "tags": [
                                    TAG.Point,
                                    TAG.Duct,
                                    TAG.Air,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                            },
                            "Exhaust_Air_Static_Pressure_Setpoint": {
                                BRICK.hasSubstance: BRICK.Exhaust_Air,
                                BRICK.hasQuantity: QUDTQK.StaticPressure,
                                "tags": [
                                    TAG.Point,
                                    TAG.Exhaust,
                                    TAG.Air,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                            },
                            "Hot_Water_Static_Pressure_Setpoint": {
                                BRICK.hasSubstance: BRICK.Hot_Water,
                                BRICK.hasQuantity: QUDTQK.StaticPressure,
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                            },
                            "Supply_Air_Static_Pressure_Setpoint": {
                                BRICK.hasSubstance: [
                                    BRICK.Supply_Air,
                                    BRICK.Discharge_Air,
                                ],
                                BRICK.hasSubstance: [
                                    BRICK.Supply_Air,
                                    BRICK.Discharge_Air,
                                ],
                                BRICK.hasQuantity: QUDTQK.StaticPressure,
                                "aliases": [
                                    BRICK["Discharge_Air_Static_Pressure_Setpoint"]
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                            },
                            "Underfloor_Air_Plenum_Static_Pressure_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Underfloor,
                                    TAG.Air,
                                    TAG.Plenum,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ]
                            },
                        },
                        "tags": [TAG.Point, TAG.Static, TAG.Pressure, TAG.Setpoint],
                    },
                    "Velocity_Pressure_Setpoint": {
                        "tags": [TAG.Point, TAG.Velocity, TAG.Pressure, TAG.Setpoint],
                    },
                },
                "tags": [TAG.Point, TAG.Pressure, TAG.Setpoint],
            },
            "Reset_Setpoint": {
                "tags": [TAG.Point, TAG.Reset, TAG.Setpoint],
                BRICK.hasQuantity: QUDTQK.Dimensionless,
                "subclasses": {
                    "Supply_Air_Flow_Reset_Setpoint": {
                        "aliases": [BRICK["Discharge_Air_Flow_Reset_Setpoint"]],
                        BRICK.hasSubstance: BRICK.Discharge_Air,
                        BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                        "tags": [
                            TAG.Point,
                            TAG.Supply,
                            TAG.Discharge,
                            TAG.Air,
                            TAG.Flow,
                            TAG.Reset,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Supply_Air_Flow_High_Reset_Setpoint": {
                                "aliases": [
                                    BRICK["Discharge_Air_Flow_High_Reset_Setpoint"]
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                    TAG.High,
                                ],
                            },
                            "Supply_Air_Flow_Low_Reset_Setpoint": {
                                "aliases": [
                                    BRICK["Discharge_Air_Flow_Low_Reset_Setpoint"]
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                    TAG.Low,
                                ],
                            },
                        },
                    },
                    "Temperature_High_Reset_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.Temperature,
                        "tags": [
                            TAG.Point,
                            TAG.Temperature,
                            TAG.High,
                            TAG.Reset,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Leaving_Hot_Water_Temperature_High_Reset_Setpoint": {
                                BRICK.hasSubstance: BRICK.Leaving_Hot_Water,
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Leaving,
                                    TAG.Temperature,
                                    TAG.High,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Leaving_Medium_Temperature_Hot_Water_Temperature_High_Reset_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Medium,
                                            TAG.Temperature,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Leaving,
                                            TAG.Temperature,
                                            TAG.High,
                                            TAG.Reset,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Entering_Hot_Water_Temperature_High_Reset_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Entering,
                                    TAG.Temperature,
                                    TAG.High,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Entering_Medium_Temperature_Hot_Water_Temperature_High_Reset_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Medium,
                                            TAG.Temperature,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Entering,
                                            TAG.Temperature,
                                            TAG.High,
                                            TAG.Reset,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Outside_Air_Temperature_High_Reset_Setpoint": {
                                BRICK.hasSubstance: BRICK.Outside_Air,
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                "tags": [
                                    TAG.Point,
                                    TAG.Outside,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.High,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                            },
                            "Return_Air_Temperature_High_Reset_Setpoint": {
                                BRICK.hasSubstance: BRICK.Return_Air,
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                "tags": [
                                    TAG.Point,
                                    TAG.Return,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.High,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                    "Temperature_Low_Reset_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.Temperature,
                        "tags": [
                            TAG.Point,
                            TAG.Temperature,
                            TAG.Low,
                            TAG.Reset,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Leaving_Hot_Water_Temperature_Low_Reset_Setpoint": {
                                BRICK.hasSubstance: BRICK.Leaving_Hot_Water,
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Leaving,
                                    TAG.Temperature,
                                    TAG.Low,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Leaving_Medium_Temperature_Hot_Water_Temperature_Low_Reset_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Medium,
                                            TAG.Temperature,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Leaving,
                                            TAG.Temperature,
                                            TAG.Low,
                                            TAG.Reset,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Entering_Hot_Water_Temperature_Low_Reset_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Entering,
                                    TAG.Temperature,
                                    TAG.Low,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Entering_Medium_Temperature_Hot_Water_Temperature_Low_Reset_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Medium,
                                            TAG.Temperature,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Entering,
                                            TAG.Temperature,
                                            TAG.Low,
                                            TAG.Reset,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Outside_Air_Temperature_Low_Reset_Setpoint": {
                                BRICK.hasSubstance: BRICK.Outside_Air,
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                "tags": [
                                    TAG.Point,
                                    TAG.Outside,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Low,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                            },
                            "Return_Air_Temperature_Low_Reset_Setpoint": {
                                BRICK.hasSubstance: BRICK.Return_Air,
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                "tags": [
                                    TAG.Point,
                                    TAG.Return,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Low,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                },
            },
            "Speed_Setpoint": {
                BRICK.hasQuantity: BRICK.Speed,
                "tags": [TAG.Point, TAG.Speed, TAG.Setpoint],
                "subclasses": {
                    "Rated_Speed_Setpoint": {
                        BRICK.hasQuantity: BRICK.Speed,
                        "tags": [TAG.Point, TAG.Rated, TAG.Speed, TAG.Setpoint],
                    },
                },
            },
            "Temperature_Setpoint": {
                BRICK.hasQuantity: QUDTQK.Temperature,
                "tags": [TAG.Point, TAG.Temperature, TAG.Setpoint],
                "subclasses": {
                    "Air_Temperature_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.Temperature,
                        BRICK.hasSubstance: BRICK.Air,
                        "tags": [TAG.Point, TAG.Air, TAG.Temperature, TAG.Setpoint],
                        "subclasses": {
                            "Effective_Air_Temperature_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                BRICK.hasSubstance: BRICK.Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Effective,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Mixed_Air_Temperature_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                BRICK.hasSubstance: BRICK.Mixed_Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Mixed,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Occupied_Air_Temperature_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                BRICK.hasSubstance: BRICK.Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Occupied,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Return_Air_Temperature_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                BRICK.hasSubstance: BRICK.Return_Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Return,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Effective_Return_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Return,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Effective,
                                        ],
                                        "parents": [
                                            BRICK.Effective_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Occupied_Return_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Return,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Occupied,
                                        ],
                                        "parents": [
                                            BRICK.Occupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Unoccupied_Return_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Return,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Unoccupied,
                                        ],
                                        "parents": [
                                            BRICK.Unoccupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                },
                            },
                            "Room_Air_Temperature_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                BRICK.hasSubstance: BRICK.Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Room,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Effective_Room_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Room,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Effective,
                                        ],
                                        "parents": [
                                            BRICK.Effective_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Occupied_Room_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Room,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Occupied,
                                        ],
                                        "parents": [
                                            BRICK.Occupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Unoccupied_Room_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Room,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Unoccupied,
                                        ],
                                        "parents": [
                                            BRICK.Unoccupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                },
                            },
                            "Target_Zone_Air_Temperature_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                BRICK.hasSubstance: BRICK.Zone_Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Target,
                                    TAG.Zone,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Effective_Target_Zone_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Effective,
                                            TAG.Target,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Effective_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Occupied_Target_Zone_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Occupied,
                                            TAG.Target,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Occupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Unoccupied_Target_Zone_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Unoccupied,
                                            TAG.Target,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Unoccupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Standby_Target_Zone_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Standby,
                                            TAG.Target,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Cooling_Zone_Air_Temperature_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                BRICK.hasSubstance: BRICK.Zone_Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Cool,
                                    TAG.Zone,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Effective_Cooling_Zone_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Effective,
                                            TAG.Cool,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Effective_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Occupied_Cooling_Zone_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Occupied,
                                            TAG.Cool,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Occupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Unoccupied_Cooling_Zone_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Unoccupied,
                                            TAG.Cool,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Unoccupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Standby_Cooling_Zone_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Standby,
                                            TAG.Cool,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Heating_Zone_Air_Temperature_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                BRICK.hasSubstance: BRICK.Zone_Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Heat,
                                    TAG.Zone,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Effective_Heating_Zone_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Effective,
                                            TAG.Heat,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Effective_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Occupied_Heating_Zone_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Occupied,
                                            TAG.Heat,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Occupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Unoccupied_Heating_Zone_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Unoccupied,
                                            TAG.Heat,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Unoccupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Standby_Heating_Zone_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Standby,
                                            TAG.Heat,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Outside_Air_Temperature_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                BRICK.hasSubstance: BRICK.Outside_Air,
                                "subclasses": {
                                    "Low_Outside_Air_Temperature_Enable_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Low,
                                            TAG.Outside,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Enable,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Disable_Hot_Water_System_Outside_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Disable,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.System,
                                            TAG.Outside,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Enable_Hot_Water_System_Outside_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Enable,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.System,
                                            TAG.Outside,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Open_Heating_Valve_Outside_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Open,
                                            TAG.Heat,
                                            TAG.Valve,
                                            TAG.Outside,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Heating_Temperature_Setpoint],
                                    },
                                    "Outside_Air_Lockout_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Outside,
                                            TAG.Air,
                                            TAG.Lockout,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                                "tags": [
                                    TAG.Point,
                                    TAG.Outside,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Unoccupied_Air_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Unoccupied,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Supply_Air_Temperature_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                BRICK.hasSubstance: [
                                    BRICK.Supply_Air,
                                    BRICK.Discharge_Air,
                                ],
                                "aliases": [
                                    BRICK["Discharge_Air_Temperature_Setpoint"]
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Effective_Supply_Air_Temperature_Setpoint": {
                                        "aliases": [
                                            BRICK[
                                                "Effective_Discharge_Air_Temperature_Setpoint"
                                            ]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Effective,
                                        ],
                                        "parents": [
                                            BRICK.Effective_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Occupied_Supply_Air_Temperature_Setpoint": {
                                        "aliases": [
                                            BRICK[
                                                "Occupied_Discharge_Air_Temperature_Setpoint"
                                            ]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Occupied,
                                        ],
                                        "parents": [
                                            BRICK.Occupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Unoccupied_Supply_Air_Temperature_Setpoint": {
                                        "aliases": [
                                            BRICK[
                                                "Unoccupied_Discharge_Air_Temperature_Setpoint"
                                            ]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Unoccupied,
                                        ],
                                        "parents": [
                                            BRICK.Unoccupied_Air_Temperature_Setpoint
                                        ],
                                    },
                                    "Supply_Air_Temperature_Heating_Setpoint": {
                                        "aliases": [
                                            BRICK[
                                                "Discharge_Air_Temperature_Heating_Setpoint"
                                            ]
                                        ],
                                        "parents": [BRICK.Heating_Temperature_Setpoint],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Supply_Air_Temperature_Cooling_Setpoint": {
                                        "aliases": [
                                            BRICK[
                                                "Discharge_Air_Temperature_Cooling_Setpoint"
                                            ]
                                        ],
                                        "parents": [BRICK.Cooling_Temperature_Setpoint],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Cool,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Min_Air_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Min,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ]
                            },
                            "Max_Air_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Max,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ]
                            },
                        },
                    },
                    "Cooling_Temperature_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.Temperature,
                        "tags": [TAG.Point, TAG.Temperature, TAG.Setpoint, TAG.Cool],
                        "subclasses": {
                            "Occupied_Cooling_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                    TAG.Cool,
                                    TAG.Occupied,
                                ],
                            },
                            "Unoccupied_Cooling_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                    TAG.Cool,
                                    TAG.Unoccupied,
                                ],
                            },
                        },
                    },
                    "Heating_Temperature_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.Temperature,
                        "tags": [TAG.Point, TAG.Temperature, TAG.Setpoint, TAG.Heat],
                        "subclasses": {
                            "Occupied_Heating_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                    TAG.Heat,
                                    TAG.Occupied,
                                ],
                            },
                            "Unoccupied_Heating_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                    TAG.Heat,
                                    TAG.Unoccupied,
                                ],
                            },
                        },
                    },
                    "Schedule_Temperature_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.Temperature,
                        "tags": [
                            TAG.Point,
                            TAG.Temperature,
                            TAG.Setpoint,
                            TAG.Schedule,
                        ],
                    },
                    "Radiant_Panel_Temperature_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.Temperature,
                        "tags": [
                            TAG.Point,
                            TAG.Radiant,
                            TAG.Panel,
                            TAG.Temperature,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Inside_Face_Surface_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Inside,
                                    TAG.Face,
                                    TAG.Surface,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Outside_Face_Surface_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Outside,
                                    TAG.Face,
                                    TAG.Surface,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Embedded_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Embedded,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Core_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Core,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                        },
                    },
                    "Water_Temperature_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.Temperature,
                        BRICK.hasSubstance: BRICK.Water,
                        "subclasses": {
                            "Domestic_Hot_Water_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Domestic,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Hot_Water_Temperature_Setpoint],
                                "subclasses": {
                                    "Entering_Domestic_Hot_Water_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Domestic,
                                            TAG.Hot,
                                            TAG.Entering,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Entering_Water_Temperature_Setpoint
                                        ],
                                    },
                                    "Leaving_Domestic_Hot_Water_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Domestic,
                                            TAG.Hot,
                                            TAG.Leaving,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Leaving_Water_Temperature_Setpoint
                                        ],
                                    },
                                },
                            },
                            "Chilled_Water_Temperature_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                BRICK.hasSubstance: BRICK.Chilled_Water,
                                "tags": [
                                    TAG.Point,
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Hot_Water_Temperature_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                BRICK.hasSubstance: BRICK.Hot_Water,
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Leaving_Water_Temperature_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                BRICK.hasSubstance: BRICK.Leaving_Water,
                                "tags": [
                                    TAG.Point,
                                    TAG.Leaving,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Leaving_Condenser_Water_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Leaving,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Condenser,
                                        ],
                                    },
                                    "Leaving_Hot_Water_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Leaving,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Hot,
                                        ],
                                        "parents": [
                                            BRICK.Hot_Water_Temperature_Setpoint
                                        ],
                                    },
                                    "Leaving_Chilled_Water_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Leaving,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Chilled,
                                        ],
                                        "parents": [
                                            BRICK.Chilled_Water_Temperature_Setpoint
                                        ],
                                    },
                                    "Entering_Condenser_Water_Temperature_Setpoint": {
                                        BRICK.hasQuantity: QUDTQK.Temperature,
                                        BRICK.hasSubstance: BRICK.Entering_Condenser_Water,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Entering,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Condenser,
                                        ],
                                    },
                                },
                            },
                            "Entering_Water_Temperature_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                BRICK.hasSubstance: BRICK.Entering_Water,
                                "tags": [
                                    TAG.Point,
                                    TAG.Entering,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Entering_Hot_Water_Temperature_Setpoint": {
                                        BRICK.hasQuantity: QUDTQK.Temperature,
                                        BRICK.hasSubstance: BRICK.Entering_Hot_Water,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Entering,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Hot,
                                        ],
                                        "parents": [
                                            BRICK.Hot_Water_Temperature_Setpoint
                                        ],
                                    },
                                    "Entering_Chilled_Water_Temperature_Setpoint": {
                                        BRICK.hasQuantity: QUDTQK.Temperature,
                                        BRICK.hasSubstance: BRICK.Entering_Chilled_Water,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Entering,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Chilled,
                                        ],
                                        "parents": [
                                            BRICK.Chilled_Water_Temperature_Setpoint
                                        ],
                                    },
                                },
                            },
                            "Min_Water_Temperature_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                BRICK.hasSubstance: BRICK.Water,
                                "tags": [
                                    TAG.Point,
                                    TAG.Min,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Max_Water_Temperature_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.Temperature,
                                BRICK.hasSubstance: BRICK.Water,
                                "tags": [
                                    TAG.Point,
                                    TAG.Max,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                        "tags": [TAG.Point, TAG.Water, TAG.Temperature, TAG.Setpoint],
                    },
                },
            },
            "CO2_Setpoint": {
                BRICK.hasQuantity: BRICK.CO2_Concentration,
                "subclasses": {
                    "Return_Air_CO2_Setpoint": {
                        BRICK.hasQuantity: BRICK.CO2_Concentration,
                        "tags": [TAG.Point, TAG.Return, TAG.Air, TAG.CO2, TAG.Setpoint],
                    }
                },
                "tags": [TAG.Point, TAG.CO2, TAG.Setpoint],
            },
            "Time_Setpoint": {
                BRICK.hasQuantity: QUDTQK.Time,
                "tags": [TAG.Point, TAG.Time, TAG.Setpoint],
                "subclasses": {
                    "Deceleration_Time_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.Time,
                        "tags": [TAG.Point, TAG.Time, TAG.Setpoint, TAG.Deceleration],
                    },
                    "Acceleration_Time_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.Time,
                        "tags": [TAG.Point, TAG.Time, TAG.Setpoint, TAG.Acceleration],
                    },
                },
            },
            "Differential_Setpoint": {
                BRICK.hasQuantity: QUDTQK.Dimensionless,
                "subclasses": {
                    "Differential_Temperature_Setpoint": {
                        BRICK.hasQuantity: BRICK.Differential_Temperature,
                        "tags": [
                            TAG.Point,
                            TAG.Differential,
                            TAG.Temperature,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Water_Differential_Temperature_Setpoint": {
                                BRICK.hasQuantity: BRICK.Differential_Temperature,
                                BRICK.hasSubstance: BRICK.Water,
                                "tags": [
                                    TAG.Point,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Differential_Air_Temperature_Setpoint": {
                                BRICK.hasQuantity: BRICK.Differential_Temperature,
                                "tags": [
                                    TAG.Point,
                                    TAG.Differential,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                    "Differential_Speed_Setpoint": {
                        BRICK.hasQuantity: BRICK.Speed,
                        "tags": [TAG.Point, TAG.Differential, TAG.Speed, TAG.Setpoint],
                    },
                    "Temperature_Differential_Reset_Setpoint": {
                        BRICK.hasQuantity: BRICK.Differential_Temperature,
                        "tags": [
                            TAG.Point,
                            TAG.Temperature,
                            TAG.Differential,
                            TAG.Reset,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Supply_Air_Temperature_Reset_Differential_Setpoint": {
                                BRICK.hasSubstance: [
                                    BRICK.Supply_Air,
                                    BRICK.Discharge_Air,
                                ],
                                BRICK.hasQuantity: BRICK.Differential_Temperature,
                                "aliases": [
                                    BRICK[
                                        "Discharge_Air_Temperature_Reset_Differential_Setpoint"
                                    ]
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Differential,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Supply_Air_Temperature_High_Reset_Setpoint": {
                                        BRICK.hasSubstance: BRICK.Supply_Air,
                                        BRICK.hasQuantity: QUDTQK.Temperature,
                                        "aliases": [
                                            BRICK[
                                                "Discharge_Air_Temperature_High_Reset_Setpoint"
                                            ]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Differential,
                                            TAG.Reset,
                                            TAG.Setpoint,
                                            TAG.High,
                                        ],
                                        "parents": [
                                            BRICK["Temperature_High_Reset_Setpoint"]
                                        ],
                                    },
                                    "Supply_Air_Temperature_Low_Reset_Setpoint": {
                                        BRICK.hasSubstance: BRICK.Supply_Air,
                                        BRICK.hasQuantity: QUDTQK.Temperature,
                                        "aliases": [
                                            BRICK[
                                                "Discharge_Air_Temperature_Low_Reset_Setpoint"
                                            ]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Differential,
                                            TAG.Reset,
                                            TAG.Setpoint,
                                            TAG.Low,
                                        ],
                                        "parents": [
                                            BRICK["Temperature_Low_Reset_Setpoint"]
                                        ],
                                    },
                                },
                            },
                        },
                    },
                    "Differential_Pressure_Setpoint": {
                        BRICK.hasQuantity: BRICK.Differential_Pressure,
                        "subclasses": {
                            "Air_Differential_Pressure_Setpoint": {
                                BRICK.hasSubstance: BRICK.Air,
                                BRICK.hasQuantity: BRICK.Differential_Pressure,
                                "tags": [
                                    TAG.Point,
                                    TAG.Air,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Exhaust_Air_Differential_Pressure_Setpoint": {
                                        BRICK.hasSubstance: BRICK.Exhaust_Air,
                                        BRICK.hasQuantity: BRICK.Differential_Pressure,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Exhaust,
                                            TAG.Air,
                                            TAG.Setpoint,
                                            TAG.Pressure,
                                            TAG.Differential,
                                        ],
                                    },
                                    "Return_Air_Differential_Pressure_Setpoint": {
                                        BRICK.hasSubstance: BRICK.Return_Air,
                                        BRICK.hasQuantity: BRICK.Differential_Pressure,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Return,
                                            TAG.Air,
                                            TAG.Setpoint,
                                            TAG.Pressure,
                                            TAG.Differential,
                                        ],
                                    },
                                    "Supply_Air_Differential_Pressure_Setpoint": {
                                        BRICK.hasSubstance: BRICK.Supply_Air,
                                        BRICK.hasQuantity: BRICK.Differential_Pressure,
                                        "aliases": [
                                            BRICK[
                                                "Discharge_Air_Differential_Pressure_Setpoint"
                                            ]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Setpoint,
                                            TAG.Pressure,
                                            TAG.Differential,
                                        ],
                                    },
                                },
                            },
                            "Water_Differential_Pressure_Setpoint": {
                                BRICK.hasSubstance: BRICK.Water,
                                BRICK.hasQuantity: BRICK.Differential_Pressure,
                                "tags": [
                                    TAG.Point,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Chilled_Water_Differential_Pressure_Setpoint": {
                                        BRICK.hasSubstance: BRICK.Chilled_Water,
                                        BRICK.hasQuantity: BRICK.Differential_Pressure,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Hot_Water_Differential_Pressure_Setpoint": {
                                        BRICK.hasSubstance: BRICK.Hot_Water,
                                        BRICK.hasQuantity: BRICK.Differential_Pressure,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Setpoint,
                                        ],
                                        "subclasses": {
                                            "Medium_Temperature_Hot_Water_Differential_Pressure_Setpoint": {
                                                BRICK.hasQuantity: BRICK.Differential_Pressure,
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Medium,
                                                    TAG.Temperature,
                                                    TAG.Hot,
                                                    TAG.Water,
                                                    TAG.Differential,
                                                    TAG.Pressure,
                                                    TAG.Setpoint,
                                                ],
                                            },
                                            "Domestic_Hot_Water_Differential_Pressure_Setpoint": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Domestic,
                                                    TAG.Temperature,
                                                    TAG.Hot,
                                                    TAG.Water,
                                                    TAG.Differential,
                                                    TAG.Pressure,
                                                    TAG.Setpoint,
                                                ],
                                            },
                                        },
                                    },
                                },
                            },
                            "Load_Shed_Differential_Pressure_Setpoint": {
                                BRICK.hasQuantity: BRICK.Differential_Pressure,
                                "parents": [BRICK.Load_Shed_Setpoint],
                                "subclasses": {
                                    "Chilled_Water_Differential_Pressure_Load_Shed_Setpoint": {
                                        BRICK.hasQuantity: BRICK.Differential_Pressure,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Load,
                                            TAG.Shed,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Chilled_Water_Differential_Pressure_Setpoint
                                        ],
                                    },
                                },
                                "tags": [
                                    TAG.Point,
                                    TAG.Load,
                                    TAG.Shed,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                        "tags": [
                            TAG.Point,
                            TAG.Differential,
                            TAG.Pressure,
                            TAG.Setpoint,
                        ],
                    },
                    "Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed_Setpoint": {
                        BRICK.hasQuantity: BRICK.Differential_Pressure,
                        "tags": [
                            TAG.Point,
                            TAG.Medium,
                            TAG.Temperature,
                            TAG.Hot,
                            TAG.Water,
                            TAG.Differential,
                            TAG.Pressure,
                            TAG.Shed,
                            TAG.Load,
                            TAG.Setpoint,
                        ],
                    },
                    "Differential_Pressure_Deadband_Setpoint": {
                        BRICK.hasQuantity: BRICK.Differential_Pressure,
                        "tags": [
                            TAG.Point,
                            TAG.Differential,
                            TAG.Pressure,
                            TAG.Deadband,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Hot_Water_Differential_Pressure_Deadband_Setpoint": {
                                BRICK.hasSubstance: BRICK.Hot_Water,
                                BRICK.hasQuantity: BRICK.Differential_Pressure,
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                            },
                            "Chilled_Water_Differential_Pressure_Deadband_Setpoint": {
                                BRICK.hasSubstance: BRICK.Chilled_Water,
                                BRICK.hasQuantity: BRICK.Differential_Pressure,
                                "tags": [
                                    TAG.Point,
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                            },
                            "Leaving_Water_Differential_Pressure_Deadband_Setpoint": {
                                BRICK.hasSubstance: BRICK.Leaving_Water,
                                BRICK.hasQuantity: BRICK.Differential_Pressure,
                                "tags": [
                                    TAG.Point,
                                    TAG.Leaving,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                            },
                            "Entering_Water_Differential_Pressure_Deadband_Setpoint": {
                                BRICK.hasSubstance: BRICK.Entering_Water,
                                BRICK.hasQuantity: BRICK.Differential_Pressure,
                                "tags": [
                                    TAG.Point,
                                    TAG.Entering,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                },
            },
        },
    }
}
