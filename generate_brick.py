from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.extras.infixowl import Restriction

BRICK = Namespace("https://brickschema.org/schema/1.0.3/Brick#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")

G = Graph()
G.bind('rdf', RDF)
G.bind('owl', OWL)
G.bind('rdfs', RDFS)
G.bind('skos', SKOS)
G.bind('brick', BRICK)

A = RDF.type

def define_subclasses(definitions, superclass):
    for subclass, properties in definitions.items():
        G.add( (BRICK[subclass], A, OWL.Class) )
        G.add( (BRICK[subclass], RDFS.subClassOf, superclass) )
        for k, v in properties.items():
            if not apply_prop(subclass, k, v):
                if isinstance(v, dict) and k == "subclasses":
                    define_subclasses(v, BRICK[subclass])

def apply_prop(prop, pred, obj):
    if isinstance(obj, Literal):
        G.add( (BRICK[prop], pred, obj) )
        return True
    elif isinstance(obj, URIRef):
        G.add( (BRICK[prop], pred, obj) )
        return True
    elif isinstance(obj, str):
        G.add( (BRICK[prop], pred, BRICK[obj]) )
        return True
    elif isinstance(obj, list):
        for l in obj:
            apply_prop(prop, pred, l)
        return True
    return False

def define_properties(definitions, superprop=None):
    for prop, properties in definitions.items():
        G.add( (BRICK[prop], A, OWL.ObjectProperty) )
        if superprop is not None:
            G.add( (BRICK[prop], RDFS.subPropertyOf, superprop) )
        for k, v in properties.items():
            if not apply_prop(prop, k, v):
                if isinstance(v, dict) and k == "subproperties":
                    define_properties(v, BRICK[prop])


"""
Declare root classes
"""
G.add( (BRICK.Equipment, A, OWL.Class) )
G.add( (BRICK.Location, A, OWL.Class) )
G.add( (BRICK.Point, A, OWL.Class) )
G.add( (BRICK.Substance, A, OWL.Class) )

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
    "WS": {
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

define_subclasses(equipment_subclasses, BRICK.Equipment)

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
    },
    "Thermostat": {
        SKOS.definition: Literal("An automatic control device used to maintain temperature at a fixed or adjustable setpoint."),
    },
    "Terminal_Unit": {
        SKOS.definition: Literal("A device that regulates the volumetric flow rate and/or the temperature of the controlled medium."),
    },
    "Space_Heater": {
        SKOS.definition: Literal("A heater used to warm the air in an enclosed area, such as a room or office"),
    },
    "Pump": {
        SKOS.definition: Literal("Machine for imparting energy to a fluid, causing it to do work, drawing a fluid into itself through an entrance port, and forcing the fluid out through an exhaust port."),
    },
    "Fume_Hood": {
        SKOS.definition: Literal("A fume-collection device mounted over a work space, table, or shelf and serving to conduct unwanted gases away from the area enclosed."),
    },
    "Filter": {
        SKOS.definition: Literal("Device to remove gases from a mixture of gases"),
    },
    "Fan": {
        SKOS.definition: Literal("Any device with two or more blades or vanes attached to a rotating shaft used to produce an airflow for the purpose of comfort, ventilation, exhaust, heating, cooling, or any other gaseous transport."),
    },
    "Economizer": {
        SKOS.definition: Literal("Device that, on proper variable sensing, initiates control signals or actions to conserve energy. A control system that reduces the mechanical heating and cooling requirement."),
    },
    "Damper": {
        SKOS.definition: Literal("Element inserted into an air-distribution system or element of an air-distribution system permitting modification of the air resistance of the system and consequently changing the airflow rate or shutting off the airflow."),
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
    },
    "CWS": {
        OWL.equivalentClass: "Chilled_Water_System",
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
    },
}

define_subclasses(hvac_subclasses, BRICK.HVAC)

"""
Valve subclasses
"""
valve_subclasses = {
    "Heating_Valve": {
        "subclasses": {
            "Reheat_Valve": {},
        },
        # OWL.equivalentClass: Restriction(BRICK.hasTag, graph=G, allValuesFrom=BRICK.Valve)
    },
    "Chilled_Water_Valve": {},
    "Isolation_Valve": {},
}

define_subclasses(valve_subclasses, BRICK.Valve)

##### Defining substances
substances = {
    "Fluid": {
        "subclasses": {
            "Gas": {
                "subclasses": {
                    "Air": {},
                    "Steam": {
                        SKOS.definition: Literal("Water in its gaseous form"),
                    },
                },
            },
            "Liquid": {
                "subclasses": {
                    "Water": {
                        SKOS.definition: Literal("Water in its liquid form"),
                    },
                },
            },
        },
    },
    "Solid": {
        "subclasses": {
            "Ice": {
                SKOS.definition: Literal("Water in its solid form"),
            },
        },
    }
}
define_subclasses(substances, BRICK.Substance)


"""
Defining properties
"""
properties = {
    "isLocationOf": {
        OWL.inverseOf: "hasLocation",
        RDFS.domain: BRICK.Location,
    },
    "hasLocation": {
        OWL.inverseOf: "isLocationOf",
        RDFS.range: BRICK.Location,
    },

    "hasInputSubstance": {
        RDFS.range: BRICK.Substance,
    },
    "hasOutputSubstance": {
        RDFS.range: BRICK.Substance,
    },

    "feeds": {
        A: [OWL.TransitiveProperty],
        OWL.inverseOf: "isFedBy",
        "subproperties": {
            "feedsAir": {
                A: [OWL.TransitiveProperty],
                SKOS.definition: Literal("Passes air"),
                # TODO: add restriction that it needs an air-based equipment on either side?
                # this is equivalent with the classes that have :
                # Restriction (onProperty=brick:hasInputSubstance, hasValue=brick:Air) AND
                # Restriction (onProperty=brick:hasOutputSubstance, hasValue=brick:Air)
            },
        },
    },
    "isFedBy": {
        A: [OWL.TransitiveProperty],
        OWL.inverseOf: "feeds",
    },

    "hasPoint": {
        OWL.inverseOf: "isPointOf",
        RDFS.range: BRICK.Point,
    },
    "isPointOf": {
        OWL.inverseOf: "hasPoint",
        RDFS.domain: BRICK.Point,
    },

    "hasPart": {
        OWL.inverseOf: "isPartOf",
    },
    "isPartOf": {
        OWL.inverseOf: "hasPart",
    },

    # Haystack-style
    "ahuRef": {
        RDFS.domain: BRICK.AHU,
    }
}

define_properties(properties)

G.add( (BRICK.hasTag, A, OWL.ObjectProperty) )


r = Restriction(BRICK.hasTag, graph=G, value=BRICK.Valve)
r.serialize(graph=G)


s = G.serialize(format='ttl')
with open('Brick.ttl','wb') as f:
    f.write(s)
