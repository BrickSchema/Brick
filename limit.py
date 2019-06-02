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
                    "Max_Speed_Setpoint": {},
                    "Min_Speed_Setpoint": {},
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
                    "Damper_Max_Position_Setpoint_Limit": {},
                    "Damper_Min_Position_Setpoint_Limit": {},
                },
            },
            "Differential_Pressure_Setpoint_Limit": {
                "subclasses": {
                    "Max_Chilled_Water_Differential_Pressure_Setpoint": {},
                    "Min_Chilled_Water_Differential_Pressure_Setpoint": {},
                    "Max_Hot_Water_Differential_Pressure_Setpoint": {},
                    "Min_Hot_Water_Differential_Pressure_Setpoint": {},
                },
            },
            "Static_Pressure_Setpoint_Limit": {
                "subclasses": {
                    "Static_Pressure_Min_Setpoint_Limit": {},
                    "Static_Pressure_Max_Setpoint_Limit": {},
                },
            },
            "Max_Limit": {
                "subclasses": {
                    "Max_Speed_Setpoint": {},
                    "Max_Discharge_Air_Static_Pressure_Setpoint": {},
                    "Max_Supply_Air_Static_Pressure_Setpoint": {},
                    "Damper_Max_Position_Setpoint_Limit": {},
                    "Max_Chilled_Water_Differential_Pressure_Setpoint": {},
                    "Max_Hot_Water_Differential_Pressure_Setpoint": {},
                    "Static_Pressure_Max_Setpoint_Limit": {
                        "subclasses": {
                            "Max_Discharge_Air_Static_Pressure_Setpoint_Limit": {},
                            "Max_Supply_Air_Static_Pressure_Setpoint_Limit": {},
                        },
                    },
                    "Max_Air_Flow_Setpoint_Limit": {
                        "subclasses": {
                            "Cooling_Max_Discharge_Air_Flow_Setpoint_Limit": {
                                "subclasses": {
                                    "Cooling_Max_Supply_Air_Flow_Setpoint_Limit": {},
                                    "Occupied_Cooling_Max_Supply_Air_Flow_Setpoint_Limit": {},
                                    "Occupied_Cooling_Max_Discharge_Air_Flow_Setpoint_Limit": {},
                                    "Unoccupied_Cooling_Max_Discharge_Air_Flow_Setpoint_Limit": {},
                                },
                            },
                            "Heating_Max_Discharge_Air_Flow_Setpoint_Limit": {
                                "subclasses": {
                                    "Heating_Max_Supply_Air_Flow_Setpoint_Limit": {},
                                    "Occupied_Heating_Max_Supply_Air_Flow_Setpoint_Limit": {},
                                    "Occupied_Heating_Max_Discharge_Air_Flow_Setpoint_Limit": {},
                                    "Unoccupied_Heating_Max_Discharge_Air_Flow_Setpoint_Limit": {},
                                },
                            },
                        },
                    },
                },
            },
            "Min_Limit": {
                "subclasses": {
                    "Min_Speed_Setpoint": {},
                    "Min_Hot_Water_Differential_Pressure_Setpoint": {},
                    "Min_Chilled_Water_Differential_Pressure_Setpoint": {},
                    "Damper_Min_Position_Setpoint_Limit": {},
                    "Min_Discharge_Air_Static_Pressure_Setpoint": {},
                    "Min_Supply_Air_Static_Pressure_Setpoint": {},
                    "Static_Pressure_Min_Setpoint_Limit": {
                        "subclasses": {
                            "Min_Discharge_Air_Static_Pressure_Setpoint_Limit": {},
                            "Min_Supply_Air_Static_Pressure_Setpoint_Limit": {},
                        },
                    },
                    "Min_Air_Flow_Setpoint_Limit": {
                        "subclasses": {
                            "Min_Outside_Air_Flow_Setpoint_Limit": {},
                            "Cooling_Min_Discharge_Air_Flow_Setpoint_Limit": {
                                "subclasses": {
                                    "Cooling_Min_Supply_Air_Flow_Setpoint_Limit": {},
                                    "Occupied_Cooling_Min_Supply_Air_Flow_Setpoint_Limit": {},
                                    "Occupied_Cooling_Min_Discharge_Air_Flow_Setpoint_Limit": {},
                                    "Unoccupied_Cooling_Min_Discharge_Air_Flow_Setpoint_Limit": {},
                                },
                            },
                            "Heating_Min_Discharge_Air_Flow_Setpoint_Limit": {
                                "subclasses": {
                                    "Heating_Min_Supply_Air_Flow_Setpoint_Limit": {},
                                    "Occupied_Heating_Min_Supply_Air_Flow_Setpoint_Limit": {},
                                    "Occupied_Heating_Min_Discharge_Air_Flow_Setpoint_Limit": {},
                                    "Unoccupied_Heating_Min_Discharge_Air_Flow_Setpoint_Limit": {},
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
