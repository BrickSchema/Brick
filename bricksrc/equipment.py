from .namespaces import TAG, OWL, BRICK

"""
Set up subclasses of the equipment superclass
"""
equipment_subclasses = {
    "HVAC_Equipment": {"tags": [TAG.HVAC, TAG.Equipment]},
    "Weather_Station": {"tags": [TAG.Weather, TAG.Station, TAG.Equipment]},
    "Electrical_Equipment": {
        "tags": [TAG.Electrical, TAG.Equipment],
        "subclasses": {
            "Energy_Storage": {
                "tags": [TAG.Energy, TAG.Storage, TAG.Equipment],
                "subclasses": {
                    "Battery": {
                        "tags": [TAG.Battery, TAG.Energy, TAG.Storage, TAG.Equipment],
                    },
                },
            },
            "Inverter": {"tags": [TAG.Inverter, TAG.Equipment]},
            "PlugStrip": {"tags": [TAG.PlugStrip, TAG.Equipment]},
            "Disconnect_Switch": {"tags": [TAG.Disconnect, TAG.Switch, TAG.Equipment]},
            "Switchgear": {"tags": [TAG.Switchgear, TAG.Equipment]},
            "Bus_Riser": {"tags": [TAG.Riser, TAG.Equipment]},
            "Transformer": {"tags": [TAG.Transformer, TAG.Equipment]},
            "Motor_Control_Center": {
                # TODO: add TAG.Motor back
                "tags": [TAG.Equipment, TAG.Control, TAG.Center]
            },
            "Breaker_Panel": {"tags": [TAG.Breaker, TAG.Equipment]},
        },
    },
    "Gas_Distribution": {"tags": [TAG.Gas, TAG.Distribution, TAG.Equipment]},
    "Meter": {
        "tags": [TAG.Meter, TAG.Equipment],
        "subclasses": {
            "Electrical_Meter": {
                "tags": [TAG.Electrical, TAG.Meter, TAG.Equipment],
                "subclasses": {
                    "Building_Electrical_Meter": {
                        "tags": [
                            TAG.Building,
                            TAG.Electrical,
                            TAG.Meter,
                            TAG.Equipment,
                        ],
                        "parents": [BRICK.Building_Meter],
                    }
                },
            },
            "Gas_Meter": {
                "tags": [TAG.Meter, TAG.Equipment, TAG.Gas],
                "subclasses": {
                    "Building_Gas_Meter": {
                        "tags": [TAG.Building, TAG.Gas, TAG.Meter, TAG.Equipment],
                        "parents": [BRICK.Building_Meter],
                    }
                },
            },
            "Thermal_Power_Meter": {
                "tags": [TAG.Meter, TAG.Equipment, TAG.Thermal, TAG.Power],
            },
            "Water_Meter": {
                "tags": [TAG.Meter, TAG.Equipment, TAG.Water],
                "subclasses": {
                    "Building_Water_Meter": {
                        "tags": [TAG.Building, TAG.Water, TAG.Meter, TAG.Equipment],
                        "parents": [BRICK.Building_Meter],
                    },
                    "Chilled_Water_Meter": {
                        "tags": [TAG.Meter, TAG.Equipment, TAG.Water, TAG.Chilled],
                        "subclasses": {
                            "Building_Chilled_Water_Meter": {
                                "tags": [
                                    TAG.Building,
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.Meter,
                                    TAG.Equipment,
                                ],
                                "parents": [BRICK.Building_Meter],
                            },
                        },
                    },
                    "Hot_Water_Meter": {
                        "tags": [TAG.Meter, TAG.Equipment, TAG.Water, TAG.Hot],
                        "subclasses": {
                            "Building_Hot_Water_Meter": {
                                "tags": [
                                    TAG.Building,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Meter,
                                    TAG.Equipment,
                                ],
                                "parents": [BRICK.Building_Meter],
                            },
                        },
                    },
                },
            },
            "Building_Meter": {"tags": [TAG.Meter, TAG.Equipment, TAG.Building]},
        },
    },
    "Motor": {
        "tags": [TAG.Equipment, TAG.Motor],
        "subclasses": {
            "Variable_Frequency_Drive": {
                "tags": [TAG.Equipment, TAG.Variable, TAG.Frequency, TAG.Drive],
                OWL.equivalentClass: BRICK["VFD"],
            },
            "VFD": {
                "tags": [TAG.Equipment, TAG.VFD],
                "subclasses": {
                    "Heat_Wheel_VFD": {
                        "tags": [TAG.Equipment, TAG.Heat, TAG.Wheel, TAG.VFD]
                    },
                    "Pump_VFD": {"tags": [TAG.Equipment, TAG.Pump, TAG.VFD]},
                    "Fan_VFD": {"tags": [TAG.Equipment, TAG.Fan, TAG.VFD]},
                },
            },
        },
    },
    "Water_Distribution": {"tags": [TAG.Water, TAG.Distribution, TAG.Equipment]},
    "Steam_Distribution": {"tags": [TAG.Steam, TAG.Distribution, TAG.Equipment]},
    "PV_Array": {
        "tags": [TAG.Solar, TAG.PV, TAG.Equipment, TAG.Array],
    },
    "PV_Panel": {
        "tags": [TAG.Solar, TAG.PV, TAG.Equipment, TAG.Panel],
        "subclasses": {
            "PVT_Panel": {
                "tags": [
                    TAG.Solar,
                    TAG.Equipment,
                    TAG.Thermal,
                    TAG.PV,
                    TAG.Panel,
                    TAG.Collector,
                ],
                "parents": [BRICK.Solar_Thermal_Collector],
            },
        },
    },
    "Solar_Thermal_Collector": {
        "tags": [TAG.Solar, TAG.Equipment, TAG.Thermal, TAG.Collector]
    },  # NOTE: Though Panel is a type of Collector.
    "Louver": {"tags": [TAG.Shade, TAG.Equipment, TAG.Louver]},
    "Lighting_Equipment": {
        "tags": [TAG.Lighting, TAG.Equipment],
        "subclasses": {
            "Lighting": {
                "subclasses": {
                    "Luminaire": {"tags": [TAG.Luminaire, TAG.Equipment]},
                    "Luminaire_Driver": {
                        "tags": [TAG.Luminaire, TAG.Driver, TAG.Equipment],
                    },
                },
            },
            "Interface": {
                "tags": [TAG.Equipment, TAG.Interface],
                "subclasses": {
                    "Switch": {
                        "tags": [TAG.Equipment, TAG.Interface, TAG.Switch],
                        "subclasses": {
                            "Dimmer": {
                                "tags": [
                                    TAG.Equipment,
                                    TAG.Interface,
                                    TAG.Switch,
                                    TAG.Dimmer,
                                ],
                            },
                        },
                    },
                    "Touchpanel": {
                        "tags": [TAG.Equipment, TAG.Interface, TAG.Touchpanel],
                    },
                },
            },
        },
    },
    "Furniture": {"tags": [TAG.Equipment, TAG.Furniture]},
    "Fire_Safety_Equipment": {
        "tags": [TAG.Equipment, TAG.Fire, TAG.Safety, TAG.Equipment],
        "subclasses": {
            "Fire_Control_Panel": {
                "tags": [TAG.Equipment, TAG.Fire, TAG.Safety, TAG.Panel],
            },
        },
    },
    "Elevator": {"tags": [TAG.Elevator, TAG.Equipment]},
    "Security_Equipment": {"tags": [TAG.Security, TAG.Equipment]},
    "Safety_Equipment": {"tags": [TAG.Safety, TAG.Equipment]},
    "Camera": {"tags": [TAG.Camera, TAG.Equipment]},
    "Water_Heater": {
        "tags": [TAG.Water, TAG.Heater, TAG.Equipment],
        "subclasses": {
            "Collection_Basin_Water_Heater": {
                "tags": [
                    TAG.Collection,
                    TAG.Basin,
                    TAG.Water,
                    TAG.Heater,
                    TAG.Equipment,
                ],
            }
        },
    },
}

