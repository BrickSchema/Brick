from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.collection import Collection
from rdflib.extras.infixowl import Restriction

from .namespaces import *


setpoint_definitions = {
    "Setpoint": {
        "tags": [ TAG.Setpoint ],
        "subclasses": {
            "Enthalpy_Setpoint": {
                "tags": [ TAG.Enthalpy, TAG.Setpoint ],
            },
            "Dew_Point_Setpoint": {
                "tags": [ TAG.Dewpoint, TAG.Setpoint ],
            },
            "Demand_Setpoint": {
                "tags": [ TAG.Demand, TAG.Setpoint ],
                "subclasses": {
                    "Cooling_Demand_Setpoint": {
                        "tags": [ TAG.Cooling, TAG.Demand, TAG.Setpoint ],
                    },
                    "Cooling_Request_Percent_Setpoint": {
                        "tags": [ TAG.Cooling, TAG.Request, TAG.Percent, TAG.Setpoint ],
                        "parents": [BRICK.Cooling_Request_Setpoint],
                    },
                    "Cooling_Request_Setpoint": {
                        "tags": [ TAG.Cooling, TAG.Request, TAG.Setpoint ],
                    },
                    "Heating_Demand_Setpoint": {
                        "tags": [ TAG.Heating, TAG.Demand, TAG.Setpoint ],
                    },
                    "Heating_Request_Setpoint": {
                        "tags": [ TAG.Heating, TAG.Request, TAG.Setpoint ],
                        "subclasses": {
                            "Heating_Request_Percent_Setpoint": {
                                "tags": [ TAG.Heating, TAG.Request, TAG.Percent, TAG.Setpoint ],
                            },
                        }
                    },
                    "Preheat_Demand_Setpoint": {
                        "tags": [ TAG.Preheat, TAG.Demand, TAG.Setpoint ],
                    },
                    "Air_Flow_Demand_Setpoint": {
                        "tags": [ TAG.Air, TAG.Flow, TAG.Demand, TAG.Setpoint ],
                        "subclasses": {
                            "Discharge_Air_Flow_Demand_Setpoint": {
                                "tags": [ TAG.Discharge, TAG.Air, TAG.Flow, TAG.Demand, TAG.Setpoint ],
                            },
                            "Supply_Air_Flow_Demand_Setpoint": {
                                "tags": [ TAG.Supply, TAG.Air, TAG.Flow, TAG.Demand, TAG.Setpoint ],
                            }
                        }
                    }
                }
            },
            "Damper_Position_Setpoint": {
                "tags": [ TAG.Damper, TAG.Position, TAG.Setpoint ],
            },
            "Deadband_Setpoint": {
                "subclasses": {
                    "Differential_Pressure_Deadband_Setpoint": {
                        "subclasses": {
                            "Hot_Water_Differential_Pressure_Deadband_Setpoint": {
                                "tags": [ TAG.Hot, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Deadband, TAG.Setpoint ],
                                "parents": [BRICK.Hot_Water_Differential_Pressure_Setpoint],
                            },
                            "Chilled_Water_Differential_Pressure_Deadband_Setpoint": {
                                "tags": [ TAG.Chilled, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Deadband, TAG.Setpoint ],
                                "parents": [BRICK.Chilled_Water_Differential_Pressure_Setpoint],
                                "subclasses": {
                                    "Chilled_Water_Pump_Differential_Pressure_Deadband_Setpoint": {
                                        "tags": [ TAG.Chilled, TAG.Water, TAG.Pump, TAG.Differential, TAG.Pressure, TAG.Deadband, TAG.Setpoint ],
                                    },
                                },
                            },
                            "Cooling_Discharge_Air_Temperature_Deadband_Setpoint": {
                                "tags": [ TAG.Cooling, TAG.Discharge, TAG.Air, TAG.Temperature, TAG.Deadband, TAG.Setpoint ],
                                "parents": [BRICK.Discharge_Air_Temperature_Cooling_Setpoint],
                            },
                            "Supply_Water_Differential_Pressure_Deadband_Setpoint": {
                                "subclasses": {
                                    "Thermal_Energy_Storage_Supply_Water_Differential_Pressure_Deadband_Setpoint": {
                                        "tags": [ TAG.Thermal, TAG.Energy, TAG.Storage, TAG.Supply, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Deadband, TAG.Setpoint ],
                                    }
                                },
                                "tags": [ TAG.Supply, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Deadband, TAG.Setpoint ],
                            },
                        },
                        "tags": [ TAG.Differential, TAG.Pressure, TAG.Deadband, TAG.Setpoint ],
                        "parents": [BRICK.Differential_Pressure_Setpoint],
                    },
                    "Temperature_Deadband_Setpoint": {
                        "subclasses": {
                            "Occupied_Cooling_Temperature_Deadband_Setpoint": {
                                "tags": [ TAG.Occupied, TAG.Cooling, TAG.Temperature, TAG.Deadband, TAG.Setpoint ],
                            },
                            "Occupied_Heating_Temperature_Deadband_Setpoint": {
                                "tags": [ TAG.Occupied, TAG.Heating, TAG.Temperature, TAG.Deadband, TAG.Setpoint ],
                            },
                            "Discharge_Air_Temperature_Deadband_Setpoint": {
                                "subclasses": {
                                    "Heating_Discharge_Air_Temperature_Deadband_Setpoint": {
                                        "tags": [ TAG.Heating, TAG.Discharge, TAG.Air, TAG.Temperature, TAG.Deadband, TAG.Setpoint ],
                                        "parents": [BRICK.Discharge_Air_Temperature_Heating_Setpoint],
                                    },
                                    "Cooling_Discharge_Air_Temperature_Deadband_Setpoint": {
                                        "tags": [ TAG.Cooling, TAG.Discharge, TAG.Air, TAG.Temperature, TAG.Deadband, TAG.Setpoint ],
                                        "parents": [BRICK.Discharge_Air_Temperature_Cooling_Setpoint],
                                    }
                                },
                                "tags": [ TAG.Discharge, TAG.Air, TAG.Temperature, TAG.Deadband, TAG.Setpoint ],
                                "parents": [BRICK.Discharge_Air_Temperature_Setpoint],
                            },
                            "Supply_Air_Temperature_Deadband_Setpoint": {
                                "subclasses": {
                                    "Heating_Supply_Air_Temperature_Deadband_Setpoint": {
                                        "tags": [ TAG.Heating, TAG.Supply, TAG.Air, TAG.Temperature, TAG.Deadband, TAG.Setpoint ],
                                    },
                                    "Cooling_Supply_Air_Temperature_Deadband_Setpoint": {
                                        "tags": [ TAG.Cooling, TAG.Supply, TAG.Air, TAG.Temperature, TAG.Deadband, TAG.Setpoint ],
                                    }
                                },
                                "tags": [ TAG.Supply, TAG.Air, TAG.Temperature, TAG.Deadband, TAG.Setpoint ],
                                "parents": [BRICK.Air_Temperature_Setpoint],
                            },
                            "Supply_Water_Temperature_Deadband_Setpoint": {
                                "subclasses": {
                                    "Heat_Exchanger_Supply_Water_Temperature_Deadband_Setpoint": {
                                        "tags": [ TAG.Heat, TAG.Exchanger, TAG.Supply, TAG.Water, TAG.Temperature, TAG.Deadband, TAG.Setpoint ],
                                    }
                                },
                                "tags": [ TAG.Supply, TAG.Water, TAG.Temperature, TAG.Deadband, TAG.Setpoint ],
                                "parents": [BRICK.Water_Temperature_Setpoint],
                            }
                        },
                        "tags": [ TAG.Temperature, TAG.Deadband, TAG.Setpoint ],
                        "parents": [BRICK.Temperature_Setpoint],
                    },
                    "Air_Flow_Deadband_Setpoint": {
                        "subclasses": {
                            "Exhaust_Air_Stack_Flow_Deadband_Setpoint": {
                                "tags": [ TAG.Exhaust, TAG.Air, TAG.Stack, TAG.Flow, TAG.Deadband, TAG.Setpoint ],
                                "parents": [BRICK.Exhaust_Air_Stack_Flow_Setpoint],
                            }
                        },
                        "tags": [ TAG.Air, TAG.Flow, TAG.Deadband, TAG.Setpoint ],
                        "parents": [BRICK.Air_Flow_Setpoint],
                    },
                    "Static_Pressure_Deadband_Setpoint": {
                        "tags": [ TAG.Static, TAG.Pressure, TAG.Deadband, TAG.Setpoint ],
                        "parents": [BRICK.Static_Pressure_Setpoint],
                    },
                },
                "tags": [ TAG.Deadband, TAG.Setpoint ],
            },
            "Flow_Setpoint": {
                "tags": [TAG.Flow, TAG.Setpoint],
                "subclasses": {
                    "Air_Flow_Setpoint": {
                        "tags": [TAG.Air, TAG.Flow, TAG.Setpoint],
                        "subclasses": {
                            "Air_Flow_Demand_Setpoint": {
                                "tags": [ TAG.Air, TAG.Flow, TAG.Demand, TAG.Setpoint ],
                            },
                            "Discharge_Air_Flow_Setpoint": {
                                "subclasses": {
                                    "Discharge_Air_Flow_Demand_Setpoint": {
                                        "tags": [ TAG.Discharge, TAG.Air, TAG.Flow, TAG.Demand, TAG.Setpoint ],
                                    },
                                    "Cooling_Discharge_Air_Flow_Setpoint": {
                                        "tags": [ TAG.Cooling, TAG.Discharge, TAG.Air, TAG.Flow, TAG.Setpoint ],
                                    },
                                    "Heating_Discharge_Air_Flow_Setpoint": {
                                        "tags": [ TAG.Heating, TAG.Discharge, TAG.Air, TAG.Flow, TAG.Setpoint ],
                                    }
                                },
                                "tags": [ TAG.Discharge, TAG.Air, TAG.Flow, TAG.Setpoint ],
                            },
                            "Exhaust_Air_Flow_Setpoint": {
                                "subclasses": {
                                    "Exhaust_Air_Stack_Flow_Setpoint": {
                                        "tags": [ TAG.Exhaust, TAG.Air, TAG.Stack, TAG.Flow, TAG.Setpoint ],
                                    }
                                },
                                "tags": [ TAG.Exhaust, TAG.Air, TAG.Flow, TAG.Setpoint ],
                            },
                            "Fan_Air_Flow_Setpoint": {
                                "tags": [ TAG.Fan, TAG.Air, TAG.Flow, TAG.Setpoint ],
                            },
                            "Outside_Air_Flow_Setpoint": {
                                "tags": [ TAG.Outside, TAG.Air, TAG.Flow, TAG.Setpoint ],
                            },
                            "Supply_Air_Flow_Setpoint": {
                                "subclasses": {
                                    "Supply_Air_Flow_Demand_Setpoint": {
                                        "tags": [ TAG.Supply, TAG.Air, TAG.Flow, TAG.Demand, TAG.Setpoint ],
                                    },
                                    "Occupied_Supply_Air_Flow_Setpoint": {
                                        "subclasses": {
                                            "Occupied_Cooling_Supply_Air_Flow_Setpoint": {
                                                "tags": [ TAG.Occupied, TAG.Cooling, TAG.Supply, TAG.Air, TAG.Flow, TAG.Setpoint ],
                                                "parents": [BRICK.Cooling_Supply_Air_Flow_Setpoint],
                                            },
                                            "Occupied_Heating_Supply_Air_Flow_Setpoint": {
                                                "tags": [ TAG.Occupied, TAG.Heating, TAG.Supply, TAG.Air, TAG.Flow, TAG.Setpoint ],
                                                "parents": [BRICK.Heating_Supply_Air_Flow_Setpoint],
                                            }
                                        },
                                        "tags": [ TAG.Occupied, TAG.Supply, TAG.Air, TAG.Flow, TAG.Setpoint ],
                                    },
                                    "Cooling_Supply_Air_Flow_Setpoint": {
                                        "tags": [ TAG.Cooling, TAG.Supply, TAG.Air, TAG.Flow, TAG.Setpoint ],
                                    },
                                    "Heating_Supply_Air_Flow_Setpoint": {
                                        "tags": [ TAG.Heating, TAG.Supply, TAG.Air, TAG.Flow, TAG.Setpoint ],
                                    }
                                },
                                "tags": [ TAG.Supply, TAG.Air, TAG.Flow, TAG.Setpoint ],
                            }
                        },
                        "tags": [ TAG.Air, TAG.Flow, TAG.Setpoint ],
                    }
                },
                "tags": [ TAG.Flow, TAG.Setpoint ],
            },
            "Humidity_Setpoint": {
                "subclasses": {
                    "High_Humidity_Alarm_Setpoint": {
                        "tags": [ TAG.High, TAG.Humidity, TAG.Alarm, TAG.Setpoint ],
                    },
                    "Low_Humidity_Alarm_Setpoint": {
                        "tags": [ TAG.Low, TAG.Humidity, TAG.Alarm, TAG.Setpoint ],
                    }
                },
                "tags": [ TAG.Humidity, TAG.Setpoint ],
            },
            "Load_Setpoint": {
                "subclasses": {
                    "Load_Shed_Setpoint": {
                        "tags": [ TAG.Shed, TAG.Load, TAG.Setpoint ],
                    }
                },
                "tags": [ TAG.Load, TAG.Setpoint ],
            },
            "Luminance_Setpoint": {
                "tags": [ TAG.Luminance, TAG.Setpoint ],
            },
            "Mode_Setpoint": {
                "subclasses": {
                    "Dual_Band_Mode_Setpoint": {
                        "tags": [ TAG.Dual, TAG.Band, TAG.Mode, TAG.Setpoint ],
                    },
                    "Unoccupied_Mode_Setpoint": {
                        "tags": [ TAG.Unoccupied, TAG.Mode, TAG.Setpoint ],
                    },
                    "Occupied_Mode_Setpoint": {
                        "tags": [ TAG.Occupied, TAG.Mode, TAG.Setpoint ],
                    }
                },
                "tags": [ TAG.Mode, TAG.Setpoint ],
            },
            "Pressure_Setpoint": {
                "subclasses": {
                    "Differential_Pressure_Setpoint": {
                        "subclasses": {
                            "Chilled_Water_Differential_Pressure_Setpoint": {
                                "tags": [ TAG.Chilled, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Setpoint ],
                            },
                            "Hot_Water_Differential_Pressure_Setpoint": {
                                "tags": [ TAG.Hot, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Setpoint ],
                            },
                            "Load_Shed_Differential_Pressure_Setpoint": {
                                "parents": [BRICK.Load_Shed_Setpoint],
                                "subclasses": {
                                    "Chilled_Water_Differential_Pressure_Load_Shed_Setpoint": {
                                        "tags": [ TAG.Chilled, TAG.Water, TAG.Differential, TAG.Pressure, TAG.Load, TAG.Shed, TAG.Setpoint ],
                                        "parents": [BRICK.Chilled_Water_Differential_Pressure_Setpoint],
                                    },
                                },
                                "tags": [ TAG.Load, TAG.Shed, TAG.Differential, TAG.Pressure, TAG.Setpoint ],
                            }
                        },
                        "tags": [ TAG.Differential, TAG.Pressure, TAG.Setpoint ],
                    },
                    "Static_Pressure_Setpoint": {
                        "subclasses": {
                            "Building_Air_Static_Pressure_Setpoint": {
                                "tags": [ TAG.Building, TAG.Air, TAG.Static, TAG.Pressure, TAG.Setpoint ],
                            },
                            "Chilled_Water_Static_Pressure_Setpoint": {
                                "tags": [ TAG.Chilled, TAG.Water, TAG.Static, TAG.Pressure, TAG.Setpoint ],
                            },
                            "Discharge_Air_Static_Pressure_Setpoint": {
                                "tags": [ TAG.Discharge, TAG.Air, TAG.Static, TAG.Pressure, TAG.Setpoint ],
                            },
                            "Exhaust_Air_Static_Pressure_Setpoint": {
                                "tags": [ TAG.Exhaust, TAG.Air, TAG.Static, TAG.Pressure, TAG.Setpoint ],
                            },
                            "Hot_Water_Static_Pressure_Setpoint": {
                                "tags": [ TAG.Hot, TAG.Water, TAG.Static, TAG.Pressure, TAG.Setpoint ],
                            },
                            "Supply_Air_Static_Pressure_Setpoint": {
                                "tags": [ TAG.Supply, TAG.Air, TAG.Static, TAG.Pressure, TAG.Setpoint ],
                            }
                        },
                        "tags": [ TAG.Static, TAG.Pressure, TAG.Setpoint ],
                    },
                    "Velocity_Pressure_Setpoint": {
                        "tags": [ TAG.Velocity, TAG.Pressure, TAG.Setpoint ],
                    }
                },
                "tags": [ TAG.Pressure, TAG.Setpoint ],
            },
            "Reset_Setpoint": {
                "Discharge_Air_Flow_Reset_Setpoint": {
                    "subclasses": {
                        "Discharge_Air_Flow_Reset_High_Setpoint": {},
                        "Discharge_Air_Flow_Reset_Low_Setpoint": {}
                    }
                },
                "Discharge_Air_Temperature_Reset_High_Setpoint": {},
                "Discharge_Air_Temperature_Reset_Low_Setpoint": {},
                "Supply_Air_Temperature_Reset_High_Setpoint": {},
                "Supply_Air_Temperature_Reset_Low_Setpoint": {},
                "Temperature_Differential_Reset_Setpoint": {
                    "subclasses": {
                        "Discharge_Air_Temperature_Reset_Differential_Setpoint": {},
                        "Supply_Air_Temperature_Reset_Differential_Setpoint": {}
                    }
                },
                "Temperature_High_Reset_Setpoint": {
                    "subclasses": {
                        "Hot_Water_Supply_Temperature_High_Reset_Setpoint": {
                            "subclasses": {
                                "Medium_Temperature_Hot_Water_Discharge_Temperature_High_Reset_Setpoint": {},
                                "Medium_Temperature_Hot_Water_Supply_Temperature_High_Reset_Setpoint": {}
                            }
                        }
                    }
                },
                "Outside_Air_Temperature_High_Reset_Setpoint": {},
                "Temperature_Low_Reset_Setpoint": {
                    "subclasses": {
                        "Hot_Water_Supply_Temperature_Low_Reset_Setpoint": {
                            "subclasses": {
                                "Medium_Temperature_Hot_Water_Discharge_Temperature_Low_Reset_Setpoint": {},
                                "Medium_Temperature_Hot_Water_Supply_Temperature_Low_Reset_Setpoint": {}
                            }
                        },
                        "Outside_Air_Temperature_Low_Reset_Setpoint": {}
                    }
                },
                "tags": [ TAG.Reset, TAG.Setpoint ],
            },
            "Speed_Setpoint": {
                "subclasses": {
                    "Differential_Speed_Setpoint": {
                        "subclasses": {
                            "Return_Fan_Differential_Speed_Setpoint": {
                                "tags": [ TAG.Discharge, TAG.Fan, TAG.Differential, TAG.Speed, TAG.Setpoint ],
                            },
                            "Return_Fan_Differential_Speed_Setpoint": {
                                "tags": [ TAG.Return, TAG.Fan, TAG.Differential, TAG.Speed, TAG.Setpoint ],
                            },
                            "Supply_Fan_Differential_Speed_Setpoint": {
                                "tags": [ TAG.Supply, TAG.Fan, TAG.Differential, TAG.Speed, TAG.Setpoint ],
                            }
                        },
                        "tags": [ TAG.Differential, TAG.Speed, TAG.Setpoint ],
                    }
                },
                "tags": [ TAG.Speed, TAG.Setpoint ],
            },
            "Temperature_Setpoint": {
                "tags": [TAG.Temperature, TAG.Setpoint],
                "subclasses": {
                    "Air_Temperature_Setpoint": {
                        "tags": [ TAG.Air, TAG.Temperature, TAG.Setpoint ],
                        "subclasses": {
                            "Discharge_Air_Temperature_Setpoint": {
                                "tags": [ TAG.Discharge, TAG.Air, TAG.Temperature, TAG.Setpoint ],
                                "subclasses": {
                                    "Discharge_Air_Temperature_Heating_Setpoint": {
                                        OWL.equivalentClass: "Minimum_Discharge_Air_Temperature_Setpoint",
                                        "tags": [ TAG.Discharge, TAG.Air, TAG.Temperature, TAG.Heating, TAG.Setpoint ],
                                    },
                                    "Minimum_Discharge_Air_Temperature_Setpoint": {},
                                    "Maximum_Discharge_Air_Temperature_Setpoint": {},
                                    "Discharge_Air_Temperature_Cooling_Setpoint": {
                                        OWL.equivalentClass: "Maximum_Discharge_Air_Temperature_Setpoint",
                                        "tags": [ TAG.Discharge, TAG.Air, TAG.Temperature, TAG.Cooling, TAG.Setpoint ],
                                    }
                                },
                                "tags": [ TAG.Discharge, TAG.Air, TAG.Temperature, TAG.Setpoint ],
                            },
                            "Mixed_Air_Temperature_Setpoint": {
                                "tags": [ TAG.Mixed, TAG.Air, TAG.Temperature, TAG.Setpoint ],
                            },
                            "Room_Air_Temperature_Setpoint": {
                                "tags": [ TAG.Room, TAG.Air, TAG.Temperature, TAG.Setpoint ],
                            },
                            "Zone_Air_Temperature_Setpoint": {
                                "tags": [ TAG.Zone, TAG.Air, TAG.Temperature, TAG.Setpoint ],
                            },
                            "Effective_Air_Temperature_Setpoint": {
                                "tags": [ TAG.Effective, TAG.Air, TAG.Temperature, TAG.Setpoint ],
                            },
                            "Outside_Air_Temperature_Setpoint": {
                                "subclasses": {
                                    "Low_Outside_Air_Temperature_Enable_Setpoint": {
                                        "tags": [ TAG.Low, TAG.Outside, TAG.Air, TAG.Temperature, TAG.Enable, TAG.Setpoint ],
                                    },
                                    "Open_Heating_Valve_Outside_Air_Temperature_Setpoint": {
                                        "tags": [ TAG.Open, TAG.Heating, TAG.Valve, TAG.Outside, TAG.Air, TAG.Temperature, TAG.Setpoint ],
                                    },
                                    "Outside_Air_Lockout_Temperature_Setpoint": {
                                        "tags": [ TAG.Outside, TAG.Air, TAG.Lockout, TAG.Temperature, TAG.Setpoint ],
                                    }
                                },
                                "tags": [ TAG.Outside, TAG.Air, TAG.Temperature, TAG.Setpoint ],
                            }
                        },
                        "tags": [ TAG.Air, TAG.Temperature, TAG.Setpoint ],
                    },
                    "Water_Temperature_Setpoint": {
                        "subclasses": {
                            "Entering_Water_Temperature_Setpoint": {
                                "tags": [ TAG.Entering, TAG.Water, TAG.Temperature, TAG.Setpoint ],
                            },
                            "Leaving_Water_Temperature_Setpoint": {
                                "tags": [TAG.Leaving, TAG.Setpoint, TAG.Temperature, TAG.Water],
                            }
                        },
                        "tags": [ TAG.Water, TAG.Temperature, TAG.Setpoint ],
                    }
                },
                "tags": [ TAG.Temperature, TAG.Setpoint ],
            },
            "CO2_Setpoint": {
                "tags": [TAG.Setpoint, TAG.CO2],
                "subclasses": {
                    "Return_Air_CO2_Setpoint": {
                        "tags": [TAG.Return, TAG.Air, TAG.Setpoint, TAG.CO2],
                        "subclasses": {
                            "Max_Return_Air_CO2_Setpoint": {
                                "tags": [ TAG.Max, TAG.Return, TAG.Air, TAG.CO2, TAG.Setpoint ],
                            }
                        },
                        "tags": [ TAG.Return, TAG.Air, TAG.CO2, TAG.Setpoint ],
                    }
                },
                "tags": [ TAG.CO2, TAG.Setpoint ],
            }
        }
    }
}

