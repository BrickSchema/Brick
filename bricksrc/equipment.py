from rdflib import Literal
from .namespaces import TAG, OWL, SKOS, BRICK

"""
Set up subclasses of the equipment superclass
"""
equipment_subclasses = {
    "HVAC": {
        OWL.equivalentClass: BRICK["Heating_Ventilation_Air_Conditioning_System"],
        "tags": [TAG.Heat, TAG.Ventilation, TAG.Air, TAG.Conditioning, TAG.System],
    },
    "Heating_Ventilation_Air_Conditioning_System": {
        OWL.equivalentClass: BRICK["HVAC"],
        "tags": [TAG.HVAC],
    },
    "Weather": {"tags": [TAG.Weather]},
    "Electrical_System": {
        "tags": [TAG.Electrical, TAG.System],
        "subclasses": {
            "Emergency_Power_Off_System": {
                "tags": [TAG.Emergency, TAG.Power, TAG.Off, TAG.Equipment],
            },
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
        },
    },
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
            "Water_Meter": {
                "tags": [TAG.Meter, TAG.Equipment, TAG.Water],
                "parents": [BRICK.Water_System],
                "subclasses": {
                    "Building_Water_Meter": {
                        "tags": [TAG.Building, TAG.Water, TAG.Meter, TAG.Equipment],
                        "parents": [BRICK.Building_Meter],
                    },
                    "Chilled_Water_Meter": {
                        "tags": [TAG.Meter, TAG.Equipment, TAG.Water, TAG.Chilled],
                        "parents": [BRICK.Chilled_Water_System],
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
                        "parents": [BRICK.Chilled_Water_System],
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
    "Water_System": {
        "tags": [TAG.Water, TAG.Equipment],
        "subclasses": {
            "Chilled_Water_System": {
                OWL.equivalentClass: BRICK["CWS"],
                "tags": [TAG.Water, TAG.Chilled, TAG.Equipment],
            },
            "Hot_Water_System": {
                OWL.equivalentClass: BRICK["HWS"],
                "tags": [TAG.Water, TAG.Hot, TAG.Equipment],
                "subclasses": {
                    "Domestic_Hot_Water_System": {
                        "tags": [TAG.Domestic, TAG.Water, TAG.Hot, TAG.Equipment],
                    },
                },
            },
            "CWS": {
                OWL.equivalentClass: BRICK["Chilled_Water_System"],
                "tags": [TAG.CWS],
            },
            "HWS": {OWL.equivalentClass: BRICK["Hot_Water_System"], "tags": [TAG.HWS]},
        },
    },
    "Steam_System": {"tags": [TAG.Steam, TAG.Equipment]},
    "Solar_Panel": {"tags": [TAG.Solar, TAG.Equipment]},
    "Shading_System": {
        "tags": [TAG.Shade, TAG.Equipment],
        "subclasses": {"Louver": {"tags": [TAG.Shade, TAG.Equipment, TAG.Louver]}},
    },
    "Lighting_System": {
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
    "Fire_Safety_System": {
        "tags": [TAG.Equipment, TAG.Fire, TAG.Safety, TAG.System],
        "subclasses": {
            "Fire_Control_Panel": {
                "tags": [TAG.Equipment, TAG.Fire, TAG.Safety, TAG.Panel],
                OWL.equivalentClass: BRICK["FCP"],
            },
            "FCP": {"tags": [TAG.FCP, TAG.Equipment]},
        },
    },
    "Elevator": {"tags": [TAG.Elevator, TAG.Equipment]},
    "Security_Equipment": {"tags": [TAG.Security, TAG.Equipment]},
    "Camera": {"tags": [TAG.Camera, TAG.Equipment]},
}


"""
Define classes of HVAC equipment
"""
hvac_subclasses = {
    "Variable_Frequency_Drive": {
        "tags": [TAG.Equipment, TAG.Variable, TAG.Frequency, TAG.Drive],
        OWL.equivalentClass: BRICK["VFD"],
        SKOS.definition: Literal(
            "Electronic device that varies its output frequency to vary the rotating speed of a motor, given a fixed input frequency. Used with fans or pumps to vary the flow in the system as a function of a maintained pressure."
        ),
    },
    "Valve": {
        "tags": [TAG.Valve, TAG.Equipment]
        # subclasses defined in 'valve_subclasses'
    },
    "VFD": {
        "tags": [TAG.Equipment, TAG.VFD],
        "subclasses": {
            "Heat_Wheel_VFD": {"tags": [TAG.Equipment, TAG.Heat, TAG.Wheel, TAG.VFD]},
            "Preheat_Valve_VFD": {"tags": [TAG.Equipment, TAG.Preheat, TAG.VFD]},
        },
    },
    "Thermostat": {
        "tags": [TAG.Equipment, TAG.Thermostat],
        SKOS.definition: Literal(
            "An automatic control device used to maintain temperature at a fixed or adjustable setpoint."
        ),
    },
    "Terminal_Unit": {
        "tags": [TAG.Equipment, TAG.Terminal, TAG.Unit],
        SKOS.definition: Literal(
            "A device that regulates the volumetric flow rate and/or the temperature of the controlled medium."
        ),
        "subclasses": {
            "Fan_Coil_Unit": {
                "tags": [TAG.Equipment, TAG.Fan, TAG.Coil, TAG.Unit],
                OWL.equivalentClass: BRICK["FCU"],
            },
            "FCU": {"tags": [TAG.FCU]},
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
        },
    },
    "Space_Heater": {
        "tags": [TAG.Equipment, TAG.Space, TAG.Heater],
        SKOS.definition: Literal(
            "A heater used to warm the air in an enclosed area, such as a room or office"
        ),
    },
    "Pump": {
        "tags": [TAG.Equipment, TAG.Pump],
        SKOS.definition: Literal(
            "Machine for imparting energy to a fluid, causing it to do work, drawing a fluid into itself through an entrance port, and forcing the fluid out through an exhaust port."
        ),
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
        },
    },
    "HX": {"tags": [TAG.Equipment, TAG.HX]},
    "Fume_Hood": {
        "tags": [TAG.Equipment, TAG.Fume, TAG.Hood],
        SKOS.definition: Literal(
            "A fume-collection device mounted over a work space, table, or shelf and serving to conduct unwanted gases away from the area enclosed."
        ),
    },
    "Filter": {
        "tags": [TAG.Equipment, TAG.Filter],
        SKOS.definition: Literal("Device to remove gases from a mixture of gases"),
        "subclasses": {
            "Mixed_Air_Filter": {
                "tags": [TAG.Equipment, TAG.Mixed, TAG.Air, TAG.Filter],
            },
        },
    },
    "Fan": {
        SKOS.definition: Literal(
            "Any device with two or more blades or vanes attached to a rotating shaft used to produce an airflow for the purpose of comfort, ventilation, exhaust, heating, cooling, or any other gaseous transport."
        ),
        "tags": [TAG.Equipment, TAG.Fan],
        "subclasses": {
            "Cooling_Tower_Fan": {
                "tags": [TAG.Cool, TAG.Tower, TAG.Equipment, TAG.Fan],
            },
            "Exhaust_Fan": {"tags": [TAG.Equipment, TAG.Fan, TAG.Exhaust]},
            "Return_Fan": {"tags": [TAG.Equipment, TAG.Fan, TAG.Return]},
            "Standby_Fan": {"tags": [TAG.Equipment, TAG.Fan, TAG.Standby]},
            "Discharge_Fan": {"tags": [TAG.Equipment, TAG.Fan, TAG.Discharge]},
            "Supply_Fan": {
                "tags": [TAG.Equipment, TAG.Fan, TAG.Supply],
                "subclasses": {
                    "Booster_Fan": {"tags": [TAG.Equipment, TAG.Fan, TAG.Booster]},
                },
            },
        },
    },
    "Economizer": {
        "tags": [TAG.Equipment, TAG.Economizer],
        SKOS.definition: Literal(
            "Device that, on proper variable sensing, initiates control signals or actions to conserve energy. A control system that reduces the mechanical heating and cooling requirement."
        ),
    },
    "Damper": {
        SKOS.definition: Literal(
            "Element inserted into an air-distribution system or element of an air-distribution system permitting modification of the air resistance of the system and consequently changing the airflow rate or shutting off the airflow."
        ),
        "tags": [TAG.Equipment, TAG.Damper],
        "subclasses": {
            "Economizer_Damper": {"tags": [TAG.Equipment, TAG.Damper, TAG.Economizer]},
            "Exhaust_Damper": {"tags": [TAG.Equipment, TAG.Damper, TAG.Exhaust]},
            "Outside_Damper": {"tags": [TAG.Equipment, TAG.Damper, TAG.Outside]},
            "Return_Damper": {"tags": [TAG.Equipment, TAG.Damper, TAG.Return]},
        },
    },
    "Condenser": {
        "tags": [TAG.Equipment, TAG.Condenser],
        SKOS.definition: Literal(
            "A heat exchanger in which the primary heat transfer vapor changes its state to a liquid phase."
        ),
    },
    "Computer_Room_Air_Conditioning": {
        "tags": [TAG.Equipment, TAG.Computer, TAG.Room, TAG.Air, TAG.Conditioning],
        SKOS.definition: Literal(
            "A device that monitors and maintains the temperature, air distribution and humidity in a network room or data center. "
        ),
        OWL.equivalentClass: BRICK["CRAC"],
    },
    "CRAC": {
        "tags": [TAG.Equipment, TAG.CRAC],
        OWL.equivalentClass: BRICK["Computer_Room_Air_Conditioning"],
        "subclasses": {
            "Standby_CRAC": {"tags": [TAG.Equipment, TAG.CRAC, TAG.Standby]},
        },
    },
    "Compressor": {
        "tags": [TAG.Equipment, TAG.Compressor],
        SKOS.definition: Literal(
            "(1) device for mechanically increasing the pressure of a gas. (2) often described as being either open, hermetic, or semihermetic to describe how the compressor and motor drive is situated in relation to the gas or vapor being compressed. Types include centrifugal, axial flow, reciprocating, rotary screw, rotary vane, scroll, or diaphragm. 1. device for mechanically increasing the pressure of a gas. 2. specific machine, with or without accessories, for compressing refrigerant vapor."
        ),
    },
    "Coil": {
        SKOS.definition: Literal(
            "Exchanger that transfers heat from an exhaust airstream to a separated supply airstream."
        ),
        "tags": [TAG.Equipment, TAG.Coil],
        "subclasses": {
            "Cooling_Coil": {"tags": [TAG.Equipment, TAG.Coil, TAG.Cool]},
            "Heating_Coil": {"tags": [TAG.Equipment, TAG.Coil, TAG.Heat]},
        },
    },
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
    "Boiler": {
        "tags": [TAG.Equipment, TAG.Boiler],
        SKOS.definition: Literal(
            "A closed, pressure vessel that uses fuel or electricity for heating water or other fluids to supply steam or hot water for heating, humidification, or other applications."
        ),
    },
    "Air_Handler_Unit": {
        "tags": [TAG.Equipment, TAG.Air, TAG.Handler, TAG.Unit],
        SKOS.definition: Literal(
            "Assembly consisting of sections containing a fan or fans and other necessary equipment to perform one or more of the following functions: circulating, filtration, heating, cooling, heat recovery, humidifying, dehumidifying, and mixing of air. Is usually connected to an air-distribution system."
        ),
        OWL.equivalentClass: BRICK["AHU"],
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
                SKOS.definition: Literal(
                    "A valve installed on the return side of a heat exchanger"
                ),
            },
            "Domestic_Hot_Water_Valve": {
                "tags": [
                    TAG.Domestic,
                    TAG.Water,
                    TAG.Hot,
                    TAG.Valve,
                    TAG.Heat,
                    TAG.Equipment,
                ],
                "parents": [BRICK.Domestic_Hot_Water_System, BRICK.Water_Valve],
            },
            "Preheat_Hot_Water_Valve": {
                "tags": [
                    TAG.Preheat,
                    TAG.Water,
                    TAG.Hot,
                    TAG.Valve,
                    TAG.Heat,
                    TAG.Equipment,
                ],
                "parents": [BRICK.Hot_Water_System, BRICK.Water_Valve],
            },
        },
    },
    "Cooling_Valve": {"tags": [TAG.Valve, TAG.Cool, TAG.Equipment]},
    "Water_Valve": {
        "tags": [TAG.Valve, TAG.Water, TAG.Equipment],
        "subclasses": {
            "Chilled_Water_Valve": {
                "tags": [TAG.Chilled, TAG.Valve, TAG.Water, TAG.Equipment],
                "parents": [BRICK.Chilled_Water_System],
            },
        },
    },
    "Isolation_Valve": {"tags": [TAG.Isolation, TAG.Valve, TAG.Equipment]},
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
                SKOS.definition: Literal(
                    "Used in physical security systems to read a credential that allows access through access points. "
                    "Usually card badge credentials for locked doors or monitored checkpoints."
                ),
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
                SKOS.definition: Literal(
                    "An optical instrument to capture still images or record moving images, which are stored on a physical or digital medium."
                ),
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
                SKOS.definition: Literal("A Network Video Recorder."),
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
                SKOS.definition: Literal("A Network Video Recorder."),
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
                SKOS.definition: Literal(
                    "A phone specifically provided for making calls to emergency services."
                ),
            },
            "Video_Intercom": {
                "tags": [TAG.Equipment, TAG.Security, TAG.Intercom, TAG.Video],
                SKOS.definition: Literal(
                    "An intercom device that has video capabilites as well as voice capabilities"
                ),
            },
        },
    },
}
