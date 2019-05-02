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

sensor_definitions = {
    "Sensor": {
        "tagvalues": [
            [BRICK.hasTag, TAG.Sensor]
        ],
        "subclasses": {
            "Air_Grains_Sensor": {
                "tagvalues": [
                    [BRICK.hasTag, TAG.Sensor],
                    [BRICK.hasTag, TAG.Air],
                    [BRICK.hasTag, TAG.Grains],
                ],
                "substances": [
                    [BRICK.measures, OWL.someValuesFrom, BRICK.Air],
                    [BRICK.measures, OWL.someValuesFrom, BRICK.Grains],
                    [RDF.type, OWL.hasValue, BRICK.Sensor],
                ],
                "subclasses": {
                    "Outside_Air_Grains_Sensor": {},
                    "Return_Air_Grains_Sensor": {},
                },
            },
            "Angle_Sensor": {
                "subclasses": {
                    "Solar_Azimuth_Angle_Sensor": {},
                    "Solar_Zenith_Angle_Sensor": {},
                },
            },
            "CO2_Sensor": {
                "tagvalues": [
                    [BRICK.hasTag, TAG.Sensor],
                    [BRICK.hasTag, TAG.CO2],
                ],
                "substances": [
                    [BRICK.measures, OWL.someValuesFrom, BRICK.CO2],
                    [RDF.type, OWL.hasValue, BRICK.Sensor],
                ],
                "subclasses": {
                    "CO2_Differential_Sensor": {},
                    "CO2_Level_Sensor": {},
                    "Outside_Air_CO2_Sensor": {},
                    "Return_Air_CO2_Sensor": {},
                },
            },
            "Capacity_Sensor": {
                "tagvalues": [
                    [BRICK.hasTag, TAG.Sensor],
                    [BRICK.hasTag, TAG.Capacity],
                ],
            },
            "Conductivity_Sensor": {
                "tagvalues": [
                    [BRICK.hasTag, TAG.Sensor],
                    [BRICK.hasTag, TAG.Conductivity],
                ],
                "subclasses": {
                    "Deionised_Water_Conductivity_Sensor": {
                        "substances": [
                            [BRICK.measures, OWL.someValuesFrom, BRICK.Water, OWL.minCardinality, 1],
                            [RDF.type, OWL.hasValue, BRICK.Sensor],
                        ],
                    },
                },
            },
            "Current_Sensor": {
                "tagvalues": [
                    [BRICK.hasTag, TAG.Sensor],
                    [BRICK.hasTag, TAG.Current],
                ],
                "subclasses": {
                    "Load_Current_Sensor": {},
                    "Motor_Current_Sensor": {},
                    "Photovoltaic_Current_Output_Sensor": {
                        OWL.equivalentClass: "PV_Current_Output_Sensor",
                    },
                },
            },
            "Damper_Position_Sensor": {},
            "Demand_Sensor": {
                "tagvalues": [
                    [BRICK.hasTag, TAG.Sensor],
                    [BRICK.hasTag, TAG.Power],
                ],
                "subclasses": {
                    "Peak_Power_Demand_Sensor": {},    
                },
            },
            "Dewpoint_Sensor": {
                "tagvalues": [
                    [BRICK.hasTag, TAG.Sensor],
                    [BRICK.hasTag, TAG.Dewpoint],
                ],
                "substances": [
                    [BRICK.measures, OWL.someValuesFrom, BRICK.Air, OWL.minCardinality, 1],
                    [RDF.type, OWL.hasValue, BRICK.Sensor],
                ],
                "subclasses": {
                    "Outside_Air_Dewpoint_Sensor": {},
                    "Return_Air_Dewpoint_Sensor": {},
                },
            },
            "Direction_Sensor": {
                "subclasses": {
                    "Wind_Direction_Sensor": {},
                },
            },
            "Energy_Sensor": {
                "tagvalues": [
                    [BRICK.hasTag, TAG.Sensor],
                    [BRICK.hasTag, TAG.Energy],
                ],
            },
            "Enthalpy_Sensor": {
                "tagvalues": [
                    [BRICK.hasTag, TAG.Sensor],
                    [BRICK.hasTag, TAG.Enthalpy],
                ],
                "subclasses": {
                    "Air_Enthalpy_Sensor": {
                        "substances": [
                            [BRICK.measures, OWL.someValuesFrom, BRICK.Air, OWL.minCardinality, 1],
                            [RDF.type, OWL.hasValue, BRICK.Sensor],
                        ],
                        "subclasses": {
                            "Outside_Air_Enthalpy_Sensor": {},
                            "Return_Air_Enthalpy_Sensor": {},
                        },
                    },
                },
            },
            "Flow_Sensor": {
                "tagvalues": [
                    [BRICK.hasTag, TAG.Sensor],
                    [BRICK.hasTag, TAG.Flow],
                ],
                "subclasses": {
                    "Air_Flow_Sensor": {
                        "tagvalues": [
                            [BRICK.hasTag, TAG.Sensor],
                            [BRICK.hasTag, TAG.Air],
                            [BRICK.hasTag, TAG.Flow],
                        ],
                        "substances": [
                            [BRICK.measures, OWL.someValuesFrom, BRICK.Air, OWL.minCardinality, 1],
                            [RDF.type, OWL.hasValue, BRICK.Flow_Sensor],
                        ],
                        "subclasses": {
                            "Bypass_Air_Flow_Sensor": {},
                            "Discharge_Air_Flow_Sensor": {
                                "subclasses": {
                                    "Average_Discharge_Air_Flow_Sensor": {},
                                    "Average_Supply_Air_Flow_Sensor": {},
                                },
                            },
                            "Exhaust_Air_Flow_Sensor": {
                                "subclasses": {
                                    "Exhaust_Air_Stack_Flow_Sensor": {},
                                },
                            },
                            # TODO elide this and just attach to equipment?
                            "Fan_Air_Flow_Sensor": {
                                "subclasses": {
                                    "Booster_Fan_Air_Flow_Sensor":{},
                                    "Discharge_Fan_Air_Flow_Sensor":{},
                                    "Return_Fan_Air_Flow_Sensor":{},
                                    "Supply_Fan_Air_Flow_Sensor":{},
                                },
                            },
                            "Fume_Hood_Air_Flow_Sensor": {},
                            "Outside_Air_Flow_Sensor": {},
                            "Return_Air_Flow_Sensor": {},
                            "Supply_Air_Flow_Sensor": {},
                        },
                    },
                    "Water_Flow_Sensor": {
                        "tagvalues": [
                            [BRICK.hasTag, TAG.Sensor],
                            [BRICK.hasTag, TAG.Water],
                            [BRICK.hasTag, TAG.Flow],
                        ],
                        "substances": [
                            [BRICK.measures, OWL.someValuesFrom, BRICK.Water, OWL.minCardinality, 1],
                            [RDF.type, OWL.hasValue, BRICK.Flow_Sensor],
                        ],
                        "subclasses": {
                            "Supply_Water_Flow_Sensor": {
                                "subclasses": {
                                    "Chilled_Water_Discharge_Flow_Sensor": {},
                                    "Chilled_Water_Supply_Flow_Sensor": {},
                                },
                            },
                        },
                    },
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
                            #[BRICK.measures, OWL.someValuesFrom, BRICK.Air],
                            #[RDF.type, OWL.hasValue, BRICK.Temperature_Sensor],
                            [BRICK.measures, OWL.someValuesFrom, BRICK.Air, OWL.minCardinality, 1],
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
