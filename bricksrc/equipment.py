from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.collection import Collection
from rdflib.extras.infixowl import Restriction

from .namespaces import *

"""
Set up subclasses of the equipment superclass
"""
equipment_subclasses = {
    "HVAC": {},
    "Heating_Ventilation_Air_Conditioning_System": {
        OWL.equivalentClass: "HVAC",
    },
    "Weather": {
        "tags": [TAG.Weather],
    },
    "Water_System": {
        "subclasses": {
            "Chilled_Water_System": {
                "tags": [TAG.Water, TAG.Chilled, TAG.Equipment],
            },
            "Hot_Water_System": {
                "tags": [TAG.Water, TAG.Hot, TAG.Equipment],
            },
        }
    },
    "Steam_System": {
        "tags": [TAG.Steam, TAG.Equipment],
    },
    "Solar_Panel": {
        "tags": [TAG.Solar, TAG.Equipment],
    },
    "Shading_System": {
        "tags": [TAG.Shade, TAG.Equipment],
    },
    "Power_System": {
        "tags": [TAG.Power, TAG.Equipment],
    },
    "PlugStrip": {
        "tags": [TAG.Plugstrip, TAG.Equipment],
    },
    "Meter": {
        "tags": [TAG.Meter, TAG.Equipment],
        "subclasses": {
            "Building_Meter": {
                "tags": [TAG.Meter, TAG.Equipment, TAG.Building],
            },
        },
    },
    "Lighting_System": {
        "tags": [TAG.Lighting, TAG.Equipment],
        "subclasses": {
            "Lighting": {
                "subclasses": {
                    "Luminaire": {},
                    "Luminaire_Driver": {},
                },
            },
            "Interface": {
                "subclasses": {
                    "Switch": {
                        "subclasses": {
                            "Dimmer": {},
                        },
                    },
                    "Touchpanel": {},
                },
            },
        },
    },
    "Furniture": {
    },
    "Fire_Safety_System": {
    },
    "Energy_Storage": {
    },
    "Elevator": {
    },
}