"""
Define classes of HVAC equipment
"""
hvac_subclasses = {
    "Valve": {
        "tags": [TAG.Valve, TAG.Equipment]
        # subclasses defined in 'valve_subclasses'
    },
    "Thermostat": {"tags": [TAG.Equipment, TAG.Thermostat]},
    "Terminal_Unit": {
        "tags": [TAG.Equipment, TAG.Terminal, TAG.Unit],
        "subclasses": {
            "Constant_Air_Volume_Box": {
                "tags": [TAG.Equipment, TAG.Constant, TAG.Volume, TAG.Box],
                OWL.equivalentClass: BRICK["CAV"],
            },
            "CAV": {"tags": [TAG.Equipment, TAG.CAV]},
            "Fan_Coil_Unit": {
                "tags": [TAG.Equipment, TAG.Fan, TAG.Coil, TAG.Unit],
                OWL.equivalentClass: BRICK["FCU"],
            },
            "FCU": {"tags": [TAG.FCU, TAG.Equipment]},
            "Variable_Air_Volume_Box": {
                "tags": [TAG.Equipment, TAG.Variable, TAG.Volume, TAG.Box],
                OWL.equivalentClass: BRICK["VAV"],
                "subclasses": {
                    "Variable_Air_Volume_Box_With_Reheat": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Variable,
                            TAG.Volume,
                            TAG.Box,
                            TAG.Reheat,
                        ],
                        OWL.equivalentClass: BRICK["RVAV"],
                    },
                    "RVAV": {"tags": [TAG.Equipment, TAG.RVAV]},
                },
            },
            "VAV": {"tags": [TAG.Equipment, TAG.VAV]},
            "Radiant_Panel": {
                "tags": [TAG.Equipment, TAG.Radiant, TAG.Panel],
                "subclasses": {
                    "Thermally_Activated_Building_System": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Thermally,
                            TAG.Activated,
                            TAG.Building,
                            TAG.System,
                        ],
                        OWL.equivalentClass: BRICK["TABS"],
                    },
                    "TABS": {"tags": [TAG.Equipment, TAG.TABS]},
                    "Embedded_Surface_System": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Embedded,
                            TAG.Surface,
                            TAG.System,
                        ],
                        OWL.equivalentClass: BRICK["ESS"],
                    },
                    "ESS": {"tags": [TAG.Equipment, TAG.ESS]},
                    "Radiant_Ceiling_Panel": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Radiant,
                            TAG.Ceiling,
                            TAG.Panel,
                        ],
                        OWL.equivalentClass: BRICK["RCP"],
                    },
                    "RCP": {"tags": [TAG.Equipment, TAG.RCP]},
                },
            },
            "Radiator": {
                "tags": [TAG.Equipment, TAG.Radiator],
                "subclasses": {
                    "Steam_Radiator": {
                        "tags": [TAG.Equipment, TAG.Radiator, TAG.Steam]
                    },
                    "Hot_Water_Radiator": {
                        "tags": [TAG.Equipment, TAG.Radiator, TAG.Hot, TAG.Water]
                    },
                    "Electric_Radiator": {
                        "tags": [TAG.Equipment, TAG.Radiator, TAG.Electric]
                    },
                    "Baseboard_Radiator": {
                        "tags": [TAG.Equipment, TAG.Radiator, TAG.Baseboard],
                        "subclasses": {
                            "Steam_Baseboard_Radiator": {
                                "tags": [
                                    TAG.Equipment,
                                    TAG.Radiator,
                                    TAG.Baseboard,
                                    TAG.Steam,
                                ],
                                "parents": [BRICK.Steam_Radiator],
                            },
                            "Electric_Baseboard_Radiator": {
                                "tags": [
                                    TAG.Equipment,
                                    TAG.Radiator,
                                    TAG.Baseboard,
                                    TAG.Electric,
                                ],
                                "parents": [BRICK.Electric_Radiator],
                            },
                            "Hot_Water_Baseboard_Radiator": {
                                "tags": [
                                    TAG.Equipment,
                                    TAG.Radiator,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Baseboard,
                                ],
                                "parents": [BRICK.Hot_Water_Radiator],
                            },
                        },
                    },
                },
            },
        },
    },
    "Space_Heater": {"tags": [TAG.Equipment, TAG.Space, TAG.Heater]},
    "Pump": {
        "tags": [TAG.Equipment, TAG.Pump],
        "subclasses": {
            "Water_Pump": {
                "tags": [TAG.Equipment, TAG.Pump, TAG.Water],
                "subclasses": {
                    "Chilled_Water_Pump": {
                        "tags": [TAG.Equipment, TAG.Pump, TAG.Chilled, TAG.Water],
                    },
                    "Condenser_Water_Pump": {
                        "tags": [TAG.Equipment, TAG.Pump, TAG.Condenser, TAG.Water],
                    },
                    "Hot_Water_Pump": {
                        "tags": [TAG.Equipment, TAG.Pump, TAG.Hot, TAG.Water],
                    },
                },
            },
        },
    },
    "Heat_Exchanger": {
        "tags": [TAG.Equipment, TAG.Heat, TAG.Exchanger],
        OWL.equivalentClass: BRICK["HX"],
        "subclasses": {
            "Evaporative_Heat_Exchanger": {
                "tags": [TAG.Evaporative, TAG.Equipment, TAG.Heat, TAG.Exchanger],
            },
            "Condenser_Heat_Exchanger": {
                "tags": [TAG.Condenser, TAG.Equipment, TAG.Heat, TAG.Exchanger],
            },
            "Heat_Wheel": {"tags": [TAG.Equipment, TAG.Heat, TAG.Wheel]},
            "Coil": {
                "tags": [TAG.Equipment, TAG.Coil],
                "subclasses": {
                    "Cooling_Coil": {
                        "tags": [TAG.Equipment, TAG.Coil, TAG.Cool],
                        "subclasses": {
                            "Chilled_Water_Coil": {
                                "tags": [TAG.Equipment, TAG.Coil, TAG.Cool, TAG.Water]
                            },
                        },
                    },
                    "Heating_Coil": {
                        "tags": [TAG.Equipment, TAG.Coil, TAG.Heat],
                        "subclasses": {
                            "Hot_Water_Coil": {
                                "tags": [TAG.Equipment, TAG.Coil, TAG.Hot, TAG.Water]
                            },
                        },
                    },
                },
            },
        },
    },
    "HX": {"tags": [TAG.Equipment, TAG.HX]},
    "Fume_Hood": {"tags": [TAG.Equipment, TAG.Fume, TAG.Hood]},
    "Filter": {
        "tags": [TAG.Equipment, TAG.Filter],
        "subclasses": {
            "Mixed_Air_Filter": {
                "tags": [TAG.Equipment, TAG.Mixed, TAG.Air, TAG.Filter],
            },
            "Pre_Filter": {"tags": [TAG.Equipment, TAG.Pre, TAG.Filter]},
            "Final_Filter": {"tags": [TAG.Equipment, TAG.Final, TAG.Filter]},
            "Intake_Air_Filter": {
                "tags": [TAG.Equipment, TAG.Intake, TAG.Air, TAG.Filter]
            },
            "Return_Air_Filter": {
                "tags": [TAG.Equipment, TAG.Return, TAG.Air, TAG.Filter]
            },
        },
    },
    "Fan": {
        "tags": [TAG.Equipment, TAG.Fan],
        "subclasses": {
            "Cooling_Tower_Fan": {
                "tags": [TAG.Cool, TAG.Tower, TAG.Equipment, TAG.Fan],
            },
            "Exhaust_Fan": {"tags": [TAG.Equipment, TAG.Fan, TAG.Exhaust]},
            "Return_Fan": {"tags": [TAG.Equipment, TAG.Fan, TAG.Return]},
            "Booster_Fan": {"tags": [TAG.Equipment, TAG.Fan, TAG.Booster]},
            "Standby_Fan": {"tags": [TAG.Equipment, TAG.Fan, TAG.Standby]},
            "Discharge_Fan": {"tags": [TAG.Equipment, TAG.Fan, TAG.Discharge]},
            "Supply_Fan": {
                "tags": [TAG.Equipment, TAG.Fan, TAG.Supply],
                OWL.equivalentClass: BRICK["Discharge_Fan"],
            },
            "Ceiling_Fan": {"tags": [TAG.Equipment, TAG.Fan, TAG.Ceiling]},
            "Fresh_Air_Fan": {"tags": [TAG.Equipment, TAG.Fan, TAG.Fresh, TAG.Air]},
        },
    },
    "Economizer": {"tags": [TAG.Equipment, TAG.Economizer]},
    "Damper": {
        "tags": [TAG.Equipment, TAG.Damper],
        "subclasses": {
            "Economizer_Damper": {"tags": [TAG.Equipment, TAG.Damper, TAG.Economizer]},
            "Exhaust_Damper": {"tags": [TAG.Equipment, TAG.Damper, TAG.Exhaust]},
            "Outside_Damper": {"tags": [TAG.Equipment, TAG.Damper, TAG.Outside]},
            "Return_Damper": {"tags": [TAG.Equipment, TAG.Damper, TAG.Return]},
            "Mixed_Damper": {"tags": [TAG.Equipment, TAG.Damper, TAG.Mixed]},
        },
    },
    "Condenser": {"tags": [TAG.Equipment, TAG.Condenser]},
    "Computer_Room_Air_Conditioning": {
        "tags": [TAG.Equipment, TAG.Computer, TAG.Room, TAG.Air, TAG.Conditioning],
        OWL.equivalentClass: BRICK["CRAC"],
    },
    "CRAC": {
        "tags": [TAG.Equipment, TAG.CRAC],
        OWL.equivalentClass: BRICK["Computer_Room_Air_Conditioning"],
        "subclasses": {
            "Standby_CRAC": {"tags": [TAG.Equipment, TAG.CRAC, TAG.Standby]},
        },
    },
    "Compressor": {"tags": [TAG.Equipment, TAG.Compressor]},
    "Cooling_Tower": {"tags": [TAG.Equipment, TAG.Cooling, TAG.Tower]},
    "Chiller": {
        "tags": [TAG.Equipment, TAG.Chiller],
        "subclasses": {
            "Absorption_Chiller": {
                "tags": [TAG.Equipment, TAG.Chiller, TAG.Absorption],
            },
            "Centrifugal_Chiller": {
                "tags": [TAG.Equipment, TAG.Chiller, TAG.Centrifugal],
            },
        },
    },
    "Humidifier": {"tags": [TAG.Equipment, TAG.Humidifier]},
    "Boiler": {"tags": [TAG.Equipment, TAG.Boiler], "parents": [BRICK.Water_Heater]},
    "Air_Handler_Unit": {
        # here for historical purposes
        "tags": [TAG.Equipment, TAG.Air, TAG.Handler, TAG.Unit],
        OWL.equivalentClass: [BRICK["AHU"], BRICK["Air_Handling_Unit"]],
    },
    "Air_Handling_Unit": {
        "tags": [TAG.Equipment, TAG.Air, TAG.Handling, TAG.Unit],
        OWL.equivalentClass: [BRICK["AHU"], BRICK["Air_Handler_Unit"]],
    },
    "AHU": {
        "tags": [TAG.Equipment, TAG.AHU],
        "subclasses": {
            "Rooftop_Unit": {
                OWL.equivalentClass: BRICK["RTU"],
                "tags": [TAG.Equipment, TAG.Rooftop, TAG.AHU],
            },
            "RTU": {
                "tags": [TAG.Equipment, TAG.RTU],
                OWL.equivalentClass: BRICK["Rooftop_Unit"],
            },
            "PAU": {"tags": [TAG.Equipment, TAG.PAU]},
        },
    },
}

