from rdflib import Literal
from .namespaces import TAG, BRICK, QUDTQK

command_definitions = {
    "Command": {
        "tags": [TAG.Point, TAG.Command],
        "subclasses": {
            # intermediate classes introduced by the Brick 2.0 point attribute work
            "Max_Command": {
                "tags": [TAG.Point, TAG.Max, TAG.Command],
            },
            "Min_Command": {
                "tags": [TAG.Point, TAG.Min, TAG.Command],
            },
            "Boiler_Command": {
                BRICK.ofEquipment: BRICK.Boiler,
                "tags": [TAG.Boiler, TAG.Command, TAG.Point],
            },
            "Tint_Command": {
                "tags": [TAG.Tint, TAG.Command, TAG.Point],
                BRICK.hasQuantity: QUDTQK.Transmittance,
            },
            "Fan_Command": {
                BRICK.ofEquipment: BRICK.Fan,
                "tags": [TAG.Fan, TAG.Command, TAG.Point],
                "subclasses": {
                    "Fan_Speed_Command": {
                        BRICK.hasQuantity: QUDTQK.Speed,
                        BRICK.ofEquipment: BRICK.Fan,
                        "tags": [TAG.Fan, TAG.Command, TAG.Point, TAG.Speed],
                    }
                },
            },
            "Relay_Command": {
                BRICK.ofEquipment: BRICK.Relay,
                "tags": [TAG.Point, TAG.Relay, TAG.Command],
            },
            "Level_Command": {
                "tags": [TAG.Level, TAG.Command, TAG.Point],
            },
            "Lighting_Level_Command": {
                BRICK.ofEquipment: BRICK.Lighting,
                "tags": [TAG.Point, TAG.Lighting, TAG.Level, TAG.Command],
            },
            "Lighting_Correlated_Color_Temperature_Command": {
                BRICK.hasQuantity: QUDTQK.CorrelatedColorTemperature,
                BRICK.ofEquipment: BRICK.Lighting,
                "tags": [
                    TAG.Point,
                    TAG.Lighting,
                    TAG.Correlated,
                    TAG.Color,
                    TAG.Temperature,
                    TAG.Command,
                ],
            },
            "Speed_Command": {
                BRICK.hasQuantity: QUDTQK.Speed,
                "tags": [TAG.Point, TAG.Speed, TAG.Command],
            },
            "Cooling_Command": {
                BRICK.ofProcess: BRICK.Cooling,
                "tags": [TAG.Point, TAG.Cool, TAG.Command],
            },
            "Heating_Command": {
                BRICK.ofProcess: BRICK.Heating,
                "tags": [TAG.Point, TAG.Heat, TAG.Command],
            },
            "Preheat_Command": {
                BRICK.ofProcess: BRICK.Preheat,
                "tags": [TAG.Point, TAG.Preheat, TAG.Command],
            },
            "Reheat_Command": {
                BRICK.ofProcess: BRICK.Reheat,
                "tags": [TAG.Point, TAG.Reheat, TAG.Command],
            },
            "Luminance_Command": {
                BRICK.hasQuantity: QUDTQK.Luminance,
                "tags": [TAG.Point, TAG.Luminance, TAG.Command],
            },
            "Bypass_Command": {"tags": [TAG.Point, TAG.Bypass, TAG.Command]},
            "Damper_Command": {
                BRICK.ofEquipment: BRICK.Damper,
                "tags": [TAG.Point, TAG.Damper, TAG.Command],
                "subclasses": {
                    "Damper_Position_Command": {
                        BRICK.ofEquipment: BRICK.Damper,
                        BRICK.hasQuantity: BRICK.Position,
                        "tags": [TAG.Point, TAG.Damper, TAG.Position, TAG.Command],
                        "parents": [BRICK.Position_Command],
                    },
                },
            },
            "Dehumidify_Command": {
                BRICK.ofProcess: BRICK.Dehumidification,
                # TODO(Brick 2.0): "parents": [BRICK.Enable_Command],  # spreadsheet moves this under Enable_Command, which changes its meaning
                "tags": [TAG.Point, TAG.Dehumidify, TAG.Command],
                BRICK.hasSubstance: BRICK.Air,
            },
            "Humidify_Command": {
                BRICK.ofProcess: BRICK.Humidification,
                # TODO(Brick 2.0): "parents": [BRICK.Enable_Command],  # spreadsheet moves this under Enable_Command, which changes its meaning
                "tags": [TAG.Point, TAG.Humidify, TAG.Command],
                BRICK.hasSubstance: BRICK.Air,
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
                BRICK.ofEquipment: BRICK.Pump,
                # TODO: position?
                "tags": [TAG.Point, TAG.Pump, TAG.Command],
            },
            "Valve_Command": {
                BRICK.ofEquipment: BRICK.Valve,
                # TODO: position?
                "tags": [TAG.Point, TAG.Valve, TAG.Command],
                "subclasses": {
                    "Valve_Position_Command": {
                        BRICK.ofEquipment: BRICK.Valve,
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
                        BRICK.ofEquipment: BRICK.Filter,
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
                        BRICK.ofEquipment: BRICK.VFD,
                        "tags": [TAG.Point, TAG.Enable, TAG.Command, TAG.VFD],
                    },
                    "System_Enable_Command": {
                        BRICK.ofSystem: BRICK.System,
                        "tags": [TAG.Point, TAG.Enable, TAG.Command, TAG.System],
                        "subclasses": {
                            "Chilled_Water_System_Enable_Command": {
                                BRICK.ofSystem: BRICK.Chilled_Water_System,
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
                                BRICK.ofSystem: BRICK.Hot_Water_System,
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
                                        BRICK.ofSystem: BRICK.Domestic_Hot_Water_System,
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
                        BRICK.ofProcess: BRICK.Run,
                        "tags": [TAG.Point, TAG.Enable, TAG.Command, TAG.Run],
                    },
                    "Enable_Differential_Enthalpy_Command": {
                        BRICK.hasQuantity: QUDTQK.Enthalpy,
                        BRICK.isDifferential: Literal(True),
                        "tags": [
                            TAG.Point,
                            TAG.Enable,
                            TAG.Command,
                            TAG.Differential,
                            TAG.Enthalpy,
                        ],
                    },
                    "Enable_Differential_Temperature_Command": {
                        BRICK.hasQuantity: QUDTQK.Temperature,
                        BRICK.isDifferential: Literal(True),
                        "tags": [
                            TAG.Point,
                            TAG.Enable,
                            TAG.Command,
                            TAG.Differential,
                            TAG.Temperature,
                        ],
                    },
                    "Enable_Fixed_Enthalpy_Command": {
                        BRICK.hasQuantity: QUDTQK.Enthalpy,
                        "tags": [
                            TAG.Point,
                            TAG.Enable,
                            TAG.Command,
                            TAG.Fixed,
                            TAG.Enthalpy,
                        ],
                    },
                    "Enable_Fixed_Temperature_Command": {
                        BRICK.hasQuantity: QUDTQK.Temperature,
                        "tags": [
                            TAG.Point,
                            TAG.Enable,
                            TAG.Command,
                            TAG.Fixed,
                            TAG.Temperature,
                        ],
                    },
                    "Stage_Enable_Command": {
                        BRICK.hasEnumeration: BRICK["EnumerationKind-Stage"],
                        "tags": [TAG.Stage, TAG.Enable, TAG.Command, TAG.Point],
                    },
                    "Heating_Enable_Command": {
                        BRICK.ofProcess: BRICK.Heating,
                        "tags": [TAG.Heating, TAG.Enable, TAG.Command, TAG.Point],
                    },
                    "Cooling_Enable_Command": {
                        BRICK.ofProcess: BRICK.Cooling,
                        "tags": [TAG.Cooling, TAG.Enable, TAG.Command, TAG.Point],
                    },
                },
            },
            "Disable_Command": {
                "tags": [TAG.Point, TAG.Disable, TAG.Command],
                "subclasses": {
                    "Disable_Differential_Enthalpy_Command": {
                        BRICK.hasQuantity: QUDTQK.Enthalpy,
                        BRICK.isDifferential: Literal(True),
                        "tags": [
                            TAG.Point,
                            TAG.Disable,
                            TAG.Command,
                            TAG.Differential,
                            TAG.Enthalpy,
                        ],
                    },
                    "Disable_Differential_Temperature_Command": {
                        BRICK.hasQuantity: QUDTQK.Temperature,
                        BRICK.isDifferential: Literal(True),
                        "tags": [
                            TAG.Point,
                            TAG.Disable,
                            TAG.Command,
                            TAG.Differential,
                            TAG.Temperature,
                        ],
                    },
                    "Disable_Fixed_Enthalpy_Command": {
                        BRICK.hasQuantity: QUDTQK.Enthalpy,
                        "tags": [
                            TAG.Point,
                            TAG.Disable,
                            TAG.Command,
                            TAG.Fixed,
                            TAG.Enthalpy,
                        ],
                    },
                    "Disable_Fixed_Temperature_Command": {
                        BRICK.hasQuantity: QUDTQK.Temperature,
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
                BRICK.ofProcess: BRICK.Load_Shed,
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
                        BRICK.inMode: BRICK.Unoccupied,
                        BRICK.ofProcess: BRICK.Load_Shed,
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
                        BRICK.inMode: BRICK.Occupied,
                        BRICK.ofProcess: BRICK.Load_Shed,
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
                BRICK.hasEnumeration: BRICK["EnumerationKind-Mode"],
                "tags": [TAG.Point, TAG.Mode, TAG.Command],
                "subclasses": {
                    "Automatic_Mode_Command": {
                        BRICK.hasEnumeration: BRICK["EnumerationKind-Automatic_Mode"],
                        "tags": [TAG.Point, TAG.Automatic, TAG.Mode, TAG.Command],
                    },
                    "Maintenance_Mode_Command": {
                        BRICK.hasEnumeration: BRICK["EnumerationKind-Maintenance_Mode"],
                        "tags": [TAG.Point, TAG.Maintenance, TAG.Mode, TAG.Command],
                    },
                    "Box_Mode_Command": {
                        "tags": [TAG.Point, TAG.Box, TAG.Mode, TAG.Command],
                    },
                },
            },
            "Frequency_Command": {
                "tags": [TAG.Point, TAG.Frequency, TAG.Command],
                BRICK.hasQuantity: QUDTQK.Frequency,
                "subclasses": {
                    "Max_Frequency_Command": {
                        "parents": [BRICK.Max_Command],
                        "tags": [TAG.Point, TAG.Max, TAG.Frequency, TAG.Command],
                    },
                    "Min_Frequency_Command": {
                        "parents": [BRICK.Min_Command],
                        "tags": [TAG.Point, TAG.Min, TAG.Frequency, TAG.Command],
                    },
                },
            },
            "Occupancy_Command": {
                BRICK.hasEnumeration: BRICK["EnumerationKind-Occupancy"],
                "tags": [TAG.Point, TAG.Occupancy, TAG.Command],
            },
            "On_Off_Command": {
                BRICK.hasEnumeration: BRICK["EnumerationKind-On_Off"],
                "tags": [TAG.Point, TAG.On, TAG.Off, TAG.Command],
                "subclasses": {
                    "Off_Command": {
                        BRICK.hasEnumeration: BRICK["On_Off-Off"],
                        "tags": [TAG.Point, TAG.Off, TAG.Command],
                    },
                    "On_Command": {
                        BRICK.hasEnumeration: BRICK["On_Off-On"],
                        "tags": [TAG.Point, TAG.On, TAG.Command],
                    },
                    "Open_Close_Command": {
                        BRICK.hasEnumeration: BRICK["EnumerationKind-Open_Close"],
                        "tags": [TAG.Point, TAG.Open, TAG.Close, TAG.Command],
                    },
                    "Lead_On_Off_Command": {
                        BRICK.hasEnumeration: BRICK["EnumerationKind-On_Off"],
                        "tags": [TAG.Point, TAG.Lead, TAG.On, TAG.Off, TAG.Command],
                    },
                    "Steam_On_Off_Command": {
                        BRICK.hasEnumeration: BRICK["EnumerationKind-On_Off"],
                        BRICK.hasSubstance: BRICK.Steam,
                        "tags": [TAG.Point, TAG.Steam, TAG.On, TAG.Off, TAG.Command],
                    },
                    "Start_Stop_Command": {
                        BRICK.hasEnumeration: BRICK["EnumerationKind-Start_Stop"],
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