"""
Define classes of HVAC equipment
"""
hvac_subclasses = {
    "Variable_Frequency_Drive": {
        OWL.equivalentClass: "VFD",
        SKOS.definition: Literal("Electronic device that varies its output frequency to vary the rotating speed of a motor, given a fixed input frequency. Used with fans or pumps to vary the flow in the system as a function of a maintained pressure."),
    },
    "Valve": {
        "tags": [TAG.Valve, TAG.Equipment]
        # subclasses defined in 'valve_subclasses'
    },
    "VFD": {
        "subclasses": {
            "Heat_Wheel_VFD": {},
            "Preheat_Valve_VFD": {},
        },
    },
    "Thermostat": {
        SKOS.definition: Literal("An automatic control device used to maintain temperature at a fixed or adjustable setpoint."),
    },
    "Terminal_Unit": {
        SKOS.definition: Literal("A device that regulates the volumetric flow rate and/or the temperature of the controlled medium."),
        "subclasses": {
            "Fan_Coil_Unit": {
                OWL.equivalentClass: "FCU",
            },
            "FCU": {},
            "Variable_Air_Volume_Box": {
                OWL.equivalentClass: "VAV",
                "subclasses": {
                    "Variable_Air_Volume_Box_With_Reheat": {
                        OWL.equivalentClass: "RVAV",
                    },
                    "RVAV": {},
                },
            },
            "VAV": {},
        },
    },
    "Space_Heater": {
        SKOS.definition: Literal("A heater used to warm the air in an enclosed area, such as a room or office"),
    },
    "Pump": {
        SKOS.definition: Literal("Machine for imparting energy to a fluid, causing it to do work, drawing a fluid into itself through an entrance port, and forcing the fluid out through an exhaust port."),
        "subclasses": {
            "Water_Pump": {
                "subclasses": {
                    "Chilled_Water_Pump": {},
                    "Condenser_Water_Pump": {},
                    "Hot_Water_Pump": {},
                },
            },
        },
    },
    "Heat_Exchanger": {
        OWL.equivalentClass: "HX",
        "subclasses": {
            "Evaporative_Heat_Exchanger": {},
            "Condenser_Heat_Exchanger": {},
        },
    },
    "HX": {},
    "Fume_Hood": {
        SKOS.definition: Literal("A fume-collection device mounted over a work space, table, or shelf and serving to conduct unwanted gases away from the area enclosed."),
    },
    "Filter": {
        SKOS.definition: Literal("Device to remove gases from a mixture of gases"),
        "subclasses": {
            "Mixed_Air_Filter": {},
        },
    },
    "Fan": {
        SKOS.definition: Literal("Any device with two or more blades or vanes attached to a rotating shaft used to produce an airflow for the purpose of comfort, ventilation, exhaust, heating, cooling, or any other gaseous transport."),
        "tags": [TAG.Equipment, TAG.Fan],
        "subclasses": {
            "Cooling_Tower_Fan": {
            },
            "Exhaust_Fan": {
                "tags": [TAG.Equipment, TAG.Fan, TAG.Exhaust],
            },
            "Return_Fan": {
                "tags": [TAG.Equipment, TAG.Fan, TAG.Return],
            },
            "Standby_Fan": {
                "tags": [TAG.Equipment, TAG.Fan, TAG.Standby],
            },
            "Discharge_Fan": {
                "tags": [TAG.Equipment, TAG.Fan, TAG.Discharge],
            },
            "Supply_Fan": {
                "tags": [TAG.Equipment, TAG.Fan, TAG.Supply],
                "subclasses": {
                    "Booster_Fan": {
                        "tags": [TAG.Equipment, TAG.Fan, TAG.Booster],
                    },
                },
            },
        },
    },
    "Economizer": {
        SKOS.definition: Literal("Device that, on proper variable sensing, initiates control signals or actions to conserve energy. A control system that reduces the mechanical heating and cooling requirement."),
    },
    "Damper": {
        SKOS.definition: Literal("Element inserted into an air-distribution system or element of an air-distribution system permitting modification of the air resistance of the system and consequently changing the airflow rate or shutting off the airflow."),
        "tags": [TAG.Equipment, TAG.Damper],
        "subclasses": {
            "Economizer_Damper": {
                "tags": [TAG.Equipment, TAG.Damper, TAG.Economizer],
            },
            "Exhaust_Damper": {
                "tags": [TAG.Equipment, TAG.Damper, TAG.Exhaust],
            },
            "Outside_Damper": {
                "tags": [TAG.Equipment, TAG.Damper, TAG.Outside],
            },
            "Return_Damper": {
                "tags": [TAG.Equipment, TAG.Damper, TAG.Return],
            },
        },
    },
    "Condenser": {
        SKOS.definition: Literal("A heat exchanger in which the primary heat transfer vapor changes its state to a liquid phase."),
    },
    "Computer_Room_Air_Conditioning": {
        SKOS.definition: Literal("A device that monitors and maintains the temperature, air distribution and humidity in a network room or data center. "),
        OWL.equivalentClass: "CRAC",
    },
    "CRAC": {
        OWL.equivalentClass: "Computer_Room_Air_Conditioning",
    },
    "Compressor": {
        SKOS.definition: Literal("(1) device for mechanically increasing the pressure of a gas. (2) often described as being either open, hermetic, or semihermetic to describe how the compressor and motor drive is situated in relation to the gas or vapor being compressed. Types include centrifugal, axial flow, reciprocating, rotary screw, rotary vane, scroll, or diaphragm. 1. device for mechanically increasing the pressure of a gas. 2. specific machine, with or without accessories, for compressing refrigerant vapor."),
    },
    "Coil": {
        SKOS.definition: Literal("Exchanger that transfers heat from an exhaust airstream to a separated supply airstream."),
                "tags": [TAG.Equipment, TAG.Coil],
        "subclasses": {
            "Cooling_Coil": {
                "tags": [TAG.Equipment, TAG.Coil, TAG.Cool],
            },
            "Heating_Coil": {
                "tags": [TAG.Equipment, TAG.Coil, TAG.Heat],
            },
        },
    },
    "Chiller": {
        "subclasses": {
            "Absorption_Chiller": {},
            "Centrifugal_Chiller": {},
        },
    },
    "Boiler": {
        SKOS.definition: Literal("A closed, pressure vessel that uses fuel or electricity for heating water or other fluids to supply steam or hot water for heating, humidification, or other applications."),
    },
    "Air_Handler_Unit": {
        SKOS.definition: Literal("Assembly consisting of sections containing a fan or fans and other necessary equipment to perform one or more of the following functions: circulating, filtration, heating, cooling, heat recovery, humidifying, dehumidifying, and mixing of air. Is usually connected to an air-distribution system."),
        OWL.equivalentClass: "AHU",
    },
    "AHU": {
        "tags": [ TAG.Equipment, TAG.AHU],
        "subclasses": {
            "Rooftop_Unit": {
                OWL.equivalentClass: "RTU",
                "tags": [TAG.Equipment, TAG.Rooftop, TAG.AHU],
            },
            "RTU": {},
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
            "Reheat_Valve": {
                "tags": [TAG.Valve, TAG.Reheat, TAG.Heat, TAG.Equipment],
            },
            "Domestic_Hot_Water_Valve": {
                "tags": [TAG.Domestic, TAG.Water, TAG.Hot, TAG.Valve, TAG.Heat, TAG.Equipment],
                "parents": [BRICK.Hot_Water_System, BRICK.Water_Valve],
            },
            "Preheat_Hot_Water_Valve": {
                "tags": [TAG.Preheat, TAG.Water, TAG.Hot, TAG.Valve, TAG.Heat, TAG.Equipment],
                "parents": [BRICK.Hot_Water_System, BRICK.Water_Valve],
            },
        },
    },
    "Water_Valve": {
        "tags": [TAG.Valve, TAG.Water, TAG.Equipment],
        "subclasses": {
            "Chilled_Water_Valve": {
                "tags": [TAG.Chilled, TAG.Valve, TAG.Water, TAG.Equipment],
                "parents": [BRICK.Chilled_Water_System],
            },
        },
    },
    "Isolation_Valve": {
        "tags": [TAG.Isolation, TAG.Valve, TAG.Equipment],
    },
}
