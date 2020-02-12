from .namespaces import TAG, BRICK

status_definitions = {
    "Status": {
        "tags": [TAG.Point, TAG.Status],
        "subclasses": {
            "Direction_Status": {
                "subclasses": {
                    "Motor_Direction_Status": {
                        "tags": [TAG.Point, TAG.Motor, TAG.Direction, TAG.Status],
                    },
                },
                "tags": [TAG.Point, TAG.Direction, TAG.Status],
            },
            "Disable_Status": {"tags": [TAG.Point, TAG.Disable, TAG.Status]},
            "Drive_Ready_Status": {
                "tags": [TAG.Point, TAG.Drive, TAG.Ready, TAG.Status],
            },
            "Emergency_Air_Flow_Status": {
                "tags": [TAG.Point, TAG.Emergency, TAG.Air, TAG.Flow, TAG.Status],
            },
            "Emergency_Generator_Status": {
                "tags": [TAG.Point, TAG.Emergency, TAG.Generator, TAG.Status],
            },
            "Emergency_Power_Off_Status": {
                "tags": [TAG.Point, TAG.Emergency, TAG.Power, TAG.Off, TAG.Status],
                "parents": [BRICK.Off_Status],
                "subclasses": {
                    "Emergency_Power_Off_Activated_By_High_Temperature_Status": {
                        "tags": [
                            TAG.Point,
                            TAG.Emergency,
                            TAG.Power,
                            TAG.Off,
                            TAG.High,
                            TAG.Temperature,
                            TAG.Status,
                        ],
                    },
                    "Emergency_Power_Off_Activated_By_Leak_Detection_System_Status": {
                        "tags": [
                            TAG.Point,
                            TAG.Emergency,
                            TAG.Power,
                            TAG.Off,
                            TAG.Leak,
                            TAG.Detection,
                            TAG.Status,
                        ],
                    },
                    "Emergency_Power_Off_Enable_Status": {
                        "tags": [
                            TAG.Point,
                            TAG.Emergency,
                            TAG.Power,
                            TAG.Off,
                            TAG.Enable,
                            TAG.Status,
                        ],
                    },
                    "Emergency_Power_Off_System_Enable_Status": {
                        "tags": [
                            TAG.Point,
                            TAG.Emergency,
                            TAG.Power,
                            TAG.Off,
                            TAG.Enable,
                            TAG.Status,
                        ],
                    },
                },
            },
            "Emergency_Push_Button_Status": {
                "tags": [TAG.Point, TAG.Emergency, TAG.Push, TAG.Button, TAG.Status],
            },
            "Enable_Status": {
                "subclasses": {
                    "Heat_Exchanger_System_Enable_Status": {
                        "tags": [
                            TAG.Point,
                            TAG.Heat,
                            TAG.Exchanger,
                            TAG.System,
                            TAG.Enable,
                            TAG.Status,
                        ],
                        "parents": [BRICK.System_Status],
                    },
                    "Run_Enable_Status": {
                        "tags": [TAG.Point, TAG.Run, TAG.Enable, TAG.Status],
                        "parents": [BRICK.Run_Status],
                    },
                },
                "tags": [TAG.Point, TAG.Enable, TAG.Status],
            },
            "Even_Month_Status": {
                "tags": [TAG.Point, TAG.Even, TAG.Month, TAG.Status],
            },
            "Fan_Status": {"tags": [TAG.Point, TAG.Fan, TAG.Status]},
            "Fault_Status": {
                "subclasses": {
                    "Fault_Indicator_Status": {
                        "tags": [TAG.Point, TAG.Indicator, TAG.Fault, TAG.Status],
                    },
                    "Humidifier_Fault_Status": {
                        "tags": [TAG.Point, TAG.Humidifier, TAG.Fault, TAG.Status],
                    },
                    "Last_Fault_Code_Status": {
                        "tags": [TAG.Point, TAG.Last, TAG.Fault, TAG.Code, TAG.Status],
                    },
                },
                "tags": [TAG.Point, TAG.Fault, TAG.Status],
            },
            "Filter_Status": {
                "subclasses": {
                    "Pre_Filter_Status": {
                        "tags": [TAG.Point, TAG.Pre, TAG.Filter, TAG.Status],
                    }
                },
                "tags": [TAG.Point, TAG.Filter, TAG.Status],
            },
            "Freeze_Status": {"tags": [TAG.Point, TAG.Freeze, TAG.Status]},
            "Hand_Auto_Status": {"tags": [TAG.Point, TAG.Hand, TAG.Auto, TAG.Status]},
            "Hold_Status": {"tags": [TAG.Point, TAG.Hold, TAG.Status]},
            "Load_Shed_Status": {
                "subclasses": {
                    "Hot_Water_Discharge_Temperature_Load_Shed_Status": {
                        "tags": [
                            TAG.Point,
                            TAG.Hot,
                            TAG.Water,
                            TAG.Discharge,
                            TAG.Temperature,
                            TAG.Load,
                            TAG.Shed,
                            TAG.Status,
                        ],
                    },
                    "Hot_Water_Supply_Temperature_Load_Shed_Status": {
                        "tags": [
                            TAG.Point,
                            TAG.Hot,
                            TAG.Water,
                            TAG.Supply,
                            TAG.Temperature,
                            TAG.Load,
                            TAG.Shed,
                            TAG.Status,
                        ],
                        "subclasses": {
                            "Medium_Temperature_Hot_Water_Supply_Temperature_Load_Shed_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Medium,
                                    TAG.Temperature,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Supply,
                                    TAG.Temperature,
                                    TAG.Load,
                                    TAG.Shed,
                                    TAG.Status,
                                ],
                            },
                        },
                    },
                    "Differential_Pressure_Load_Shed_Status": {
                        "subclasses": {
                            "Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Medium,
                                    TAG.Temperature,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Load,
                                    TAG.Shed,
                                    TAG.Status,
                                ],
                                "subclasses": {
                                    "Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed_Reset_Status": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Medium,
                                            TAG.Temperature,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Load,
                                            TAG.Shed,
                                            TAG.Reset,
                                            TAG.Status,
                                        ],
                                    },
                                },
                            },
                            "Chilled_Water_Differential_Pressure_Load_Shed_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Load,
                                    TAG.Shed,
                                    TAG.Status,
                                ],
                                "subclasses": {
                                    "Chilled_Water_Differential_Pressure_Load_Shed_Reset_Status": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Load,
                                            TAG.Shed,
                                            TAG.Reset,
                                            TAG.Status,
                                        ],
                                    },
                                },
                            },
                            "Hot_Water_Differential_Pressure_Load_Shed_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Load,
                                    TAG.Shed,
                                    TAG.Status,
                                ],
                                "subclasses": {
                                    "Hot_Water_Differential_Pressure_Load_Shed_Reset_Status": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Load,
                                            TAG.Shed,
                                            TAG.Reset,
                                            TAG.Status,
                                        ],
                                    },
                                },
                            },
                        },
                        "tags": [
                            TAG.Point,
                            TAG.Differential,
                            TAG.Pressure,
                            TAG.Load,
                            TAG.Shed,
                            TAG.Status,
                        ],
                        "parents": [BRICK.Pressure_Status],
                    },
                },
                "tags": [TAG.Point, TAG.Load, TAG.Shed, TAG.Status],
            },
            "Manual_Auto_Status": {
                "tags": [TAG.Point, TAG.Manual, TAG.Auto, TAG.Status],
            },
            "Mode_Status": {
                "subclasses": {
                    "Occupied_Mode_Status": {
                        "tags": [TAG.Point, TAG.Occupied, TAG.Mode, TAG.Status],
                    },
                    "System_Mode_Status": {
                        "tags": [TAG.Point, TAG.System, TAG.Mode, TAG.Status],
                        "parents": [BRICK.System_Status],
                    },
                    "Operating_Mode_Status": {
                        "subclasses": {
                            "Vent_Operating_Mode_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Vent,
                                    TAG.Operating,
                                    TAG.Mode,
                                    TAG.Status,
                                ],
                            }
                        },
                        "tags": [TAG.Point, TAG.Operating, TAG.Mode, TAG.Status],
                    },
                },
                "tags": [TAG.Point, TAG.Mode, TAG.Status],
            },
            "Occupancy_Status": {
                "subclasses": {
                    "Temporary_Occupancy_Status": {
                        "tags": [TAG.Point, TAG.Temporary, TAG.Occupancy, TAG.Status],
                    }
                },
                "tags": [TAG.Point, TAG.Occupancy, TAG.Status],
            },
            "On_Off_Status": {
                "subclasses": {
                    "Cooling_On_Off_Status": {
                        "tags": [TAG.Point, TAG.Cool, TAG.On, TAG.Off, TAG.Status],
                    },
                    "Dehumidification_On_Off_Status": {
                        "tags": [
                            TAG.Point,
                            TAG.Dehumidification,
                            TAG.On,
                            TAG.Off,
                            TAG.Status,
                        ],
                    },
                    "EconCycle_On_Off_Status": {
                        "tags": [TAG.Point, TAG.Econcycle, TAG.On, TAG.Off, TAG.Status],
                    },
                    "Heating_On_Off_Status": {
                        "tags": [TAG.Point, TAG.Heat, TAG.On, TAG.Off, TAG.Status],
                    },
                    "Humidification_On_Off_Status": {
                        "tags": [
                            TAG.Point,
                            TAG.Humidification,
                            TAG.On,
                            TAG.Off,
                            TAG.Status,
                        ],
                    },
                    "Locally_On_Off_Status": {
                        "tags": [TAG.Point, TAG.Locally, TAG.On, TAG.Off, TAG.Status],
                    },
                    "Remotely_On_Off_Status": {
                        "tags": [TAG.Point, TAG.Remotely, TAG.On, TAG.Off, TAG.Status],
                    },
                    "Standby_Unit_On_Off_Status": {
                        "tags": [
                            TAG.Point,
                            TAG.Standby,
                            TAG.Unit,
                            TAG.On,
                            TAG.Off,
                            TAG.Status,
                        ],
                        "subclasses": {
                            "Standby_Glycool_Unit_On_Off_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Standby,
                                    TAG.Glycool,
                                    TAG.Unit,
                                    TAG.On,
                                    TAG.Off,
                                    TAG.Status,
                                ],
                            },
                        },
                    },
                },
                "tags": [TAG.Point, TAG.On, TAG.Off, TAG.Status],
                "parents": [BRICK.On_Status, BRICK.Off_Status],
            },
            "Off_Status": {
                "tags": [TAG.Point, TAG.Off, TAG.Status],
                "subclasses": {
                    "Turn_Off_Status": {
                        "tags": [TAG.Point, TAG.Turn, TAG.Off, TAG.Status],
                    },
                },
            },
            "On_Status": {
                "tags": [TAG.Point, TAG.On, TAG.Status],
                "subclasses": {
                    "Turn_On_Status": {
                        "tags": [TAG.Point, TAG.Turn, TAG.On, TAG.Status],
                    },
                },
            },
            "Overridden_Status": {
                "subclasses": {
                    "Overridden_Off_Status": {
                        "tags": [TAG.Point, TAG.Overridden, TAG.Off, TAG.Status],
                        "parents": [BRICK.Off_Status],
                    },
                    "Overridden_On_Status": {
                        "tags": [TAG.Point, TAG.Overridden, TAG.On, TAG.Status],
                        "parents": [BRICK.On_Status],
                    },
                },
                "tags": [TAG.Point, TAG.Overridden, TAG.Status],
            },
            "Pressure_Status": {
                "subclasses": {
                    "Discharge_Air_Duct_Pressure_Status": {
                        "tags": [
                            TAG.Point,
                            TAG.Discharge,
                            TAG.Air,
                            TAG.Duct,
                            TAG.Pressure,
                            TAG.Status,
                        ],
                    },
                    "Supply_Air_Duct_Pressure_Status": {
                        "tags": [
                            TAG.Point,
                            TAG.Supply,
                            TAG.Air,
                            TAG.Duct,
                            TAG.Pressure,
                            TAG.Status,
                        ],
                    },
                },
                "tags": [TAG.Point, TAG.Pressure, TAG.Status],
            },
            "Lead_Lag_Status": {"tags": [TAG.Point, TAG.Lead, TAG.Lag, TAG.Status]},
            "Stages_Status": {"tags": [TAG.Point, TAG.Stages, TAG.Status]},
            "Start_Stop_Status": {
                "subclasses": {
                    "Fan_Start_Stop_Status": {
                        "tags": [TAG.Point, TAG.Fan, TAG.Start, TAG.Stop, TAG.Status],
                        "parents": [BRICK.Fan_Status],
                    },
                    "Motor_Start_Stop_Status": {
                        "tags": [TAG.Point, TAG.Motor, TAG.Start, TAG.Stop, TAG.Status],
                    },
                    "Pump_Start_Stop_Status": {
                        "tags": [TAG.Point, TAG.Pump, TAG.Start, TAG.Stop, TAG.Status],
                    },
                    "Run_Status": {
                        "tags": [TAG.Point, TAG.Run, TAG.Status],
                        "subclasses": {
                            "Run_Request_Status": {
                                "tags": [TAG.Point, TAG.Request, TAG.Run, TAG.Status],
                            },
                        },
                    },
                },
                "tags": [TAG.Point, TAG.Start, TAG.Stop, TAG.Status],
            },
            "System_Shutdown_Status": {
                "tags": [TAG.Point, TAG.System, TAG.Shutdown, TAG.Status],
                "parents": [BRICK.System_Status],
            },
            "System_Status": {"tags": [TAG.Point, TAG.System, TAG.Status]},
            "Speed_Status": {"tags": [TAG.Point, TAG.Speed, TAG.Status]},
        },
    }
}
