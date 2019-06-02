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

limit_definitions = {
    "Limit": {
        "tagvalues": [[BRICK.hasTag, TAG.Limit]],
        "subclasses": {
            "Speed_Setpoint_Limit": {
                "subclasses": {
                    "Max_Speed_Setpoint_Limit": {},
                    "Min_Speed_Setpoint_Limit": {},
                },
            },
            "Air_Flow_Setpoint_Limit": {
                "subclasses": {
                    "Max_Air_Flow_Setpoint_Limit": {},
                    "Min_Air_Flow_Setpoint_Limit": {},
                },
            },
            "Damper_Position_Limit": {
                "subclasses": {
                    "Max_Damper_Position_Setpoint_Limit": {},
                    "Min_Damper_Position_Setpoint_Limit": {},
                },
            },
            "Differential_Pressure_Setpoint_Limit": {
                "subclasses": {
                    "Max_Chilled_Water_Differential_Pressure_Setpoint_Limit": {},
                    "Min_Chilled_Water_Differential_Pressure_Setpoint_Limit": {},
                    "Max_Hot_Water_Differential_Pressure_Setpoint_Limit": {},
                    "Min_Hot_Water_Differential_Pressure_Setpoint_Limit": {},
                },
            },
            "Static_Pressure_Setpoint_Limit": {
                "subclasses": {
                    "Min_Static_Pressure_Setpoint_Limit": {},
                    "Max_Static_Pressure_Setpoint_Limit": {},
                },
            },
            "Max_Limit": {
                "subclasses": {
                    "Max_Speed_Setpoint_Limit": {},
                    "Max_Discharge_Air_Static_Pressure_Setpoint_Limit": {},
                    "Max_Supply_Air_Static_Pressure_Setpoint_Limit": {},
                    "Max_Damper_Position_Setpoint_Limit": {},
                    "Max_Chilled_Water_Differential_Pressure_Setpoint_Limit": {},
                    "Max_Hot_Water_Differential_Pressure_Setpoint_Limit": {},
                    "Max_Static_Pressure_Setpoint_Limit": {
                        "subclasses": {
                            "Max_Discharge_Air_Static_Pressure_Setpoint_Limit": {},
                            "Max_Supply_Air_Static_Pressure_Setpoint_Limit": {},
                        },
                    },
                    "Max_Air_Flow_Setpoint_Limit": {
                        "subclasses": {
                            "Max_Cooling_Supply_Air_Flow_Setpoint_Limit": {
                                "subclasses": {
                                    "Max_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit": {},
                                    "Max_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit": {},
                                },
                            },
                            "Max_Cooling_Discharge_Air_Flow_Setpoint_Limit": {
                                "subclasses": {
                                    "Max_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit": {},
                                    "Max_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit": {},
                                },
                            },
                            "Max_Heating_Supply_Air_Flow_Setpoint_Limit": {
                                "subclasses": {
                                    "Max_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit": {},
                                    "Max_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit": {},
                                },
                            },
                            "Max_Heating_Discharge_Air_Flow_Setpoint_Limit": {
                                "subclasses": {
                                    "Max_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit": {},
                                    "Max_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit": {},
                                },
                            },
                        },
                    },
                },
            },
            "Min_Limit": {
                "subclasses": {
                    "Min_Speed_Setpoint_Limit": {},
                    "Min_Hot_Water_Differential_Pressure_Setpoint_Limit": {},
                    "Min_Chilled_Water_Differential_Pressure_Setpoint_Limit": {},
                    "Min_Damper_Position_Setpoint_Limit": {},
                    "Min_Discharge_Air_Static_Pressure_Setpoint_Limit": {},
                    "Min_Supply_Air_Static_Pressure_Setpoint_Limit": {},
                    "Min_Static_Pressure_Setpoint_Limit": {
                        "subclasses": {
                            "Min_Discharge_Air_Static_Pressure_Setpoint_Limit": {},
                            "Min_Supply_Air_Static_Pressure_Setpoint_Limit": {},
                        },
                    },
                    "Min_Air_Flow_Setpoint_Limit": {
                        "subclasses": {
                            "Min_Outside_Air_Flow_Setpoint_Limit": {},
                            "Min_Cooling_Supply_Air_Flow_Setpoint_Limit": {
                                "subclasses": {
                                    "Min_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit": {},
                                    "Min_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit": {},
                                },
                            },
                            "Min_Cooling_Discharge_Air_Flow_Setpoint_Limit": {
                                "subclasses": {
                                    "Min_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit": {},
                                    "Min_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit": {},
                                },
                            },
                            "Min_Heating_Supply_Air_Flow_Setpoint_Limit": {
                                "subclasses": {
                                    "Min_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit": {},
                                    "Min_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit": {},
                                },
                            },
                            "Min_Heating_Discharge_Air_Flow_Setpoint_Limit": {
                                "subclasses": {
                                    "Min_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit": {},
                                    "Min_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit": {},
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
