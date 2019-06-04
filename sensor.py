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
        "tags": [TAG.Sensor],
        "subclasses": {
            "Air_Grains_Sensor": {
                "tags": [TAG.Sensor, TAG.Air, TAG.Grains],
                "substances": [
                    [BRICK.measures, BRICK.Air],
                    [BRICK.measures, BRICK.Grains],
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
                "tags": [TAG.Sensor, TAG.CO2],
                "substances": [
                    [BRICK.measures, BRICK.Air],
                    [BRICK.measures, BRICK.CO2],
                ],
                "subclasses": {
                    "CO2_Differential_Sensor": {},
                    "CO2_Level_Sensor": {},
                    "Outside_Air_CO2_Sensor": {},
                    "Return_Air_CO2_Sensor": {},
                },
            },
            "Capacity_Sensor": {
                "tags": [TAG.Sensor, TAG.Capacity],
                "substances": [
                    [BRICK.measures, BRICK.Capacity],
                ],
            },
            "Conductivity_Sensor": {
                "tags": [TAG.Sensor, TAG.Conductivity],
                "substances": [
                    [BRICK.measures, BRICK.Conductivity],
                ],
                "subclasses": {
                    "Deionised_Water_Conductivity_Sensor": {
                        "tags": [TAG.Sensor, TAG.Conductivity, TAG.Water, TAG.Deionised],
                    },
                },
            },
            "Current_Sensor": {
                "tags": [TAG.Sensor, TAG.Current],
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
                "tags": [TAG.Sensor, TAG.Power],
                "substances": [
                    [BRICK.measures, BRICK.Power],
                ],
                "subclasses": {
                    "Peak_Power_Demand_Sensor": {},    
                },
            },
            "Dewpoint_Sensor": {
                "tags": [TAG.Sensor, TAG.Dewpoint],
                "substances": [
                    [BRICK.measures, BRICK.Dewpoint],
                ],
                "subclasses": {
                    "Outside_Air_Dewpoint_Sensor": {
                        "tags": [TAG.Sensor, TAG.Dewpoint, TAG.Air, TAG.Outside],
                    },
                    "Return_Air_Dewpoint_Sensor": {
                        "tags": [TAG.Sensor, TAG.Dewpoint, TAG.Air, TAG.Return],
                    },
                },
            },
            "Direction_Sensor": {
                "tags": [TAG.Sensor, TAG.Direction],
                "substances": [
                    [BRICK.measures, BRICK.Direction],
                ],
                "subclasses": {
                    "Wind_Direction_Sensor": {
                        "tags": [TAG.Sensor, TAG.Direction, TAG.Wind],
                        "substances": [
                            [BRICK.measures, BRICK.Wind_Direction],
                        ],
                    },
                },
            },
            "Energy_Sensor": {
                "tags": [TAG.Sensor, TAG.Energy],
                "substances": [
                    [BRICK.measures, BRICK.Energy],
                ],
            },
            "Enthalpy_Sensor": {
                "tags": [TAG.Sensor, TAG.Enthalpy],
                "substances": [
                    [BRICK.measures, BRICK.Enthalpy],
                ],
                "subclasses": {
                    "Air_Enthalpy_Sensor": {
                        "substances": [
                            [BRICK.measures, BRICK.Enthalpy],
                            [BRICK.measures, BRICK.Air],
                        ],
                        "subclasses": {
                            "Outside_Air_Enthalpy_Sensor": {},
                            "Return_Air_Enthalpy_Sensor": {},
                        },
                    },
                },
            },
            "Flow_Sensor": {
                "tags": [TAG.Sensor, TAG.Flow],
                "substances": [
                    [BRICK.measures, BRICK.Flow],
                ],
                "subclasses": {
                    "Air_Flow_Sensor": {
                        "substances": [
                            [BRICK.measures, BRICK.Flow],
                            [BRICK.measures, BRICK.Air],
                        ],
                        "tags": [TAG.Sensor, TAG.Flow, TAG.Air],
                        "subclasses": {
                            "Bypass_Air_Flow_Sensor": {
                                "tags": [TAG.Sensor, TAG.Flow, TAG.Air, TAG.Bypass],
                            },
                            "Discharge_Air_Flow_Sensor": {
                                "tags": [TAG.Sensor, TAG.Flow, TAG.Air, TAG.Discharge],
                                "subclasses": {
                                    "Average_Discharge_Air_Flow_Sensor": {},
                                    "Average_Supply_Air_Flow_Sensor": {},
                                },
                            },
                            "Exhaust_Air_Flow_Sensor": {
                                "tags": [TAG.Sensor, TAG.Flow, TAG.Air, TAG.Exhaust],
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
                            "Outside_Air_Flow_Sensor": {
                                "tags": [TAG.Sensor, TAG.Flow, TAG.Air, TAG.Outside],
                            },
                            "Return_Air_Flow_Sensor": {
                                "tags": [TAG.Sensor, TAG.Flow, TAG.Air, TAG.Return],
                            },
                            "Supply_Air_Flow_Sensor": {
                                "tags": [TAG.Sensor, TAG.Flow, TAG.Air, TAG.Supply],
                            },
                        },
                    },
                    "Water_Flow_Sensor": {
                        "tags": [TAG.Sensor, TAG.Flow, TAG.Water],
                        "substances": [
                            [BRICK.measures, BRICK.Flow],
                            [BRICK.measures, BRICK.Water],
                        ],
                        "subclasses": {
                            "Supply_Water_Flow_Sensor": {
                                "tags": [TAG.Sensor, TAG.Flow, TAG.Water, TAG.Supply],
                                "subclasses": {
                                    "Chilled_Water_Discharge_Flow_Sensor": {
                                        "tags": [TAG.Sensor, TAG.Flow, TAG.Water, TAG.Discharge, TAG.Chilled],
                                    },
                                    "Chilled_Water_Supply_Flow_Sensor": {
                                        "tags": [TAG.Sensor, TAG.Flow, TAG.Water, TAG.Supply, TAG.Chilled],
                                    },
                                },
                            },
                        },
                    },
                },
            },
            "Frequency_Sensor": {
                "substances": [
                    [BRICK.measures, BRICK.Frequency],
                ],
                "tags": [TAG.Sensor, TAG.Frequency],
                "subclasses": {
                    "Output_Frequency_Sensor": {},
                },
            },
            "Frost_Sensor": {
                "tags": [TAG.Sensor, TAG.Frost],
                "substances": [
                    [BRICK.measures, BRICK.Frost],
                ],
            },
            "Hail_Sensor": {
                "tags": [TAG.Sensor, TAG.Hail],
                "substances": [
                    [BRICK.measures, BRICK.Hail],
                ],
            },
            "Humidity_Sensor": {
                "tags": [TAG.Sensor, TAG.Humidity],
                "substances": [
                    [BRICK.measures, BRICK.Humidity],
                ],
                "subclasses": {
                    "Air_Humidity_Sensor": {
                        "tags": [TAG.Sensor, TAG.Humidity, TAG.Air],
                        "substances": [
                            [BRICK.measures, BRICK.Humidity],
                            [BRICK.measures, BRICK.Air],
                        ],
                        "subclasses": {
                            "Discharge_Air_Humidity_Sensor:":{
                                "tags": [TAG.Sensor, TAG.Humidity, TAG.Air, TAG.Discharge],
                            },
                            "Exhaust_Air_Humidity_Sensor:":{
                                "tags": [TAG.Sensor, TAG.Humidity, TAG.Air, TAG.Exhaust],
                            },
                            "Outside_Air_Humidity_Sensor:":{
                                "tags": [TAG.Sensor, TAG.Humidity, TAG.Air, TAG.Outside],
                            },
                            "Relative_Humidity_Sensor:":{
                                "tags": [TAG.Sensor, TAG.Humidity, TAG.Air, TAG.Relative],
                            },
                            "Return_Air_Humidity_Sensor:":{
                                "tags": [TAG.Sensor, TAG.Humidity, TAG.Air, TAG.Return],
                            },
                            "Supply_Air_Humidity_Sensor:":{
                                "tags": [TAG.Sensor, TAG.Humidity, TAG.Air, TAG.Supply],
                            },
                            "Zone_Humidity_Sensor:":{
                                "tags": [TAG.Sensor, TAG.Humidity, TAG.Zone],
                            },
                        },
                    },
                },
            },
            "Luminance_Sensor": {
                "tags": [TAG.Sensor, TAG.Luminance],
                "substances": [
                    [BRICK.measures, BRICK.Luminance],
                ],
                "subclasses": {
                    "Outside_Luminance_Sensor": {
                        "tags": [TAG.Sensor, TAG.Luminance, TAG.Outside],
                    },
                },
            },
            "Motion_Sensor": {
                "tags": [TAG.Sensor, TAG.Motion],
                "subclasses": {
                    "PIR_Sensor": {
                        "tags": [TAG.Sensor, TAG.PIR],
                    },
                },
            },
            "Occupancy_Sensor": {
                "tags": [TAG.Sensor, TAG.Occupancy],
                "subclasses": {
                    "PIR_Sensor": {},
                },
            },
            "Piezoelectric_Sensor": {
                "tags": [TAG.Sensor, TAG.Piezoelectric],
            },
            "Pressure_Sensor": {
                "tags": [TAG.Sensor, TAG.Pressure],
                "substances": [
                    [BRICK.measures, BRICK.Pressure],
                ],
                "subclasses": {
                    "Differential_Pressure_Sensor": {
                        "tags": [TAG.Sensor, TAG.Pressure, TAG.Differential],
                        "subclasses": {
                            "Chilled_Water_Differential_Pressure_Sensor": {
                                "tags": [TAG.Sensor, TAG.Pressure, TAG.Differential, TAG.Water, TAG.Chilled],
                                "substances": [
                                    [BRICK.measures, BRICK.Pressure],
                                    [BRICK.measures, BRICK.Water],
                                ],
                            },
                            "Filter_Differential_Pressure_Sensor": {
                                "tags": [TAG.Sensor, TAG.Pressure, TAG.Differential, TAG.Filter],
                            },
                            "Heat_Wheel_Differential_Pressure_Sensor": {
                                "tags": [TAG.Sensor, TAG.Pressure, TAG.Differential, TAG.Wheel, TAG.Heat],
                            },
                            "Hot_Water_Differential_Pressure_Sensor": {
                                "tags": [TAG.Sensor, TAG.Pressure, TAG.Differential, TAG.Water, TAG.Hot],
                                "substances": [
                                    [BRICK.measures, BRICK.Pressure],
                                    [BRICK.measures, BRICK.Water],
                                ],
                                "subclasses": {
                                    "Medium_Temperature_Hot_Water_Differential_Pressure_Sensor": {},
                                },
                            },
                        },
                    },
                    "Static_Pressure_Sensor": {
                        "tags": [TAG.Sensor, TAG.Pressure, TAG.Static],
                        "subclasses": {
                            "Building_Static_Pressure_Sensor:": {
                                "substances": [
                                    [BRICK.measures, BRICK.Pressure],
                                    [BRICK.measures, BRICK.Air],
                                ],
                            },
                            "Discharge_Air_Static_Pressure_Sensor:": {
                                "tags": [TAG.Sensor, TAG.Pressure, TAG.Static, TAG.Air, TAG.Discharge],
                                "substances": [
                                    [BRICK.measures, BRICK.Pressure],
                                    [BRICK.measures, BRICK.Air],
                                ],
                            },
                            "Supply_Air_Static_Pressure_Sensor:": {
                                "tags": [TAG.Sensor, TAG.Pressure, TAG.Static, TAG.Air, TAG.Supply],
                                "substances": [
                                    [BRICK.measures, BRICK.Pressure],
                                    [BRICK.measures, BRICK.Air],
                                ],
                            },
                            "Exhaust_Air_Static_Pressure_Sensor:": {
                                "tags": [TAG.Sensor, TAG.Pressure, TAG.Static, TAG.Air, TAG.Exhaust],
                                "substances": [
                                    [BRICK.measures, BRICK.Pressure],
                                    [BRICK.measures, BRICK.Air],
                                ],
                                "subclasses": {
                                    "Average_Exhaust_Air_Static_Pressure_Sensor:": {},
                                    "Lowest_Exhaust_Air_Static_Pressure_Sensor:": {},
                                },
                            },
                        },
                    },
                    "Velocity_Pressure_Sensor:": {
                        "tags": [TAG.Sensor, TAG.Pressure, TAG.Velocity],
                        "subclasses": {
                            "Discharge_Air_Velocity_Pressure_Sensor:": {
                                "tags": [TAG.Sensor, TAG.Pressure, TAG.Velocity, TAG.Discharge, TAG.Air],
                            },
                            "Exhaust_Air_Velocity_Pressure_Sensor:": {
                                "tags": [TAG.Sensor, TAG.Pressure, TAG.Velocity, TAG.Exhaust, TAG.Air],
                            },
                            "Supply_Air_Velocity_Pressure_Sensor:": {
                                "tags": [TAG.Sensor, TAG.Pressure, TAG.Velocity, TAG.Supply, TAG.Air],
                            },
                        },
                    }
                },
            },
            "Rain_Sensor": {
                "tags": [TAG.Sensor, TAG.Rain],
                "subclasses": {
                    "Rain_Duration_Sensor": {
                        "tags": [TAG.Sensor, TAG.Rain, TAG.Duration],
                    },
                },
            },
            "Duration_Sensor": {
                "tags": [TAG.Sensor, TAG.Duration],
                "subclasses": {
                    "Rain_Duration_Sensor": {},
                    "Run_Time_Sensor": {},
                    "On_Timer_Sensor": {},
                },
            },
            "Solar_Radiance_Sensor": {
                "tags": [TAG.Sensor, TAG.Radiance, TAG.Solar],
            },
            "Speed_Sensor": {
                "tags": [TAG.Sensor, TAG.Speed],
                "substances": [
                    [BRICK.measures, BRICK.Speed],
                ],
                "subclasses": {
                    "Differential_Speed_Sensor": {
                        "tags": [TAG.Sensor, TAG.Speed, TAG.Differential],
                        "subclasses": {
                            "Heat_Wheel_Speed_Sensor": {
                                "tags": [TAG.Sensor, TAG.Speed, TAG.Heat, TAG.Wheel],
                            },
                            "Return_Fan_Differential_Speed_Sensor": {},
                        },
                    },
                    "Motor_Speed_Sensor": {},
                    "Wind_Speed_Sensor": {
                        "tags": [TAG.Sensor, TAG.Speed, TAG.Wind],
                        "substances": [
                            [BRICK.measures, BRICK.Wind_Speed],
                        ],
                    },
                },
            },
            "Torque_Sensor": {
                "tags": [TAG.Sensor, TAG.Torque],
                "subclasses": {
                    "Motor_Torque_Sensor": {},
                },
            },
            "Trace_Heat_Sensor": {},
            "Voltage_Sensor": {
                "tags": [TAG.Sensor, TAG.Voltage],
                "substances": [
                    [BRICK.measures, BRICK.Voltage],
                ],
                "subclasses": {
                    "Battery_Voltage_Sensor": {
                        "tags": [TAG.Sensor, TAG.Voltage, TAG.Battery],
                    },
                    "DC_Bus_Voltage_Sensor": {},
                    "Heat_Wheel_Voltage_Sensor": {},
                    "Output_Voltage_Sensor": {},
                },
            },
            "Water_Level_Sensor": {
                "tags": [TAG.Sensor, TAG.Water, TAG.Level],
                "substances": [
                    [BRICK.measures, BRICK.Water],
                    [BRICK.measures, BRICK.Level],
                ],
                "subclasses": {
                    "Deionised_Water_Level_Sensor": {
                        "tags": [TAG.Sensor, TAG.Water, TAG.Level, TAG.Deionised],
                        OWL.equivalentClass: "DI_Water_Level_Sensor",
                    }
                },
            },
            "Temperature_Sensor": {
                "tags": [TAG.Sensor, TAG.Temperature],
                "substances": [
                    [BRICK.measures, BRICK.Temperature],
                ],
                "subclasses": {
                    "Zone_Temperature_Sensor": {
                        "tags": [TAG.Sensor, TAG.Temperature, TAG.Zone],
                        "subclasses": {
                            "Average_Zone_Temperature_Sensor": {
                                "tags": [TAG.Sensor, TAG.Temperature, TAG.Zone, TAG.Average],
                            },
                            "Highest_Zone_Temperature_Sensor": {
                                "tags": [TAG.Sensor, TAG.Temperature, TAG.Zone, TAG.Highest],
                                OWL.equivalentClass: "Warmest_Zone_Temperature_Sensor"
                            },
                            "Lowest_Zone_Temperature_Sensor": {
                                "tags": [TAG.Sensor, TAG.Temperature, TAG.Zone, TAG.Lowest],
                                OWL.equivalentClass: "Coldest_Zone_Temperature_Sensor"
                            },
                        },
                    },
                    "Air_Temperature_Sensor": {
                        "tags": [TAG.Sensor, TAG.Temperature, TAG.Air],
                        "substances": [
                            [BRICK.measures, BRICK.Temperature],
                            [BRICK.measures, BRICK.Air],
                        ],
                        "subclasses": {
                            "Discharge_Air_Temperature_Sensor": {
                                "tags": [TAG.Sensor, TAG.Temperature, TAG.Air, TAG.Discharge],
                                OWL.equivalentClass: "Supply_Air_Temperature_Sensor",
                                "subclasses": {
                                    "Cooling_Coil_Discharge_Air_Temperature_Sensor": {},
                                    "Heat_Wheel_Discharge_Air_Temperature_Sensor": {},
                                    "Preheat_Discharge_Air_Temperature_Sensor": {},
                                },
                            },
                            "Zone_Air_Temperature_Sensor": {},
                            "Exhaust_Air_Temperature_Sensor": {
                                "tags": [TAG.Sensor, TAG.Temperature, TAG.Air, TAG.Exhaust],
                            },
                            "Mixed_Air_Temperature_Sensor": {
                                "tags": [TAG.Sensor, TAG.Temperature, TAG.Air, TAG.Mixed],
                            },
                            "Return_Air_Temperature_Sensor": {
                                "tags": [TAG.Sensor, TAG.Temperature, TAG.Air, TAG.Return],
                            },
                            "Outside_Air_Temperature_Sensor": {
                                "tags": [TAG.Sensor, TAG.Temperature, TAG.Air, TAG.Outside],
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
                        "tags": [TAG.Sensor, TAG.Temperature, TAG.Water],
                        "substances": [
                            [BRICK.measures, BRICK.Temperature],
                            [BRICK.measures, BRICK.Water],
                        ],
                        "subclasses": {
                            "Heat_Exchanger_Supply_Water_Temperature_Sensor": {},
                            "Hot_Water_Supply_Temperature_Sensor": {
                                "tags": [TAG.Sensor, TAG.Temperature, TAG.Water, TAG.Hot, TAG.Supply],
                                "subclasses": {
                                    "Domestic_Hot_Water_Supply_Temperature_Sensor": {},
                                    "High_Temperature_Hot_Water_Supply_Temperature_Sensor": {},
                                    "Medium_Temperature_Hot_Water_Supply_Temperature_Sensor": {},
                                },
                            },
                            "Chilled_Water_Temperature_Sensor": {
                                "tags": [TAG.Sensor, TAG.Temperature, TAG.Water, TAG.Chilled],
                                "subclasses": {
                                    "Chilled_Water_Differential_Temperature_Sensor": {},
                                    "Chilled_Water_Supply_Temperature_Sensor": {
                                        "tags": [TAG.Sensor, TAG.Temperature, TAG.Water, TAG.Chilled, TAG.Supply],
                                        OWL.equivalentClass: "Chilled_Water_Discharge_Temperature_Sensor",
                                    },
                                },
                            },
                            "Entering_Water_Temperature_Sensor": {
                                "tags": [TAG.Sensor, TAG.Temperature, TAG.Water, TAG.Entering],
                                "subclasses": {
                                    "Hot_Water_Coil_Entering_Temperature_Sensor": {},
                                    "Ice_Tank_Entering_Water_Temperature_Sensor": {},
                                    "PreHeat_Coil_Entering_Air_Temperature_Sensor": {},
                                },
                            },
                            "Leaving_Water_Temperature_Sensor": {
                                "tags": [TAG.Sensor, TAG.Temperature, TAG.Water, TAG.Leaving],
                                "subclasses": {
                                    "Ice_Tank_Leaving_Water_Temperature_Sensor": {},
                                    "PreHeat_Coil_Leaving_Air_Temperature_Sensor": {},
                                },
                            },
                            "Return_Water_Temperature_Sensor": {
                                "tags": [TAG.Sensor, TAG.Temperature, TAG.Water, TAG.Return],
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
