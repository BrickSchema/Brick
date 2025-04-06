from rdflib import Literal
from .namespaces import BRICK, TAG, OWL, QUDTQK

parameter_definitions = {
    "Parameter": {
        "tags": [TAG.Point, TAG.Parameter],
        "subclasses": {
            "Delay_Parameter": {
                "tags": [TAG.Point, TAG.Delay, TAG.Parameter],
                "subclasses": {
                    "Alarm_Delay_Parameter": {
                        "tags": [TAG.Point, TAG.Alarm, TAG.Delay, TAG.Parameter],
                    },
                },
            },
            "Time_Parameter": {
                BRICK.hasQuantity: BRICK.Time,
                "tags": [TAG.Point, TAG.Time, TAG.Parameter],
                "subclasses": {
                    "Deceleration_Time_Parameter": {
                        BRICK.hasQuantity: BRICK.Time,
                        "tags": [TAG.Point, TAG.Time, TAG.Parameter, TAG.Deceleration],
                    },
                    "Acceleration_Time_Parameter": {
                        BRICK.hasQuantity: BRICK.Time,
                        "tags": [TAG.Point, TAG.Time, TAG.Parameter, TAG.Acceleration],
                    },
                },
            },
            "Alarm_Sensitivity_Parameter": {
                "tags": [TAG.Point, TAG.Alarm, TAG.Sensitivity, TAG.Parameter],
                "subclasses": {
                    "Temperature_Alarm_Sensitivity_Parameter": {
                        "tags": [
                            TAG.Point,
                            TAG.Alarm,
                            TAG.Sensitivity,
                            TAG.Parameter,
                            TAG.Temperature,
                        ]
                    },
                    "CO2_Alarm_Sensitivity_Parameter": {
                        "tags": [
                            TAG.Point,
                            TAG.Alarm,
                            TAG.Sensitivity,
                            TAG.Parameter,
                            TAG.CO2,
                        ]
                    },
                },
            },
            "Humidity_Parameter": {
                "tags": [TAG.Point, TAG.Humidity, TAG.Parameter],
                "subclasses": {
                    "High_Humidity_Alarm_Parameter": {
                        "tags": [
                            TAG.Point,
                            TAG.High,
                            TAG.Humidity,
                            TAG.Alarm,
                            TAG.Parameter,
                        ],
                    },
                    "Low_Humidity_Alarm_Parameter": {
                        "tags": [
                            TAG.Point,
                            TAG.Low,
                            TAG.Humidity,
                            TAG.Alarm,
                            TAG.Parameter,
                        ],
                    },
                },
            },
            "Load_Parameter": {
                "tags": [TAG.Point, TAG.Load, TAG.Parameter],
                "subclasses": {
                    "Max_Load_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Max,
                            TAG.Load,
                            TAG.Parameter,
                        ],
                    },
                    "Min_Load_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Min,
                            TAG.Load,
                            TAG.Parameter,
                        ],
                    },
                },
            },
            "Deadband": {
                "tags": [TAG.Point, TAG.Deadband, TAG.Parameter],
                BRICK.hasQuantity: QUDTQK.Dimensionless,
                "subclasses": {
                    "Humidity_Deadband": {
                        BRICK.hasQuantity: QUDTQK.RelativeHumidity,
                        "tags": [TAG.Point, TAG.Deadband, TAG.Parameter, TAG.Humidity],
                    },
                    "Temperature_Deadband": {
                        BRICK.hasQuantity: BRICK.Temperature,
                        "subclasses": {
                            "Occupied_Cooling_Temperature_Deadband": {
                                BRICK.hasQuantity: BRICK.Temperature,
                                "tags": [
                                    TAG.Point,
                                    TAG.Occupied,
                                    TAG.Cool,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Parameter,
                                ],
                                "parents": [BRICK.Cooling_Temperature_Setpoint],
                            },
                            "Occupied_Heating_Temperature_Deadband": {
                                BRICK.hasQuantity: BRICK.Temperature,
                                "tags": [
                                    TAG.Point,
                                    TAG.Occupied,
                                    TAG.Heat,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Parameter,
                                ],
                                "parents": [BRICK.Heating_Temperature_Setpoint],
                            },
                            "Unoccupied_Cooling_Temperature_Deadband": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Unoccupied,
                                    TAG.Cool,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Parameter,
                                ],
                                "parents": [BRICK.Cooling_Temperature_Setpoint],
                            },
                            "Unoccupied_Heating_Temperature_Deadband": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Unoccupied,
                                    TAG.Heat,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Parameter,
                                ],
                                "parents": [BRICK.Heating_Temperature_Setpoint],
                            },
                            "Supply_Air_Temperature_Deadband": {
                                BRICK.hasSubstance: [
                                    BRICK.Supply_Air,
                                    BRICK.Discharge_Air,
                                ],
                                BRICK.hasSubstance: [
                                    BRICK.Supply_Air,
                                    BRICK.Discharge_Air,
                                ],
                                BRICK.hasQuantity: BRICK.Temperature,
                                "aliases": [
                                    BRICK["Discharge_Air_Temperature_Deadband"]
                                ],
                                "subclasses": {
                                    "Heating_Supply_Air_Temperature_Deadband": {
                                        "aliases": [
                                            BRICK[
                                                "Heating_Discharge_Air_Temperature_Deadband"
                                            ]
                                        ],
                                        BRICK.hasQuantity: BRICK.Temperature,
                                        BRICK.hasSubstance: BRICK.Discharge_Air,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Heat,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Deadband,
                                            TAG.Parameter,
                                        ],
                                        "parents": [
                                            BRICK.Discharge_Air_Temperature_Heating_Setpoint,
                                            BRICK.Heating_Temperature_Setpoint,
                                        ],
                                    },
                                    "Cooling_Supply_Air_Temperature_Deadband": {
                                        "aliases": [
                                            BRICK[
                                                "Cooling_Discharge_Air_Temperature_Deadband"
                                            ]
                                        ],
                                        BRICK.hasQuantity: BRICK.Temperature,
                                        BRICK.hasSubstance: BRICK.Discharge_Air,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Cool,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Deadband,
                                            TAG.Parameter,
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
                                    TAG.Parameter,
                                ],
                                "parents": [
                                    BRICK.Discharge_Air_Temperature_Setpoint,
                                    BRICK.Air_Temperature_Setpoint,
                                ],
                            },
                            "Entering_Water_Temperature_Deadband": {
                                BRICK.hasSubstance: BRICK.Entering_Water,
                                BRICK.hasQuantity: BRICK.Temperature,
                                "tags": [
                                    TAG.Point,
                                    TAG.Entering,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Parameter,
                                ],
                                "parents": [BRICK.Entering_Water_Temperature_Setpoint],
                            },
                            "Leaving_Water_Temperature_Deadband": {
                                BRICK.hasSubstance: BRICK.Leaving_Water,
                                BRICK.hasQuantity: BRICK.Temperature,
                                "tags": [
                                    TAG.Point,
                                    TAG.Leaving,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Parameter,
                                ],
                                "parents": [BRICK.Leaving_Water_Temperature_Setpoint],
                            },
                        },
                        "tags": [
                            TAG.Point,
                            TAG.Temperature,
                            TAG.Deadband,
                            TAG.Parameter,
                        ],
                        "parents": [BRICK.Temperature_Setpoint],
                    },
                    "Air_Flow_Deadband": {
                        BRICK.hasSubstance: BRICK.Air,
                        BRICK.hasQuantity: QUDTQK.VolumeFlowRate,
                        "subclasses": {
                            "Exhaust_Air_Stack_Flow_Deadband": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Exhaust,
                                    TAG.Air,
                                    TAG.Stack,
                                    TAG.Flow,
                                    TAG.Deadband,
                                    TAG.Parameter,
                                ],
                                "parents": [BRICK.Exhaust_Air_Stack_Flow_Setpoint],
                            }
                        },
                        "tags": [
                            TAG.Point,
                            TAG.Air,
                            TAG.Flow,
                            TAG.Deadband,
                            TAG.Parameter,
                        ],
                        "parents": [BRICK.Air_Flow_Setpoint],
                    },
                    "Static_Pressure_Deadband": {
                        BRICK.hasQuantity: BRICK.Static_Pressure,
                        "tags": [
                            TAG.Point,
                            TAG.Static,
                            TAG.Pressure,
                            TAG.Deadband,
                            TAG.Parameter,
                        ],
                        "parents": [BRICK.Static_Pressure_Setpoint],
                        "subclasses": {
                            "Supply_Air_Static_Pressure_Deadband": {
                                BRICK.hasSubstance: [
                                    BRICK.Supply_Air,
                                    BRICK.Discharge_Air,
                                ],
                                BRICK.hasSubstance: [
                                    BRICK.Supply_Air,
                                    BRICK.Discharge_Air,
                                ],
                                BRICK.hasQuantity: BRICK.Static_Pressure,
                                "aliases": [
                                    BRICK["Discharge_Air_Static_Pressure_Deadband"]
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Deadband,
                                    TAG.Parameter,
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
            "Temperature_Parameter": {
                "tags": [TAG.Point, TAG.Temperature, TAG.Parameter],
                "subclasses": {
                    "High_Temperature_Alarm_Parameter": {
                        "tags": [
                            TAG.Point,
                            TAG.High,
                            TAG.Temperature,
                            TAG.Alarm,
                            TAG.Parameter,
                        ],
                    },
                    "Low_Temperature_Alarm_Parameter": {
                        "tags": [
                            TAG.Point,
                            TAG.Low,
                            TAG.Temperature,
                            TAG.Alarm,
                            TAG.Parameter,
                        ],
                    },
                    "Low_Freeze_Protect_Temperature_Parameter": {
                        "tags": [
                            TAG.Point,
                            TAG.Low,
                            TAG.Freeze,
                            TAG.Protect,
                            TAG.Temperature,
                            TAG.Parameter,
                        ],
                    },
                    "Lockout_Temperature_Differential_Parameter": {
                        "tags": [
                            TAG.Point,
                            TAG.Lockout,
                            TAG.Temperature,
                            TAG.Differential,
                            TAG.Sensor,
                        ],
                        "subclasses": {
                            "Outside_Air_Lockout_Temperature_Differential_Parameter": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Outside,
                                    TAG.Air,
                                    TAG.Lockout,
                                    TAG.Temperature,
                                    TAG.Differential,
                                    TAG.Parameter,
                                ],
                                "subclasses": {
                                    "Low_Outside_Air_Lockout_Temperature_Differential_Parameter": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Low,
                                            TAG.Outside,
                                            TAG.Air,
                                            TAG.Lockout,
                                            TAG.Temperature,
                                            TAG.Differential,
                                            TAG.Parameter,
                                        ],
                                    },
                                    "High_Outside_Air_Lockout_Temperature_Differential_Parameter": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.High,
                                            TAG.Outside,
                                            TAG.Air,
                                            TAG.Lockout,
                                            TAG.Temperature,
                                            TAG.Differential,
                                            TAG.Parameter,
                                        ],
                                    },
                                },
                            },
                        },
                    },
                },
            },
            "PID_Parameter": {
                "tags": [TAG.Point, TAG.Parameter, TAG.PID],
                "subclasses": {
                    "Gain_Parameter": {
                        "tags": [TAG.Point, TAG.Parameter, TAG.PID, TAG.Gain],
                        "subclasses": {
                            "Integral_Gain_Parameter": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Parameter,
                                    TAG.PID,
                                    TAG.Gain,
                                    TAG.Integral,
                                ],
                                "subclasses": {
                                    "Supply_Air_Integral_Gain_Parameter": {
                                        "aliases": [
                                            BRICK[
                                                "Discharge_Air_Integral_Gain_Parameter"
                                            ]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Integral,
                                            TAG.Gain,
                                            TAG.Parameter,
                                            TAG.PID,
                                        ],
                                    },
                                },
                            },
                            "Proportional_Gain_Parameter": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Parameter,
                                    TAG.PID,
                                    TAG.Gain,
                                    TAG.Proportional,
                                ],
                                "subclasses": {
                                    "Supply_Air_Proportional_Gain_Parameter": {
                                        "aliases": [
                                            BRICK[
                                                "Discharge_Air_Proportional_Gain_Parameter"
                                            ]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Parameter,
                                            TAG.PID,
                                            TAG.Gain,
                                            TAG.Proportional,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                        ],
                                    },
                                },
                            },
                            "Derivative_Gain_Parameter": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Parameter,
                                    TAG.PID,
                                    TAG.Gain,
                                    TAG.Derivative,
                                ],
                            },
                        },
                    },
                    "Step_Parameter": {
                        "tags": [TAG.Point, TAG.Parameter, TAG.Step],
                        "subclasses": {
                            "Differential_Pressure_Step_Parameter": {
                                "subclasses": {
                                    "Chilled_Water_Differential_Pressure_Step_Parameter": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Step,
                                            TAG.Parameter,
                                        ],
                                    }
                                },
                                "tags": [
                                    TAG.Point,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Step,
                                    TAG.Parameter,
                                ],
                            },
                            "Static_Pressure_Step_Parameter": {
                                "subclasses": {
                                    "Air_Static_Pressure_Step_Parameter": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Air,
                                            TAG.Static,
                                            TAG.Pressure,
                                            TAG.Step,
                                            TAG.Parameter,
                                        ],
                                        "subclasses": {
                                            "Supply_Air_Static_Pressure_Step_Parameter": {
                                                "aliases": [
                                                    BRICK[
                                                        "Discharge_Air_Static_Pressure_Step_Parameter"
                                                    ]
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Supply,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Static,
                                                    TAG.Pressure,
                                                    TAG.Step,
                                                    TAG.Parameter,
                                                ],
                                            },
                                        },
                                    }
                                },
                                "tags": [
                                    TAG.Point,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Step,
                                    TAG.Parameter,
                                ],
                            },
                            "Temperature_Step_Parameter": {
                                "subclasses": {
                                    "Air_Temperature_Step_Parameter": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Step,
                                            TAG.Parameter,
                                        ],
                                        "subclasses": {
                                            "Supply_Air_Temperature_Step_Parameter": {
                                                "aliases": [
                                                    BRICK[
                                                        "Discharge_Air_Temperature_Step_Parameter"
                                                    ]
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Supply,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Temperature,
                                                    TAG.Step,
                                                    TAG.Parameter,
                                                ],
                                            },
                                        },
                                    }
                                },
                                "parents": [BRICK.Temperature_Parameter],
                                "tags": [
                                    TAG.Point,
                                    TAG.Temperature,
                                    TAG.Step,
                                    TAG.Parameter,
                                ],
                            },
                        },
                    },
                    "Time_Parameter": {
                        "tags": [TAG.Point, TAG.Parameter, TAG.Time],
                        "subclasses": {
                            "Integral_Time_Parameter": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Parameter,
                                    TAG.PID,
                                    TAG.Time,
                                    TAG.Integral,
                                ],
                                "subclasses": {
                                    "Air_Temperature_Integral_Time_Parameter": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Parameter,
                                            TAG.PID,
                                            TAG.Time,
                                            TAG.Integral,
                                        ],
                                        "parents": [BRICK.Temperature_Parameter],
                                        "subclasses": {
                                            "Cooling_Supply_Air_Temperature_Integral_Time_Parameter": {
                                                "aliases": [
                                                    BRICK[
                                                        "Cooling_Discharge_Air_Temperature_Integral_Time_Parameter"
                                                    ]
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Cool,
                                                    TAG.Supply,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Temperature,
                                                    TAG.Integral,
                                                    TAG.Time,
                                                    TAG.Parameter,
                                                    TAG.PID,
                                                ],
                                            },
                                            "Heating_Supply_Air_Temperature_Integral_Time_Parameter": {
                                                "aliases": [
                                                    BRICK[
                                                        "Heating_Discharge_Air_Temperature_Integral_Time_Parameter"
                                                    ]
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Heat,
                                                    TAG.Supply,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Temperature,
                                                    TAG.Integral,
                                                    TAG.Time,
                                                    TAG.Parameter,
                                                    TAG.PID,
                                                ],
                                            },
                                        },
                                    },
                                    "Differential_Pressure_Integral_Time_Parameter": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Integral,
                                            TAG.Time,
                                            TAG.Parameter,
                                            TAG.PID,
                                        ],
                                        "subclasses": {
                                            "Hot_Water_Differential_Pressure_Integral_Time_Parameter": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Hot,
                                                    TAG.Water,
                                                    TAG.Differential,
                                                    TAG.Pressure,
                                                    TAG.Integral,
                                                    TAG.Time,
                                                    TAG.Parameter,
                                                    TAG.PID,
                                                ],
                                            },
                                            "Chilled_Water_Differential_Pressure_Integral_Time_Parameter": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Chilled,
                                                    TAG.Water,
                                                    TAG.Differential,
                                                    TAG.Pressure,
                                                    TAG.Integral,
                                                    TAG.Time,
                                                    TAG.Parameter,
                                                    TAG.PID,
                                                ],
                                            },
                                            "Leaving_Water_Differential_Pressure_Integral_Time_Parameter": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Leaving,
                                                    TAG.Water,
                                                    TAG.Differential,
                                                    TAG.Pressure,
                                                    TAG.Integral,
                                                    TAG.Time,
                                                    TAG.Parameter,
                                                    TAG.PID,
                                                ],
                                            },
                                            "Entering_Water_Differential_Pressure_Integral_Time_Parameter": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Entering,
                                                    TAG.Water,
                                                    TAG.Differential,
                                                    TAG.Pressure,
                                                    TAG.Integral,
                                                    TAG.Time,
                                                    TAG.Parameter,
                                                    TAG.PID,
                                                ],
                                            },
                                        },
                                    },
                                    "Exhaust_Air_Flow_Integral_Time_Parameter": {
                                        "subclasses": {
                                            "Exhaust_Air_Stack_Flow_Integral_Time_Parameter": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Exhaust,
                                                    TAG.Air,
                                                    TAG.Stack,
                                                    TAG.Flow,
                                                    TAG.Integral,
                                                    TAG.Time,
                                                    TAG.Parameter,
                                                    TAG.PID,
                                                ],
                                            }
                                        },
                                        "tags": [
                                            TAG.Point,
                                            TAG.Exhaust,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Integral,
                                            TAG.Time,
                                            TAG.Parameter,
                                            TAG.PID,
                                        ],
                                    },
                                    "Static_Pressure_Integral_Time_Parameter": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Static,
                                            TAG.Pressure,
                                            TAG.Integral,
                                            TAG.Time,
                                            TAG.Parameter,
                                            TAG.PID,
                                        ],
                                        "subclasses": {
                                            "Supply_Air_Static_Pressure_Integral_Time_Parameter": {
                                                "aliases": [
                                                    BRICK[
                                                        "Discharge_Air_Static_Pressure_Integral_Time_Parameter"
                                                    ]
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Supply,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Static,
                                                    TAG.Pressure,
                                                    TAG.Integral,
                                                    TAG.Time,
                                                    TAG.Parameter,
                                                    TAG.PID,
                                                ],
                                            },
                                        },
                                    },
                                    "Entering_Water_Temperature_Integral_Time_Parameter": {
                                        "parents": [BRICK.Temperature_Parameter],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Entering,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Integral,
                                            TAG.Time,
                                            TAG.Parameter,
                                            TAG.PID,
                                        ],
                                    },
                                    "Leaving_Water_Temperature_Integral_Time_Parameter": {
                                        "parents": [BRICK.Temperature_Parameter],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Leaving,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Integral,
                                            TAG.Time,
                                            TAG.Parameter,
                                            TAG.PID,
                                        ],
                                    },
                                },
                            },
                            "Derivative_Time_Parameter": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Parameter,
                                    TAG.PID,
                                    TAG.Time,
                                    TAG.Derivative,
                                ],
                            },
                        },
                    },
                    "Proportional_Band_Parameter": {
                        "tags": [
                            TAG.Point,
                            TAG.Proportional,
                            TAG.Band,
                            TAG.Parameter,
                            TAG.PID,
                        ],
                        "subclasses": {
                            "Differential_Pressure_Proportional_Band": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Proportional,
                                    TAG.Band,
                                    TAG.PID,
                                ],
                                "subclasses": {
                                    "Hot_Water_Differential_Pressure_Proportional_Band_Parameter": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Proportional,
                                            TAG.Band,
                                            TAG.Parameter,
                                            TAG.PID,
                                        ],
                                    },
                                    "Chilled_Water_Differential_Pressure_Proportional_Band_Parameter": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Proportional,
                                            TAG.Band,
                                            TAG.Parameter,
                                            TAG.PID,
                                        ],
                                    },
                                    "Leaving_Water_Differential_Pressure_Proportional_Band_Parameter": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Leaving,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Proportional,
                                            TAG.Band,
                                            TAG.Parameter,
                                            TAG.PID,
                                        ],
                                    },
                                    "Entering_Water_Differential_Pressure_Proportional_Band_Parameter": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Entering,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Proportional,
                                            TAG.Band,
                                            TAG.Parameter,
                                            TAG.PID,
                                        ],
                                    },
                                },
                            },
                            "Supply_Air_Temperature_Proportional_Band_Parameter": {
                                "aliases": [
                                    BRICK[
                                        "Discharge_Air_Temperature_Proportional_Band_Parameter"
                                    ]
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Proportional,
                                    TAG.Band,
                                    TAG.Parameter,
                                    TAG.PID,
                                ],
                                "parents": [BRICK.Temperature_Parameter],
                                "subclasses": {
                                    "Cooling_Supply_Air_Temperature_Proportional_Band_Parameter": {
                                        "aliases": [
                                            BRICK[
                                                "Cooling_Discharge_Air_Temperature_Proportional_Band_Parameter"
                                            ]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Cool,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Proportional,
                                            TAG.Band,
                                            TAG.Parameter,
                                            TAG.PID,
                                        ],
                                    },
                                    "Heating_Supply_Air_Temperature_Proportional_Band_Parameter": {
                                        "aliases": [
                                            BRICK[
                                                "Heating_Discharge_Air_Temperature_Proportional_Band_Parameter"
                                            ]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Heat,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Proportional,
                                            TAG.Band,
                                            TAG.Parameter,
                                            TAG.PID,
                                        ],
                                    },
                                },
                            },
                            "Exhaust_Air_Flow_Proportional_Band_Parameter": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Exhaust,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Proportional,
                                    TAG.Band,
                                    TAG.Parameter,
                                    TAG.PID,
                                ],
                                "subclasses": {
                                    "Exhaust_Air_Stack_Flow_Proportional_Band_Parameter": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Exhaust,
                                            TAG.Air,
                                            TAG.Stack,
                                            TAG.Flow,
                                            TAG.Proportional,
                                            TAG.Band,
                                            TAG.Parameter,
                                            TAG.PID,
                                        ],
                                    },
                                },
                            },
                            "Static_Pressure_Proportional_Band_Parameter": {
                                "subclasses": {
                                    "Exhaust_Air_Static_Pressure_Proportional_Band_Parameter": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Exhaust,
                                            TAG.Air,
                                            TAG.Static,
                                            TAG.Pressure,
                                            TAG.Proportional,
                                            TAG.Band,
                                            TAG.Parameter,
                                            TAG.PID,
                                        ],
                                    },
                                    "Supply_Air_Static_Pressure_Proportional_Band_Parameter": {
                                        "aliases": [
                                            BRICK[
                                                "Discharge_Air_Static_Pressure_Proportional_Band_Parameter"
                                            ]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Static,
                                            TAG.Pressure,
                                            TAG.Proportional,
                                            TAG.Band,
                                            TAG.Parameter,
                                            TAG.PID,
                                        ],
                                    },
                                },
                                "tags": [
                                    TAG.Point,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Proportional,
                                    TAG.Band,
                                    TAG.Parameter,
                                    TAG.PID,
                                ],
                            },
                            "Entering_Water_Temperature_Proportional_Band_Parameter": {
                                "parents": [BRICK.Temperature_Parameter],
                                "tags": [
                                    TAG.Point,
                                    TAG.Entering,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Proportional,
                                    TAG.Band,
                                    TAG.Parameter,
                                    TAG.PID,
                                ],
                            },
                            "Leaving_Water_Temperature_Proportional_Band_Parameter": {
                                "parents": [BRICK.Temperature_Parameter],
                                "tags": [
                                    TAG.Point,
                                    TAG.Leaving,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Proportional,
                                    TAG.Band,
                                    TAG.Parameter,
                                    TAG.PID,
                                ],
                            },
                        },
                    },
                },
            },
            "Tolerance_Parameter": {
                "tags": [TAG.Point, TAG.Tolerance, TAG.Parameter],
                "subclasses": {
                    "Humidity_Tolerance_Parameter": {
                        "tags": [TAG.Point, TAG.Tolerance, TAG.Parameter, TAG.Humidity],
                        "parents": [BRICK.Humidity_Parameter],
                    },
                    "Temperature_Tolerance_Parameter": {
                        "parents": [BRICK.Temperature_Parameter],
                        "tags": [
                            TAG.Point,
                            TAG.Tolerance,
                            TAG.Parameter,
                            TAG.Temperature,
                        ],
                    },
                },
            },
            "Limit": {
                "tags": [TAG.Point, TAG.Parameter, TAG.Limit],
                "subclasses": {
                    "Close_Limit": {
                        "tags": [TAG.Point, TAG.Close, TAG.Parameter, TAG.Limit],
                    },
                    "Speed_Setpoint_Limit": {
                        "tags": [
                            TAG.Point,
                            TAG.Speed,
                            TAG.Limit,
                            TAG.Parameter,
                        ],
                        "subclasses": {
                            "Max_Speed_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Max,
                                    TAG.Speed,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                                "parents": [BRICK.Max_Limit],
                            },
                            "Min_Speed_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Min,
                                    TAG.Speed,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                                "parents": [BRICK.Min_Limit],
                            },
                        },
                    },
                    "Air_Temperature_Setpoint_Limit": {
                        "tags": [
                            TAG.Point,
                            TAG.Air,
                            TAG.Temperature,
                            TAG.Limit,
                            TAG.Parameter,
                        ],
                        "parents": [BRICK.Temperature_Parameter],
                        "subclasses": {
                            "Supply_Air_Temperature_Setpoint_Limit": {
                                "aliases": [
                                    BRICK["Discharge_Air_Temperature_Setpoint_Limit"]
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                                "subclasses": {
                                    "Max_Supply_Air_Temperature_Setpoint_Limit": {
                                        "aliases": [
                                            BRICK[
                                                "Max_Discharge_Air_Temperature_Setpoint_Limit"
                                            ]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Max,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Limit,
                                            TAG.Parameter,
                                        ],
                                        "parents": [
                                            BRICK.Max_Temperature_Setpoint_Limit
                                        ],
                                    },
                                    "Min_Supply_Air_Temperature_Setpoint_Limit": {
                                        "aliases": [
                                            BRICK[
                                                "Min_Discharge_Air_Temperature_Setpoint_Limit"
                                            ]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Min,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Limit,
                                            TAG.Parameter,
                                        ],
                                        "parents": [
                                            BRICK.Min_Temperature_Setpoint_Limit
                                        ],
                                    },
                                },
                            },
                        },
                    },
                    "Air_Flow_Setpoint_Limit": {
                        "tags": [
                            TAG.Point,
                            TAG.Air,
                            TAG.Flow,
                            TAG.Limit,
                            TAG.Parameter,
                        ],
                        "subclasses": {
                            "Max_Air_Flow_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Max,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                            },
                            "Min_Air_Flow_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Min,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                            },
                        },
                    },
                    "Current_Limit": {
                        "tags": [TAG.Point, TAG.Current, TAG.Limit, TAG.Parameter],
                    },
                    "Position_Limit": {
                        "tags": [TAG.Point, TAG.Position, TAG.Limit],
                        "subclasses": {
                            "Max_Position_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Max,
                                    TAG.Position,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                                "parents": [BRICK.Max_Limit],
                            },
                            "Min_Position_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Min,
                                    TAG.Position,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                                "parents": [BRICK.Min_Limit],
                            },
                        },
                    },
                    "Differential_Pressure_Setpoint_Limit": {
                        "tags": [
                            TAG.Point,
                            TAG.Differential,
                            TAG.Pressure,
                            TAG.Limit,
                            TAG.Parameter,
                        ],
                        "subclasses": {
                            "Max_Chilled_Water_Differential_Pressure_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Max,
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                            },
                            "Min_Chilled_Water_Differential_Pressure_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Min,
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                            },
                            "Max_Hot_Water_Differential_Pressure_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Max,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                            },
                            "Min_Hot_Water_Differential_Pressure_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Min,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                            },
                        },
                    },
                    "Fresh_Air_Setpoint_Limit": {
                        "tags": [
                            TAG.Point,
                            TAG.Fresh,
                            TAG.Air,
                            TAG.Limit,
                            TAG.Parameter,
                        ],
                        "subclasses": {
                            "Min_Fresh_Air_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Min,
                                    TAG.Fresh,
                                    TAG.Air,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                                "parents": [BRICK.Min_Limit],
                            },
                            "Max_Fresh_Air_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Max,
                                    TAG.Fresh,
                                    TAG.Air,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                                "parents": [BRICK.Max_Limit],
                            },
                        },
                    },
                    "Ventilation_Air_Flow_Ratio_Limit": {
                        "tags": [
                            TAG.Point,
                            TAG.Ventilation,
                            TAG.Air,
                            TAG.Ratio,
                            TAG.Limit,
                        ],
                    },
                    "Static_Pressure_Setpoint_Limit": {
                        "tags": [
                            TAG.Point,
                            TAG.Static,
                            TAG.Pressure,
                            TAG.Limit,
                            TAG.Parameter,
                        ],
                        "subclasses": {
                            "Min_Static_Pressure_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Min,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                            },
                            "Max_Static_Pressure_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Max,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                            },
                            "High_Static_Pressure_Cutout_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.High,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Cutout,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                            },
                        },
                    },
                    "Max_Limit": {
                        "tags": [TAG.Point, TAG.Max, TAG.Limit, TAG.Parameter],
                        "subclasses": {
                            "Max_Speed_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Max,
                                    TAG.Speed,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                            },
                            "Max_Supply_Air_Static_Pressure_Setpoint_Limit": {
                                "aliases": [
                                    BRICK[
                                        "Max_Discharge_Air_Static_Pressure_Setpoint_Limit"
                                    ]
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Max,
                                    TAG.Supply,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                            },
                            "Max_Chilled_Water_Differential_Pressure_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Max,
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                            },
                            "Max_Hot_Water_Differential_Pressure_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Max,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                            },
                            "Max_Static_Pressure_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Max,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                                "subclasses": {
                                    "Max_Supply_Air_Static_Pressure_Setpoint_Limit": {
                                        "aliases": [
                                            BRICK[
                                                "Max_Discharge_Air_Static_Pressure_Setpoint_Limit"
                                            ]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Max,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Static,
                                            TAG.Pressure,
                                            TAG.Limit,
                                            TAG.Parameter,
                                        ],
                                    },
                                },
                            },
                            "Max_Temperature_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Max,
                                    TAG.Temperature,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                                "parents": [BRICK.Temperature_Parameter],
                            },
                            "Max_Air_Flow_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Max,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                                "subclasses": {
                                    "Max_Outside_Air_Flow_Setpoint_Limit": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Max,
                                            TAG.Outside,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Limit,
                                            TAG.Parameter,
                                        ],
                                    },
                                    "Max_Cooling_Supply_Air_Flow_Setpoint_Limit": {
                                        "aliases": [
                                            BRICK[
                                                "Max_Cooling_Discharge_Air_Flow_Setpoint_Limit"
                                            ]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Max,
                                            TAG.Cool,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Limit,
                                            TAG.Parameter,
                                        ],
                                        "subclasses": {
                                            "Max_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit": {
                                                "aliases": [
                                                    BRICK[
                                                        "Max_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit"
                                                    ]
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Max,
                                                    TAG.Occupied,
                                                    TAG.Cool,
                                                    TAG.Supply,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Limit,
                                                    TAG.Parameter,
                                                ],
                                            },
                                            "Max_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit": {
                                                "aliases": [
                                                    BRICK[
                                                        "Max_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit"
                                                    ]
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Max,
                                                    TAG.Unoccupied,
                                                    TAG.Cool,
                                                    TAG.Supply,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Limit,
                                                    TAG.Parameter,
                                                ],
                                            },
                                        },
                                    },
                                    "Max_Heating_Supply_Air_Flow_Setpoint_Limit": {
                                        "aliases": [
                                            BRICK[
                                                "Max_Heating_Discharge_Air_Flow_Setpoint_Limit"
                                            ]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Max,
                                            TAG.Heat,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Limit,
                                            TAG.Parameter,
                                        ],
                                        "subclasses": {
                                            "Max_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit": {
                                                "aliases": [
                                                    BRICK[
                                                        "Max_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit"
                                                    ]
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Max,
                                                    TAG.Occupied,
                                                    TAG.Heat,
                                                    TAG.Supply,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Limit,
                                                    TAG.Parameter,
                                                ],
                                            },
                                            "Max_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit": {
                                                "aliases": [
                                                    BRICK[
                                                        "Max_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit"
                                                    ]
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Max,
                                                    TAG.Unoccupied,
                                                    TAG.Heat,
                                                    TAG.Supply,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Limit,
                                                    TAG.Parameter,
                                                ],
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    "Min_Limit": {
                        "tags": [TAG.Point, TAG.Min, TAG.Limit, TAG.Parameter],
                        "subclasses": {
                            "Min_Speed_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Min,
                                    TAG.Speed,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                            },
                            "Min_Hot_Water_Differential_Pressure_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Min,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                            },
                            "Min_Chilled_Water_Differential_Pressure_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Min,
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                            },
                            "Min_Supply_Air_Static_Pressure_Setpoint_Limit": {
                                "aliases": [
                                    BRICK[
                                        "Min_Discharge_Air_Static_Pressure_Setpoint_Limit"
                                    ]
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Min,
                                    TAG.Supply,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                            },
                            "Min_Temperature_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Min,
                                    TAG.Temperature,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                                "parents": [BRICK.Temperature_Parameter],
                            },
                            "Min_Static_Pressure_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Min,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                                "subclasses": {
                                    "Min_Supply_Air_Static_Pressure_Setpoint_Limit": {
                                        "aliases": [
                                            BRICK[
                                                "Min_Discharge_Air_Static_Pressure_Setpoint_Limit"
                                            ]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Min,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Static,
                                            TAG.Pressure,
                                            TAG.Limit,
                                            TAG.Parameter,
                                        ],
                                    },
                                },
                            },
                            "Min_Air_Flow_Setpoint_Limit": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Min,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Limit,
                                    TAG.Parameter,
                                ],
                                "subclasses": {
                                    "Min_Outside_Air_Flow_Setpoint_Limit": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Min,
                                            TAG.Outside,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Limit,
                                            TAG.Parameter,
                                        ],
                                    },
                                    "Min_Cooling_Supply_Air_Flow_Setpoint_Limit": {
                                        "aliases": [
                                            BRICK[
                                                "Min_Cooling_Discharge_Air_Flow_Setpoint_Limit"
                                            ]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Min,
                                            TAG.Cool,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Limit,
                                            TAG.Parameter,
                                        ],
                                        "subclasses": {
                                            "Min_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit": {
                                                "aliases": [
                                                    BRICK[
                                                        "Min_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit"
                                                    ]
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Min,
                                                    TAG.Occupied,
                                                    TAG.Cool,
                                                    TAG.Supply,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Limit,
                                                    TAG.Parameter,
                                                ],
                                            },
                                            "Min_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit": {
                                                "aliases": [
                                                    BRICK[
                                                        "Min_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit"
                                                    ]
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Min,
                                                    TAG.Unoccupied,
                                                    TAG.Cool,
                                                    TAG.Supply,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Limit,
                                                    TAG.Parameter,
                                                ],
                                            },
                                        },
                                    },
                                    "Min_Heating_Supply_Air_Flow_Setpoint_Limit": {
                                        "aliases": [
                                            BRICK[
                                                "Min_Heating_Discharge_Air_Flow_Setpoint_Limit"
                                            ]
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Min,
                                            TAG.Heat,
                                            TAG.Supply,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Limit,
                                            TAG.Parameter,
                                        ],
                                        "subclasses": {
                                            "Min_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit": {
                                                "aliases": [
                                                    BRICK[
                                                        "Min_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit"
                                                    ]
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Min,
                                                    TAG.Occupied,
                                                    TAG.Heat,
                                                    TAG.Supply,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Limit,
                                                    TAG.Parameter,
                                                ],
                                            },
                                            "Min_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit": {
                                                "aliases": [
                                                    BRICK[
                                                        "Min_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit"
                                                    ]
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Min,
                                                    TAG.Unoccupied,
                                                    TAG.Heat,
                                                    TAG.Supply,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Limit,
                                                    TAG.Parameter,
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
        },
    }
}