"""
Valve subclasses
"""
valve_subclasses = {
    "Heating_Valve": {
        "tags": [TAG.Valve, TAG.Heat, TAG.Equipment],
        "subclasses": {
            "Reheat_Valve": {"tags": [TAG.Valve, TAG.Reheat, TAG.Heat, TAG.Equipment]},
            "Return_Heating_Valve": {
                "tags": [TAG.Valve, TAG.Return, TAG.Heat, TAG.Equipment],
            },
        },
    },
    "Cooling_Valve": {"tags": [TAG.Valve, TAG.Cool, TAG.Equipment]},
    "Water_Valve": {
        "tags": [TAG.Valve, TAG.Water, TAG.Equipment],
        "subclasses": {
            "Chilled_Water_Valve": {
                "tags": [TAG.Chilled, TAG.Valve, TAG.Water, TAG.Equipment],
            },
            "Condenser_Water_Valve": {
                "tags": [TAG.Condenser, TAG.Valve, TAG.Water, TAG.Equipment],
            },
            "Hot_Water_Valve": {
                "tags": [TAG.Hot, TAG.Valve, TAG.Water, TAG.Equipment],
                "parents": [BRICK.Heating_Valve],
                "subclasses": {
                    "Domestic_Hot_Water_Valve": {
                        "tags": [
                            TAG.Domestic,
                            TAG.Water,
                            TAG.Hot,
                            TAG.Valve,
                            TAG.Heat,
                            TAG.Equipment,
                        ]
                    },
                    "Preheat_Hot_Water_Valve": {
                        "tags": [
                            TAG.Preheat,
                            TAG.Water,
                            TAG.Hot,
                            TAG.Valve,
                            TAG.Heat,
                            TAG.Equipment,
                        ]
                    },
                },
            },
            "Makeup_Water_Valve": {
                "tags": [
                    TAG.Fluid,
                    TAG.Liquid,
                    TAG.Water,
                    TAG.Makeup,
                    TAG.Valve,
                    TAG.Equipment,
                ]
            },
        },
    },
    "Gas_Valve": {"tags": [TAG.Gas, TAG.Valve, TAG.Equipment]},
    "Isolation_Valve": {
        "tags": [TAG.Isolation, TAG.Valve, TAG.Equipment],
        "subclasses": {
            "Condenser_Water_Isolation_Valve": {
                "tags": [
                    TAG.Condenser,
                    TAG.Water,
                    TAG.Isolation,
                    TAG.Valve,
                    TAG.Equipment,
                ]
            }
        },
    },
    "Steam_Valve": {"tags": [TAG.Steam, TAG.Valve, TAG.Equipment]},
    "Bypass_Valve": {
        "tags": [TAG.Bypass, TAG.Valve, TAG.Equipment],
        "subclasses": {
            "Differential_Pressure_Bypass_Valve": {
                "tags": [
                    TAG.Differential,
                    TAG.Pressure,
                    TAG.Bypass,
                    TAG.Valve,
                    TAG.Equipment,
                ],
            },
            "Condenser_Water_Bypass_Valve": {
                "tags": [TAG.Condenser, TAG.Water, TAG.Bypass, TAG.Valve, TAG.Equipment]
            },
        },
    },
}

