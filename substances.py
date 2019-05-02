from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.collection import Collection
from rdflib.extras.infixowl import Restriction

BRICK = Namespace("https://brickschema.org/schema/1.0.3/Brick#")
TAG = Namespace("https://brickschema.org/schema/1.0.3/BrickTag#")
BLDG = Namespace("https://brickschema.org/schema/1.0.3/ExampleBuilding#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
A = RDF.type

##### Defining substances
substances = {
    "Fluid": {
        "subclasses": {
            "Gas": {
                "subclasses": {
                    "Air": {
                        "subclasses": {
                            "Outside_Air": {
                                SKOS.definition: Literal("air external to a defined zone (e.g., corridors)."),
                             },
                            "Mixed_Air": {
                                SKOS.definition: Literal("(1) air that contains two or more streams of air. (2) combined outdoor air and recirculated air."),
                             },
                            "Return_Air": {
                                SKOS.definition: Literal("air removed from a space to be recirculated or exhausted. Air extracted from a space and totally or partially returned to an air conditioner, furnace, or other heating, cooling, or ventilating system."),
                            },
                            "Exhaust_Air": {
                                SKOS.definition: Literal("air that must be removed from a space due to contaminants, regardless of pressurization"),
                            },
                            "Supply_Air": {
                                SKOS.definition: Literal("(1) air delivered by mechanical or natural ventilation to a space, composed of any combination of outdoor air, recirculated air, or transfer air. (2) air entering a space from an air-conditioning, heating, or ventilating apparatus for the purpose of comfort conditioning. Supply air is generally filtered, fan forced, and either heated, cooled, humidified, or dehumidified as necessary to maintain specified conditions. Only the quantity of outdoor air within the supply airflow may be used as replacement air."),
                            },
                        },
                    },
                    "Steam": {
                        SKOS.definition: Literal("water in the vapor phase."),
                    },
                },
            },
            "Liquid": {
                "subclasses": {
                    "Water": {
                        SKOS.definition: Literal("transparent, odorless, tasteless liquid; a compound of hydrogen and oxygen (H2O), containing 11.188% hydrogen and 88.812% oxygen by mass; freezing at 32°F (0°C); boiling near 212°F (100°C)."),
                        "subclasses": {
                            "Chilled_Water": {
                                SKOS.definition: Literal( "water used as a cooling medium (particularly in air-conditioning systems or in processes) at below ambient temperature."),
                            },
                        },
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
            "Frost": {},
            "Hail": {},
        },
    },
    "Enthalpy": {
        SKOS.definition: Literal("(also known as heat content), thermodynamic quantity equal to the sum of the internal energy of a system plus the product of the pressure volume work done on the system. H = E + pv, where H = enthalpy or total heat content, E = internal energy of the system, p = pressure, and v = volume. (Compare to [[specific enthalpy]].)"),
    },
    "Luminance": {},
}
