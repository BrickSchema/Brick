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

parameter_definitions = {
    "PID_Parameter":{
        "tags": [TAG.Parameter, TAG.PID],
        "subclasses": {
            "Gain_Parameter": {
                "tags": [TAG.Parameter, TAG.PID, TAG.Gain],
                "subclasses": {
                    "Integral_Gain_Parameter": {
                        "tags": [TAG.Parameter, TAG.PID, TAG.Gain, TAG.Integral],
                        "subclasses": {
                            "Supply_Air_Integral_Gain_Parameter": {
                                "tags": [TAG.Supply, TAG.Air, TAG.Integral, TAG.Gain, TAG.Parameter, TAG.PID],
                            }
                        }
                    },
                    "Proportional_Gain_Parameter": {
                        "tags": [TAG.Parameter, TAG.PID, TAG.Gain, TAG.Proportional],
                        "subclasses": {
                            "Supply_Air_Proportional_Gain_Parameter": {
                                "tags": [TAG.Parameter, TAG.PID, TAG.Gain, TAG.Proportional, TAG.Supply, TAG.Air],
                            },
                        }
                    },
                    "Derivative_Gain_Parameter": {
                        "tags": [TAG.Parameter, TAG.PID, TAG.Gain, TAG.Derivative],
                    },
                }
            },
            "Step_Parameter": {
                "tags": [TAG.Parameter, TAG.PID, TAG.Step],
                "subclasses": {
                    "Differential_Pressure_Step_Parameter": {
                        "subclasses": {
                            "Chilled_Water_Differential_Pressure_Step_Parameter": {
                                "tags": [ TAG.Chilled, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Step, TAG.Parameter , TAG.PID ],
                            }
                        },
                        "tags": [ TAG.Differential, TAG.Pressure, TAG.Step, TAG.Parameter , TAG.PID ],
                    },
                    "Static_Pressure_Step_Parameter": {
                        "subclasses": {
                            "Air_Static_Pressure_Step_Parameter": {
                                "tags": [ TAG.Air, TAG.Static, TAG.Pressure, TAG.Step, TAG.Parameter , TAG.PID ],
                            }
                        },
                        "tags": [ TAG.Static, TAG.Pressure, TAG.Step, TAG.Parameter , TAG.PID ],
                    },
                    "Temperature_Step_Parameter": {
                        "subclasses": {
                            "Air_Temperature_Step_Parameter": {
                                "tags": [ TAG.Air, TAG.Temperature, TAG.Step, TAG.Parameter, TAG.PID  ],
                            }
                        },
                        "tags": [ TAG.Temperature, TAG.Step, TAG.Parameter , TAG.PID ],
                    }
                },
            },
            "Time_Parameter":{
                "Integral_Time_Parameter": {
                    "tags": [TAG.Parameter, TAG.PID, TAG.Time, TAG.Integral],
                    "subclasses": {
                        "Chilled_Water_Differential_Pressure_Integral_Time_Parameter": {
                            "tags": [TAG.Chilled, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Integral, TAG.Time, TAG.Parameter, TAG.PID ],
                        },
                        "Cooling_Discharge_Air_Temperature_Integral_Time_Parameter": {
                            "tags": [ TAG.Cooling, TAG.Discharge, TAG.Air, TAG.Temperature, TAG.Integral, TAG.Time, TAG.Parameter, TAG.PID  ],
                        },
                        "Cooling_Supply_Air_Temperature_Integral_Time_Parameter": {
                            "tags": [ TAG.Cooling, TAG.Supply, TAG.Air, TAG.Temperature, TAG.Integral, TAG.Time, TAG.Parameter, TAG.PID  ],
                        },
                        "Differential_Pressure_Integral_Time_Parameter": {
                            "tags": [ TAG.Differential, TAG.Pressure, TAG.Integral, TAG.Time, TAG.Parameter, TAG.PID ],
                            "subclasses": {
                                "Hot_Water_Differential_Pressure_Integral_Time_Parameter": {
                                    "tags": [ TAG.Hot, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Integral, TAG.Time, TAG.Parameter , TAG.PID ],
                                },
                                "Chilled_Water_Differential_Pressure_Integral_Time_Parameter": {
                                    "tags": [ TAG.Chilled, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Integral, TAG.Time, TAG.Parameter, TAG.PID  ],
                                }
                            },
                        },
                        "Discharge_Air_Static_Pressure_Integral_Time_Parameter": {
                            "tags": [ TAG.Discharge, TAG.Air, TAG.Static, TAG.Pressure, TAG.Integral, TAG.Time, TAG.Parameter, TAG.PID  ],
                        },
                        "Exhaust_Air_Flow_Integral_Time_Parameter": {
                            "subclasses": {
                                "Exhaust_Air_Stack_Flow_Integral_Time_Parameter": {
                                    "tags": [ TAG.Exhaust, TAG.Air, TAG.Stack, TAG.Flow, TAG.Integral, TAG.Time, TAG.Parameter, TAG.PID  ],
                                }
                            },
                            "tags": [ TAG.Exhaust, TAG.Air, TAG.Flow, TAG.Integral, TAG.Time, TAG.Parameter, TAG.PID  ],
                        },
                        "Heating_Discharge_Air_Temperature_Integral_Time_Parameter": {
                            "tags": [ TAG.Heating, TAG.Discharge, TAG.Air, TAG.Temperature, TAG.Integral, TAG.Time, TAG.Parameter, TAG.PID  ],
                        },
                        "Heating_Supply_Air_Temperature_Integral_Time_Parameter": {
                            "tags": [ TAG.Heating, TAG.Supply, TAG.Air, TAG.Temperature, TAG.Integral, TAG.Time, TAG.Parameter, TAG.PID  ],
                        },
                        "Static_Pressure_Integral_Time_Parameter": {
                            "tags": [ TAG.Static, TAG.Pressure, TAG.Integral, TAG.Time, TAG.Parameter, TAG.PID  ],
                        },
                        "Supply_Air_Static_Pressure_Integral_Time_Parameter": {
                            "tags": [ TAG.Supply, TAG.Air, TAG.Static, TAG.Pressure, TAG.Integral, TAG.Time, TAG.Parameter , TAG.PID ],
                        },
                        "Supply_Water_Differential_Pressure_Integral_Time_Parameter": {
                            "tags": [ TAG.Supply, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Integral, TAG.Time, TAG.Parameter , TAG.PID ],
                        },
                        "Supply_Water_Temperature_Integral_Time_Parameter": {
                            "tags": [ TAG.Supply, TAG.Water, TAG.Temperature, TAG.Integral, TAG.Time, TAG.Parameter , TAG.PID ],
                        }
                    },
                },
                "Derivative_Time_Parameter": {
                    "tags": [TAG.Parameter, TAG.PID, TAG.Time, TAG.Derivative],
                },
            },
            "Proportional_Band_Parameter": {
                "tags": [TAG.Parameter, TAG.PID, TAG.Proportional, TAG.Band, TAG.Parameter, TAG.PID ],
                "subclasses": {
                    "Chilled_Water_Differential_Pressure_Proportional_Band_Parameter": {
                        "tags": [ TAG.Chilled, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Proportional, TAG.Band, TAG.Parameter , TAG.PID ],
                    },
                    "Cooling_Discharge_Air_Temperature_Proportional_Band_Parameter": {
                        "tags": [ TAG.Cooling, TAG.Discharge, TAG.Air, TAG.Temperature, TAG.Proportional, TAG.Band, TAG.Parameter , TAG.PID ],
                    },
                    "Cooling_Supply_Air_Temperature_Proportional_Band_Parameter": {
                        "tags": [ TAG.Cooling, TAG.Supply, TAG.Air, TAG.Temperature, TAG.Proportional, TAG.Band, TAG.Parameter, TAG.PID  ],
                    },
                    "Differential_Pressure_Proportional_Band": {
                        "tags": [ TAG.Differential, TAG.Pressure, TAG.Proportional, TAG.Band , TAG.PID ],
                    },
                    "Hot_Water_Differential_Pressure_Proportional_Band_Parameter": {
                        "tags": [ TAG.Hot, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Proportional, TAG.Band, TAG.Parameter , TAG.PID ],
                    },
                    "Discharge_Air_Static_Pressure_Proportional_Band_Parameter": {
                        "tags": [ TAG.Discharge, TAG.Air, TAG.Static, TAG.Pressure, TAG.Proportional, TAG.Band, TAG.Parameter , TAG.PID ],
                    },
                    "Discharge_Air_Temperature_Proportional_Band_Parameter": {
                        "tags": [ TAG.Discharge, TAG.Air, TAG.Temperature, TAG.Proportional, TAG.Band, TAG.Parameter , TAG.PID ],
                    },
                    "Supply_Air_Temperature_Proportional_Band_Parameter": {
                        "tags": [ TAG.Supply, TAG.Air, TAG.Temperature, TAG.Proportional, TAG.Band, TAG.Parameter , TAG.PID ],
                    },
                    "Exhaust_Air_Flow_Proportional_Band_Parameter": {
                        "tags": [ TAG.Exhaust, TAG.Air, TAG.Flow, TAG.Proportional, TAG.Band, TAG.Parameter , TAG.PID ],
                    },
                    "Heating_Discharge_Air_Temperature_Proportional_Band_Parameter": {
                        "tags": [ TAG.Heating, TAG.Discharge, TAG.Air, TAG.Temperature, TAG.Proportional, TAG.Band, TAG.Parameter , TAG.PID ],
                    },
                    "Heating_Supply_Air_Temperature_Proportional_Band_Parameter": {
                        "tags": [ TAG.Heating, TAG.Supply, TAG.Air, TAG.Temperature, TAG.Proportional, TAG.Band, TAG.Parameter , TAG.PID ],
                    },
                    "Static_Pressure_Proportional_Band_Parameter": {
                        "subclasses": {
                            "Exhaust_Air_Static_Pressure_Proportional_Band_Parameter": {
                                "tags": [ TAG.Exhaust, TAG.Air, TAG.Static, TAG.Pressure, TAG.Proportional, TAG.Band, TAG.Parameter, TAG.PID  ],
                            }
                        },
                        "tags": [ TAG.Static, TAG.Pressure, TAG.Proportional, TAG.Band, TAG.Parameter , TAG.PID ],
                    },
                    "Supply_Air_Static_Pressure_Proportional_Band_Parameter": {
                        "tags": [ TAG.Supply, TAG.Air, TAG.Static, TAG.Pressure, TAG.Proportional, TAG.Band, TAG.Parameter , TAG.PID ],
                    },
                    "Supply_Water_Differential_Pressure_Proportional_Band_Parameter": {
                        "subclasses": {
                            "Discharge_Water_Differential_Pressure_Proportional_Band_Parameter": {
                                "tags": [TAG.Discharge, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Proportional, TAG.Band, TAG.Parameter , TAG.PID ],
                            },
                            "Supply_Water_Differential_Pressure_Proportional_Band_Parameter": {
                                "tags": [TAG.Supply, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Proportional, TAG.Bandsetpoint , TAG.PID ],
                            }
                        },
                        "tags": [ TAG.Supply, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Proportional, TAG.Band, TAG.Parameter , TAG.PID ],
                    },
                    "Supply_Water_Temperature_Proportional_Band_Parameter": {
                        "tags": [ TAG.Supply, TAG.Water, TAG.Temperature, TAG.Proportional, TAG.Band, TAG.Parameter, TAG.PID ],
                    },
                    "Discharge_Water_Temperature_Proportional_Band_Parameter": {
                        "tags": [TAG.Discharge, TAG.Water, TAG.Temperature, TAG.Proportional, TAG.Band, TAG.Parameter, TAG.PID ],
                    },
                },
            },
        }
    },
    "Limit": {
        "tags": [TAG.Parameter, TAG.Limit],
        "subclasses": {
            "Speed_Setpoint_Limit": {
                "tags": [TAG.Speed, TAG.Setpoint, TAG.Limit],
                "subclasses": {
                    "Max_Speed_Setpoint_Limit": {
                        "tags": [TAG.Max, TAG.Speed, TAG.Setpoint, TAG.Limit],
                    },
                    "Min_Speed_Setpoint_Limit": {
                        "tags": [TAG.Min, TAG.Speed, TAG.Setpoint, TAG.Limit],
                    },
                },
            },
            "Air_Flow_Setpoint_Limit": {
                "tags": [TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                "subclasses": {
                    "Max_Air_Flow_Setpoint_Limit": {
                        "tags": [TAG.Max, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                    },
                    "Min_Air_Flow_Setpoint_Limit": {
                        "tags": [TAG.Min, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                    },
                },
            },
            "Damper_Position_Limit": {
                "tags": [TAG.Damper, TAG.Position, TAG.Limit],
                "subclasses": {
                    "Max_Damper_Position_Setpoint_Limit": {
                        "tags": [TAG.Max, TAG.Damper, TAG.Position, TAG.Setpoint, TAG.Limit],
                    },
                    "Min_Damper_Position_Setpoint_Limit": {
                        "tags": [TAG.Min, TAG.Damper, TAG.Position, TAG.Setpoint, TAG.Limit],
                    },
                },
            },
            "Differential_Pressure_Setpoint_Limit": {
                "tags": [TAG.Differential, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                "subclasses": {
                    "Max_Chilled_Water_Differential_Pressure_Setpoint_Limit": {
                        "tags": [TAG.Max, TAG.Chilled, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                    },
                    "Min_Chilled_Water_Differential_Pressure_Setpoint_Limit": {
                        "tags": [TAG.Min, TAG.Chilled, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                    },
                    "Max_Hot_Water_Differential_Pressure_Setpoint_Limit": {
                        "tags": [TAG.Max, TAG.Hot, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                    },
                    "Min_Hot_Water_Differential_Pressure_Setpoint_Limit": {
                        "tags": [TAG.Min, TAG.Hot, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                    },
                },
            },
            "Static_Pressure_Setpoint_Limit": {
                "tags": [TAG.Static, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                "subclasses": {
                    "Min_Static_Pressure_Setpoint_Limit": {
                        "tags": [TAG.Min, TAG.Static, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                    },
                    "Max_Static_Pressure_Setpoint_Limit": {
                        "tags": [TAG.Max, TAG.Static, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                    },
                },
            },
            "Max_Limit": {
                "tags": [TAG.Max, TAG.Limit],
                "subclasses": {
                    "Max_Speed_Setpoint_Limit": {
                        "tags": [TAG.Max, TAG.Speed, TAG.Setpoint, TAG.Limit],
                    },
                    "Max_Discharge_Air_Static_Pressure_Setpoint_Limit": {
                        "tags": [TAG.Max, TAG.Discharge, TAG.Air, TAG.Static, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                    },
                    "Max_Supply_Air_Static_Pressure_Setpoint_Limit": {
                        "tags": [TAG.Max, TAG.Supply, TAG.Air, TAG.Static, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                    },
                    "Max_Damper_Position_Setpoint_Limit": {
                        "tags": [TAG.Max, TAG.Damper, TAG.Position, TAG.Setpoint, TAG.Limit],
                    },
                    "Max_Chilled_Water_Differential_Pressure_Setpoint_Limit": {
                        "tags": [TAG.Max, TAG.Chilled, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                    },
                    "Max_Hot_Water_Differential_Pressure_Setpoint_Limit": {
                        "tags": [TAG.Max, TAG.Hot, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                    },
                    "Max_Static_Pressure_Setpoint_Limit": {
                        "tags": [TAG.Max, TAG.Static, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                        "subclasses": {
                            "Max_Discharge_Air_Static_Pressure_Setpoint_Limit": {
                                "tags": [TAG.Max, TAG.Discharge, TAG.Air, TAG.Static, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                            },
                            "Max_Supply_Air_Static_Pressure_Setpoint_Limit": {
                                "tags": [TAG.Max, TAG.Supply, TAG.Air, TAG.Static, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                            },
                        },
                    },
                    "Max_Air_Flow_Setpoint_Limit": {
                        "tags": [TAG.Max, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                        "subclasses": {
                            "Max_Cooling_Supply_Air_Flow_Setpoint_Limit": {
                                "tags": [TAG.Max, TAG.Cooling, TAG.Supply, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                "subclasses": {
                                    "Max_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit": {
                                        "tags": [TAG.Max, TAG.Occupied, TAG.Cooling, TAG.Supply, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                    },
                                    "Max_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit": {
                                        "tags": [TAG.Max, TAG.Unoccupied, TAG.Cooling, TAG.Supply, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                    },
                                },
                            },
                            "Max_Cooling_Discharge_Air_Flow_Setpoint_Limit": {
                                "tags": [TAG.Max, TAG.Cooling, TAG.Discharge, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                "subclasses": {
                                    "Max_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit": {
                                        "tags": [TAG.Max, TAG.Occupied, TAG.Cooling, TAG.Discharge, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                    },
                                    "Max_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit": {
                                        "tags": [TAG.Max, TAG.Unoccupied, TAG.Cooling, TAG.Discharge, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                    },
                                },
                            },
                            "Max_Heating_Supply_Air_Flow_Setpoint_Limit": {
                                "tags": [TAG.Max, TAG.Heating, TAG.Supply, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                "subclasses": {
                                    "Max_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit": {
                                        "tags": [TAG.Max, TAG.Occupied, TAG.Heating, TAG.Supply, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                    },
                                    "Max_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit": {
                                        "tags": [TAG.Max, TAG.Unoccupied, TAG.Heating, TAG.Supply, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                    },
                                },
                            },
                            "Max_Heating_Discharge_Air_Flow_Setpoint_Limit": {
                                "tags": [TAG.Max, TAG.Heating, TAG.Discharge, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                "subclasses": {
                                    "Max_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit": {
                                        "tags": [TAG.Max, TAG.Occupied, TAG.Heating, TAG.Discharge, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                    },
                                    "Max_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit": {
                                        "tags": [TAG.Max, TAG.Unoccupied, TAG.Heating, TAG.Discharge, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                    },
                                },
                            },
                        },
                    },
                },
            },
            "Min_Limit": {
                "tags": [TAG.Min, TAG.Limit],
                "subclasses": {
                    "Min_Speed_Setpoint_Limit": {
                        "tags": [TAG.Min, TAG.Speed, TAG.Setpoint, TAG.Limit],
                    },
                    "Min_Hot_Water_Differential_Pressure_Setpoint_Limit": {
                        "tags": [TAG.Min, TAG.Hot, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                    },
                    "Min_Chilled_Water_Differential_Pressure_Setpoint_Limit": {
                        "tags": [TAG.Min, TAG.Chilled, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                    },
                    "Min_Damper_Position_Setpoint_Limit": {
                        "tags": [TAG.Min, TAG.Damper, TAG.Position, TAG.Setpoint, TAG.Limit],
                    },
                    "Min_Discharge_Air_Static_Pressure_Setpoint_Limit": {
                        "tags": [TAG.Min, TAG.Discharge, TAG.Air, TAG.Static, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                    },
                    "Min_Supply_Air_Static_Pressure_Setpoint_Limit": {
                        "tags": [TAG.Min, TAG.Supply, TAG.Air, TAG.Static, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                    },
                    "Min_Static_Pressure_Setpoint_Limit": {
                        "tags": [TAG.Min, TAG.Static, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                        "subclasses": {
                            "Min_Discharge_Air_Static_Pressure_Setpoint_Limit": {
                                "tags": [TAG.Min, TAG.Discharge, TAG.Air, TAG.Static, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                            },
                            "Min_Supply_Air_Static_Pressure_Setpoint_Limit": {
                                "tags": [TAG.Min, TAG.Supply, TAG.Air, TAG.Static, TAG.Pressure, TAG.Setpoint, TAG.Limit],
                            },
                        },
                    },
                    "Min_Air_Flow_Setpoint_Limit": {
                        "tags": [TAG.Min, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                        "subclasses": {
                            "Min_Outside_Air_Flow_Setpoint_Limit": {
                                "tags": [TAG.Min, TAG.Outside, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                            },
                            "Min_Cooling_Supply_Air_Flow_Setpoint_Limit": {
                                "tags": [TAG.Min, TAG.Cooling, TAG.Supply, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                "subclasses": {
                                    "Min_Occupied_Cooling_Supply_Air_Flow_Setpoint_Limit": {
                                        "tags": [TAG.Min, TAG.Occupied, TAG.Cooling, TAG.Supply, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                    },
                                    "Min_Unoccupied_Cooling_Supply_Air_Flow_Setpoint_Limit": {
                                        "tags": [TAG.Min, TAG.Unoccupied, TAG.Cooling, TAG.Supply, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                    },
                                },
                            },
                            "Min_Cooling_Discharge_Air_Flow_Setpoint_Limit": {
                                "tags": [TAG.Min, TAG.Cooling, TAG.Discharge, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                "subclasses": {
                                    "Min_Occupied_Cooling_Discharge_Air_Flow_Setpoint_Limit": {
                                        "tags": [TAG.Min, TAG.Occupied, TAG.Cooling, TAG.Discharge, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                    },
                                    "Min_Unoccupied_Cooling_Discharge_Air_Flow_Setpoint_Limit": {
                                        "tags": [TAG.Min, TAG.Unoccupied, TAG.Cooling, TAG.Discharge, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                    },
                                },
                            },
                            "Min_Heating_Supply_Air_Flow_Setpoint_Limit": {
                                "tags": [TAG.Min, TAG.Heating, TAG.Supply, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                "subclasses": {
                                    "Min_Occupied_Heating_Supply_Air_Flow_Setpoint_Limit": {
                                        "tags": [TAG.Min, TAG.Occupied, TAG.Heating, TAG.Supply, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                    },
                                    "Min_Unoccupied_Heating_Supply_Air_Flow_Setpoint_Limit": {
                                        "tags": [TAG.Min, TAG.Unoccupied, TAG.Heating, TAG.Supply, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                    },
                                },
                            },
                            "Min_Heating_Discharge_Air_Flow_Setpoint_Limit": {
                                "tags": [TAG.Min, TAG.Heating, TAG.Discharge, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                "subclasses": {
                                    "Min_Occupied_Heating_Discharge_Air_Flow_Setpoint_Limit": {
                                        "tags": [TAG.Min, TAG.Occupied, TAG.Heating, TAG.Discharge, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                    },
                                    "Min_Unoccupied_Heating_Discharge_Air_Flow_Setpoint_Limit": {
                                        "tags": [TAG.Min, TAG.Unoccupied, TAG.Heating, TAG.Discharge, TAG.Air, TAG.Flow, TAG.Setpoint, TAG.Limit],
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