security_subclasses = {
    "Access_Control_Equipment": {
        "tags": [TAG.Equipment, TAG.Security, TAG.Access, TAG.Control],
        "subclasses": {
            "Access_Reader": {
                "tags": [
                    TAG.Equipment,
                    TAG.Security,
                    TAG.Access,
                    TAG.Reader,
                    TAG.Control,
                ],
            },
        },
        # TODO subclasses
        # Access (Control) Panel: The controller panel will typically have electrical connections for the selected credential reader,
        # a relay output to control the door release, door position input, programmable inputs and outputs, and inputs for the REX.
        # Accsss Control Sub Panel (Alarm Panel)?
        # Panel_Input: Input into the access panel: switch toggle, button press, credential entered/scanned/swiped, etc
        # Panel_Output: Ouput from the access panel: some sort of function is activated, door area is unlocked, etc
        # Reader_Aux_Input: The input from the reader on the “other” side of the controlled door
        # Reader_Aux_Output: The output from the reader on the “other” side of the controlled door
        # Biometric Reader: Reader of biometric characteristics to be used for authentication
        # REX: Request to exit. a required accessory in an access control system, which can take the form of anything from a
        #    mushroom button to an infrared sensor. In an access control system, the REX (Request to exit) trips a relay in the panel
        #    to bypass “door forced” alarms within the access control software to avoid false alarms in the audit report. It can also be
        #    used to trip a relay which changes the state of an electric electronic item from on to off, lock to unlock or open to close.
        # Magnetic_Lock: Electromagnetic or magnetic lock, a locking mechanisim that consists of an electromagnet and an armature plate.
        # Electrified_Lock: An electronic lock, a locking device that works by means of electric current. Can be controlled remotely
        #     depending on the locking system.
        # Door_Release: An electronic input device used to immediately unlock specififed doors that are equipped with electronic locks.
        # Badge Station: A kiosk or checkpoint that requires the use of a badge in order to verify credentials and to grant access.
    },
    "Video_Surveillance_Equipment": {
        "tags": [TAG.Equipment, TAG.Security, TAG.Video, TAG.Surveillance],
        "subclasses": {
            "Surveillance_Camera": {
                "tags": [
                    TAG.Equipment,
                    TAG.Security,
                    TAG.Video,
                    TAG.Surveillance,
                    TAG.Camera,
                ],
                "parents": [BRICK.Camera]
                # TODO: subclass of PTZ (Pan/Tilt/Zoom) cameras?
            },
            "NVR": {
                "tags": [
                    TAG.Equipment,
                    TAG.Security,
                    TAG.Video,
                    TAG.Surveillance,
                    TAG.NVR,
                ],
                OWL.equivalentClass: BRICK["Network_Video_Recorder"],
            },
            "Network_Video_Recorder": {
                "tags": [
                    TAG.NVR,
                    TAG.Equipment,
                    TAG.Security,
                    TAG.Video,
                    TAG.Recorder,
                    TAG.Network,
                ],
                OWL.equivalentClass: BRICK["NVR"],
            },
        },
        # TODO
        # Encoder: (Do we imply video encoder here?) - A device that is used to convert information from one format to another.
        # Switch: Again this sounds generic - A device that can connect, disconnect, or divert current in an electrical current (or signal)
        # - is any specific kind of switch e.g. PoESwitch implied here?
        # Video_Wall (or should this be in a separate classification with displays and monitors?)
    },
    "Intrusion_Detection_Equipment": {
        "tags": [TAG.Equipment, TAG.Security, TAG.Intrusion, TAG.Detection],
        # TODO
        # Motion sensor - but maybe to Points, but still need a way to represent security motion sensors
        # Security Control Panel: The central hub of a security system. All devices are connected to the security panel for easy
        #    and efficient access for different security protocols (i.e. Intrusion security) and events. Question: How’s this different from
        #    Access Panel? Is this specific to Intrusion detection system or more general?
        # Glass_Break_Sensor: a sensor used in electronic alarms that detect if pane of glass has been shattered or is broken.
        # Duress_Button: Panic button, an electronic input device used to help alerting someone in emergency situations.
        # Door_Contacts: Door contact sensor, a peripheral security sensor that lets an alarm system know whether a door is
        # open or closed.
    },
    "Intercom_Equipment": {
        "tags": [TAG.Equipment, TAG.Security, TAG.Intercom],
        "subclasses": {
            "Emergency_Phone": {
                "tags": [
                    TAG.Equipment,
                    TAG.Security,
                    TAG.Intercom,
                    TAG.Emergency,
                    TAG.Phone,
                ],
            },
            "Video_Intercom": {
                "tags": [TAG.Equipment, TAG.Security, TAG.Intercom, TAG.Video],
            },
        },
    },
}

