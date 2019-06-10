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
        "tags": [TAG.Setpoint],
        "subclasses": {
            "Enthalpy_Setpoint": {
                "tags": [TAG.Enthalpy, TAG.Setpoint],
            },
            "Dew_Point_Setpoint": {
                "tags": [TAG.Dewpoint, TAG.Setpoint],
            },
            "Demand_Setpoint": {
                "tags": [TAG.Demand, TAG.Setpoint],
                "subclasses": {
                    "Cooling_Demand_Setpoint": {
                        "tags": [TAG.Cooling, TAG.Demand, TAG.Setpoint],
                    },
                    "Cooling_Request_Percent_Setpoint": {},
                    "Cooling_Request_Setpoint": {},
                    "Heating_Demand_Setpoint": {
                        "tags": [TAG.Heating, TAG.Demand, TAG.Setpoint],
                    },
                    "Heating_Request_Percent_Setpoint": {},
                    "Heating_Request_Setpoint": {},
                    "Preheat_Demand_Setpoint": {},
                    "Air_Flow_Demand_Setpoint": {
                        "tags": [TAG.Air, TAG.Flow, TAG.Demand, TAG.Setpoint],
                        "subclasses": {
                            "Discharge_Air_Flow_Demand_Setpoint": {
                                "tags": [TAG.Discharge, TAG.Air, TAG.Flow, TAG.Demand, TAG.Setpoint],
                            },
                            "Supply_Air_Flow_Demand_Setpoint": {
                                "tags": [TAG.Supply, TAG.Air, TAG.Flow, TAG.Demand, TAG.Setpoint],
                            },
                        },
                    },
                },
            },
            "Damper_Position_Setpoint": {
                "tags": [TAG.Damper, TAG.Position, TAG.Setpoint],
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
                            "Air_Flow_Demand_Setpoint": {},
                            "Discharge_Air_Flow_Setpoint": {
                                "subclasses": {
                                    # Do the same for Max/Min? Occupied/Unoccupied?
                                    "Discharge_Air_Flow_Demand_Setpoint": {},
                                    "Cooling_Discharge_Air_Flow_Setpoint": {},
                                    "Heating_Discharge_Air_Flow_Setpoint": {},
                                },
                            },
                            "Exhaust_Air_Flow_Setpoint": {
                                "subclasses": {
                                    "Exhaust_Air_Stack_Flow_Setpoint": {},
                                },
                            },
                            "Fan_Air_Flow_Setpoint": {},
                            "Outside_Air_Flow_Setpoint": {},
                            "Supply_Air_Flow_Setpoint": {
                                "subclasses": {
                                    "Supply_Air_Flow_Demand_Setpoint": {},
                                    "Occupied_Supply_Air_Flow_Setpoint": {
                                        "subclasses": {
                                            "Occupied_Cooling_Supply_Air_Flow_Setpoint": {},
                                            "Occupied_Heating_Supply_Air_Flow_Setpoint": {},
                                        },
                                    },
                                    "Cooling_Supply_Air_Flow_Setpoint": {},
                                    "Heating_Supply_Air_Flow_Setpoint": {},
                                },
                            },
                        },
                    },
                },
            },
            "Humidity_Setpoint": {
                "subclasses": {
                    "High_Humidity_Alarm_Setpoint": {},
                    "Low_Humidity_Alarm_Setpoint": {},
                },
            },
            "Increase_Decrease_Step_Setpoint": {
                "subclasses": {
                    "Differential_Pressure_Increase_Decrease_Step_Setpoint": {
                        "subclasses": {
                            "Chilled_Water_Differential_Pressure_Increase_Decrease_Step_Setpoint": {},
                        },
                    },
                    "Static_Pressure_Increase_Decrease_Step_Setpoint": {
                        "subclasses": {
                            "Air_Static_Pressure_Increase_Decrease_Step_Setpoint": {},
                        },
                    },
                    "Temperature_Increase_Decrease_Step_Setpoint": {
                        "subclasses": {
                            "Air_Temperature_Increase_Decrease_Step_Setpoint": {},
                        },
                    },
                },
            },
            "Integral_Gain_Setpoint": {},
            "Integral_Time_Setpoint": {
                "subclasses": {
                  "Chilled_Water_Differential_Pressure_Integral_Time_Setpoint": {},
                  "Cooling_Discharge_Air_Temperature_Integral_Time_Setpoint": {},
                  "Cooling_Supply_Air_Temperature_Integral_Time_Setpoint": {},
                  "Differential_Pressure_Integral_Time": {
                    "subclasses": {
                        "Chilled_Water_Pump_Differential_Pressure_Integration_Time_Setpoint": {},
                    },
                  },
                  "Differential_Pressure_Integral_Time_Setpoint": {
                      "subclasses": {
                          "Hot_Water_Differential_Pressure_Integral_Time_Setpoint": {},
                      },
                  },
                  "Discharge_Air_Static_Pressure_Integral_Time_Setpoint": {},
                  "Exhaust_Air_Flow_Integral_Time_Setpoint": {
                      "subclasses": {
                          "Exhaust_Air_Stack_Flow_Integral_Time_Setpoint": {},
                      },
                  },
                  "Heating_Discharge_Air_Temperature_Integral_Time_Setpoint": {},
                  "Heating_Supply_Air_Temperature_Integral_Time_Setpoint": {},
                  "Static_Pressure_Integral_Time_Setpoint": {},
                  "Supply_Air_Static_Pressure_Integral_Time_Setpoint": {},
                  "Supply_Water_Differential_Pressure_Integral_Time_Setpoint": {},
                  "Supply_Water_Temperature_Integral_Time_Setpoint": {},
                },
            },
            "Load_Setpoint": {
                "subclasses": {
                    "Max_Load_Setpoint": {},
                },
            },
            "Luminance_Setpoint": {},
            "Mode_Setpoint": {
                "subclasses": {
                    "Dual_Band_Mode_Setpoint": {}, # are these duplicated elsewhere?
                    "Unoccupied_Mode_Setpoint": {},
                    "Occupied_Mode_Setpoint": {},
                },
            },
            "Pressure_Setpoint": {
                "subclasses": {
                    "Differential_Pressure_Setpoint": {
                        "subclasses": {
                            "Chilled_Water_Differential_Pressure_Setpoint": {},
                            "Hot_Water_Differential_Pressure_Setpoint": {},
                            "Load_Shed_Differential_Pressure_Setpoint": {
                                "subclasses": {
                                    "Chilled_Water_Differential_Pressure_Load_Shed_Setpoint": {},
                                    "Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed_Setpoint": {},
                                },
                            },
                        },
                    },
                    "Static_Pressure_Setpoint": {
                        "subclasses": {
                            "Building_Static_Pressure_Setpoint": {},
                            "Chilled_Water_Static_Pressure_Setpoint": {},
                            "Discharge_Air_Static_Pressure_Setpoint": {},
                            "Exhaust_Air_Static_Pressure_Setpoint": {},
                            "High_Static_Pressure_Cutout_Limit_Setpoint": {},
                            "Hot_Water_Static_Pressure_Setpoint": {},
                            "Supply_Air_Static_Pressure_Setpoint": {},
                        },
                    },
                    "Velocity_Pressure_Setpoint": {},
                },
            },
            "Proportional_Band_Setpoint": {
                "subclasses": {
                    "Chilled_Water_Differential_Pressure_Proportional_Band_Setpoint": {},
                    "Cooling_Discharge_Air_Temperature_Proportional_Band_Setpoint": {},
                    "Cooling_Supply_Air_Temperature_Proportional_Band_Setpoint": {},
                    "Differential_Pressure_Proportional_Band": {},
                    "Hot_Water_Differential_Pressure_Proportional_Band_Setpoint": {},
                    "Discharge_Air_Static_Pressure_Proportional_Band_Setpoint": {},
                    "Discharge_Air_Temperature_Proportional_Band_Setpoint": {},
                    "Supply_Air_Temperature_Proportional_Band_Setpoint": {},
                    "Exhaust_Air_Flow_Proportional_Band_Setpoint": {},
                    "Heating_Discharge_Air_Temperature_Proportional_Band_Setpoint": {},
                    "Heating_Supply_Air_Temperature_Proportional_Band_Setpoint": {},
                    "Static_Pressure_Proportional_Band_Setpoint": {
                        "subclasses": {
                            "Exhaust_Air_Static_Pressure_Proportional_Band_Setpoint": {},
                        },
                    },
                    "Supply_Air_Static_Pressure_Proportional_Band_Setpoint": {},
                    "Supply_Water_Differential_Pressure_Proportional_Band_Setpoint": {
                        "subclasses": {
                            "Thermal_Energy_Storage_Discharge_Water_Differential_Pressure_Proportional" "Band" "Setpoint": {},
                            "Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Proportional_Band" "Setpoint": {},
                        },
                    },
                    "Supply_Water_Temperature_Proportional_Band_Setpoint": {
                        "subclasses": {
                            "Heat_Exchanger_Discharge_Water_Temperature_Proportional_Band_Setpoint": {},
                            "Heat_Exchanger_Supply_Water_Temperature_Proportional_Band_Setpoint": {},
                        },
                    }
                },
            },
            "Reset_Setpoint": {
                "Discharge_Air_Flow_Reset_Setpoint": {
                    "subclasses": {
                        "Discharge_Air_Flow_Reset_High_Setpoint": {},
                        "Discharge_Air_Flow_Reset_Low_Setpoint": {},
                    },
                },
                "Discharge_Air_Temperature_Reset_High_Setpoint": {},
                "Discharge_Air_Temperature_Reset_Low_Setpoint": {},
                "Supply_Air_Temperature_Reset_High_Setpoint": {},
                "Supply_Air_Temperature_Reset_Low_Setpoint": {},
                "Temperature_Differential_Reset_Setpoint": {
                    "subclasses": {
                        "Discharge_Air_Temperature_Reset_Differential_Setpoint": {},
                        "Supply_Air_Temperature_Reset_Differential_Setpoint": {},
                    },
                },
                "Temperature_High_Reset_Setpoint": {
                    "subclasses": {
                        "Hot_Water_Supply_Temperature_High_Reset_Setpoint": {
                            "subclasses": {
                                "Medium_Temperature_Hot_Water_Discharge_Temperature_High_Reset_Setpoint": {},
                                "Medium_Temperature_Hot_Water_Supply_Temperature_High_Reset_Setpoint": {},
                            },
                        },
                    },
                  },
                "Outside_Air_Temperature_High_Reset_Setpoint": {},
                "Temperature_Low_Reset_Setpoint": {
                    "subclasses": {
                        "Hot_Water_Supply_Temperature_Low_Reset_Setpoint": {
                            "subclasses": {
                                "Medium_Temperature_Hot_Water_Discharge_Temperature_Low_Reset_Setpoint": {},
                                "Medium_Temperature_Hot_Water_Supply_Temperature_Low_Reset_Setpoint": {},
                            },
                        },
                        "Outside_Air_Temperature_Low_Reset_Setpoint": {},
                    },
                },
            },
            "Speed_Setpoint": {
                "subclasses": {
                    "Differential_Speed_Setpoint": {
                        "subclasses": {
                            "Return_Discharge_Fan_Differential_Speed_Setpoint": {},
                            "Return_Fan_Differential_Speed_Setpoint": {},
                            "Return_Supply_Fan_Differential_Speed_Setpoint": {},
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
}
