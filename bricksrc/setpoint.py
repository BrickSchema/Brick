from .namespaces import TAG, BRICK, RDFS, QUDTQK
from rdflib import Literal

setpoint_definitions = {
    "Setpoint": {
        RDFS.seeAlso: "https://xp20.ashrae.org/terminology/index.php?term=setpoint",
        "tags": [
            TAG.Point,
            TAG.Setpoint,
        ],
        "subclasses": {
            "Dewpoint_Setpoint": {
                BRICK.hasQuantity: QUDTQK.DewPointTemperature,
                "tags": [
                    TAG.Point,
                    TAG.Dewpoint,
                    TAG.Setpoint,
                ],
            },
            "Differential_Setpoint": {
                BRICK.hasQuantity: QUDTQK.Dimensionless,
                "subclasses": {
                    "Differential_Pressure_Setpoint": {
                        BRICK.hasQuantity: BRICK.Differential_Pressure,
                        "tags": [
                            TAG.Point,
                            TAG.Differential,
                            TAG.Pressure,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Air_Differential_Pressure_Setpoint": {
                                BRICK.hasQuantity: BRICK.Differential_Pressure,
                                BRICK.hasSubstance: BRICK.Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Air,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Exhaust_Air_Differential_Pressure_Setpoint": {
                                        BRICK.hasQuantity: BRICK.Differential_Pressure,
                                        BRICK.hasSubstance: BRICK.Exhaust_Air,
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
                                        BRICK.hasQuantity: BRICK.Differential_Pressure,
                                        BRICK.hasSubstance: BRICK.Return_Air,
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
                                        "aliases": [
                                            BRICK.Discharge_Air_Differential_Pressure_Setpoint,
                                        ],
                                        BRICK.hasQuantity: BRICK.Differential_Pressure,
                                        BRICK.hasSubstance: BRICK.Supply_Air,
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
                                BRICK.hasQuantity: BRICK.Differential_Pressure,
                                BRICK.hasSubstance: BRICK.Water,
                                "tags": [
                                    TAG.Point,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Chilled_Water_Differential_Pressure_Setpoint": {
                                        BRICK.hasQuantity: BRICK.Differential_Pressure,
                                        BRICK.hasSubstance: BRICK.Chilled_Water,
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
                                        BRICK.hasQuantity: BRICK.Differential_Pressure,
                                        BRICK.hasSubstance: BRICK.Hot_Water,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Setpoint,
                                        ],
                                        "subclasses": {
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
                                        },
                                    },
                                },
                            },
                        },
                    },
                    "Differential_Speed_Setpoint": {
                        BRICK.hasQuantity: BRICK.Speed,
                        "tags": [
                            TAG.Point,
                            TAG.Differential,
                            TAG.Speed,
                            TAG.Setpoint,
                        ],
                    },
                    "Differential_Temperature_Setpoint": {
                        BRICK.hasQuantity: BRICK.Differential_Temperature,
                        "tags": [
                            TAG.Point,
                            TAG.Differential,
                            TAG.Temperature,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
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
                        },
                    },
                    "Load_Shed_Differential_Pressure_Setpoint": {
                        BRICK.hasQuantity: BRICK.Differential_Pressure,
                        "parents": [
                            BRICK.Load_Shed_Setpoint,
                        ],
                        "tags": [
                            TAG.Point,
                            TAG.Load,
                            TAG.Shed,
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
                },
            },
            "Enthalpy_Setpoint": {
                BRICK.hasQuantity: QUDTQK.Enthalpy,
                "tags": [
                    TAG.Point,
                    TAG.Setpoint,
                    TAG.Enthalpy,
                ],
            },
            "Flow_Setpoint": {
                BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                "tags": [
                    TAG.Point,
                    TAG.Flow,
                    TAG.Setpoint,
                ],
                "subclasses": {
                    "Air_Flow_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                        BRICK.hasSubstance: BRICK.Air,
                        "tags": [
                            TAG.Point,
                            TAG.Air,
                            TAG.Flow,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Exhaust_Air_Flow_Setpoint": {
                                BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                BRICK.hasSubstance: BRICK.Exhaust_Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Exhaust,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
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
                                    },
                                },
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
                                "aliases": [
                                    BRICK.Discharge_Air_Flow_Setpoint,
                                ],
                                BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                BRICK.hasSubstance: [
                                    BRICK.Supply_Air,
                                    BRICK.Discharge_Air,
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Cooling_Supply_Air_Flow_Setpoint": {
                                        "aliases": [
                                            BRICK.Cooling_Discharge_Air_Flow_Setpoint,
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
                                        "subclasses": {
                                            "Occupied_Cooling_Supply_Air_Flow_Setpoint": {
                                                "aliases": [
                                                    BRICK.Occupied_Cooling_Discharge_Air_Flow_Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Cooling_Discharge_Air_Flow_Setpoint,
                                                    BRICK.Cooling_Supply_Air_Flow_Setpoint,
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
                                            },
                                            "Unoccupied_Cooling_Supply_Air_Flow_Setpoint": {
                                                "aliases": [
                                                    BRICK.Unoccupied_Cooling_Discharge_Air_Flow_Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Cooling_Discharge_Air_Flow_Setpoint,
                                                    BRICK.Cooling_Supply_Air_Flow_Setpoint,
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
                                            },
                                        },
                                    },
                                    "Heating_Supply_Air_Flow_Setpoint": {
                                        "aliases": [
                                            BRICK.Heating_Discharge_Air_Flow_Setpoint,
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
                                        "subclasses": {
                                            "Occupied_Heating_Supply_Air_Flow_Setpoint": {
                                                "aliases": [
                                                    BRICK.Occupied_Heating_Discharge_Air_Flow_Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Heating_Discharge_Air_Flow_Setpoint,
                                                    BRICK.Heating_Supply_Air_Flow_Setpoint,
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
                                            },
                                            "Unoccupied_Heating_Supply_Air_Flow_Setpoint": {
                                                "aliases": [
                                                    BRICK.Unoccupied_Heating_Discharge_Air_Flow_Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Heating_Discharge_Air_Flow_Setpoint,
                                                    BRICK.Heating_Supply_Air_Flow_Setpoint,
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
                                            },
                                        },
                                    },
                                    "Occupied_Supply_Air_Flow_Setpoint": {
                                        "aliases": [
                                            BRICK.Occupied_Discharge_Air_Flow_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Occupied,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                        "subclasses": {
                                            "Occupied_Cooling_Supply_Air_Flow_Setpoint": {
                                                "aliases": [
                                                    BRICK.Occupied_Cooling_Discharge_Air_Flow_Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Cooling_Discharge_Air_Flow_Setpoint,
                                                    BRICK.Cooling_Supply_Air_Flow_Setpoint,
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
                                            },
                                            "Occupied_Heating_Supply_Air_Flow_Setpoint": {
                                                "aliases": [
                                                    BRICK.Occupied_Heating_Discharge_Air_Flow_Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Heating_Discharge_Air_Flow_Setpoint,
                                                    BRICK.Heating_Supply_Air_Flow_Setpoint,
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
                                            },
                                        },
                                    },
                                    "Unoccupied_Supply_Air_Flow_Setpoint": {
                                        "aliases": [
                                            BRICK.Unoccupied_Discharge_Air_Flow_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Unoccupied,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                        "subclasses": {
                                            "Unoccupied_Cooling_Supply_Air_Flow_Setpoint": {
                                                "aliases": [
                                                    BRICK.Unoccupied_Cooling_Discharge_Air_Flow_Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Cooling_Discharge_Air_Flow_Setpoint,
                                                    BRICK.Cooling_Supply_Air_Flow_Setpoint,
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
                                            },
                                            "Unoccupied_Heating_Supply_Air_Flow_Setpoint": {
                                                "aliases": [
                                                    BRICK.Unoccupied_Heating_Discharge_Air_Flow_Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Heating_Discharge_Air_Flow_Setpoint,
                                                    BRICK.Heating_Supply_Air_Flow_Setpoint,
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
                                            },
                                        },
                                    },
                                },
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
                                "subclasses": {
                                    "Entering_Chilled_Water_Flow_Setpoint": {
                                        BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                        BRICK.hasSubstance: BRICK.Entering_Chilled_Water,
                                        "parents": [
                                            BRICK.Chilled_Water_Flow_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Entering,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Leaving_Chilled_Water_Flow_Setpoint": {
                                        BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                        BRICK.hasSubstance: BRICK.Leaving_Chilled_Water,
                                        "parents": [
                                            BRICK.Chilled_Water_Flow_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Leaving,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
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
                                        "parents": [
                                            BRICK.Chilled_Water_Flow_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Entering,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Entering_Hot_Water_Flow_Setpoint": {
                                        BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                        BRICK.hasSubstance: BRICK.Entering_Hot_Water,
                                        "parents": [
                                            BRICK.Hot_Water_Flow_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Entering,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
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
                                "subclasses": {
                                    "Entering_Hot_Water_Flow_Setpoint": {
                                        BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                        BRICK.hasSubstance: BRICK.Entering_Hot_Water,
                                        "parents": [
                                            BRICK.Hot_Water_Flow_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Entering,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Leaving_Hot_Water_Flow_Setpoint": {
                                        BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                        BRICK.hasSubstance: BRICK.Leaving_Hot_Water,
                                        "parents": [
                                            BRICK.Hot_Water_Flow_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Leaving,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
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
                                        "parents": [
                                            BRICK.Chilled_Water_Flow_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Leaving,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Leaving_Hot_Water_Flow_Setpoint": {
                                        BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                                        BRICK.hasSubstance: BRICK.Leaving_Hot_Water,
                                        "parents": [
                                            BRICK.Hot_Water_Flow_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Leaving,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                        },
                    },
                },
            },
            "Frequency_Setpoint": {
                BRICK.hasQuantity: BRICK.Frequency,
                "tags": [
                    TAG.Point,
                    TAG.Setpoint,
                    TAG.Frequency,
                ],
            },
            "Humidity_Setpoint": {
                BRICK.hasQuantity: QUDTQK.PressureRatio,
                "tags": [
                    TAG.Point,
                    TAG.Humidity,
                    TAG.Setpoint,
                ],
                "subclasses": {
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
                    "Occupied_Humidity_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.RelativeHumidity,
                        "tags": [
                            TAG.Point,
                            TAG.Humidity,
                            TAG.Setpoint,
                            TAG.Occupied,
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
                    "Supply_Air_Humidity_Setpoint": {
                        "aliases": [
                            BRICK.Discharge_Air_Humidity_Setpoint,
                        ],
                        BRICK.hasQuantity: QUDTQK.RelativeHumidity,
                        BRICK.hasSubstance: [
                            BRICK.Supply_Air,
                            BRICK.Discharge_Air,
                        ],
                        "tags": [
                            TAG.Point,
                            TAG.Humidity,
                            TAG.Setpoint,
                            TAG.Air,
                            TAG.Supply,
                            TAG.Discharge,
                        ],
                    },
                    "Unoccupied_Humidity_Setpoint": {
                        BRICK.hasQuantity: QUDTQK.RelativeHumidity,
                        "tags": [
                            TAG.Point,
                            TAG.Humidity,
                            TAG.Setpoint,
                            TAG.Unoccupied,
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
                },
            },
            "Illuminance_Setpoint": {
                BRICK.hasQuantity: QUDTQK.Illuminance,
                "tags": [
                    TAG.Point,
                    TAG.Setpoint,
                    TAG.Illuminance,
                ],
            },
            "Load_Shed_Setpoint": {
                "tags": [
                    TAG.Point,
                    TAG.Shed,
                    TAG.Load,
                    TAG.Setpoint,
                ],
                "subclasses": {
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
                    "Load_Shed_Differential_Pressure_Setpoint": {
                        BRICK.hasQuantity: BRICK.Differential_Pressure,
                        "parents": [
                            BRICK.Load_Shed_Setpoint,
                        ],
                        "tags": [
                            TAG.Point,
                            TAG.Load,
                            TAG.Shed,
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
                },
            },
            "Luminance_Setpoint": {
                BRICK.hasQuantity: QUDTQK.Luminance,
                "tags": [
                    TAG.Point,
                    TAG.Luminance,
                    TAG.Setpoint,
                ],
            },
            "Position_Setpoint": {
                "subclasses": {
                    "Damper_Position_Setpoint": {
                        BRICK.hasQuantity: BRICK.Position,
                        "tags": [
                            TAG.Point,
                            TAG.Damper,
                            TAG.Position,
                            TAG.Setpoint,
                        ],
                    },
                    "Valve_Position_Setpoint": {},
                },
            },
            "Pressure_Setpoint": {
                BRICK.hasQuantity: BRICK.Pressure,
                "tags": [
                    TAG.Point,
                    TAG.Pressure,
                    TAG.Setpoint,
                ],
                "subclasses": {
                    "Air_Pressure_Setpoint": {
                        BRICK.hasQuantity: BRICK.Pressure,
                        "tags": [
                            TAG.Setpoint,
                            TAG.Pressure,
                            TAG.Setpoint,
                            TAG.Air,
                        ],
                        "subclasses": {
                            "Building_Air_Static_Pressure_Setpoint": {
                                BRICK.hasQuantity: BRICK.Static_Pressure,
                                BRICK.hasSubstance: BRICK.Building_Air,
                                "parents": [
                                    BRICK.Air_Pressure_Setpoint,
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Building,
                                    TAG.Air,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                    "Static_Pressure_Setpoint": {
                        BRICK.hasQuantity: BRICK.Static_Pressure,
                        "tags": [
                            TAG.Point,
                            TAG.Static,
                            TAG.Pressure,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Building_Air_Static_Pressure_Setpoint": {
                                BRICK.hasQuantity: BRICK.Static_Pressure,
                                BRICK.hasSubstance: BRICK.Building_Air,
                                "parents": [
                                    BRICK.Air_Pressure_Setpoint,
                                ],
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
                                BRICK.hasQuantity: BRICK.Static_Pressure,
                                BRICK.hasSubstance: BRICK.Chilled_Water,
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
                                BRICK.hasQuantity: BRICK.Static_Pressure,
                                BRICK.hasSubstance: BRICK.Air,
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
                                BRICK.hasQuantity: BRICK.Static_Pressure,
                                BRICK.hasSubstance: BRICK.Exhaust_Air,
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
                                BRICK.hasQuantity: BRICK.Static_Pressure,
                                BRICK.hasSubstance: BRICK.Hot_Water,
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
                                "aliases": [
                                    BRICK.Discharge_Air_Static_Pressure_Setpoint,
                                ],
                                BRICK.hasQuantity: BRICK.Static_Pressure,
                                BRICK.hasSubstance: [
                                    BRICK.Supply_Air,
                                    BRICK.Discharge_Air,
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
                                ],
                            },
                        },
                    },
                    "Velocity_Pressure_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Velocity,
                            TAG.Pressure,
                            TAG.Setpoint,
                        ],
                    },
                    "Water_Pressure_Setpoint": {
                        BRICK.hasQuantity: BRICK.Pressure,
                        "tags": [
                            TAG.Setpoint,
                            TAG.Pressure,
                            TAG.Setpoint,
                            TAG.Water,
                        ],
                    },
                },
            },
            "Speed_Setpoint": {
                BRICK.hasQuantity: BRICK.Speed,
                "tags": [
                    TAG.Point,
                    TAG.Speed,
                    TAG.Setpoint,
                ],
                "subclasses": {
                    "Rated_Speed_Setpoint": {
                        BRICK.hasQuantity: BRICK.Speed,
                        "tags": [
                            TAG.Point,
                            TAG.Rated,
                            TAG.Speed,
                            TAG.Setpoint,
                        ],
                    },
                },
            },
            "Temperature_Setpoint": {
                BRICK.hasQuantity: QUDTQK.Temperature,
                "tags": [
                    TAG.Point,
                    TAG.Temperature,
                    TAG.Setpoint,
                ],
                "subclasses": {
                    "Air_Temperature_Setpoint": {
                        BRICK.hasQuantity: BRICK.Temperature,
                        BRICK.hasSubstance: BRICK.Air,
                        "tags": [
                            TAG.Point,
                            TAG.Air,
                            TAG.Temperature,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Effective_Air_Temperature_Setpoint": {
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: BRICK.Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Effective,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Effective_Return_Air_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Effective_Air_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Return,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Effective,
                                        ],
                                    },
                                    "Effective_Room_Air_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Effective_Air_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Room,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Effective,
                                        ],
                                    },
                                    "Effective_Supply_Air_Temperature_Setpoint": {
                                        "aliases": [
                                            BRICK.Effective_Discharge_Air_Temperature_Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Effective_Air_Temperature_Setpoint,
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
                                    },
                                    "Effective_Zone_Air_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Effective_Air_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Effective,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Mixed_Air_Temperature_Setpoint": {
                                BRICK.hasQuantity: BRICK.Temperature,
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
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: BRICK.Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Occupied,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Occupied_Return_Air_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Occupied_Air_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Return,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Occupied,
                                        ],
                                    },
                                    "Occupied_Room_Air_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Occupied_Air_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Room,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Occupied,
                                        ],
                                    },
                                    "Occupied_Supply_Air_Temperature_Setpoint": {
                                        "aliases": [
                                            BRICK.Occupied_Discharge_Air_Temperature_Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Occupied_Air_Temperature_Setpoint,
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
                                    },
                                    "Occupied_Zone_Air_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Occupied_Air_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Occupied,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Return_Air_Temperature_Setpoint": {
                                BRICK.hasQuantity: BRICK.Temperature,
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
                                        "parents": [
                                            BRICK.Effective_Air_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Return,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Effective,
                                        ],
                                    },
                                    "Occupied_Return_Air_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Occupied_Air_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Return,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Occupied,
                                        ],
                                    },
                                    "Unoccupied_Return_Air_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Unoccupied_Air_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Return,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Unoccupied,
                                        ],
                                    },
                                },
                            },
                            "Room_Air_Temperature_Setpoint": {
                                BRICK.hasQuantity: BRICK.Temperature,
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
                                        "parents": [
                                            BRICK.Effective_Air_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Room,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Effective,
                                        ],
                                    },
                                    "Occupied_Room_Air_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Occupied_Air_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Room,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Occupied,
                                        ],
                                    },
                                    "Unoccupied_Room_Air_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Unoccupied_Air_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Room,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Unoccupied,
                                        ],
                                    },
                                },
                            },
                            "Supply_Air_Temperature_Setpoint": {
                                "aliases": [
                                    BRICK.Discharge_Air_Temperature_Setpoint,
                                ],
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: [
                                    BRICK.Supply_Air,
                                    BRICK.Discharge_Air,
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
                                            BRICK.Effective_Discharge_Air_Temperature_Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Effective_Air_Temperature_Setpoint,
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
                                    },
                                    "Occupied_Supply_Air_Temperature_Setpoint": {
                                        "aliases": [
                                            BRICK.Occupied_Discharge_Air_Temperature_Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Occupied_Air_Temperature_Setpoint,
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
                                    },
                                    "Supply_Air_Temperature_Cooling_Setpoint": {
                                        "aliases": [
                                            BRICK.Discharge_Air_Temperature_Cooling_Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Cooling_Temperature_Setpoint,
                                        ],
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
                                    "Supply_Air_Temperature_Heating_Setpoint": {
                                        "aliases": [
                                            BRICK.Discharge_Air_Temperature_Heating_Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Heating_Temperature_Setpoint,
                                        ],
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
                                    "Unoccupied_Supply_Air_Temperature_Setpoint": {
                                        "aliases": [
                                            BRICK.Unoccupied_Discharge_Air_Temperature_Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Unoccupied_Air_Temperature_Setpoint,
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
                                    },
                                },
                            },
                            "Zone_Air_Temperature_Setpoint": {
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: BRICK.Zone_Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Zone,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Effective_Zone_Air_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Effective_Air_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Effective,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Occupied_Zone_Air_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Occupied_Air_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Occupied,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Standby_Zone_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Standby,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Unoccupied_Zone_Air_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Unoccupied_Air_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Unoccupied,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Unoccupied_Air_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Unoccupied,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Unoccupied_Return_Air_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Unoccupied_Air_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Return,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Unoccupied,
                                        ],
                                    },
                                    "Unoccupied_Room_Air_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Unoccupied_Air_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Room,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                            TAG.Unoccupied,
                                        ],
                                    },
                                    "Unoccupied_Supply_Air_Temperature_Setpoint": {
                                        "aliases": [
                                            BRICK.Unoccupied_Discharge_Air_Temperature_Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Unoccupied_Air_Temperature_Setpoint,
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
                                    },
                                    "Unoccupied_Zone_Air_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Unoccupied_Air_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Unoccupied,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                        },
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
                    "Radiant_Panel_Temperature_Setpoint": {
                        BRICK.hasQuantity: BRICK.Temperature,
                        "tags": [
                            TAG.Point,
                            TAG.Radiant,
                            TAG.Panel,
                            TAG.Temperature,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
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
                        },
                    },
                    "Schedule_Temperature_Setpoint": {
                        BRICK.hasQuantity: BRICK.Temperature,
                        "tags": [
                            TAG.Point,
                            TAG.Temperature,
                            TAG.Setpoint,
                            TAG.Schedule,
                        ],
                    },
                    "Water_Temperature_Setpoint": {
                        BRICK.hasQuantity: BRICK.Temperature,
                        BRICK.hasSubstance: BRICK.Water,
                        "tags": [
                            TAG.Point,
                            TAG.Water,
                            TAG.Temperature,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Chilled_Water_Temperature_Setpoint": {
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: BRICK.Chilled_Water,
                                "tags": [
                                    TAG.Point,
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Entering_Chilled_Water_Temperature_Setpoint": {
                                        BRICK.hasQuantity: BRICK.Temperature,
                                        BRICK.hasSubstance: BRICK.Entering_Chilled_Water,
                                        "parents": [
                                            BRICK.Chilled_Water_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Entering,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Chilled,
                                        ],
                                    },
                                    "Leaving_Chilled_Water_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Chilled_Water_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Leaving,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Chilled,
                                        ],
                                    },
                                },
                            },
                            "Domestic_Hot_Water_Temperature_Setpoint": {
                                "parents": [
                                    BRICK.Hot_Water_Temperature_Setpoint,
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Domestic,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Entering_Domestic_Hot_Water_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Entering_Water_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Domestic,
                                            TAG.Hot,
                                            TAG.Entering,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Leaving_Domestic_Hot_Water_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Leaving_Water_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Domestic,
                                            TAG.Hot,
                                            TAG.Leaving,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Entering_Water_Temperature_Setpoint": {
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: BRICK.Entering_Water,
                                "tags": [
                                    TAG.Point,
                                    TAG.Entering,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Entering_Chilled_Water_Temperature_Setpoint": {
                                        BRICK.hasQuantity: BRICK.Temperature,
                                        BRICK.hasSubstance: BRICK.Entering_Chilled_Water,
                                        "parents": [
                                            BRICK.Chilled_Water_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Entering,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Chilled,
                                        ],
                                    },
                                    "Entering_Domestic_Hot_Water_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Entering_Water_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Domestic,
                                            TAG.Hot,
                                            TAG.Entering,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Entering_Hot_Water_Temperature_Setpoint": {
                                        BRICK.hasQuantity: BRICK.Temperature,
                                        BRICK.hasSubstance: BRICK.Entering_Hot_Water,
                                        "parents": [
                                            BRICK.Hot_Water_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Entering,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Hot,
                                        ],
                                    },
                                    "Entering_Water_Temperature_Deadband_Setpoint": {
                                        BRICK.hasQuantity: BRICK.Temperature,
                                        BRICK.hasSubstance: BRICK.Entering_Water,
                                        "parents": [
                                            BRICK.Entering_Water_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Entering,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Deadband,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Hot_Water_Temperature_Setpoint": {
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: BRICK.Hot_Water,
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Domestic_Hot_Water_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Hot_Water_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Domestic,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "subclasses": {
                                            "Entering_Domestic_Hot_Water_Temperature_Setpoint": {
                                                "parents": [
                                                    BRICK.Entering_Water_Temperature_Setpoint,
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Domestic,
                                                    TAG.Hot,
                                                    TAG.Entering,
                                                    TAG.Water,
                                                    TAG.Temperature,
                                                    TAG.Setpoint,
                                                ],
                                            },
                                            "Leaving_Domestic_Hot_Water_Temperature_Setpoint": {
                                                "parents": [
                                                    BRICK.Leaving_Water_Temperature_Setpoint,
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Domestic,
                                                    TAG.Hot,
                                                    TAG.Leaving,
                                                    TAG.Water,
                                                    TAG.Temperature,
                                                    TAG.Setpoint,
                                                ],
                                            },
                                        },
                                    },
                                    "Entering_Hot_Water_Temperature_Setpoint": {
                                        BRICK.hasQuantity: BRICK.Temperature,
                                        BRICK.hasSubstance: BRICK.Entering_Hot_Water,
                                        "parents": [
                                            BRICK.Hot_Water_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Entering,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Hot,
                                        ],
                                    },
                                    "Leaving_Hot_Water_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Hot_Water_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Leaving,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Hot,
                                        ],
                                    },
                                },
                            },
                            "Leaving_Water_Temperature_Setpoint": {
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: BRICK.Leaving_Water,
                                "tags": [
                                    TAG.Point,
                                    TAG.Leaving,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Entering_Condenser_Water_Temperature_Setpoint": {
                                        BRICK.hasQuantity: BRICK.Temperature,
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
                                    "Leaving_Chilled_Water_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Chilled_Water_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Leaving,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Chilled,
                                        ],
                                    },
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
                                    "Leaving_Domestic_Hot_Water_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Leaving_Water_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Domestic,
                                            TAG.Hot,
                                            TAG.Leaving,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Leaving_Hot_Water_Temperature_Setpoint": {
                                        "parents": [
                                            BRICK.Hot_Water_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Leaving,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                            TAG.Hot,
                                        ],
                                    },
                                    "Leaving_Water_Temperature_Deadband_Setpoint": {
                                        BRICK.hasQuantity: BRICK.Temperature,
                                        BRICK.hasSubstance: BRICK.Leaving_Water,
                                        "parents": [
                                            BRICK.Leaving_Water_Temperature_Setpoint,
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Leaving,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Deadband,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
