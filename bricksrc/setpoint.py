from .namespaces import TAG, BRICK, OWL, SKOS
from rdflib import Literal

setpoint_definitions = {
    "Setpoint": {
        "tags": [TAG.Point, TAG.Setpoint],
        "subclasses": {
            "Enthalpy_Setpoint": {"tags": [TAG.Point, TAG.Setpoint, TAG.Enthalpy]},
            "Dew_Point_Setpoint": {"tags": [TAG.Point, TAG.Dewpoint, TAG.Setpoint]},
            "Demand_Setpoint": {
                "tags": [TAG.Point, TAG.Demand, TAG.Setpoint],
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
                        "tags": [
                            TAG.Point,
                            TAG.Air,
                            TAG.Flow,
                            TAG.Demand,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Discharge_Air_Flow_Demand_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Demand,
                                    TAG.Setpoint,
                                ],
                            },
                            "Supply_Air_Flow_Demand_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
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
                "tags": [TAG.Point, TAG.Damper, TAG.Position, TAG.Setpoint],
            },
            "Deadband_Setpoint": {
                "tags": [TAG.Point, TAG.Deadband, TAG.Setpoint],
                "subclasses": {
                    "Differential_Pressure_Deadband_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Differential,
                            TAG.Pressure,
                            TAG.Deadband,
                            TAG.Setpoint,
                        ],
                        "parents": [BRICK.Differential_Pressure_Setpoint],
                        "subclasses": {
                            "Hot_Water_Differential_Pressure_Deadband_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [
                                    BRICK.Hot_Water_Differential_Pressure_Setpoint
                                ],
                            },
                            "Chilled_Water_Differential_Pressure_Deadband_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [
                                    BRICK.Chilled_Water_Differential_Pressure_Setpoint
                                ],
                                "subclasses": {
                                    "Chilled_Water_Pump_Differential_Pressure_Deadband_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Pump,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Deadband,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Discharge_Water_Differential_Pressure_Deadband_Setpoint": {
                                "subclasses": {
                                    "Thermal_Energy_Storage_Discharge_Water_Differential_Pressure_Deadband_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Thermal,
                                            TAG.Energy,
                                            TAG.Storage,
                                            TAG.Discharge,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Deadband,
                                            TAG.Setpoint,
                                        ],
                                    }
                                },
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                            },
                            "Supply_Water_Differential_Pressure_Deadband_Setpoint": {
                                "subclasses": {
                                    "Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Deadband_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Thermal,
                                            TAG.Energy,
                                            TAG.Storage,
                                            TAG.Supply,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Deadband,
                                            TAG.Setpoint,
                                        ],
                                    }
                                },
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                    "Temperature_Deadband_Setpoint": {
                        "subclasses": {
                            "Occupied_Cooling_Temperature_Deadband_Setpoint": {
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
                            "Discharge_Air_Temperature_Deadband_Setpoint": {
                                "subclasses": {
                                    "Heating_Discharge_Air_Temperature_Deadband_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Heat,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Deadband,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Discharge_Air_Temperature_Heating_Setpoint
                                        ],
                                    },
                                    "Cooling_Discharge_Air_Temperature_Deadband_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Cool,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Deadband,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Discharge_Air_Temperature_Cooling_Setpoint
                                        ],
                                    },
                                },
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Discharge_Air_Temperature_Setpoint],
                            },
                            "Supply_Air_Temperature_Deadband_Setpoint": {
                                "subclasses": {
                                    "Heating_Supply_Air_Temperature_Deadband_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Heat,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Deadband,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Heating_Temperature_Setpoint],
                                    },
                                    "Cooling_Supply_Air_Temperature_Deadband_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Cool,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Deadband,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Cooling_Temperature_Setpoint],
                                    },
                                },
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Air_Temperature_Setpoint],
                            },
                            "Supply_Water_Temperature_Deadband_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Supply_Water_Temperature_Setpoint],
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
                        "tags": [
                            TAG.Point,
                            TAG.Static,
                            TAG.Pressure,
                            TAG.Deadband,
                            TAG.Setpoint,
                        ],
                        "parents": [BRICK.Static_Pressure_Setpoint],
                        "subclasses": {
                            "Discharge_Air_Static_Pressure_Deadband_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [
                                    BRICK.Discharge_Air_Static_Pressure_Setpoint
                                ],
                            },
                            "Supply_Air_Static_Pressure_Deadband_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Air,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Deadband,
                                    TAG.Setpoint,
                                ],
                                "parents": [BRICK.Supply_Air_Static_Pressure_Setpoint],
                            },
                        },
                    },
                },
            },
            "Flow_Setpoint": {
                "tags": [TAG.Point, TAG.Flow, TAG.Setpoint],
                "subclasses": {
                    "Air_Flow_Setpoint": {
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
                            "Discharge_Air_Flow_Setpoint": {
                                "subclasses": {
                                    "Discharge_Air_Flow_Demand_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Demand,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Cooling_Discharge_Air_Flow_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Cool,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                        "subclasses": {
                                            "Unoccupied_Cooling_Discharge_Air_Flow_Setpoint": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Unoccupied,
                                                    TAG.Cool,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Setpoint,
                                                ],
                                            },
                                        },
                                    },
                                    "Heating_Discharge_Air_Flow_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Heat,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Occupied_Discharge_Air_Flow_Setpoint": {
                                        "subclasses": {
                                            "Occupied_Cooling_Discharge_Air_Flow_Setpoint": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Occupied,
                                                    TAG.Cool,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Cooling_Discharge_Air_Flow_Setpoint
                                                ],
                                            },
                                            "Occupied_Heating_Discharge_Air_Flow_Setpoint": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Occupied,
                                                    TAG.Heat,
                                                    TAG.Discharge,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Heating_Discharge_Air_Flow_Setpoint
                                                ],
                                            },
                                        },
                                        "tags": [
                                            TAG.Point,
                                            TAG.Occupied,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                            },
                            "Exhaust_Air_Flow_Setpoint": {
                                "subclasses": {
                                    "Exhaust_Air_Stack_Flow_Setpoint": {
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
                            "Fan_Air_Flow_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Fan,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                            },
                            "Outside_Air_Flow_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Outside,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                            },
                            "Supply_Air_Flow_Setpoint": {
                                "subclasses": {
                                    "Supply_Air_Flow_Demand_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Demand,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Occupied_Supply_Air_Flow_Setpoint": {
                                        "subclasses": {
                                            "Occupied_Cooling_Supply_Air_Flow_Setpoint": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Occupied,
                                                    TAG.Cool,
                                                    TAG.Supply,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Cooling_Supply_Air_Flow_Setpoint
                                                ],
                                            },
                                            "Occupied_Heating_Supply_Air_Flow_Setpoint": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Occupied,
                                                    TAG.Heat,
                                                    TAG.Supply,
                                                    TAG.Air,
                                                    TAG.Flow,
                                                    TAG.Setpoint,
                                                ],
                                                "parents": [
                                                    BRICK.Heating_Supply_Air_Flow_Setpoint
                                                ],
                                            },
                                        },
                                        "tags": [
                                            TAG.Point,
                                            TAG.Occupied,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Cooling_Supply_Air_Flow_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Cool,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Heating_Supply_Air_Flow_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Heat,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    }
                },
            },
            "Humidity_Setpoint": {"tags": [TAG.Point, TAG.Humidity, TAG.Setpoint]},
            "Load_Setpoint": {
                "subclasses": {
                    "Load_Shed_Setpoint": {
                        "tags": [TAG.Point, TAG.Shed, TAG.Load, TAG.Setpoint],
                        "subclasses": {
                            "Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed_Setpoint": {
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
                            "Medium_Temperature_Hot_Water_Supply_Temperature_Load_Shed_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Medium,
                                    TAG.Temperature,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Supply,
                                    TAG.Pressure,
                                    TAG.Shed,
                                    TAG.Load,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    }
                },
                "tags": [TAG.Point, TAG.Load, TAG.Setpoint],
            },
            "Luminance_Setpoint": {"tags": [TAG.Point, TAG.Luminance, TAG.Setpoint]},
            "Mode_Setpoint": {
                "subclasses": {
                    "Dual_Band_Mode_Setpoint": {
                        "tags": [TAG.Point, TAG.Dual, TAG.Band, TAG.Mode, TAG.Setpoint],
                    },
                    "Unoccupied_Mode_Setpoint": {
                        "tags": [TAG.Point, TAG.Unoccupied, TAG.Mode, TAG.Setpoint],
                    },
                    "Occupied_Mode_Setpoint": {
                        "tags": [TAG.Point, TAG.Occupied, TAG.Mode, TAG.Setpoint],
                    },
                },
                "tags": [TAG.Point, TAG.Mode, TAG.Setpoint],
            },
            "Pressure_Setpoint": {
                "subclasses": {
                    "Differential_Pressure_Setpoint": {
                        "subclasses": {
                            "Chilled_Water_Differential_Pressure_Setpoint": {
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
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                            },
                            "Load_Shed_Differential_Pressure_Setpoint": {
                                "parents": [BRICK.Load_Shed_Setpoint],
                                "subclasses": {
                                    "Chilled_Water_Differential_Pressure_Load_Shed_Setpoint": {
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
                    "Static_Pressure_Setpoint": {
                        "subclasses": {
                            "Building_Air_Static_Pressure_Setpoint": {
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
                                "tags": [
                                    TAG.Point,
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                            },
                            "Discharge_Air_Static_Pressure_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
                            },
                            "Exhaust_Air_Static_Pressure_Setpoint": {
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
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Air,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Setpoint,
                                ],
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
            "Request_Setpoint": {
                "tags": [TAG.Point, TAG.Request, TAG.Setpoint],
                "subclasses": {
                    "Cooling_Request_Setpoint": {
                        "tags": [TAG.Point, TAG.Cool, TAG.Request, TAG.Setpoint],
                        "subclasses": {
                            "Cooling_Request_Percent_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Cool,
                                    TAG.Request,
                                    TAG.Percent,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                    "Heating_Request_Setpoint": {
                        "tags": [TAG.Point, TAG.Heat, TAG.Request, TAG.Setpoint],
                        "subclasses": {
                            "Heating_Request_Percent_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Heat,
                                    TAG.Request,
                                    TAG.Percent,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                },
            },
            "Reset_Setpoint": {
                "tags": [TAG.Point, TAG.Reset, TAG.Setpoint],
                SKOS.definition: Literal("Setpoints used in Reset strategies"),
                "subclasses": {
                    "Discharge_Air_Flow_Reset_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Discharge,
                            TAG.Air,
                            TAG.Flow,
                            TAG.Reset,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Discharge_Air_Flow_Reset_High_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                    TAG.High,
                                ],
                            },
                            "Discharge_Air_Flow_Reset_Low_Setpoint": {
                                "tags": [
                                    TAG.Point,
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
                    "Temperature_Differential_Reset_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Temperature,
                            TAG.Differential,
                            TAG.Reset,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Discharge_Air_Temperature_Reset_Differential_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Differential,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Discharge_Air_Temperature_Reset_High_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Differential,
                                            TAG.Reset,
                                            TAG.Setpoint,
                                            TAG.High,
                                        ],
                                    },
                                    "Discharge_Air_Temperature_Reset_Low_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Differential,
                                            TAG.Reset,
                                            TAG.Setpoint,
                                            TAG.Low,
                                        ],
                                    },
                                },
                            },
                            "Supply_Air_Temperature_Reset_Differential_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Differential,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                    "Temperature_High_Reset_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Temperature,
                            TAG.High,
                            TAG.Reset,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Hot_Water_Supply_Temperature_High_Reset_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Supply,
                                    TAG.Temperature,
                                    TAG.High,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Medium_Temperature_Hot_Water_Discharge_Temperature_High_Reset_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Medium,
                                            TAG.Temperature,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Discharge,
                                            TAG.Temperature,
                                            TAG.High,
                                            TAG.Reset,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Medium_Temperature_Hot_Water_Supply_Temperature_High_Reset_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Medium,
                                            TAG.Temperature,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Supply,
                                            TAG.Temperature,
                                            TAG.High,
                                            TAG.Reset,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Supply_Air_Temperature_Reset_High_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.High,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                            },
                            "Outside_Air_Temperature_High_Reset_Setpoint": {
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
                        },
                    },
                    "Temperature_Low_Reset_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Temperature,
                            TAG.Low,
                            TAG.Reset,
                            TAG.Setpoint,
                        ],
                        "subclasses": {
                            "Supply_Air_Temperature_Reset_Low_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Low,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                            },
                            "Hot_Water_Supply_Temperature_Low_Reset_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Supply,
                                    TAG.Temperature,
                                    TAG.Low,
                                    TAG.Reset,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Medium_Temperature_Hot_Water_Supply_Temperature_Low_Reset_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Medium,
                                            TAG.Temperature,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Supply,
                                            TAG.Temperature,
                                            TAG.Low,
                                            TAG.Reset,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Medium_Temperature_Hot_Water_Discharge_Temperature_Low_Reset_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Medium,
                                            TAG.Temperature,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Discharge,
                                            TAG.Temperature,
                                            TAG.Low,
                                            TAG.Reset,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Outside_Air_Temperature_Low_Reset_Setpoint": {
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
                        },
                    },
                },
            },
            "Speed_Setpoint": {
                "tags": [TAG.Point, TAG.Speed, TAG.Setpoint],
                "subclasses": {
                    "Rated_Speed_Setpoint": {
                        "tags": [TAG.Point, TAG.Rated, TAG.Speed, TAG.Setpoint],
                    },
                    "Differential_Speed_Setpoint": {
                        "tags": [TAG.Point, TAG.Differential, TAG.Speed, TAG.Setpoint],
                        "subclasses": {
                            "Discharge_Fan_Differential_Speed_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Fan,
                                    TAG.Differential,
                                    TAG.Speed,
                                    TAG.Setpoint,
                                ],
                            },
                            "Return_Fan_Differential_Speed_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Return,
                                    TAG.Fan,
                                    TAG.Differential,
                                    TAG.Speed,
                                    TAG.Setpoint,
                                ],
                            },
                            "Supply_Fan_Differential_Speed_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Fan,
                                    TAG.Differential,
                                    TAG.Speed,
                                    TAG.Setpoint,
                                ],
                            },
                        },
                    },
                },
            },
            "Temperature_Setpoint": {
                "tags": [TAG.Point, TAG.Temperature, TAG.Setpoint],
                "subclasses": {
                    "Air_Temperature_Setpoint": {
                        "tags": [TAG.Point, TAG.Air, TAG.Temperature, TAG.Setpoint],
                        "subclasses": {
                            "Differential_Air_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Differential,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Discharge_Air_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Discharge_Air_Temperature_Heating_Setpoint": {
                                        OWL.equivalentClass: BRICK[
                                            "Min_Discharge_Air_Temperature_Setpoint"
                                        ],
                                        "parents": [BRICK.Heating_Temperature_Setpoint],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Heat,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Min_Discharge_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Min,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Max_Discharge_Air_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Max,
                                            TAG.Setpoint,
                                        ],
                                    },
                                    "Discharge_Air_Temperature_Cooling_Setpoint": {
                                        OWL.equivalentClass: BRICK[
                                            "Max_Discharge_Air_Temperature_Setpoint"
                                        ],
                                        "parents": [BRICK.Cooling_Temperature_Setpoint],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Cool,
                                            TAG.Setpoint,
                                        ],
                                    },
                                },
                            },
                            "Effective_Air_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Effective,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                                "subclasses": {
                                    "Effective_Air_Temperature_Cooling_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Effective,
                                            TAG.Air,
                                            TAG.Cool,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Cooling_Temperature_Setpoint],
                                    },
                                    "Effective_Air_Temperature_Heating_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Effective,
                                            TAG.Air,
                                            TAG.Heat,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Heating_Temperature_Setpoint],
                                    },
                                },
                            },
                            "Mixed_Air_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Mixed,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Room_Air_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Room,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Zone_Air_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Zone,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Outside_Air_Temperature_Setpoint": {
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
                                        SKOS.definition: Literal(
                                            "Disables hot water system when outside air temperature reaches the indicated value"
                                        ),
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
                                        SKOS.definition: Literal(
                                            "Enables hot water system when outside air temperature reaches the indicated value"
                                        ),
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
                                "subclasses": {
                                    "Unoccupied_Air_Temperature_Cooling_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Unoccupied,
                                            TAG.Cool,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Cooling_Temperature_Setpoint],
                                    },
                                    "Unoccupied_Air_Temperature_Heating_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Unoccupied,
                                            TAG.Heat,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [BRICK.Heating_Temperature_Setpoint],
                                    },
                                },
                            },
                        },
                    },
                    "Cooling_Temperature_Setpoint": {
                        "tags": [TAG.Point, TAG.Temperature, TAG.Setpoint, TAG.Cool],
                    },
                    "Heating_Temperature_Setpoint": {
                        "tags": [TAG.Point, TAG.Temperature, TAG.Setpoint, TAG.Heat],
                    },
                    "Schedule_Temperature_Setpoint": {
                        "tags": [
                            TAG.Point,
                            TAG.Temperature,
                            TAG.Setpoint,
                            TAG.Schedule,
                        ],
                        SKOS.definition: Literal(
                            "The current setpoint as indicated by the schedule"
                        ),
                    },
                    "Water_Temperature_Setpoint": {
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
                                "subclasses": {
                                    "Domestic_Hot_Water_Supply_Temperature_Setpoint": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Domestic,
                                            TAG.Hot,
                                            TAG.Supply,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Setpoint,
                                        ],
                                        "parents": [
                                            BRICK.Supply_Water_Temperature_Setpoint
                                        ],
                                    }
                                },
                            },
                            "Discharge_Water_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Discharge,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Supply_Water_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Supply,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Entering_Water_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Entering,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Setpoint,
                                ],
                            },
                            "Leaving_Water_Temperature_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Leaving,
                                    TAG.Setpoint,
                                    TAG.Temperature,
                                    TAG.Water,
                                ],
                            },
                        },
                        "tags": [TAG.Point, TAG.Water, TAG.Temperature, TAG.Setpoint],
                    },
                },
            },
            "CO2_Setpoint": {
                "subclasses": {
                    "Return_Air_CO2_Setpoint": {
                        "subclasses": {
                            "Max_Return_Air_CO2_Setpoint": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Max,
                                    TAG.Return,
                                    TAG.Air,
                                    TAG.CO2,
                                    TAG.Setpoint,
                                ],
                            }
                        },
                        "tags": [TAG.Point, TAG.Return, TAG.Air, TAG.CO2, TAG.Setpoint],
                    }
                },
                "tags": [TAG.Point, TAG.CO2, TAG.Setpoint],
            },
            "Time_Setpoint": {
                "tags": [TAG.Point, TAG.Time, TAG.Setpoint],
                "subclasses": {
                    "Deceleration_Time_Setpoint": {
                        "tags": [TAG.Point, TAG.Time, TAG.Setpoint, TAG.Deceleration],
                    },
                    "Acceleration_Time_Setpoint": {
                        "tags": [TAG.Point, TAG.Time, TAG.Setpoint, TAG.Acceleration],
                    },
                },
            },
        },
    }
}
