from rdflib import Literal
from .namespaces import TAG, OWL, BRICK, REC
from .meters import meter_subclasses

"""
Set up subclasses of the equipment superclass
"""
equipment_subclasses = {
    "ICT_Equipment": {
        "tags": [TAG.ICT, TAG.Equipment],
        "subclasses": {
            "ICT_Hardware": {
                "tags": [TAG.Equipment, TAG.ICT, TAG.Hardware],
                "subclasses": {
                    "Tablet": {
                        "tags": [TAG.Equipment, TAG.ICT, TAG.Hardware, TAG.Tablet]
                    },
                    "Server": {
                        "tags": [TAG.Equipment, TAG.ICT, TAG.Hardware, TAG.Server]
                    },
                },
            },
            "ICT_Rack": {
                "tags": [TAG.Equipment, TAG.ICT, TAG.Rack],
            },
            "Sensor_Equipment": {
                "tags": [TAG.Sensor, TAG.Equipment, TAG.ICT],
                "subclasses": {
                    "Daylight_Sensor_Equipment": {
                        "tags": [TAG.Daylight, TAG.Sensor, TAG.Equipment, TAG.ICT],
                    },
                    "IAQ_Sensor_Equipment": {
                        "tags": [TAG.IAQ, TAG.Sensor, TAG.Equipment, TAG.ICT],
                    },
                    "Leak_Detector_Equipment": {
                        "tags": [TAG.Leak, TAG.Detector, TAG.Equipment, TAG.ICT],
                    },
                    "Occupancy_Sensor_Equipment": {
                        "tags": [TAG.Occupancy, TAG.Sensor, TAG.Equipment, TAG.ICT],
                    },
                    "People_Count_Sensor_Equipment": {
                        "tags": [
                            TAG.People,
                            TAG.Count,
                            TAG.Sensor,
                            TAG.Equipment,
                            TAG.ICT,
                        ],
                    },
                    "Thermostat_Equipment": {
                        "tags": [TAG.Thermostat, TAG.Equipment, TAG.ICT],
                    },
                    "Vibration_Sensor_Equipment": {
                        "tags": [TAG.Vibration, TAG.Sensor, TAG.Equipment, TAG.ICT],
                    },
                },
            },
            "Controller": {
                "tags": [TAG.Equipment, TAG.ICT, TAG.Controller],
                "subclasses": {
                    "BACnet_Controller": {
                        "tags": [TAG.Equipment, TAG.BACnet, TAG.Controller],
                    },
                    "Modbus_Controller": {
                        "tags": [TAG.Equipment, TAG.Modbus, TAG.Controller],
                    },
                },
            },
            "Data_Network_Equipment": {
                "tags": [TAG.Equipment, TAG.Data, TAG.Network],
                "subclasses": {
                    "Ethernet_Port": {
                        "tags": [TAG.Ethernet, TAG.Port, TAG.Equipment],
                    },
                    "Ethernet_Switch": {
                        "tags": [TAG.Ethernet, TAG.Switch, TAG.Equipment],
                    },
                    "Network_Router": {
                        "tags": [TAG.Network, TAG.Router, TAG.Equipment],
                    },
                    "Network_Security_Equipment": {
                        "tags": [TAG.Network, TAG.Security, TAG.Equipment],
                    },
                    "Wireless_Access_Point": {
                        "tags": [TAG.Wireless, TAG.Access, TAG.Point, TAG.Equipment],
                    },
                },
            },
            "Gateway": {
                "tags": [TAG.Equipment, TAG.Gateway, TAG.ICT],
            },
            "Audio_Visual_Equipment": {
                "tags": [TAG.Equipment, TAG.ICT, TAG.Audio, TAG.Visual]
            },
        },
    },
    "HVAC_Equipment": {
        "tags": [TAG.HVAC, TAG.Equipment],
        "constraints": {
            BRICK.hasPart: [BRICK.HVAC_Equipment, BRICK.Valve],
            BRICK.feeds: [BRICK.HVAC_Equipment, BRICK.Valve, REC.Space],
        },
    },
    "Weather_Station": {"tags": [TAG.Weather, TAG.Station, TAG.Equipment]},
    "Shading_Equipment": {
        "tags": [TAG.Shade, TAG.Equipment],
        "subclasses": {
            "Blind": {"tags": [TAG.Shade, TAG.Blind, TAG.Equipment]},
            "Automatic_Tint_Window": {
                "tags": [TAG.Shade, TAG.Equipment, TAG.Automatic, TAG.Tint, TAG.Window]
            },
        },
    },
    "Electrical_Equipment": {
        "tags": [TAG.Electrical, TAG.Equipment],
        "subclasses": {
            "Electric_Vehicle_Charging_Station": {
                "tags": [
                    TAG.Electric,
                    TAG.Vehicle,
                    TAG.Charging,
                    TAG.Station,
                    TAG.Equipment,
                ],
                "constraints": {BRICK.hasPart: [BRICK.Electric_Vehicle_Charging_Port]},
            },
            "Electric_Vehicle_Charging_Port": {
                "tags": [
                    TAG.Electric,
                    TAG.Vehicle,
                    TAG.Charging,
                    TAG.Port,
                    TAG.Equipment,
                ],
            },
            "Energy_Storage": {
                "tags": [TAG.Energy, TAG.Storage, TAG.Equipment],
                "subclasses": {
                    "Battery": {
                        "tags": [TAG.Battery, TAG.Energy, TAG.Storage, TAG.Equipment],
                    }
                },
            },
            "Inverter": {
                "tags": [TAG.Inverter, TAG.Equipment],
                "subclasses": {
                    "Photovoltaic_Inverter": {
                        "tags": [TAG.Photovoltaic, TAG.Inverter, TAG.Equipment]
                    }
                },
            },
            "PlugStrip": {"tags": [TAG.PlugStrip, TAG.Equipment]},
            "Switchgear": {
                "tags": [
                    TAG.Switchgear,
                    TAG.Equipment,
                ],
                "subclasses": {
                    "Automatic_Switch": {
                        "tags": [
                            TAG.Automatic,
                            TAG.Switch,
                            TAG.Equipment,
                        ]
                    },
                    "Circuit_Breaker": {
                        "tags": [
                            TAG.Circuit,
                            TAG.Breaker,
                        ],
                        "subclasses": {
                            "Main_Circuit_Breaker": {
                                "tags": [
                                    TAG.Main,
                                    TAG.Circuit,
                                    TAG.Breaker,
                                    TAG.Equipment,
                                ]
                            }
                        },
                    },
                    "Disconnect_Switch": {
                        "tags": [
                            TAG.Disconnect,
                            TAG.Switch,
                            TAG.Equipment,
                        ],
                        "subclasses": {
                            "Main_Disconnect_Switch": {
                                "tags": [
                                    TAG.Main,
                                    TAG.Disconnect,
                                    TAG.Switch,
                                    TAG.Equipment,
                                ]
                            },
                            "Building_Disconnect_Switch": {
                                "tags": [
                                    TAG.Building,
                                    TAG.Disconnect,
                                    TAG.Switch,
                                    TAG.Equipment,
                                ]
                            },
                        },
                    },
                    "Isolation_Switch": {
                        "tags": [TAG.Isolation, TAG.Switch, TAG.Equipment],
                        "aliases": [BRICK.Disconnect_Switch],
                    },
                    "Transfer_Switch": {
                        "tags": [
                            TAG.Transfer,
                            TAG.Switch,
                            TAG.Equipment,
                        ],
                        "subclasses": {
                            "Automatic_Transfer_Switch": {
                                "parents": [BRICK.Automatic_Switch],
                                "tags": [
                                    TAG.Automatic,
                                    TAG.Transfer,
                                    TAG.Switch,
                                    TAG.Equipment,
                                ],
                            },
                            "Static_Transfer_Switch": {
                                "parents": [BRICK.Automatic_Switch],
                                "tags": [
                                    TAG.Static,
                                    TAG.Transfer,
                                    TAG.Switch,
                                    TAG.Equipment,
                                ],
                            },
                        },
                    },
                },
            },
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
        "subclasses": meter_subclasses,
    },
    "Motor": {
        "tags": [TAG.Equipment, TAG.Motor],
        "subclasses": {
            "Variable_Frequency_Drive": {
                "tags": [
                    TAG.Equipment,
                    TAG.Variable,
                    TAG.Frequency,
                    TAG.Drive,
                    TAG.VFD,
                ],
                "aliases": [BRICK["VFD"]],
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
    "Lighting_Equipment": {
        "tags": [TAG.Lighting, TAG.Equipment],
        "constraints": {
            BRICK.hasPart: [BRICK.Lighting_Equipment, BRICK.Electrical_Equipment],
            BRICK.feeds: [BRICK.Lighting_Equipment, REC.Space],
        },
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
    "Furniture": {
        "tags": [TAG.Equipment, TAG.Furniture],
        "subclasses": {
            "Stage_Riser": {
                "tags": [TAG.Equipment, TAG.Furniture, TAG.Stage, TAG.Riser],
            },
        },
    },
    "Fire_Safety_Equipment": {
        "tags": [TAG.Equipment, TAG.Fire, TAG.Safety],
        "subclasses": {
            "Fire_Control_Panel": {
                "tags": [TAG.Equipment, TAG.Fire, TAG.Safety, TAG.Panel, TAG.Control],
            },
            "Fire_Alarm_Control_Panel": {
                "tags": [
                    TAG.Equipment,
                    TAG.Fire,
                    TAG.Safety,
                    TAG.Panel,
                    TAG.Control,
                    TAG.Alarm,
                ],
            },
            "Fire_Alarm": {
                "tags": [TAG.Equipment, TAG.Fire, TAG.Safety, TAG.Alarm],
            },
            "Manual_Fire_Alarm_Activation_Equipment": {
                "tags": [
                    TAG.Equipment,
                    TAG.Fire,
                    TAG.Safety,
                    TAG.Alarm,
                    TAG.Activation,
                    TAG.Manual,
                ],
                "subclasses": {
                    "Fire_Alarm_Pull_Station": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Fire,
                            TAG.Safety,
                            TAG.Pull,
                            TAG.Station,
                            TAG.Alarm,
                            TAG.Manual,
                        ],
                    },
                    "Fire_Alarm_Manual_Call_Point": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Fire,
                            TAG.Safety,
                            TAG.Call,
                            TAG.Station,
                            TAG.Alarm,
                            TAG.Manual,
                        ],
                    },
                },
            },
            "Heat_Detector": {
                "tags": [TAG.Equipment, TAG.Fire, TAG.Safety, TAG.Heat, TAG.Detector],
            },
            "Smoke_Detector": {
                "tags": [TAG.Equipment, TAG.Fire, TAG.Safety, TAG.Smoke, TAG.Detector],
            },
        },
    },
    "Elevator": {"tags": [TAG.Elevator, TAG.Equipment]},
    "Security_Equipment": {"tags": [TAG.Security, TAG.Equipment]},
    "Safety_Equipment": {"tags": [TAG.Safety, TAG.Equipment]},
    "Camera": {"tags": [TAG.Camera, TAG.Equipment]},
    "Relay": {"tags": [TAG.Relay, TAG.Equipment]},
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
    "Tank": {
        "tags": [TAG.Tank, TAG.Equipment],
        "subclasses": {
            "Storage_Tank": {
                "tags": [TAG.Tank, TAG.Equipment, TAG.Storage],
                "subclasses": {
                    "Water_Storage_Tank": {
                        "tags": [TAG.Water, TAG.Storage, TAG.Equipment],
                        "subclasses": {
                            "Chilled_Water_Storage_Tank": {
                                "tags": [
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.Storage,
                                    TAG.Equipment,
                                ]
                            },
                            "Cold_Water_Storage_Tank": {
                                "tags": [
                                    TAG.Cold,
                                    TAG.Water,
                                    TAG.Storage,
                                    TAG.Equipment,
                                ]
                            },
                            "Hot_Water_Storage_Tank": {
                                "tags": [TAG.Hot, TAG.Water, TAG.Storage, TAG.Equipment]
                            },
                            "Fire_Sprinkler_Water_Storage_Tank": {
                                "tags": [
                                    TAG.Fire,
                                    TAG.Water,
                                    TAG.Storage,
                                    TAG.Equipment,
                                ]
                            },
                            "Rain_Water_Storage_Tank": {
                                "tags": [
                                    TAG.Rain,
                                    TAG.Water,
                                    TAG.Storage,
                                    TAG.Equipment,
                                ]
                            },
                        },
                    },
                    "Thermal_Energy_Storage_Tank": {
                        "tags": [
                            TAG.Thermal,
                            TAG.Energy,
                            TAG.Storage,
                            TAG.Tank,
                            TAG.Equipment,
                        ],
                        "subclasses": {
                            "Chilled_Water_Thermal_Energy_Storage_Tank": {
                                "tags": [
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.Thermal,
                                    TAG.Energy,
                                    TAG.Storage,
                                    TAG.Tank,
                                    TAG.Equipment,
                                ],
                            },
                            "Hot_Water_Thermal_Energy_Storage_Tank": {
                                "tags": [
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Thermal,
                                    TAG.Energy,
                                    TAG.Storage,
                                    TAG.Tank,
                                    TAG.Equipment,
                                ],
                            },
                        },
                    },
                },
            },
            "Thermal_Expansion_Tank": {
                "tags": [TAG.Tank, TAG.Equipment],
                "subclasses": {
                    "Chilled_Water_Thermal_Expansion_Tank": {
                        "tags": [
                            TAG.Chilled,
                            TAG.Thermal,
                            TAG.Expansion,
                            TAG.Tank,
                            TAG.Equipment,
                        ],
                    },
                    "Hot_Water_Thermal_Expansion_Tank": {
                        "tags": [
                            TAG.Hot,
                            TAG.Thermal,
                            TAG.Expansion,
                            TAG.Tank,
                            TAG.Equipment,
                        ],
                    },
                    "Fire_Sprinkler_Thermal_Expansion_Tank": {
                        "tags": [
                            TAG.Fire,
                            TAG.Thermal,
                            TAG.Expansion,
                            TAG.Tank,
                            TAG.Equipment,
                        ],
                    },
                },
            },
            "Separation_Tank": {
                "tags": [TAG.Tank, TAG.Equipment],
                "subclasses": {
                    "Grease_Interceptor": {
                        "tags": [TAG.Waste, TAG.Tank, TAG.Equipment],
                    }
                },
            },
        },
    },
}

"""
Define classes of HVAC equipment
"""
hvac_subclasses = {
    "Branch_Selector": {"tags": [TAG.Equipment, TAG.HVAC, TAG.Branch, TAG.Selector]},
    "Dry_Cooler": {"tags": [TAG.Equipment, TAG.HVAC, TAG.Dry, TAG.Cooler]},
    "HVAC_Valve": {
        "tags": [TAG.HVAC, TAG.Valve, TAG.Equipment],
        "parents": [BRICK.Valve],
        # subclasses defined in 'valve_subclasses'
    },
    "Hot_Deck": {"tags": [TAG.Equipment, TAG.Hot, TAG.Deck]},
    "Cold_Deck": {"tags": [TAG.Equipment, TAG.Cold, TAG.Deck]},
    "Thermostat": {
        "tags": [TAG.Equipment, TAG.Thermostat],
        "parents": [BRICK.Sensor_Equipment],
    },
    "Terminal_Unit": {
        "tags": [TAG.Equipment, TAG.Terminal, TAG.Unit],
        "subclasses": {
            "Constant_Air_Volume_Box": {
                "tags": [TAG.Equipment, TAG.Constant, TAG.Volume, TAG.Box, TAG.CAV],
                "aliases": [BRICK["CAV"]],
            },
            "Fan_Coil_Unit": {
                "tags": [TAG.Equipment, TAG.Fan, TAG.Coil, TAG.Unit, TAG.FCU],
                "aliases": [BRICK["FCU"]],
                "subclasses": {
                    "Cassette_Fan_Coil_Unit": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Fan,
                            TAG.Coil,
                            TAG.Unit,
                            TAG.FCU,
                            TAG.Cassette,
                            TAG.Ceiling,
                        ]
                    },
                    "Duct_Fan_Coil_Unit": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Fan,
                            TAG.Coil,
                            TAG.Unit,
                            TAG.FCU,
                            TAG.Duct,
                            TAG.Horizontal,
                        ],
                        "aliases": [BRICK["Horizontal_Fan_Coil_Unit"]],
                    },
                    "Floor_Fan_Coil_Unit": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Fan,
                            TAG.Coil,
                            TAG.Unit,
                            TAG.FCU,
                            TAG.Floor,
                        ]
                    },
                    "Wall_Fan_Coil_Unit": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Fan,
                            TAG.Coil,
                            TAG.Unit,
                            TAG.FCU,
                            TAG.Wall,
                            TAG.Mounted,
                        ]
                    },
                },
            },
            "Variable_Air_Volume_Box": {
                "tags": [TAG.Equipment, TAG.Variable, TAG.Volume, TAG.Box, TAG.VAV],
                "aliases": [BRICK["VAV"]],
                "subclasses": {
                    "Variable_Air_Volume_Box_With_Reheat": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Variable,
                            TAG.Volume,
                            TAG.Box,
                            TAG.Reheat,
                            TAG.RVAV,
                        ],
                        "aliases": [BRICK["RVAV"]],
                    },
                },
            },
            "Radiant_Panel": {
                "tags": [TAG.Equipment, TAG.Radiant, TAG.Panel],
                "subclasses": {
                    "Thermally_Activated_Building_System_Panel": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Thermally,
                            TAG.Activated,
                            TAG.Building,
                            TAG.System,
                            TAG.TABS,
                            TAG.Panel,
                        ],
                        "aliases": [BRICK["TABS_Panel"]],
                    },
                    "Embedded_Surface_System_Panel": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Embedded,
                            TAG.Surface,
                            TAG.System,
                            TAG.ESS,
                            TAG.Panel,
                        ],
                        "aliases": [BRICK["ESS_Panel"]],
                    },
                    "Radiant_Ceiling_Panel": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Radiant,
                            TAG.Ceiling,
                            TAG.RC,
                            TAG.Panel,
                        ],
                        "aliases": [BRICK["RC_Panel"]],
                    },
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
            "Air_Diffuser": {
                "tags": [
                    TAG.Equipment,
                    TAG.Air,
                    TAG.Diffuser,
                ],
                "subclasses": {
                    "Jet_Nozzle_Air_Diffuser": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Jet,
                            TAG.Nozzle,
                            TAG.Air,
                            TAG.Diffuser,
                        ]
                    },
                    "Laminar_Flow_Air_Diffuser": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Laminar,
                            TAG.Flow,
                            TAG.Air,
                            TAG.Diffuser,
                        ]
                    },
                    "Displacement_Flow_Air_Diffuser": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Displacement,
                            TAG.Flow,
                            TAG.Air,
                            TAG.Diffuser,
                        ]
                    },
                },
            },
            "Chilled_Beam": {
                "tags": [TAG.Equipment, TAG.Chilled, TAG.Beam],
                "subclasses": {
                    "Active_Chilled_Beam": {
                        "tags": [TAG.Equipment, TAG.Active, TAG.Chilled, TAG.Beam]
                    },
                    "Passive_Chilled_Beam": {
                        "tags": [TAG.Equipment, TAG.Passive, TAG.Chilled, TAG.Beam]
                    },
                },
            },
            "Induction_Unit": {"tags": [TAG.Equipment, TAG.Induction, TAG.Unit]},
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
                        "subclasses": {
                            "Chilled_Water_Circulator_Pump": {
                                "tags": [
                                    TAG.Equipment,
                                    TAG.Pump,
                                    TAG.Circulator,
                                    TAG.Chilled,
                                    TAG.Water,
                                ],
                                "parents": [BRICK.Circulator_Pump],
                            },
                            "Chilled_Water_Booster_Pump": {
                                "tags": [
                                    TAG.Equipment,
                                    TAG.Pump,
                                    TAG.Booster,
                                    TAG.Chilled,
                                    TAG.Water,
                                ],
                                "parents": [BRICK.Booster_Pump],
                            },
                        },
                    },
                    "Condenser_Water_Pump": {
                        "tags": [TAG.Equipment, TAG.Pump, TAG.Condenser, TAG.Water],
                        "subclasses": {
                            "Condenser_Water_Circulator_Pump": {
                                "tags": [
                                    TAG.Equipment,
                                    TAG.Pump,
                                    TAG.Circulator,
                                    TAG.Condenser,
                                    TAG.Water,
                                ],
                                "parents": [BRICK.Circulator_Pump],
                            },
                            "Condenser_Water_Booster_Pump": {
                                "tags": [
                                    TAG.Equipment,
                                    TAG.Pump,
                                    TAG.Booster,
                                    TAG.Condenser,
                                    TAG.Water,
                                ],
                                "parents": [BRICK.Booster_Pump],
                            },
                        },
                    },
                    "Hot_Water_Pump": {
                        "tags": [TAG.Equipment, TAG.Pump, TAG.Hot, TAG.Water],
                        "subclasses": {
                            "Hot_Water_Circulator_Pump": {
                                "tags": [
                                    TAG.Equipment,
                                    TAG.Pump,
                                    TAG.Circulator,
                                    TAG.Hot,
                                    TAG.Water,
                                ],
                                "parents": [BRICK.Circulator_Pump],
                                "subclasses": {
                                    "Domestic_Hot_Water_Circulator_Pump": {
                                        "tags": [
                                            TAG.Equipment,
                                            TAG.Pump,
                                            TAG.Circulator,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Domestic,
                                        ],
                                    },
                                },
                            },
                            "Hot_Water_Booster_Pump": {
                                "tags": [
                                    TAG.Equipment,
                                    TAG.Pump,
                                    TAG.Booster,
                                    TAG.Hot,
                                    TAG.Water,
                                ],
                                "parents": [BRICK.Booster_Pump],
                            },
                        },
                    },
                },
            },
            "Circulator_Pump": {
                "tags": [TAG.Equipment, TAG.Pump, TAG.Circulator],
            },
            "Booster_Pump": {
                "tags": [TAG.Equipment, TAG.Pump, TAG.Booster],
            },
        },
    },
    "Heat_Exchanger": {
        "tags": [TAG.Equipment, TAG.Heat, TAG.Exchanger, TAG.HX],
        "aliases": [BRICK["HX"]],
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
                                "tags": [
                                    TAG.Chilled,
                                    TAG.Equipment,
                                    TAG.Coil,
                                    TAG.Cool,
                                    TAG.Water,
                                ]
                            },
                            "Direct_Expansion_Cooling_Coil": {
                                "tags": [
                                    TAG.Equipment,
                                    TAG.Coil,
                                    TAG.Cool,
                                    TAG.Direct,
                                    TAG.Expansion,
                                ]
                            },
                        },
                    },
                    "Heating_Coil": {
                        "tags": [TAG.Equipment, TAG.Coil, TAG.Heat],
                        "subclasses": {
                            "Hot_Water_Coil": {
                                "tags": [
                                    TAG.Equipment,
                                    TAG.Coil,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Heat,
                                ]
                            },
                            "Direct_Expansion_Heating_Coil": {
                                "tags": [
                                    TAG.Equipment,
                                    TAG.Coil,
                                    TAG.Heat,
                                    TAG.Direct,
                                    TAG.Expansion,
                                ]
                            },
                        },
                    },
                },
            },
        },
    },
    "Packaged_Heat_Pump": {
        "tags": [
            TAG.Equipment,
            TAG.Heat,
            TAG.Pump,
        ],
        "subclasses": {
            "Packaged_Air_Source_Heat_Pump": {
                "tags": [
                    TAG.Equipment,
                    TAG.Air,
                    TAG.Source,
                    TAG.Heat,
                    TAG.Pump,
                ],
            },
            "Packaged_Water_Source_Heat_Pump": {
                "tags": [
                    TAG.Equipment,
                    TAG.Water,
                    TAG.Source,
                    TAG.Heat,
                    TAG.Pump,
                ],
            },
        },
    },
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
            "Transfer_Fan": {
                "tags": [TAG.Equipment, TAG.Fan, TAG.Transfer],
            },
            "Cooling_Tower_Fan": {
                "tags": [TAG.Cool, TAG.Tower, TAG.Equipment, TAG.Fan],
            },
            "Exhaust_Fan": {
                "tags": [TAG.Equipment, TAG.Fan, TAG.Exhaust],
                "subclasses": {
                    "Fume_Hood": {"tags": [TAG.Equipment, TAG.Fume, TAG.Hood]},
                },
            },
            "Return_Fan": {"tags": [TAG.Equipment, TAG.Fan, TAG.Return]},
            "Booster_Fan": {"tags": [TAG.Equipment, TAG.Fan, TAG.Booster]},
            "Standby_Fan": {"tags": [TAG.Equipment, TAG.Fan, TAG.Standby]},
            "Supply_Fan": {
                "tags": [TAG.Equipment, TAG.Fan, TAG.Supply, TAG.Discharge],
                "aliases": [BRICK["Discharge_Fan"]],
            },
            "Ceiling_Fan": {"tags": [TAG.Equipment, TAG.Fan, TAG.Ceiling]},
            "Outside_Fan": {"tags": [TAG.Equipment, TAG.Fan, TAG.Outside]},
            "Relief_Fan": {"tags": [TAG.Equipment, TAG.Fan, TAG.Relief]},
            "Pressurization_Fan": {
                "tags": [TAG.Equipment, TAG.Fan, TAG.Pressurization],
            },
        },
    },
    "Economizer": {"tags": [TAG.Equipment, TAG.Economizer]},
    "Damper": {
        "tags": [TAG.Equipment, TAG.Damper],
        "subclasses": {
            "Bypass_Damper": {"tags": [TAG.Equipment, TAG.Damper, TAG.Bypass]},
            "Economizer_Damper": {"tags": [TAG.Equipment, TAG.Damper, TAG.Economizer]},
            "Exhaust_Damper": {"tags": [TAG.Equipment, TAG.Damper, TAG.Exhaust]},
            "Isolation_Damper": {"tags": [TAG.Equipment, TAG.Damper, TAG.Isolation]},
            "Outside_Damper": {"tags": [TAG.Equipment, TAG.Damper, TAG.Outside]},
            "Return_Damper": {"tags": [TAG.Equipment, TAG.Damper, TAG.Return]},
            "Mixed_Damper": {"tags": [TAG.Equipment, TAG.Damper, TAG.Mixed]},
            "Relief_Damper": {"tags": [TAG.Equipment, TAG.Damper, TAG.Relief]},
            "Zone_Damper": {"tags": [TAG.Equipment, TAG.Damper, TAG.Zone]},
        },
    },
    "Condensing_Unit": {
        "tags": [TAG.Equipment, TAG.Condenser, TAG.Condensing, TAG.Unit],
        "subclasses": {
            "Cooling_Only_Condensing_Unit": {
                "tags": [
                    TAG.Equipment,
                    TAG.Condenser,
                    TAG.Condensing,
                    TAG.Unit,
                    TAG.Cooling,
                ],
                "subclasses": {
                    "Cooling_Only_Air_Source_Condensing_Unit": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Water,
                            TAG.Source,
                            TAG.Condenser,
                            TAG.Condensing,
                            TAG.Unit,
                            TAG.Cooling,
                        ],
                    },
                    "Cooling_Only_Ground_Source_Condensing_Unit": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Ground,
                            TAG.Source,
                            TAG.Condenser,
                            TAG.Condensing,
                            TAG.Unit,
                            TAG.Cooling,
                        ],
                    },
                    "Cooling_Only_Water_Source_Condensing_Unit": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Water,
                            TAG.Source,
                            TAG.Condenser,
                            TAG.Condensing,
                            TAG.Unit,
                            TAG.Cooling,
                        ],
                    },
                },
            },
            "Heat_Pump_Condensing_Unit": {
                "tags": [
                    TAG.Equipment,
                    TAG.Condenser,
                    TAG.Condensing,
                    TAG.Unit,
                    TAG.Cooling,
                    TAG.Heating,
                ],
                "subclasses": {
                    "Heat_Pump_Air_Source_Condensing_Unit": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Air,
                            TAG.Source,
                            TAG.Heat,
                            TAG.Pump,
                        ],
                    },
                    "Heat_Pump_Ground_Source_Condensing_Unit": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Ground,
                            TAG.Source,
                            TAG.Heat,
                            TAG.Pump,
                        ],
                    },
                    "Heat_Pump_Water_Source_Condensing_Unit": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Water,
                            TAG.Source,
                            TAG.Heat,
                            TAG.Pump,
                        ],
                    },
                },
            },
            "Heat_Recovery_Condensing_Unit": {
                "tags": [
                    TAG.Equipment,
                    TAG.Condenser,
                    TAG.Condensing,
                    TAG.Unit,
                    TAG.Cooling,
                    TAG.Heating,
                    TAG.Recovery,
                ],
                "subclasses": {
                    "Heat_Recovery_Water_Source_Condensing_Unit": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Condenser,
                            TAG.Condensing,
                            TAG.Unit,
                            TAG.Cooling,
                            TAG.Heating,
                            TAG.Recovery,
                            TAG.Water,
                            TAG.Source,
                        ]
                    },
                    "Heat_Recovery_Air_Source_Condensing_Unit": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Condenser,
                            TAG.Condensing,
                            TAG.Unit,
                            TAG.Cooling,
                            TAG.Heating,
                            TAG.Recovery,
                            TAG.Water,
                            TAG.Source,
                        ]
                    },
                },
            },
        },
    },
    "Computer_Room_Air_Conditioning": {
        "tags": [
            TAG.Equipment,
            TAG.Computer,
            TAG.Room,
            TAG.Air,
            TAG.Conditioning,
            TAG.CRAC,
        ],
        "aliases": [BRICK["CRAC"]],
        "subclasses": {
            "Standby_CRAC": {"tags": [TAG.Equipment, TAG.CRAC, TAG.Standby]},
        },
    },
    "Computer_Room_Air_Handler": {
        "tags": [TAG.Equipment, TAG.Computer, TAG.Room, TAG.Air, TAG.Handler, TAG.CRAH],
        "aliases": [BRICK["CRAH"]],
    },
    "Compressor": {"tags": [TAG.Equipment, TAG.Compressor]},
    "Cooling_Tower": {"tags": [TAG.Equipment, TAG.Cool, TAG.Tower]},
    "Chiller": {
        "tags": [TAG.Equipment, TAG.Chiller],
        "subclasses": {
            "Absorption_Chiller": {
                "tags": [TAG.Equipment, TAG.Chiller, TAG.Absorption],
            },
            "Centrifugal_Chiller": {
                "tags": [TAG.Equipment, TAG.Chiller, TAG.Centrifugal],
            },
            "Water_Cooled_Chiller": {
                "tags": [
                    TAG.Equipment,
                    TAG.Water,
                    TAG.Cooled,
                    TAG.Chiller,
                ],
            },
            "Air_Cooled_Chiller": {
                "tags": [
                    TAG.Equipment,
                    TAG.Water,
                    TAG.Cooled,
                    TAG.Chiller,
                ],
            },
        },
    },
    "Humidifier": {"tags": [TAG.Equipment, TAG.Humidifier]},
    "Boiler": {
        "tags": [TAG.Equipment, TAG.Boiler],
        "subclasses": {
            "Electric_Boiler": {
                "tags": [
                    TAG.Equipment,
                    TAG.Electric,
                    TAG.Boiler,
                ],
            },
            "Natural_Gas_Boiler": {
                "tags": [
                    TAG.Equipment,
                    TAG.Natural,
                    TAG.Gas,
                    TAG.Boiler,
                ],
                "subclasses": {
                    "Condensing_Natural_Gas_Boiler": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Condensing,
                            TAG.Natural,
                            TAG.Gas,
                            TAG.Boiler,
                        ],
                    },
                    "Noncondensing_Natural_Gas_Boiler": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Noncondensing,
                            TAG.Natural,
                            TAG.Gas,
                            TAG.Boiler,
                        ],
                    },
                },
            },
        },
        "parents": [BRICK.Water_Heater],
    },
    "Refrigerant_Metering_Device": {
        "tags": [TAG.Fluid, TAG.Throttling, TAG.Device],
        "subclasses": {
            "Thermal_Expansion_Valve": {
                "tags": [
                    TAG.Refrigerant,
                    TAG.Modulating,
                    TAG.Metering,
                    TAG.Gas,
                    TAG.Liquid,
                    TAG.Expansion,
                    TAG.Valve,
                ]
            },
            "Electronic_Expansion_Valve": {
                "tags": [
                    TAG.Refrigerant,
                    TAG.Modulating,
                    TAG.Metering,
                    TAG.Gas,
                    TAG.Liquid,
                    TAG.Expansion,
                    TAG.Valve,
                ]
            },
            "Capillary_Tube_Metering_Device": {
                "tags": [TAG.Refrigerant, TAG.Gas, TAG.Fixed, TAG.Liquid, TAG.Metering]
            },
        },
    },
    "Air_Handling_Unit": {
        "tags": [TAG.Equipment, TAG.Air, TAG.Handling, TAG.Handler, TAG.Unit, TAG.AHU],
        "aliases": [
            BRICK["AHU"],
            BRICK["Air_Handler_Unit"],  # here for historical purposes
        ],
        "subclasses": {
            "Dedicated_Outdoor_Air_System_Unit": {
                "tags": [
                    TAG.Equipment,
                    TAG.Dedicated,
                    TAG.Outdoor,
                    TAG.Air,
                    TAG.System,
                    TAG.DOAS,
                ],
                "aliases": [BRICK["DOAS"]],
            },
            "Makeup_Air_Unit": {
                "tags": [TAG.Equipment, TAG.Makeup, TAG.Air, TAG.Unit, TAG.MAU],
                "aliases": [BRICK["MAU"]],
            },
            "Rooftop_Unit": {
                "tags": [TAG.Equipment, TAG.Rooftop, TAG.AHU, TAG.RTU],
                "aliases": [BRICK["RTU"]],
            },
            "Dual_Duct_Air_Handling_Unit": {
                "tags": [TAG.Equipment, TAG.AHU, TAG.Dual, TAG.DDAHU],
                "aliases": [BRICK["DDAHU"]],
            },
            "Pre-Cooling_Air_Unit": {
                "tags": [TAG.Equipment, TAG.PAU],
                "aliases": [BRICK["PAU"]],
            },
        },
    },
    "Air_Plenum": {
        "tags": [
            TAG.Equipment,
            TAG.Air,
            TAG.Plenum,
        ],
        "subclasses": {
            "Return_Air_Plenum": {
                "tags": [TAG.Equipment, TAG.Return, TAG.Air, TAG.Plenum]
            },
            "Supply_Air_Plenum": {
                "tags": [TAG.Equipment, TAG.Supply, TAG.Discharge, TAG.Air, TAG.Plenum],
                "aliases": [BRICK["Discharge_Air_Plenum"]],
                "subclasses": {
                    "Underfloor_Air_Plenum": {
                        "tags": [
                            TAG.Equipment,
                            TAG.Underfloor,
                            TAG.Air,
                            TAG.Plenum,
                        ]
                    },
                },
            },
        },
    },
    "Wall_Air_Conditioner": {
        "tags": [TAG.Equipment, TAG.Wall, TAG.Air, TAG.Conditioner]
    },
}

