"""
Provides definitions of the brick:Parameter classes
"""

from .namespaces import TAG, BRICK, OWL

parameter_definitions = {
    "Parameter": {
        "tags": [TAG.Point, TAG.Parameter],
        "subclasses": {
            # These would be new classes eliminating many high/low sp limits + high/low alarm params
            # A parameter describing the threshold value at which an alarm fires
            "Alarm_Threshold": {
                "tags": [TAG.Alarm, TAG.Threshold, TAG.Point, TAG.Parameter],
                "subclasses": {
                    "High_Alarm_Threshold": {
                        "tags": [
                            TAG.High,
                            TAG.Alarm,
                            TAG.Threshold,
                            TAG.Point,
                            TAG.Parameter,
                        ],
                    },
                    "Low_Alarm_Threshold": {
                        "tags": [
                            TAG.Low,
                            TAG.Alarm,
                            TAG.Threshold,
                            TAG.Point,
                            TAG.Parameter,
                        ],
                    },
                },
            },
            # A setpoint limit is the highest or lowest value that can be assigned to a setpoint
            "Setpoint_Limit": {
                "tags": [TAG.Setpoint, TAG.Limit, TAG.Point, TAG.Parameter],
                "parents": [BRICK.Limit],
                "subclasses": {
                    "High_Setpoint_Limit": {
                        "tags": [
                            TAG.High,
                            TAG.Setpoint,
                            TAG.Limit,
                            TAG.Point,
                            TAG.Parameter,
                        ],
                    },
                    "Low_Setpoint_Limit": {
                        "tags": [
                            TAG.Low,
                            TAG.Setpoint,
                            TAG.Limit,
                            TAG.Point,
                            TAG.Parameter,
                        ],
                    },
                },
            },
            "Delay_Parameter": {
                "tags": [TAG.Point, TAG.Delay, TAG.Parameter],
                "subclasses": {
                    "Alarm_Delay_Parameter": {
                        "tags": [TAG.Point, TAG.Alarm, TAG.Delay, TAG.Parameter],
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
                            TAG.Setpoint,
                        ],
                    },
                },
            },
            "Humidity_Parameter": {"tags": [TAG.Point, TAG.Humidity, TAG.Parameter]},
            "Temperature_Parameter": {
                "tags": [TAG.Point, TAG.Temperature, TAG.Parameter],
                "subclasses": {
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
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Integral,
                                            TAG.Gain,
                                            TAG.Parameter,
                                            TAG.PID,
                                        ],
                                    }
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
                                        "tags": [
                                            TAG.Point,
                                            TAG.Parameter,
                                            TAG.PID,
                                            TAG.Gain,
                                            TAG.Proportional,
                                            TAG.Supply,
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
                                            "Discharge_Air_Static_Pressure_Step_Parameter": {
                                                "tags": [
                                                    TAG.Point,
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
                                            "Discharge_Air_Temperature_Step_Parameter": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Temperature,
                                                    TAG.Step,
                                                    TAG.Parameter,
                                                ],
                                            },
                                            "Supply_Air_Temperature_Step_Parameter": {
                                                OWL.equivalentClass: BRICK[
                                                    "Discharge_Air_Temperature_Step_Parameter"
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Supply,
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
                                            "Cooling_Discharge_Air_Temperature_Integral_Time_Parameter": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Cool,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Temperature,
                                                    TAG.Integral,
                                                    TAG.Time,
                                                    TAG.Parameter,
                                                    TAG.PID,
                                                ],
                                            },
                                            "Cooling_Supply_Air_Temperature_Integral_Time_Parameter": {
                                                OWL.equivalentClass: BRICK[
                                                    "Cooling_Discharge_Air_Temperature_Integral_Time_Parameter"
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Cool,
                                                    TAG.Supply,
                                                    TAG.Air,
                                                    TAG.Temperature,
                                                    TAG.Integral,
                                                    TAG.Time,
                                                    TAG.Parameter,
                                                    TAG.PID,
                                                ],
                                            },
                                            "Heating_Discharge_Air_Temperature_Integral_Time_Parameter": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Heat,
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
                                                OWL.equivalentClass: BRICK[
                                                    "Heating_Discharge_Air_Temperature_Integral_Time_Parameter"
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Heat,
                                                    TAG.Supply,
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
                                            "Discharge_Water_Differential_Pressure_Integral_Time_Parameter": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Discharge,
                                                    TAG.Water,
                                                    TAG.Differential,
                                                    TAG.Pressure,
                                                    TAG.Integral,
                                                    TAG.Time,
                                                    TAG.Parameter,
                                                    TAG.PID,
                                                ],
                                            },
                                            "Supply_Water_Differential_Pressure_Integral_Time_Parameter": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Supply,
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
                                            "Discharge_Air_Static_Pressure_Integral_Time_Parameter": {
                                                "tags": [
                                                    TAG.Point,
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
                                            "Supply_Air_Static_Pressure_Integral_Time_Parameter": {
                                                OWL.equivalentClass: BRICK[
                                                    "Discharge_Air_Static_Pressure_Integral_Time_Parameter"
                                                ],
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Supply,
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
                                    "Supply_Water_Differential_Pressure_Integral_Time_Parameter": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Integral,
                                            TAG.Time,
                                            TAG.Parameter,
                                            TAG.PID,
                                        ],
                                    },
                                    "Supply_Water_Temperature_Integral_Time_Parameter": {
                                        "parents": [BRICK.Temperature_Parameter],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
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
                            TAG.Parameter,
                            TAG.PID,
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
                                    "Discharge_Water_Differential_Pressure_Proportional_Band_Parameter": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Discharge,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Proportional,
                                            TAG.Band,
                                            TAG.Parameter,
                                            TAG.PID,
                                        ],
                                    },
                                    "Supply_Water_Differential_Pressure_Proportional_Band_Parameter": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
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
                            "Discharge_Air_Temperature_Proportional_Band_Parameter": {
                                "tags": [
                                    TAG.Point,
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
                                    "Heating_Discharge_Air_Temperature_Proportional_Band_Parameter": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Heat,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Proportional,
                                            TAG.Band,
                                            TAG.Parameter,
                                            TAG.PID,
                                        ],
                                    },
                                    "Cooling_Discharge_Air_Temperature_Proportional_Band_Parameter": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Cool,
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
                            "Supply_Air_Temperature_Proportional_Band_Parameter": {
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Air_Temperature_Proportional_Band_Parameter"
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
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
                                        OWL.equivalentClass: BRICK[
                                            "Cooling_Discharge_Air_Temperature_Proportional_Band_Parameter"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Cool,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Proportional,
                                            TAG.Band,
                                            TAG.Parameter,
                                            TAG.PID,
                                        ],
                                    },
                                    "Heating_Supply_Air_Temperature_Proportional_Band_Parameter": {
                                        OWL.equivalentClass: BRICK[
                                            "Heating_Discharge_Air_Temperature_Proportional_Band_Parameter"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Heat,
                                            TAG.Supply,
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
                                    "Discharge_Air_Static_Pressure_Proportional_Band_Parameter": {
                                        "tags": [
                                            TAG.Point,
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
                                        OWL.equivalentClass: BRICK[
                                            "Discharge_Air_Static_Pressure_Proportional_Band_Parameter"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
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
                            "Supply_Water_Temperature_Proportional_Band_Parameter": {
                                "parents": [BRICK.Temperature_Parameter],
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Proportional,
                                    TAG.Band,
                                    TAG.Parameter,
                                    TAG.PID,
                                ],
                            },
                            "Discharge_Water_Temperature_Proportional_Band_Parameter": {
                                "parents": [BRICK.Temperature_Parameter],
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
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
                    "Current_Limit": {
                        "tags": [TAG.Point, TAG.Current, TAG.Limit, TAG.Parameter],
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
                },
            },
        },
    }
}


# setpoint limits
"""
Speed_Setpoint_Limit
Air_Temperature_Setpoint_Limit + (Discharge)
Air_Flow_Setpoint_Limit:
- occupied/unoccupied, heating/cooling, supply/discharge
Position_Setpoint_Limit
Differential_Pressure_Setpoint_Limit + (chilled water, hot water):
- hot/chilled water, discharge/supply air, many others
Fresh_Air_Setpoint_Limit
Static_Pressure_Setpoint_Limit
- high static pressure cutout setpoint limit?
"""