safety_subclasses = {
    "Automated_External_Defibrillator": {
        OWL.equivalentClass: BRICK["AED"],
        "tags": [TAG.Equipment, TAG.Safety, TAG.AED, TAG.Defibrillator],
    },
    "AED": {
        OWL.equivalentClass: BRICK["Automated_External_Defibrillator"],
        "tags": [TAG.Equipment, TAG.Safety, TAG.AED, TAG.Defibrillator],
    },
    "First_Aid_Kit": {"tags": [TAG.Equipment, TAG.Safety, TAG.Aid, TAG.FirstAid]},
    "Emergency_Wash_Station": {
        "tags": [TAG.Equipment, TAG.Safety, TAG.Wash, TAG.Station, TAG.Emergency],
        "subclasses": {
            "Eye_Wash_Station": {
                "tags": [
                    TAG.Equipment,
                    TAG.Safety,
                    TAG.Wash,
                    TAG.Station,
                    TAG.Emergency,
                    TAG.Eye,
                ],
            },
            "Safety_Shower": {
                "tags": [
                    TAG.Equipment,
                    TAG.Safety,
                    TAG.Wash,
                    TAG.Station,
                    TAG.Emergency,
                    TAG.Shower,
                ],
            },
            "Drench_Hose": {
                "tags": [
                    TAG.Equipment,
                    TAG.Safety,
                    TAG.Wash,
                    TAG.Station,
                    TAG.Emergency,
                    TAG.Drench,
                    TAG.Hose,
                ],
            },
        },
    },
}