valve_subclasses = {
    "Valve": {
        "tags": [TAG.Valve, TAG.Equipment],
        "subclasses": {
            "Natural_Gas_Seismic_Shutoff_Valve": {
                "tags": [
                    TAG.Equipment,
                    TAG.Valve,
                    TAG.Natural,
                    TAG.Gas,
                    TAG.Seismic,
                    TAG.Shutoff,
                ],
            },
            "Check_Valve": {
                "tags": [TAG.Check, TAG.Valve],
                "subclasses": {
                    "Backflow_Preventer_Valve": {
                        "tags": [TAG.Backflow, TAG.Preventer, TAG.Valve]
                    }
                },
            },
            "Pressure_Reducing_Valve": {
                "tags": [TAG.Pressure, TAG.Reducing, TAG.Valve],
                "subclasses": {
                    "Water_Pressure_Reducing_Valve": {
                        "tags": [TAG.Water, TAG.Pressure, TAG.Reducing, TAG.Valve],
                        "parents": [BRICK["Water_Valve"]],
                    },
                    "Steam_Pressure_Reducing_Valve": {
                        "tags": [TAG.Steam, TAG.Pressure, TAG.Reducing, TAG.Valve],
                        "parents": [BRICK["Steam_Valve"]],
                    },
                },
            },
            "Pressure_Regulator_Valve": {
                "tags": [TAG.Pressure, TAG.Regulator, TAG.Valve],
                "subclasses": {
                    "Gas_Pressure_Regulator_Valve": {
                        "tags": [TAG.Gas, TAG.Pressure, TAG.Regulator, TAG.Valve],
                        "parents": [BRICK["Gas_Valve"]],
                    }
                },
            },
            "Pressure_Relief_Valve": {
                "tags": [TAG.Pressure, TAG.Relief, TAG.Valve],
                "subclasses": {
                    "Steam_Pressure_Relief_Valve": {
                        "tags": [TAG.Steam, TAG.Pressure, TAG.Relief, TAG.Valve],
                        "parents": [BRICK["Steam_Valve"]],
                    },
                    "Water_Pressure_Relief_Valve": {
                        "tags": [TAG.Steam, TAG.Pressure, TAG.Relief, TAG.Valve],
                        "parents": [BRICK["Water_Valve"]],
                    },
                },
            },
            "Mixing_Valve": {
                "tags": [TAG.Mixing, TAG.Valve],
                "subclasses": {
                    "Thermostatic_Mixing_Valve": {
                        "tags": [
                            TAG.Mixed,
                            TAG.Valve,
                            TAG.Thermal,
                            TAG.Equipment,
                        ],
                    },
                    "Electronic_Mixing_Valve": {
                        "tags": [
                            TAG.Mixed,
                            TAG.Valve,
                            TAG.Electronic,
                            TAG.Equipment,
                        ],
                    },
                },
            },
            "Water_Valve": {
                "tags": [TAG.Valve, TAG.Water, TAG.Equipment],
                "subclasses": {
                    "Chilled_Water_Valve": {
                        "tags": [TAG.Chilled, TAG.Valve, TAG.Water, TAG.Equipment],
                        "parents": [BRICK.HVAC_Valve],
                    },
                    "Condenser_Water_Valve": {
                        "tags": [TAG.Condenser, TAG.Valve, TAG.Water, TAG.Equipment],
                        "parents": [BRICK.HVAC_Valve],
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
                        ],
                        "parents": [BRICK.HVAC_Valve],
                    },
                },
            },
            "Gas_Valve": {"tags": [TAG.Gas, TAG.Valve, TAG.Equipment]},
            "Steam_Valve": {"tags": [TAG.Steam, TAG.Valve, TAG.Equipment]},
            "Refrigerant_Valve": {
                "tags": [TAG.Refrigerant, TAG.Valve, TAG.Gas, TAG.Liquid],
                "subclasses": {
                    "Reversing_Valve": {
                        "tags": [
                            TAG.Refrigerant,
                            TAG.Valve,
                            TAG.Gas,
                            TAG.Liquid,
                            TAG.Reversing,
                        ]
                    },
                },
            },
        },
    }
}

