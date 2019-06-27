from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.collection import Collection
from rdflib.extras.infixowl import Restriction

from namespaces import *


sensor_definitions = {
    "Sensor": {
        "tags": [ TAG.Sensor ],
        "subclasses": {
            "Air_Grains_Sensor": {
                "tags": [ TAG.Sensor, TAG.Air, TAG.Grains ],
                "substances": [ [ BRICK.measures, BRICK.Air ], [ BRICK.measures, BRICK.Grains ], ],
                "subclasses": {
                    "Outside_Air_Grains_Sensor": {
                        "tags": [ TAG.Outside, TAG.Air, TAG.Grains, TAG.Sensor ],
                    },
                    "Return_Air_Grains_Sensor": {
                        "tags": [ TAG.Return, TAG.Air, TAG.Grains, TAG.Sensor ],
                    }
                }
            },
            "Angle_Sensor": {
                "subclasses": {
                    "Solar_Azimuth_Angle_Sensor": {
                        "tags": [ TAG.Solar, TAG.Azimuth, TAG.Angle, TAG.Sensor ],
                    },
                    "Solar_Zenith_Angle_Sensor": {
                        "tags": [ TAG.Solar, TAG.Zenith, TAG.Angle, TAG.Sensor ],
                    }
                },
                "tags": [ TAG.Angle, TAG.Sensor ],
            },
            "CO2_Sensor": {
                "tags": [ TAG.Sensor, TAG.CO2 ],
                "substances": [ [ BRICK.measures, BRICK.Air ], [ BRICK.measures, BRICK.CO2 ], ],
                "subclasses": {
                    "CO2_Differential_Sensor": {
                        "tags": [ TAG.Co2, TAG.Differential, TAG.Sensor ],
                    },
                    "CO2_Level_Sensor": {
                        "tags": [ TAG.Co2, TAG.Level, TAG.Sensor ],
                    },
                    "Outside_Air_CO2_Sensor": {
                        "tags": [ TAG.Outside, TAG.Air, TAG.Co2, TAG.Sensor ],
                    },
                    "Return_Air_CO2_Sensor": {
                        "tags": [ TAG.Return, TAG.Air, TAG.Co2, TAG.Sensor ],
                    }
                }
            },
            "Capacity_Sensor": {
                "tags": [ TAG.Sensor, TAG.Capacity ],
                "substances": [ [ BRICK.measures, BRICK.Capacity ], ], },
            "Conductivity_Sensor": {
                "tags": [ TAG.Sensor, TAG.Conductivity ],
                "substances": [ [ BRICK.measures, BRICK.Conductivity ], ],
                "subclasses": {
                    "Deionised_Water_Conductivity_Sensor": {
                        "tags": [ TAG.Sensor, TAG.Conductivity, TAG.Water, TAG.Deionised ],
                    }
                }
            },
            "Current_Sensor": {
                "tags": [ TAG.Sensor, TAG.Current ],
                "subclasses": {
                    "Load_Current_Sensor": {
                        "tags": [ TAG.Load, TAG.Current, TAG.Sensor ],
                    },
                    "Motor_Current_Sensor": {
                        "tags": [ TAG.Motor, TAG.Current, TAG.Sensor ],
                    },
                    "Photovoltaic_Current_Output_Sensor": {
                        OWL.equivalentClass: "PV_Current_Output_Sensor",
                        "tags": [ TAG.Photovoltaic, TAG.Current, TAG.Output, TAG.Sensor ],
                    }
                }
            },
            "Damper_Position_Sensor": {
                "tags": [ TAG.Damper, TAG.Position, TAG.Sensor ],
            },
            "Demand_Sensor": {
                "tags": [ TAG.Sensor, TAG.Power ],
                "substances": [ [ BRICK.measures, BRICK.Power ], ],
                "subclasses": {
                    "Active_Power_Sensor": {
                        "tags": [ TAG.Sensor, TAG.Power, TAG.Active ],
                    },
                    "Reactive_Power_Sensor": {
                        "tags": [ TAG.Sensor, TAG.Power, TAG.Reactive ],
                    },
                    "Real_Power_Sensor": {
                        "tags": [ TAG.Sensor, TAG.Power, TAG.Real ],
                    },
                    "Peak_Power_Demand_Sensor": {
                        "tags": [ TAG.Peak, TAG.Power, TAG.Demand, TAG.Sensor ],
                    }
                }
            },
            "Dewpoint_Sensor": {
                "tags": [ TAG.Sensor, TAG.Dewpoint ],
                "substances": [ [ BRICK.measures, BRICK.Dewpoint ], ],
                "subclasses": {
                    "Outside_Air_Dewpoint_Sensor": {
                        "tags": [ TAG.Sensor, TAG.Dewpoint, TAG.Air, TAG.Outside ],
                    },
                    "Return_Air_Dewpoint_Sensor": {
                        "tags": [ TAG.Sensor, TAG.Dewpoint, TAG.Air, TAG.Return ],
                    }
                }
            },
            "Direction_Sensor": {
                "tags": [ TAG.Sensor, TAG.Direction ],
                "substances": [ [ BRICK.measures, BRICK.Direction ], ],
                "subclasses": {
                    "Wind_Direction_Sensor": {
                        "tags": [ TAG.Sensor, TAG.Direction, TAG.Wind ],
                        "substances": [ [ BRICK.measures, BRICK.Wind_Direction ], ],
                    }
                }
            },
            "Energy_Sensor": {
                "tags": [ TAG.Sensor, TAG.Energy ],
                "substances": [ [ BRICK.measures, BRICK.Energy ], ],
            },
            "Enthalpy_Sensor": {
                "tags": [ TAG.Sensor, TAG.Enthalpy ],
                "substances": [ [ BRICK.measures, BRICK.Enthalpy ], ],
                "subclasses": {
                    "Air_Enthalpy_Sensor": {
                        "substances": [ [ BRICK.measures, BRICK.Enthalpy ], [ BRICK.measures, BRICK.Air ], ],
                        "subclasses": {
                            "Outside_Air_Enthalpy_Sensor": {
                                "tags": [ TAG.Outside, TAG.Air, TAG.Enthalpy, TAG.Sensor ],
                            },
                            "Return_Air_Enthalpy_Sensor": {
                                "tags": [ TAG.Return, TAG.Air, TAG.Enthalpy, TAG.Sensor ],
                            }
                        },
                        "tags": [ TAG.Air, TAG.Enthalpy, TAG.Sensor ],
                    }
                }
            },
            "Flow_Sensor": {
                "tags": [ TAG.Sensor, TAG.Flow ],
                "substances": [ [ BRICK.measures, BRICK.Flow ], ],
                "subclasses": {
                    "Air_Flow_Sensor": {
                        "substances": [ [ BRICK.measures, BRICK.Flow ], [ BRICK.measures, BRICK.Air ], ],
                        "tags": [ TAG.Sensor, TAG.Flow, TAG.Air ],
                        "subclasses": {
                            "Bypass_Air_Flow_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Flow, TAG.Air, TAG.Bypass ],
                            },
                            "Discharge_Air_Flow_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Flow, TAG.Air, TAG.Discharge ],
                                "subclasses": {
                                    "Average_Discharge_Air_Flow_Sensor": {
                                        "tags": [ TAG.Average, TAG.Discharge, TAG.Air, TAG.Flow, TAG.Sensor ],
                                    },
                                    "Average_Supply_Air_Flow_Sensor": {
                                        "tags": [ TAG.Average, TAG.Supply, TAG.Air, TAG.Flow, TAG.Sensor ],
                                    }
                                }
                            },
                            "Exhaust_Air_Flow_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Flow, TAG.Air, TAG.Exhaust ],
                                "subclasses": {
                                    "Exhaust_Air_Stack_Flow_Sensor": {
                                        "tags": [ TAG.Exhaust, TAG.Air, TAG.Stack, TAG.Flow, TAG.Sensor ],
                                    }
                                }
                            },
                            "Fan_Air_Flow_Sensor": {
                                "subclasses": {
                                    "Booster_Fan_Air_Flow_Sensor": {
                                        "tags": [ TAG.Booster, TAG.Fan, TAG.Air, TAG.Flow, TAG.Sensor ],
                                    },
                                    "Discharge_Fan_Air_Flow_Sensor": {
                                        "tags": [ TAG.Discharge, TAG.Fan, TAG.Air, TAG.Flow, TAG.Sensor ],
                                    },
                                    "Return_Fan_Air_Flow_Sensor": {
                                        "tags": [ TAG.Return, TAG.Fan, TAG.Air, TAG.Flow, TAG.Sensor ],
                                    },
                                    "Supply_Fan_Air_Flow_Sensor": {
                                        "tags": [ TAG.Supply, TAG.Fan, TAG.Air, TAG.Flow, TAG.Sensor ],
                                    }
                                },
                                "tags": [ TAG.Fan, TAG.Air, TAG.Flow, TAG.Sensor ],
                            },
                            "Fume_Hood_Air_Flow_Sensor": {
                                "tags": [ TAG.Fume, TAG.Hood, TAG.Air, TAG.Flow, TAG.Sensor ],
                            },
                            "Outside_Air_Flow_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Flow, TAG.Air, TAG.Outside ],
                            },
                            "Return_Air_Flow_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Flow, TAG.Air, TAG.Return ],
                            },
                            "Supply_Air_Flow_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Flow, TAG.Air, TAG.Supply ],
                            }
                        }
                    },
                    "Water_Flow_Sensor": {
                        "tags": [ TAG.Sensor, TAG.Flow, TAG.Water ],
                        "substances": [ [ BRICK.measures, BRICK.Flow ], [ BRICK.measures, BRICK.Water ], ],
                        "subclasses": {
                            "Supply_Water_Flow_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Flow, TAG.Water, TAG.Supply ],
                                "subclasses": {
                                    "Chilled_Water_Discharge_Flow_Sensor": {
                                        "tags": [ TAG.Sensor, TAG.Flow, TAG.Water, TAG.Discharge, TAG.Chilled ],
                                    },
                                    "Chilled_Water_Supply_Flow_Sensor": {
                                        "tags": [ TAG.Sensor, TAG.Flow, TAG.Water, TAG.Supply, TAG.Chilled ],
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "Frequency_Sensor": {
                "substances": [ [ BRICK.measures, BRICK.Frequency ], ],
                "tags": [ TAG.Sensor, TAG.Frequency ],
                "subclasses": {
                    "Output_Frequency_Sensor": {
                        "tags": [ TAG.Output, TAG.Frequency, TAG.Sensor ],
                    }
                }
            },
            "Frost_Sensor": {
                "tags": [ TAG.Sensor, TAG.Frost ],
                "substances": [ [ BRICK.measures, BRICK.Frost ], ],
            },
            "Hail_Sensor": {
                "tags": [ TAG.Sensor, TAG.Hail ],
                "substances": [ [ BRICK.measures, BRICK.Hail ], ],
            },
            "Humidity_Sensor": {
                "tags": [ TAG.Sensor, TAG.Humidity ],
                "substances": [ [ BRICK.measures, BRICK.Humidity ], ],
                "subclasses": {
                    "Air_Humidity_Sensor": {
                        "tags": [ TAG.Sensor, TAG.Humidity, TAG.Air ],
                        "substances": [ [ BRICK.measures, BRICK.Humidity ], [ BRICK.measures, BRICK.Air ], ],
                        "subclasses": {
                            "Discharge_Air_Humidity_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Humidity, TAG.Air, TAG.Discharge ],
                            },
                            "Exhaust_Air_Humidity_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Humidity, TAG.Air, TAG.Exhaust ],
                            },
                            "Outside_Air_Humidity_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Humidity, TAG.Air, TAG.Outside ],
                            },
                            "Relative_Humidity_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Humidity, TAG.Air, TAG.Relative ],
                            },
                            "Return_Air_Humidity_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Humidity, TAG.Air, TAG.Return ],
                            },
                            "Supply_Air_Humidity_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Humidity, TAG.Air, TAG.Supply ],
                            },
                            "Zone_Humidity_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Humidity, TAG.Zone ],
                            }
                        }
                    }
                }
            },
            "Luminance_Sensor": {
                "tags": [ TAG.Sensor, TAG.Luminance ],
                "substances": [ [ BRICK.measures, BRICK.Luminance ], ],
                "subclasses": {
                    "Outside_Luminance_Sensor": {
                        "tags": [ TAG.Sensor, TAG.Luminance, TAG.Outside ],
                    }
                }
            },
            "Motion_Sensor": {
                "tags": [ TAG.Sensor, TAG.Motion ],
                "subclasses": {
                    "PIR_Sensor": {
                        "tags": [ TAG.Sensor, TAG.PIR ],
                    }
                }
            },
            "Occupancy_Sensor": {
                "tags": [ TAG.Sensor, TAG.Occupancy ],
                "subclasses": {
                    "PIR_Sensor": {
                        "tags": [ TAG.Pir, TAG.Sensor ],
                    }
                }
            },
            "Piezoelectric_Sensor": {
                "tags": [ TAG.Sensor, TAG.Piezoelectric ],
            },
            "Pressure_Sensor": {
                "tags": [ TAG.Sensor, TAG.Pressure ],
                "substances": [ [ BRICK.measures, BRICK.Pressure ], ],
                "subclasses": {
                    "Differential_Pressure_Sensor": {
                        "tags": [ TAG.Sensor, TAG.Pressure, TAG.Differential ],
                        "subclasses": {
                            "Chilled_Water_Differential_Pressure_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Pressure, TAG.Differential, TAG.Water, TAG.Chilled ],
                                "substances": [ [ BRICK.measures, BRICK.Pressure ], [ BRICK.measures, BRICK.Water ], ],
                            },
                            "Filter_Differential_Pressure_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Pressure, TAG.Differential, TAG.Filter ],
                            },
                            "Heat_Wheel_Differential_Pressure_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Pressure, TAG.Differential, TAG.Wheel, TAG.Heat ],
                            },
                            "Hot_Water_Differential_Pressure_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Pressure, TAG.Differential, TAG.Water, TAG.Hot ],
                                "substances": [ [ BRICK.measures, BRICK.Pressure ], [ BRICK.measures, BRICK.Water ], ],
                                "subclasses": {
                                    "Medium_Temperature_Hot_Water_Differential_Pressure_Sensor": {
                                        "tags": [ TAG.Medium, TAG.Temperature, TAG.Hot, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Sensor ],
                                    }
                                }
                            }
                        }
                    },
                    "Static_Pressure_Sensor": {
                        "tags": [ TAG.Sensor, TAG.Pressure, TAG.Static ],
                        "subclasses": {
                            "Building_Static_Pressure_Sensor": {
                                "substances": [ [ BRICK.measures, BRICK.Pressure ], [ BRICK.measures, BRICK.Air ], ],
                                "tags": [ TAG.Building, TAG.Static, TAG.Pressure, TAG.Sensor ],
                            },
                            "Discharge_Air_Static_Pressure_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Pressure, TAG.Static, TAG.Air, TAG.Discharge ],
                                "substances": [ [ BRICK.measures, BRICK.Pressure ], [ BRICK.measures, BRICK.Air ], ],
                            },
                            "Supply_Air_Static_Pressure_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Pressure, TAG.Static, TAG.Air, TAG.Supply ],
                                "substances": [ [ BRICK.measures, BRICK.Pressure ], [ BRICK.measures, BRICK.Air ], ],
                            },
                            "Exhaust_Air_Static_Pressure_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Pressure, TAG.Static, TAG.Air, TAG.Exhaust ],
                                "substances": [ [ BRICK.measures, BRICK.Pressure ], [ BRICK.measures, BRICK.Air ], ],
                                "subclasses": {
                                    "Average_Exhaust_Air_Static_Pressure_Sensor": {
                                        "tags": [ TAG.Average, TAG.Exhaust, TAG.Air, TAG.Static, TAG.Pressure, TAG.Sensor ],
                                    },
                                    "Lowest_Exhaust_Air_Static_Pressure_Sensor": {
                                        "tags": [ TAG.Lowest, TAG.Exhaust, TAG.Air, TAG.Static, TAG.Pressure, TAG.Sensor ],
                                    }
                                }
                            }
                        }
                    },
                    "Velocity_Pressure_Sensor": {
                        "tags": [ TAG.Sensor, TAG.Pressure, TAG.Velocity ],
                        "subclasses": {
                            "Discharge_Air_Velocity_Pressure_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Pressure, TAG.Velocity, TAG.Discharge, TAG.Air ],
                            },
                            "Exhaust_Air_Velocity_Pressure_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Pressure, TAG.Velocity, TAG.Exhaust, TAG.Air ],
                            },
                            "Supply_Air_Velocity_Pressure_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Pressure, TAG.Velocity, TAG.Supply, TAG.Air ],
                            }
                        }
                    }
                }
            },
            "Rain_Sensor": {
                "tags": [ TAG.Sensor, TAG.Rain ],
                "subclasses": {
                    "Rain_Duration_Sensor": {
                        "tags": [ TAG.Sensor, TAG.Rain, TAG.Duration ],
                    }
                }
            },
            "Duration_Sensor": {
                "tags": [ TAG.Sensor, TAG.Duration ],
                "subclasses": {
                    "Rain_Duration_Sensor": {
                        "tags": [ TAG.Rain, TAG.Duration, TAG.Sensor ],
                    },
                    "Run_Time_Sensor": {
                        "tags": [ TAG.Run, TAG.Time, TAG.Sensor ],
                    },
                    "On_Timer_Sensor": {
                        "tags": [ TAG.On, TAG.Timer, TAG.Sensor ],
                    }
                }
            },
            "Solar_Radiance_Sensor": {
                "tags": [ TAG.Sensor, TAG.Radiance, TAG.Solar ],
            },
            "Speed_Sensor": {
                "tags": [ TAG.Sensor, TAG.Speed ],
                "substances": [ [ BRICK.measures, BRICK.Speed ], ],
                "subclasses": {
                    "Differential_Speed_Sensor": {
                        "tags": [ TAG.Sensor, TAG.Speed, TAG.Differential ],
                        "subclasses": {
                            "Heat_Wheel_Speed_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Speed, TAG.Heat, TAG.Wheel ],
                            },
                            "Return_Fan_Differential_Speed_Sensor": {
                                "tags": [ TAG.Return, TAG.Fan, TAG.Differential, TAG.Speed, TAG.Sensor ],
                            }
                        }
                    },
                    "Motor_Speed_Sensor": {
                        "tags": [ TAG.Motor, TAG.Speed, TAG.Sensor ],
                    },
                    "Wind_Speed_Sensor": {
                        "tags": [ TAG.Sensor, TAG.Speed, TAG.Wind ],
                        "substances": [ [ BRICK.measures, BRICK.Wind_Speed ], ],
                    }
                }
            },
            "Torque_Sensor": {
                "tags": [ TAG.Sensor, TAG.Torque ],
                "subclasses": {
                    "Motor_Torque_Sensor": {
                        "tags": [ TAG.Motor, TAG.Torque, TAG.Sensor ],
                    }
                }
            },
            "Trace_Heat_Sensor": {
                "tags": [ TAG.Trace, TAG.Heat, TAG.Sensor ],
            },
            "Voltage_Sensor": {
                "tags": [ TAG.Sensor, TAG.Voltage ],
                "substances": [ [ BRICK.measures, BRICK.Voltage ], ],
                "subclasses": {
                    "Battery_Voltage_Sensor": {
                        "tags": [ TAG.Sensor, TAG.Voltage, TAG.Battery ],
                    },
                    "DC_Bus_Voltage_Sensor": {
                        "tags": [ TAG.Dc, TAG.Bus, TAG.Voltage, TAG.Sensor ],
                    },
                    "Heat_Wheel_Voltage_Sensor": {
                        "tags": [ TAG.Heat, TAG.Wheel, TAG.Voltage, TAG.Sensor ],
                    },
                    "Output_Voltage_Sensor": {
                        "tags": [ TAG.Output, TAG.Voltage, TAG.Sensor ],
                    }
                }
            },
            "Water_Level_Sensor": {
                "tags": [ TAG.Sensor, TAG.Water, TAG.Level ],
                "substances": [ [ BRICK.measures, BRICK.Water ], [ BRICK.measures, BRICK.Level ], ],
                "subclasses": {
                    "Deionised_Water_Level_Sensor": {
                        "tags": [ TAG.Sensor, TAG.Water, TAG.Level, TAG.Deionised ],
                        OWL.equivalentClass: "DI_Water_Level_Sensor"
                    }
                }
            },
            "Temperature_Sensor": {
                "tags": [ TAG.Sensor, TAG.Temperature ],
                "substances": [ [ BRICK.measures, BRICK.Temperature ], ],
                "subclasses": {
                    "Zone_Temperature_Sensor": {
                        "tags": [ TAG.Sensor, TAG.Temperature, TAG.Zone ],
                        "subclasses": {
                            "Average_Zone_Temperature_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Temperature, TAG.Zone, TAG.Average ],
                            },
                            "Highest_Zone_Temperature_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Temperature, TAG.Zone, TAG.Highest ],
                                OWL.equivalentClass: "Warmest_Zone_Temperature_Sensor"
                            },
                            "Lowest_Zone_Temperature_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Temperature, TAG.Zone, TAG.Lowest ],
                                OWL.equivalentClass: "Coldest_Zone_Temperature_Sensor"
                            }
                        }
                    },
                    "Air_Temperature_Sensor": {
                        "tags": [ TAG.Sensor, TAG.Temperature, TAG.Air ],
                        "substances": [ [ BRICK.measures, BRICK.Temperature ], [ BRICK.measures, BRICK.Air ], ],
                        "subclasses": {
                            "Discharge_Air_Temperature_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Temperature, TAG.Air, TAG.Discharge ],
                                OWL.equivalentClass: "Supply_Air_Temperature_Sensor",
                                "subclasses": {
                                    "Cooling_Coil_Discharge_Air_Temperature_Sensor": {
                                        "tags": [ TAG.Cooling, TAG.Coil, TAG.Discharge, TAG.Air, TAG.Temperature, TAG.Sensor ],
                                    },
                                    "Heat_Wheel_Discharge_Air_Temperature_Sensor": {
                                        "tags": [ TAG.Heat, TAG.Wheel, TAG.Discharge, TAG.Air, TAG.Temperature, TAG.Sensor ],
                                    },
                                    "Preheat_Discharge_Air_Temperature_Sensor": {
                                        "tags": [ TAG.Preheat, TAG.Discharge, TAG.Air, TAG.Temperature, TAG.Sensor ],
                                    }
                                }
                            },
                            "Zone_Air_Temperature_Sensor": {
                                "tags": [ TAG.Zone, TAG.Air, TAG.Temperature, TAG.Sensor ],
                            },
                            "Exhaust_Air_Temperature_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Temperature, TAG.Air, TAG.Exhaust ],
                            },
                            "Mixed_Air_Temperature_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Temperature, TAG.Air, TAG.Mixed ],
                            },
                            "Return_Air_Temperature_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Temperature, TAG.Air, TAG.Return ],
                            },
                            "Outside_Air_Temperature_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Temperature, TAG.Air, TAG.Outside ],
                                "subclasses": {
                                    "Outside_Air_Lockout_Temperature_Differential_Sensor": {
                                        "subclasses": {
                                            "Low_Outside_Air_Lockout_Temperature_Differential_Sensor": {
                                                "tags": [ TAG.Low, TAG.Outside, TAG.Air, TAG.Lockout, TAG.Temperature, TAG.Differential, TAG.Sensor ],
                                            },
                                            "High_Outside_Air_Lockout_Temperature_Differential_Sensor": {
                                                "tags": [ TAG.High, TAG.Outside, TAG.Air, TAG.Lockout, TAG.Temperature, TAG.Differential, TAG.Sensor ],
                                            }
                                        },
                                        "tags": [ TAG.Outside, TAG.Air, TAG.Lockout, TAG.Temperature, TAG.Differential, TAG.Sensor ],
                                    }
                                }
                            }
                        }
                    },
                    "Water_Temperature_Sensor": {
                        "tags": [ TAG.Sensor, TAG.Temperature, TAG.Water ],
                        "substances": [ [ BRICK.measures, BRICK.Temperature ], [ BRICK.measures, BRICK.Water ], ],
                        "subclasses": {
                            "Heat_Exchanger_Supply_Water_Temperature_Sensor": {
                                "tags": [ TAG.Heat, TAG.Exchanger, TAG.Supply, TAG.Water, TAG.Temperature, TAG.Sensor ],
                            },
                            "Hot_Water_Supply_Temperature_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Temperature, TAG.Water, TAG.Hot, TAG.Supply ],
                                "subclasses": {
                                    "Domestic_Hot_Water_Supply_Temperature_Sensor": {
                                        "tags": [ TAG.Domestic, TAG.Hot, TAG.Water, TAG.Supply, TAG.Temperature, TAG.Sensor ],
                                    },
                                    "High_Temperature_Hot_Water_Supply_Temperature_Sensor": {
                                        "tags": [ TAG.High, TAG.Temperature, TAG.Hot, TAG.Water, TAG.Supply, TAG.Temperature, TAG.Sensor ],
                                    },
                                    "Medium_Temperature_Hot_Water_Supply_Temperature_Sensor": {
                                        "tags": [ TAG.Medium, TAG.Temperature, TAG.Hot, TAG.Water, TAG.Supply, TAG.Temperature, TAG.Sensor ],
                                    }
                                }
                            },
                            "Chilled_Water_Temperature_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Temperature, TAG.Water, TAG.Chilled ],
                                "subclasses": {
                                    "Chilled_Water_Differential_Temperature_Sensor": {
                                        "tags": [ TAG.Chilled, TAG.Water, TAG.Differential, TAG.Temperature, TAG.Sensor ],
                                    },
                                    "Chilled_Water_Supply_Temperature_Sensor": {
                                        "tags": [ TAG.Sensor, TAG.Temperature, TAG.Water, TAG.Chilled, TAG.Supply ],
                                        OWL.equivalentClass: "Chilled_Water_Discharge_Temperature_Sensor"
                                    }
                                }
                            },
                            "Entering_Water_Temperature_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Temperature, TAG.Water, TAG.Entering ],
                                "subclasses": {
                                    "Hot_Water_Coil_Entering_Temperature_Sensor": {
                                        "tags": [ TAG.Hot, TAG.Water, TAG.Coil, TAG.Entering, TAG.Temperature, TAG.Sensor ],
                                    },
                                    "Ice_Tank_Entering_Water_Temperature_Sensor": {
                                        "tags": [ TAG.Ice, TAG.Tank, TAG.Entering, TAG.Water, TAG.Temperature, TAG.Sensor ],
                                    },
                                    "PreHeat_Coil_Entering_Air_Temperature_Sensor": {
                                        "tags": [ TAG.Preheat, TAG.Coil, TAG.Entering, TAG.Air, TAG.Temperature, TAG.Sensor ],
                                    }
                                }
                            },
                            "Leaving_Water_Temperature_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Temperature, TAG.Water, TAG.Leaving ],
                                "subclasses": {
                                    "Ice_Tank_Leaving_Water_Temperature_Sensor": {
                                        "tags": [ TAG.Ice, TAG.Tank, TAG.Leaving, TAG.Water, TAG.Temperature, TAG.Sensor ],
                                    },
                                    "PreHeat_Coil_Leaving_Air_Temperature_Sensor": {
                                        "tags": [ TAG.Preheat, TAG.Coil, TAG.Leaving, TAG.Air, TAG.Temperature, TAG.Sensor ],
                                    }
                                }
                            },
                            "Return_Water_Temperature_Sensor": {
                                "tags": [ TAG.Sensor, TAG.Temperature, TAG.Water, TAG.Return ],
                                "subclasses": {
                                    "Hot_Water_Return_Temperature_Sensor": {
                                        "tags": [ TAG.Hot, TAG.Water, TAG.Return, TAG.Temperature, TAG.Sensor ],
                                    },
                                    "Chilled_Water_Return_Temperature_Sensor": {
                                        "tags": [ TAG.Chilled, TAG.Water, TAG.Return, TAG.Temperature, TAG.Sensor ],
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

