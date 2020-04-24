from rdflib import Literal
from .namespaces import TAG, BRICK, SKOS

command_definitions = {
    "Command": {
        SKOS.definition: Literal(
            "A Command is an output point that directly determines the behavior of equipment and/or affects relevant operational points."
        ),
        "tags": [TAG.Point, TAG.Command],
        "subclasses": {
            "Cooling_Command": {
                "tags": [TAG.Point, TAG.Cool, TAG.Command],
                "subclasses": {
                    "Highest_Zone_Cooling_Command": {
                        "tags": [
                            TAG.Point,
                            TAG.Highest,
                            TAG.Zone,
                            TAG.Cool,
                            TAG.Command,
                        ],
                    },
                },
            },
            "Heating_Command": {"tags": [TAG.Point, TAG.Heat, TAG.Command]},
            "Luminance_Command": {"tags": [TAG.Point, TAG.Luminance, TAG.Command]},
            "Bypass_Command": {"tags": [TAG.Point, TAG.Bypass, TAG.Command]},
            "Damper_Command": {
                "tags": [TAG.Point, TAG.Damper, TAG.Command],
                "subclasses": {
                    "Damper_Position_Command": {
                        "tags": [TAG.Point, TAG.Damper, TAG.Position, TAG.Command],
                        "parents": [BRICK.Position_Command],
                    },
                },
            },
            "Humidify_Command": {"tags": [TAG.Point, TAG.Humidify, TAG.Command]},
            "Position_Command": {"tags": [TAG.Point, TAG.Position, TAG.Command]},
            "Direction_Command": {"tags": [TAG.Point, TAG.Direction, TAG.Command]},
            "Pump_Command": {
                # TODO: position?
                "tags": [TAG.Point, TAG.Pump, TAG.Command],
            },
            "Valve_Command": {
                # TODO: position?
                "tags": [TAG.Point, TAG.Valve, TAG.Command],
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
                        "tags": [TAG.Point, TAG.Speed, TAG.Reset, TAG.Command],
                        "subclasses": {
                            "Fan_Speed_Reset_Command": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Fan,
                                    TAG.Speed,
                                    TAG.Reset,
                                    TAG.Command,
                                ],
                            },
                        },
                    },
                },
            },
            "Shutdown_Command": {
                "tags": [TAG.Point, TAG.Shutdown, TAG.Command],
                "subclasses": {
                    "Hot_Water_Shutdown_Command": {
                        "tags": [
                            TAG.Point,
                            TAG.Hot,
                            TAG.Water,
                            TAG.Shutdown,
                            TAG.Command,
                        ],
                        "subclasses": {
                            "Unoccupied_Hot_Water_Shutdown_Command": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Unoccupied,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Shutdown,
                                    TAG.Command,
                                ],
                            },
                        },
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
                    "Exhaust_Fan_Enable_Command": {
                        "tags": [
                            TAG.Point,
                            TAG.Enable,
                            TAG.Command,
                            TAG.Fan,
                            TAG.Exhaust,
                        ],
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
                },
            },
            "Disable_Command": {
                "tags": [TAG.Point, TAG.Disable, TAG.Command],
                "subclasses": {
                    "Exhaust_Fan_Disable_Command": {
                        "tags": [
                            TAG.Point,
                            TAG.Disable,
                            TAG.Command,
                            TAG.Fan,
                            TAG.Exhaust,
                        ],
                    },
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
                "tags": [TAG.Point, TAG.Fequency, TAG.Command],
                "subclasses": {
                    "Max_Frequency_Command": {
                        "tags": [TAG.Point, TAG.Max, TAG.Fequency, TAG.Command],
                    },
                },
            },
            "Occupancy_Command": {"tags": [TAG.Point, TAG.Occupancy, TAG.Command]},
            "On_Off_Command": {
                SKOS.definition: Literal(
                    "An On/Off Command controls or reports the binary status of a control loop, relay or equipment activity"
                ),
                "tags": [TAG.Point, TAG.On, TAG.Off, TAG.Command],
                "subclasses": {
                    "Off_Command": {
                        SKOS.definition: Literal(
                            "An Off Command controls or reports the binary 'off' status of a control loop, relay or equipment activity. It can only be used to stop/terminate/deactivate an associated equipment or process, or determine that the related entity is 'off'"
                        ),
                        "tags": [TAG.Point, TAG.Off, TAG.Command],
                        "subclasses": {
                            "Exhaust_Fan_Fire_Control_Panel_Off_Command": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Exhaust,
                                    TAG.Fan,
                                    TAG.Fire,
                                    TAG.Control,
                                    TAG.Panel,
                                    TAG.Off,
                                    TAG.Command,
                                ],
                            }
                        },
                    },
                    "On_Command": {
                        SKOS.definition: Literal(
                            "An On Command controls or reports the binary 'on' status of a control loop, relay or equipment activity. It can only be used to start/activate an associated equipment or process, or determine that the related entity is 'on'"
                        ),
                        "tags": [TAG.Point, TAG.On, TAG.Command],
                        "subclasses": {
                            "Exhaust_Fan_Fire_Control_Panel_On_Command": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Exhaust,
                                    TAG.Fan,
                                    TAG.Fire,
                                    TAG.Control,
                                    TAG.Panel,
                                    TAG.On,
                                    TAG.Command,
                                ],
                            }
                        },
                    },
                    "Lead_On_Off_Command": {
                        "tags": [TAG.Point, TAG.Lead, TAG.On, TAG.Off, TAG.Command],
                    },
                    "Steam_On_Off_Command": {
                        "tags": [TAG.Point, TAG.Steam, TAG.On, TAG.Off, TAG.Command],
                    },
                    "Start_Stop_Command": {
                        "tags": [TAG.Point, TAG.Start, TAG.Stop, TAG.Command],
                        SKOS.definition: Literal(
                            "A Start/Stop Command controls or reports the active/inactive status of a control sequence"
                        ),
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
            "Lockout_Command": {"tags": [TAG.Point, TAG.Lockout, TAG.Command]},
            "Run_Request_Command": {
                "tags": [TAG.Point, TAG.Run, TAG.Request, TAG.Command],
            },
        },
    }
}