"""
HVAC-specific Valve subclasses
"""
hvac_valve_subclasses = {
    "Heating_Valve": {
        "parents": [BRICK.Valve],
        "tags": [TAG.Valve, TAG.Heat, TAG.Equipment],
        "subclasses": {
            "Reheat_Valve": {"tags": [TAG.Valve, TAG.Reheat, TAG.Heat, TAG.Equipment]},
            "Return_Heating_Valve": {
                "tags": [TAG.Valve, TAG.Return, TAG.Heat, TAG.Equipment],
            },
        },
    },
    "Cooling_Valve": {
        "parents": [BRICK.Valve],
        "tags": [TAG.Valve, TAG.Cool, TAG.Equipment]
    },
    "Isolation_Valve": {
        "tags": [TAG.Isolation, TAG.Valve, TAG.Equipment],
        "parents": [BRICK.Valve],
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
    "Steam_Valve": {
        "tags": [TAG.Steam, TAG.Valve, TAG.Equipment],
        "parents": [BRICK.Valve],
    },
    "Bypass_Valve": {
        "parents": [BRICK.Valve],
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
            "Network_Video_Recorder": {
                "tags": [
                    TAG.Equipment,
                    TAG.Security,
                    TAG.Surveillance,
                    TAG.Network,
                    TAG.Video,
                    TAG.Recorder,
                    TAG.NVR,
                ],
                "aliases": [BRICK["NVR"]],
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
        "aliases": [BRICK["AED"]],
        "tags": [TAG.Equipment, TAG.Safety, TAG.Defibrillator, TAG.AED],
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
