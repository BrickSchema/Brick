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

point_definitions = {
    "Setpoint": {
        "tagvalues": [[BRICK.hasTag, TAG.Setpoint]],
        "subclasses": {
            "Enthalpy_Setpoint": {},
            "Dew_Point_Setpoint": {},
            "Demand_Setpoint": {
                "subclasses": {
                    "Cooling_Demand_Setpoint": {},
                    "Cooling_Request_Percent_Setpoint": {},
                    "Cooling_Request_Setpoint": {},
                    "Heating_Demand_Setpoint": {},
                    "Heating_Request_Percent_Setpoint": {},
                    "Heating_Request_Setpoint": {},
                    "Preheat_Demand_Setpoint": {},
                    "Discharge_Air_Flow_Demand_Setpoint": {},
                    "Supply_Air_Flow_Demand_Setpoint": {},
                },
            },
            "Damper_Position_Setpoint": {
                "subclasses": {
                    "Damper_Max_Position_Setpoint": {},
                    "Damper_Min_Position_Setpoint": {},
                },
            },
            "Dead_Band_Setpoint": {
                "subclasses": {
                    "Chilled_Water_Differential_Pressure_Dead_Band_Setpoint": {},
                    "Cooling_Discharge_Air_Temperature_Dead_Band_Setpoint": {},
                    "Cooling_Supply_Air_Temperature_Dead_Band_Setpoint": {},
                    "Differential_Pressure_Dead_Band_Setpoint": {
                        "subclasses": {
                            "Chilled_Water_Pump_Differential_Pressure_Dead_Band_Setpoint": {},
                            "Hot_Water_Differential_Pressure_Dead_Band_Setpoint": {},
                        },
                    },
                    "Discharge_Air_Temperature_Dead_Band_Setpoint": {
                        "subclasses": {
                            "Heating_Discharge_Air_Temperature_Dead_Band_Setpoint": {},
                            "Cooling_Discharge_Air_Temperature_Dead_Band_Setpoint": {},
                        },
                    },
                    "Supply_Air_Temperature_Dead_Band_Setpoint": {
                        "subclasses": {
                            "Heating_Supply_Air_Temperature_Dead_Band_Setpoint": {},
                            "Cooling_Supply_Air_Temperature_Dead_Band_Setpoint": {},
                        },
                    },
                    "Temperature_Dead_Band_Setpoint": {
                        "subclasses": {
                            "Occupied_Cooling_Temperature_Dead_Band_Setpoint": {},
                            "Occupied_Heating_Temperature_Dead_Band_Setpoint": {},
                        },
                    },
                    "Air_Flow_Dead_Band_Setpoint": {
                        "subclasses": {
                            "Exhaust_Air_Stack_Flow_Dead_Band_Setpoint": {},
                        },
                    },
                    "Static_Pressure_Dead_Band_Setpoint": {},
                    "Supply_Water_Differential_Pressure_Dead_Band_Setpoint": {
                        "subclasses": {
                            "Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Dead_Band_Setpoint": {},
                        },
                    },
                    "Supply_Water_Temperature_Dead_Band_Setpoint": {
                        "subclasses":{
                            "Heat_Exchanger_Supply_Water_Temperature_Dead_Band_Setpoint": {}
                        }
                    },
                },
            },
            "Flow_Setpoint": {
                "tagvalues": [[BRICK.hasTag, TAG["Flow"]], [BRICK.hasTag, TAG["Setpoint"]]],
                "subclasses": {
                    "Air_Flow_Setpoint": {
                        "tagvalues": [[BRICK.hasTag, TAG["Air"]], [BRICK.hasTag, TAG["Flow"]], [BRICK.hasTag, TAG["Setpoint"]]],
                        "subclasses": {
                            "Discharge_Air_Flow_Setpoint": {
                                "subclasses": {
                                    # Do the same for Max/Min? Occupied/Unoccupied?
                                    "Discharge_Air_Flow_Demand_Setpoint": {},
                                    "Cooling_Discharge_Air_Flow_Setpoint": {
                                        "subclasses": {
                                            "Cooling_Max_Discharge_Air_Flow_Setpoint": {
                                                "subclasses": {
                                                    "Occupied_Cooling_Max_Discharge_Air_Flow_Setpoint": {},
                                                    "Unoccupied_Cooling_Max_Discharge_Air_Flow_Setpoint": {},
                                                },
                                            },
                                            "Cooling_Min_Discharge_Air_Flow_Setpoint": {
                                                "subclasses": {
                                                    "Occupied_Cooling_Min_Discharge_Air_Flow_Setpoint": {},
                                                    "Unoccupied_Cooling_Min_Discharge_Air_Flow_Setpoint": {},
                                                },
                                            },
                                        },
                                    },
                                    "Heating_Discharge_Air_Flow_Setpoint": {
                                        "subclasses": {
                                            "Heating_Max_Discharge_Air_Flow_Setpoint": {
                                                "subclasses": {
                                                    "Occupied_Heating_Max_Discharge_Air_Flow_Setpoint": {},
                                                    "Unoccupied_Heating_Max_Discharge_Air_Flow_Setpoint": {},
                                                },
                                            },
                                            "Heating_Min_Discharge_Air_Flow_Setpoint": {
                                                "subclasses": {
                                                    "Occupied_Heating_Min_Discharge_Air_Flow_Setpoint": {},
                                                    "Unoccupied_Heating_Min_Discharge_Air_Flow_Setpoint": {},
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                            "Exhaust_Air_Flow_Setpoint": {
                                "subclasses": {
                                    "Exhaust_Air_Stack_Flow_Setpoint": {},
                                },
                            },
                            "Fan_Air_Flow_Setpoint": {},
                            "Outside_Air_Flow_Setpoint": {
                                "subclasses": {
                                    "Min_Outside_Air_Flow_Setpoint": {},
                                },
                            },
                            "Supply_Air_Flow_Setpoint": {
                                "subclasses": {
                                    "Supply_Air_Flow_Demand_Setpoint": {},
                                    "Occupied_Supply_Air_Flow_Setpoint": {
                                        "subclasses": {
                                            "Occupied_Cooling_Supply_Air_Flow_Setpoint": {
                                                "subclasses": {
                                                    "Occupied_Cooling_Max_Supply_Air_Flow_Setpoint": {},
                                                    "Occupied_Cooling_Min_Supply_Air_Flow_Setpoint": {},
                                                },
                                            },
                                            "Occupied_Heating_Supply_Air_Flow_Setpoint": {
                                                "subclasses": {
                                                    "Occupied_Heating_Max_Supply_Air_Flow_Setpoint": {},
                                                    "Occupied_Heating_Min_Supply_Air_Flow_Setpoint": {},
                                                },
                                            },
                                        },
                                    },
                                    "Cooling_Supply_Air_Flow_Setpoint": {
                                        "subclasses": {
                                            "Cooling_Max_Supply_Air_Flow_Setpoint": {},
                                            "Cooling_Min_Supply_Air_Flow_Setpoint": {},
                                        },
                                    },
                                    "Heating_Supply_Air_Flow_Setpoint": {
                                        "subclasses": {
                                            "Heating_Max_Supply_Air_Flow_Setpoint": {},
                                            "Heating_Min_Supply_Air_Flow_Setpoint": {},
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            "Temperature_Setpoint": {
                "tagvalues": [[BRICK.hasTag, TAG["Temperature"]], [BRICK.hasTag, TAG["Setpoint"]]],
                "subclasses": {
                    "Air_Temperature_Setpoint": {
                        "tagvalues": [[BRICK.hasTag, TAG["Air"]], [BRICK.hasTag, TAG["Temperature"]], [BRICK.hasTag, TAG["Setpoint"]]],
                        "subclasses": {
                            "Discharge_Air_Temperature_Setpoint": {
                                "tagvalues": [[BRICK.hasTag, TAG["Discharge"]], [BRICK.hasTag, TAG["Air"]], [BRICK.hasTag, TAG["Temperature"]], [BRICK.hasTag, TAG["Setpoint"]]],
                                "subclasses": {
                                    "Discharge_Air_Temperature_Heating_Setpoint": {
                                        OWL.equivalentClass: "Minimum_Discharge_Air_Temperature_Setpoint",
                                    },
                                    "Discharge_Air_Temperature_Cooling_Setpoint": {
                                        OWL.equivalentClass: "Maximum_Discharge_Air_Temperature_Setpoint",
                                    },
                                },
                            },
                            "Mixed_Air_Temperature_Setpoint": {
                                "tagvalues": [[BRICK.hasTag, TAG["Mixed"]], [BRICK.hasTag, TAG["Air"]], [BRICK.hasTag, TAG["Temperature"]], [BRICK.hasTag, TAG["Setpoint"]]],
                            },
                            "Room_Air_Temperature_Setpoint": {},
                            "Outside_Air_Temperature_Setpoint": {
                                "tagvalues": [[BRICK.hasTag, TAG["Outside"]], [BRICK.hasTag, TAG["Air"]], [BRICK.hasTag, TAG["Temperature"]], [BRICK.hasTag, TAG["Setpoint"]]],
                                "subclasses": {
                                    "Low_Outside_Air_Temperature_Enable_Setpoint": {},
                                    "Open_Heating_Valve_Outside_Air_Temperature_Setpoint": {},
                                    "Outside_Air_Lockout_Temperature_Setpoint": {},
                                },
                            },
                        },
                    },
                    "Water_Temperature_Setpoint": {
                        "tagvalues": [
                            [BRICK.hasTag, TAG.Setpoint],
                            [BRICK.hasTag, TAG.Temperature],
                            [BRICK.hasTag, TAG.Water],
                        ],
                        "subclasses": {
                            "Entering_Water_Temperature_Setpoint": {
                                "tagvalues": [
                                    [BRICK.hasTag, TAG.Entering],
                                    [BRICK.hasTag, TAG.Setpoint],
                                    [BRICK.hasTag, TAG.Temperature],
                                    [BRICK.hasTag, TAG.Water],
                                ],
                            },
                            "Leaving_Water_Temperature_Setpoint": {
                                "tagvalues": [
                                    [BRICK.hasTag, TAG.Entering],
                                    [BRICK.hasTag, TAG.Setpoint],
                                    [BRICK.hasTag, TAG.Temperature],
                                    [BRICK.hasTag, TAG.Water],
                                ],
                            },
                        },
                    },
                },
            },
            "CO2_Setpoint": {
                "tagvalues": [
                    [BRICK.hasTag, TAG.Setpoint],
                    [BRICK.hasTag, TAG.CO2],
                ],
                "subclasses": {
                    "Return_Air_CO2_Setpoint": {
                        "tagvalues": [
                            [BRICK.hasTag, TAG.Setpoint],
                            [BRICK.hasTag, TAG.Return],
                            [BRICK.hasTag, TAG.CO2],
                        ],
                        "subclasses": {
                            "Max_Return_Air_CO2_Setpoint": {
                            }
                        },
                    }
                },
            },
        },
    },
    "Sensor": {
        "tagvalues": [
            [BRICK.hasTag, TAG.Sensor]
        ],
        "subclasses": {
            "CO2_Sensor": {
                "tagvalues": [
                    [BRICK.hasTag, TAG.Sensor],
                    [BRICK.hasTag, TAG.CO2],
                ],
                "subclasses": {
                    "CO2_Differential_Sensor": {},
                    "CO2_Level_Sensor": {},
                },
            },
            "Temperature_Sensor": {
                "tagvalues": [
                    [BRICK.hasTag, TAG.Sensor],
                    [BRICK.hasTag, TAG.Temperature],
                ],
                "subclasses": {
                    "Zone_Temperature_Sensor": {
                        "subclasses": {
                            "Average_Zone_Temperature_Sensor": {},
                            "Highest_Zone_Temperature_Sensor": {
                                OWL.equivalentClass: "Warmest_Zone_Temperature_Sensor"
                            },
                            "Lowest_Zone_Temperature_Sensor": {
                                OWL.equivalentClass: "Coldest_Zone_Temperature_Sensor"
                            },
                        },
                    },
                    "Air_Temperature_Sensor": {
                        "substances": [
                            [BRICK.measures, OWL.someValuesFrom, BRICK.Air],
                            [RDF.type, OWL.hasValue, BRICK.Temperature_Sensor],
                        ],
                        "subclasses": {
                            "Discharge_Air_Temperature_Sensor": {
                                OWL.equivalentClass: "Supply_Air_Temperature_Sensor",
                                "subclasses": {
                                    "Cooling_Coil_Discharge_Air_Temperature_Sensor": {},
                                    "Heat_Wheel_Discharge_Air_Temperature_Sensor": {},
                                    "Preheat_Discharge_Air_Temperature_Sensor": {},
                                },
                            },
                            "Zone_Air_Temperature_Sensor": {},
                            "Exhaust_Air_Temperature_Sensor": {
                                "substances": [
                                    [BRICK.measures, OWL.someValuesFrom, BRICK.Exhaust_Air],
                                    [RDF.type, OWL.hasValue, BRICK.Temperature_Sensor],
                                ],
                            },
                            "Mixed_Air_Temperature_Sensor": {
                                "substances": [
                                    [BRICK.measures, OWL.someValuesFrom, BRICK.Mixed_Air],
                                    [RDF.type, OWL.hasValue, BRICK.Temperature_Sensor],
                                ],
                            },
                            "Return_Air_Temperature_Sensor": {
                                "substances": [
                                    [BRICK.measures, OWL.someValuesFrom, BRICK.Return_Air],
                                    [RDF.type, OWL.hasValue, BRICK.Temperature_Sensor],
                                ],
                            },
                            "Outside_Air_Temperature_Sensor": {
                                "substances": [
                                    [BRICK.measures, OWL.someValuesFrom, BRICK.Outside_Air],
                                    [RDF.type, OWL.hasValue, BRICK.Temperature_Sensor],
                                ],
                                "subclasses": {
                                    "Outside_Air_Lockout_Temperature_Differential_Sensor": {
                                        "subclasses": {
                                            "Low_Outside_Air_Lockout_Temperature_Differential_Sensor": {},
                                            "High_Outside_Air_Lockout_Temperature_Differential_Sensor": {},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    "Water_Temperature_Sensor": {
                        "substances": [
                            [BRICK.measures, OWL.someValuesFrom, BRICK.Water],
                            [RDF.type, OWL.hasValue, BRICK.Temperature_Sensor],
                        ],
                        "subclasses": {
                            "Chilled_Water_Supply_Temperature_Sensor": {
                                "substances": [
                                    [BRICK.measures, OWL.someValuesFrom, BRICK.Chilled_Water],
                                    [RDF.type, OWL.hasValue, BRICK.Temperature_Sensor],
                                ],
                                OWL.equivalentClass: "Chilled_Water_Discharge_Temperature_Sensor",
                            },
                            "Heat_Exchanger_Supply_Water_Temperature_Sensor": {},
                            "Hot_Water_Supply_Temperature_Sensor": {
                                "subclasses": {
                                    "Domestic_Hot_Water_Supply_Temperature_Sensor": {},
                                    "High_Temperature_Hot_Water_Supply_Temperature_Sensor": {},
                                    "Medium_Temperature_Hot_Water_Supply_Temperature_Sensor": {},
                                },
                            },
                            "Chilled_Water_Temperature_Sensor": {
                                "subclasses": {
                                    "Chilled_Water_Differential_Temperature_Sensor": {},
                                },
                            },
                            "Entering_Water_Temperature_Sensor": {
                                "subclasses": {
                                    "Hot_Water_Coil_Entering_Temperature_Sensor": {},
                                    "Ice_Tank_Entering_Water_Temperature_Sensor": {},
                                    "PreHeat_Coil_Entering_Air_Temperature_Sensor": {},
                                },
                            },
                            "Leaving_Water_Temperature_Sensor": {
                                "subclasses": {
                                    "Ice_Tank_Leaving_Water_Temperature_Sensor": {},
                                    "PreHeat_Coil_Leaving_Air_Temperature_Sensor": {},
                                },
                            },
                            "Return_Water_Temperature_Sensor": {
                                "subclasses": {
                                    "Hot_Water_Return_Temperature_Sensor": {},
                                    "Chilled_Water_Return_Temperature_Sensor": {},
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
