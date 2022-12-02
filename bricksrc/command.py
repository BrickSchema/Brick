from rdflib import Literal
from .namespaces import TAG, BRICK, QUDT

command_definitions = {
    "Command": {
        "tags": [TAG.Point, TAG.Command],
        "subclasses": {
            "Boiler_Command": {"tags": [TAG.Boiler, TAG.Command, TAG.Point]},
            "Tint_Command": {"tags": [TAG.Tint, TAG.Command, TAG.Point]},
            "Fan_Command": {
                "tags": [TAG.Fan, TAG.Command, TAG.Point],
                "subclasses": {
                    "Fan_Speed_Command": {
                        "tags": [TAG.Fan, TAG.Command, TAG.Point, TAG.Speed],
                    }
                },
            },
            "Relay_Command": {"tags": [TAG.Point, TAG.Relay, TAG.Command]},
            "Light_Command": {"tags": [TAG.Point, TAG.Light, TAG.Command]},
            "Speed_Command": {"tags": [TAG.Point, TAG.Speed, TAG.Command]},
            "Cooling_Command": {"tags": [TAG.Point, TAG.Cool, TAG.Command]},
            "Heating_Command": {"tags": [TAG.Point, TAG.Heat, TAG.Command]},
            "Preheat_Command": {"tags": [TAG.Point, TAG.Preheat, TAG.Command]},
            "Luminance_Command": {"tags": [TAG.Point, TAG.Luminance, TAG.Command]},
            "Bypass_Command": {"tags": [TAG.Point, TAG.Bypass, TAG.Command]},
            "Damper_Command": {
                "tags": [TAG.Point, TAG.Damper, TAG.Command],
                "subclasses": {
                    "Damper_Position_Command": {
                        BRICK.hasQuantity: BRICK.Position,
                        "tags": [TAG.Point, TAG.Damper, TAG.Position, TAG.Command],
                        "parents": [BRICK.Position_Command],
                    },
                },
            },
            "Humidify_Command": {
                "tags": [TAG.Point, TAG.Humidify, TAG.Command],
                BRICK.hasQuantity: BRICK.Humidity,
            },
            "Position_Command": {
                "tags": [TAG.Point, TAG.Position, TAG.Command],
                BRICK.hasQuantity: BRICK.Position,
            },
            "Direction_Command": {
                "tags": [TAG.Point, TAG.Direction, TAG.Command],
                BRICK.hasQuantity: BRICK.Direction,
            },
            "Pump_Command": {
                # TODO: position?
                "tags": [TAG.Point, TAG.Pump, TAG.Command],
            },
            "Valve_Command": {
                # TODO: position?
                "tags": [TAG.Point, TAG.Valve, TAG.Command],
                "subclasses": {
                    "Valve_Position_Command": {
                        BRICK.hasQuantity: BRICK.Position,
                        "tags": [TAG.Point, TAG.Valve, TAG.Position, TAG.Command],
                        "parents": [BRICK.Position_Command],
                    },
                },
            },
            "Reset_Command": {
                "tags": [TAG.Point, TAG.Reset, TAG.Command],
                "subclasses": {
                    "Fault_Reset_Command": {
                        "tags": [TAG.Point, TAG.Fault, TAG.Reset, TAG.Command],
                    },
                    "Filter_Reset_Command": {
                        "tags": [TAG.Point, TAG.Filter, TAG.Reset, TAG.Command],
                    },
                    "Speed_Reset_Command": {
                        BRICK.hasQuantity: BRICK.Speed,
                        "tags": [TAG.Point, TAG.Speed, TAG.Reset, TAG.Command],
                    },
                },
            },
            "Enable_Command": {
                "tags": [TAG.Point, TAG.Enable, TAG.Command],
                "subclasses": {
                    "VFD_Enable_Command": {
                        "tags": [TAG.Point, TAG.Enable, TAG.Command, TAG.VFD],
                    },
                    "System_Enable_Command": {
                        "tags": [TAG.Point, TAG.Enable, TAG.Command, TAG.System],
                        "subclasses": {
                            "Chilled_Water_System_Enable_Command": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Enable,
                                    TAG.Command,
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.System,
                                ],
                            },
                            "Hot_Water_System_Enable_Command": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Enable,
                                    TAG.Command,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.System,
                                ],
                                "subclasses": {
                                    "Domestic_Hot_Water_System_Enable_Command": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Enable,
                                            TAG.Command,
                                            TAG.Domestic,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.System,
                                        ],
                                    },
                                },
                            },
                        },
                    },
                    "Run_Enable_Command": {
                        "tags": [TAG.Point, TAG.Enable, TAG.Command, TAG.Run],
                    },
                    "Enable_Differential_Enthalpy_Command": {
                        "tags": [
                            TAG.Point,
                            TAG.Enable,
                            TAG.Command,
                            TAG.Differential,
                            TAG.Enthalpy,
                        ],
                    },
                    "Enable_Differential_Temperature_Command": {
                        "tags": [
                            TAG.Point,
                            TAG.Enable,
                            TAG.Command,
                            TAG.Differential,
                            TAG.Temperature,
                        ],
                    },
                    "Enable_Fixed_Enthalpy_Command": {
                        "tags": [
                            TAG.Point,
                            TAG.Enable,
                            TAG.Command,
                            TAG.Fixed,
                            TAG.Enthalpy,
                        ],
                    },
                    "Enable_Fixed_Temperature_Command": {
                        "tags": [
                            TAG.Point,
                            TAG.Enable,
                            TAG.Command,
                            TAG.Fixed,
                            TAG.Temperature,
                        ],
                    },
                    "Stage_Enable_Command": {
                        "tags": [TAG.Stage, TAG.Enable, TAG.Command, TAG.Point]
                    },
                    "Heating_Enable_Command": {
                        "tags": [TAG.Heating, TAG.Enable, TAG.Command, TAG.Point]
                    },
                    "Cooling_Enable_Command": {
                        "tags": [TAG.Cooling, TAG.Enable, TAG.Command, TAG.Point]
                    },
                },
            },
            "Disable_Command": {
                "tags": [TAG.Point, TAG.Disable, TAG.Command],
                "subclasses": {
                    "Disable_Differential_Enthalpy_Command": {
                        "tags": [
                            TAG.Point,
                            TAG.Disable,
                            TAG.Command,
                            TAG.Differential,
                            TAG.Enthalpy,
                        ],
                    },
                    "Disable_Differential_Temperature_Command": {
                        "tags": [
                            TAG.Point,
                            TAG.Disable,
                            TAG.Command,
                            TAG.Differential,
                            TAG.Temperature,
                        ],
                    },
                    "Disable_Fixed_Enthalpy_Command": {
                        "tags": [
                            TAG.Point,
                            TAG.Disable,
                            TAG.Command,
                            TAG.Fixed,
                            TAG.Enthalpy,
                        ],
                    },
                    "Disable_Fixed_Temperature_Command": {
                        "tags": [
                            TAG.Point,
                            TAG.Disable,
                            TAG.Command,
                            TAG.Fixed,
                            TAG.Temperature,
                        ],
                    },
                },
            },
            "Lead_Lag_Command": {"tags": [TAG.Point, TAG.Lead, TAG.Lag, TAG.Command]},
            "Load_Shed_Command": {
                "tags": [TAG.Point, TAG.Load, TAG.Shed, TAG.Command],
                "subclasses": {
                    "Standby_Load_Shed_Command": {
                        "tags": [
                            TAG.Point,
                            TAG.Standby,
                            TAG.Load,
                            TAG.Shed,
                            TAG.Command,
                        ],
                        "subclasses": {
                            "Zone_Standby_Load_Shed_Command": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Zone,
                                    TAG.Standby,
                                    TAG.Load,
                                    TAG.Shed,
                                    TAG.Command,
                                ],
                            },
                        },
                    },
                    "Unoccupied_Load_Shed_Command": {
                        "tags": [
                            TAG.Point,
                            TAG.Unoccupied,
                            TAG.Load,
                            TAG.Shed,
                            TAG.Command,
                        ],
                        "subclasses": {
                            "Zone_Unoccupied_Load_Shed_Command": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Zone,
                                    TAG.Unoccupied,
                                    TAG.Load,
                                    TAG.Shed,
                                    TAG.Command,
                                ],
                            },
                        },
                    },
                    "Occupied_Load_Shed_Command": {
                        "tags": [
                            TAG.Point,
                            TAG.Occupied,
                            TAG.Load,
                            TAG.Shed,
                            TAG.Command,
                        ],
                        "subclasses": {
                            "Zone_Occupied_Load_Shed_Command": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Zone,
                                    TAG.Occupied,
                                    TAG.Load,
                                    TAG.Shed,
                                    TAG.Command,
                                ],
                            },
                        },
                    },
                },
            },
            "Mode_Command": {
                "tags": [TAG.Point, TAG.Mode, TAG.Command],
                "subclasses": {
                    "Automatic_Mode_Command": {
                        "tags": [TAG.Point, TAG.Automatic, TAG.Mode, TAG.Command],
                    },
                    "Maintenance_Mode_Command": {
                        "tags": [TAG.Point, TAG.Maintenance, TAG.Mode, TAG.Command],
                    },
                    "Box_Mode_Command": {
                        "tags": [TAG.Point, TAG.Box, TAG.Mode, TAG.Command],
                    },
                },
            },
            "Frequency_Command": {
                "tags": [TAG.Point, TAG.Frequency, TAG.Command],
                BRICK.hasQuantity: BRICK.Frequency,
                "subclasses": {
                    "Max_Frequency_Command": {
                        "tags": [TAG.Point, TAG.Max, TAG.Frequency, TAG.Command],
                    },
                    "Min_Frequency_Command": {
                        "tags": [TAG.Point, TAG.Min, TAG.Frequency, TAG.Command],
                    },
                },
            },
            "Occupancy_Command": {"tags": [TAG.Point, TAG.Occupancy, TAG.Command]},
            "On_Off_Command": {
                "tags": [TAG.Point, TAG.On, TAG.Off, TAG.Command],
                "subclasses": {
                    "Off_Command": {"tags": [TAG.Point, TAG.Off, TAG.Command]},
                    "On_Command": {"tags": [TAG.Point, TAG.On, TAG.Command]},
                    "Lead_On_Off_Command": {
                        "tags": [TAG.Point, TAG.Lead, TAG.On, TAG.Off, TAG.Command],
                    },
                    "Steam_On_Off_Command": {
                        "tags": [TAG.Point, TAG.Steam, TAG.On, TAG.Off, TAG.Command],
                    },
                    "Start_Stop_Command": {
                        "tags": [TAG.Point, TAG.Start, TAG.Stop, TAG.Command],
                    },
                },
            },
            "Override_Command": {
                "tags": [TAG.Point, TAG.Override, TAG.Command],
                "subclasses": {
                    "Curtailment_Override_Command": {
                        "tags": [TAG.Point, TAG.Curtailment, TAG.Override, TAG.Command],
                    },
                },
            },
        },
    }
}
