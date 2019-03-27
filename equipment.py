from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.collection import Collection
from rdflib.extras.infixowl import Restriction

BRICK = Namespace("https://brickschema.org/schema/1.0.3/Brick#")
BRICKTAG = Namespace("https://brickschema.org/schema/1.0.3/BrickTag#")
BLDG = Namespace("https://brickschema.org/schema/1.0.3/ExampleBuilding#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
A = RDF.type

"""
Set up subclasses of the equipment superclass
"""
equipment_subclasses = {
    "HVAC": {
        OWL.equivalentClass: "Heating_Ventilation_Air_Conditioning_System",
    },
    "Heating_Ventilation_Air_Conditioning_System": {
        OWL.equivalentClass: "HVAC",
    },
    "Weather": {
    },
    "Water_System": {
    },
    "Steam_System": {
    },
    "Solar_Panel": {
    },
    "Shading_System": {
    },
    "Power_System": {
    },
    "PlugStrip": {
    },
    "Meter": {
    },
    "Lighting_System": {
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
    "Valve": {},
    "VFD": {
        OWL.equivalentClass: "VFD",
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
            "Variable_Air_Volume_Box": {
                OWL.equivalentClass: "VAV",
                "subclasses": {
                    "Variable_Air_Volume_Box_With_Reheat": {
                        OWL.equivalentClass: "RVAV",
                    },
                },
            },
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
        "subclasses": {
            "Cooling_Tower_Fan": {},
            "Exhaust_Fan": {},
            "Return_Fan": {},
            "Standby_Fan": {},
            "Supply_Fan": {
                "subclasses": {
                    "Booster_Fan": {}
                },
            },
        },
    },
    "Economizer": {
        SKOS.definition: Literal("Device that, on proper variable sensing, initiates control signals or actions to conserve energy. A control system that reduces the mechanical heating and cooling requirement."),
    },
    "Damper": {
        SKOS.definition: Literal("Element inserted into an air-distribution system or element of an air-distribution system permitting modification of the air resistance of the system and consequently changing the airflow rate or shutting off the airflow."),
        "subclasses": {
            "Economizer_Damper": {},
            "Exhaust_Damper": {},
            "Outside_Damper": {},
            "Return_Damper": {},
        },
    },
    "Condensor": {
        SKOS.definition: Literal("A heat exchanger in which the primary heat transfer vapor changes its state to a liquid phase."),
        OWL.equivalentClass: "Condenser",
    },
    "Condenser": {
        OWL.equivalentClass: "Condensor",
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
        "subclasses": {
            "Cooling_Coil": {},
            "Heating_Coil": {},
        },
    },
    "CWS": {
        OWL.equivalentClass: "Chilled_Water_System",
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
        OWL.equivalentClass: "Air_Handler_Unit",
        "subclasses": {
            "Rooftop_Unit": {
                OWL.equivalentClass: "RTU",
            },
        },
    },
}

"""
Valve subclasses
"""
valve_subclasses = {
    "Heating_Valve": {
        "subclasses": {
            "Reheat_Valve": {},
            "Domestic_Hot_Water_Valve": {},
            "Preheat_Hot_Water_Valve": {},
        },
        # OWL.equivalentClass: Restriction(BRICK.hasTag, graph=G, allValuesFrom=BRICK.Valve)
    },
    "Chilled_Water_Valve": {},
    "Isolation_Valve": {},
}
