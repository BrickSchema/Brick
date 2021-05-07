from rdflib import Literal
from .namespaces import BRICK, TAG, OWL, RDFS

sensor_definitions = {
    "Sensor": {
        RDFS.seeAlso: Literal(
            "https://xp20.ashrae.org/terminology/index.php?term=Sensor"
        ),
        "tags": [TAG.Point, TAG.Sensor],
        "subclasses": {
            "Adjust_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Adjust],
                "subclasses": {
                    "Warm_Cool_Adjust_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Adjust, TAG.Warm, TAG.Cool],
                    },
                },
            },
            "Air_Quality_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Air, TAG.Quality],
                "subclasses": {
                    "CO_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.CO],
                        "substances": [
                            [BRICK.measures, BRICK.Air],
                            [BRICK.measures, BRICK.CO],
                        ],
                        "subclasses": {
                            "CO_Level_Sensor": {
                                "tags": [TAG.Point, TAG.CO, TAG.Level, TAG.Sensor],
                            },
                            "CO_Differential_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.CO,
                                    TAG.Differential,
                                    TAG.Sensor,
                                ],
                            },
                            "Outside_Air_CO_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Outside,
                                    TAG.Air,
                                    TAG.CO,
                                    TAG.Sensor,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Outside_Air],
                                    [BRICK.measures, BRICK.CO],
                                ],
                            },
                            "Return_Air_CO_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Return,
                                    TAG.Air,
                                    TAG.CO,
                                    TAG.Sensor,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Return_Air],
                                    [BRICK.measures, BRICK.CO],
                                ],
                            },
                        },
                    },
                    "CO2_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.CO2],
                        "substances": [
                            [BRICK.measures, BRICK.Air],
                            [BRICK.measures, BRICK.CO2],
                        ],
                        "subclasses": {
                            "CO2_Differential_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.CO2,
                                    TAG.Differential,
                                    TAG.Sensor,
                                ],
                            },
                            "CO2_Level_Sensor": {
                                "tags": [TAG.Point, TAG.CO2, TAG.Level, TAG.Sensor],
                            },
                            "Outside_Air_CO2_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Outside,
                                    TAG.Air,
                                    TAG.CO2,
                                    TAG.Sensor,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Outside_Air],
                                    [BRICK.measures, BRICK.CO2],
                                ],
                            },
                            "Return_Air_CO2_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Return,
                                    TAG.Air,
                                    TAG.CO2,
                                    TAG.Sensor,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Return_Air],
                                    [BRICK.measures, BRICK.CO2],
                                ],
                            },
                        },
                    },
                    "NO2_Level_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Level, TAG.NO2],
                        "substances": [
                            [BRICK.measures, BRICK.Air],
                            [BRICK.measures, BRICK.NO2],
                        ],
                    },
                    "Formaldehyde_Level_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Level, TAG.Formaldehyde],
                        "substances": [
                            [BRICK.measures, BRICK.Air],
                            [BRICK.measures, BRICK.Formaldehyde_Concentration],
                        ],
                    },
                    "Ozone_Level_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Level, TAG.Ozone],
                        "substances": [
                            [BRICK.measures, BRICK.Air],
                            [BRICK.measures, BRICK.Ozone_Concentration],
                        ],
                    },
                    "Methane_Level_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Level, TAG.Methane],
                        "substances": [
                            [BRICK.measures, BRICK.Air],
                            [BRICK.measures, BRICK.Methane_Concentration],
                        ],
                    },
                    "Radioactivity_Concentration_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Radioactivity,
                            TAG.Concentration,
                        ],
                        "substances": [
                            [BRICK.measures, BRICK.Air],
                            [BRICK.measures, BRICK.Radioactivity_Concentration],
                        ],
                        "subclasses": {
                            "Radon_Concentration_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Radon,
                                    TAG.Concentration,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Air],
                                    [BRICK.measures, BRICK.Radon_Concentration],
                                ],
                            },
                        },
                    },
                    "Particulate_Matter_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Particulate, TAG.Matter],
                        "substances": [
                            [BRICK.measures, BRICK.Air],
                            [BRICK.measures, BRICK.Air_Quality],
                        ],
                        "subclasses": {
                            "PM1_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Particulate,
                                    TAG.Matter,
                                    TAG.PM1,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Air],
                                    [BRICK.measures, BRICK.PM1_Concentration],
                                ],
                                "subclasses": {
                                    "PM1_Level_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Level,
                                            TAG.Sensor,
                                            TAG.Particulate,
                                            TAG.Matter,
                                            TAG.PM1,
                                        ],
                                    }
                                },
                            },
                            "PM10_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Particulate,
                                    TAG.Matter,
                                    TAG.PM10,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Air],
                                    [BRICK.measures, BRICK.PM10_Concentration],
                                ],
                                "subclasses": {
                                    "PM10_Level_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Level,
                                            TAG.Sensor,
                                            TAG.Particulate,
                                            TAG.Matter,
                                            TAG.PM10,
                                        ],
                                    }
                                },
                            },
                            "PM2.5_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Particulate,
                                    TAG.Matter,
                                    TAG["PM2.5"],
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Air],
                                    [BRICK.measures, BRICK["PM2.5_Concentration"]],
                                ],
                                "subclasses": {
                                    "PM2.5_Level_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Level,
                                            TAG.Sensor,
                                            TAG.Particulate,
                                            TAG.Matter,
                                            TAG["PM2.5"],
                                        ],
                                    }
                                },
                            },
                            "TVOC_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Particulate,
                                    TAG.Matter,
                                    TAG.TVOC,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Air],
                                    [BRICK.measures, BRICK["TVOC_Concentration"]],
                                ],
                                "subclasses": {
                                    "TVOC_Level_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Level,
                                            TAG.Sensor,
                                            TAG.Particulate,
                                            TAG.Matter,
                                            TAG.TVOC,
                                        ],
                                    }
                                },
                            },
                        },
                    },
                },
            },
            "Air_Grains_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Air, TAG.Grains],
                "substances": [
                    [BRICK.measures, BRICK.Air],
                    [BRICK.measures, BRICK.GrainsOfMoisture],
                ],
                "subclasses": {
                    "Outside_Air_Grains_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Outside,
                            TAG.Air,
                            TAG.Grains,
                            TAG.Sensor,
                        ],
                        "substances": [
                            [BRICK.measures, BRICK.Outside_Air],
                            [BRICK.measures, BRICK.GrainsOfMoisture],
                        ],
                    },
                    "Return_Air_Grains_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Return,
                            TAG.Air,
                            TAG.Grains,
                            TAG.Sensor,
                        ],
                        "substances": [
                            [BRICK.measures, BRICK.Return_Air],
                            [BRICK.measures, BRICK.GrainsOfMoisture],
                        ],
                    },
                },
            },
            "Angle_Sensor": {
                "substances": [[BRICK.measures, BRICK.Angle]],
                "subclasses": {
                    "Solar_Azimuth_Angle_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Solar,
                            TAG.Azimuth,
                            TAG.Angle,
                            TAG.Sensor,
                        ],
                    },
                    "Solar_Zenith_Angle_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Solar,
                            TAG.Zenith,
                            TAG.Angle,
                            TAG.Sensor,
                        ],
                    },
                },
                "tags": [TAG.Point, TAG.Angle, TAG.Sensor],
            },
            "Capacity_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Capacity],
                "substances": [[BRICK.measures, BRICK.Capacity]],
            },
            "Contact_Sensor": {"tags": [TAG.Point, TAG.Sensor, TAG.Contact]},
            "Conductivity_Sensor": {
                # IFC ConductanceSensor
                # TODO: pull from
                # https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/
                "tags": [TAG.Point, TAG.Sensor, TAG.Conductivity],
                "substances": [[BRICK.measures, BRICK.Conductivity]],
                "subclasses": {
                    "Deionised_Water_Conductivity_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Conductivity,
                            TAG.Water,
                            TAG.Deionised,
                        ],
                        "substances": [
                            [BRICK.measures, BRICK.Conductivity],
                            [BRICK.measures, BRICK.Deionized_Water],
                        ],
                    }
                },
            },
            "Current_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Current],
                "substances": [[BRICK.measures, BRICK.Current]],
                "subclasses": {
                    "Load_Current_Sensor": {
                        "tags": [TAG.Point, TAG.Load, TAG.Current, TAG.Sensor],
                    },
                    "Motor_Current_Sensor": {
                        "tags": [TAG.Point, TAG.Motor, TAG.Current, TAG.Sensor],
                    },
                    "Current_Output_Sensor": {
                        "tags": [TAG.Point, TAG.Current, TAG.Output, TAG.Sensor],
                        "subclasses": {
                            "Photovoltaic_Current_Output_Sensor": {
                                OWL.equivalentClass: BRICK["PV_Current_Output_Sensor"],
                                "tags": [
                                    TAG.Point,
                                    TAG.Photovoltaic,
                                    TAG.Current,
                                    TAG.Output,
                                    TAG.Sensor,
                                ],
                            },
                            "PV_Current_Output_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.PV,
                                    TAG.Current,
                                    TAG.Output,
                                    TAG.Sensor,
                                ],
                            },
                        },
                    },
                },
            },
            "Position_Sensor": {
                "substances": [[BRICK.measures, BRICK.Position]],
                "tags": [TAG.Point, TAG.Position, TAG.Sensor],
                "subclasses": {
                    "Sash_Position_Sensor": {
                        "tags": [TAG.Point, TAG.Sash, TAG.Position, TAG.Sensor],
                    },
                    "Damper_Position_Sensor": {
                        "tags": [TAG.Point, TAG.Damper, TAG.Position, TAG.Sensor],
                    },
                    "Valve_Position_Sensor": {
                        "tags": [TAG.Point, TAG.Valve, TAG.Position, TAG.Sensor],
                    },
                },
            },
            "Demand_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Demand],
                "subclasses": {
                    "Cooling_Demand_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Demand, TAG.Cool],
                        "subclasses": {
                            "Average_Cooling_Demand_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Demand,
                                    TAG.Cool,
                                    TAG.Average,
                                ],
                            },
                        },
                    },
                    "Heating_Demand_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Demand, TAG.Heat],
                        "subclasses": {
                            "Average_Heating_Demand_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Demand,
                                    TAG.Heat,
                                    TAG.Average,
                                ],
                            },
                        },
                    },
                },
            },
            "Dewpoint_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Dewpoint],
                "substances": [[BRICK.measures, BRICK.Dewpoint]],
                "subclasses": {
                    "Outside_Air_Dewpoint_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Dewpoint,
                            TAG.Air,
                            TAG.Outside,
                        ],
                        "substances": [
                            [BRICK.measures, BRICK.Dewpoint],
                            [BRICK.measures, BRICK.Outside_Air],
                        ],
                    },
                    "Return_Air_Dewpoint_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Dewpoint,
                            TAG.Air,
                            TAG.Return,
                        ],
                        "substances": [
                            [BRICK.measures, BRICK.Dewpoint],
                            [BRICK.measures, BRICK.Return_Air],
                        ],
                    },
                    "Exhaust_Air_Dewpoint_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Dewpoint,
                            TAG.Air,
                            TAG.Exhaust,
                        ],
                        "substances": [
                            [BRICK.measures, BRICK.Dewpoint],
                            [BRICK.measures, BRICK.Exhaust_Air],
                        ],
                    },
                    "Discharge_Air_Dewpoint_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Dewpoint,
                            TAG.Air,
                            TAG.Discharge,
                        ],
                        "substances": [
                            [BRICK.measures, BRICK.Dewpoint],
                            [BRICK.measures, BRICK.Discharge_Air],
                        ],
                    },
                    "Zone_Air_Dewpoint_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Dewpoint,
                            TAG.Air,
                            TAG.Zone,
                        ],
                        "substances": [
                            [BRICK.measures, BRICK.Dewpoint],
                            [BRICK.measures, BRICK.Zone_Air],
                        ],
                    },
                },
            },
            "Direction_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Direction],
                "substances": [[BRICK.measures, BRICK.Direction]],
                "subclasses": {
                    "Wind_Direction_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Direction, TAG.Wind],
                        "substances": [[BRICK.measures, BRICK.Wind_Direction]],
                    }
                },
            },
            "Energy_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Energy],
                "substances": [[BRICK.measures, BRICK.Energy]],
            },
            "Enthalpy_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Enthalpy],
                "substances": [[BRICK.measures, BRICK.Enthalpy]],
                "subclasses": {
                    "Air_Enthalpy_Sensor": {
                        "substances": [
                            [BRICK.measures, BRICK.Enthalpy],
                            [BRICK.measures, BRICK.Air],
                        ],
                        "subclasses": {
                            "Outside_Air_Enthalpy_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Outside,
                                    TAG.Air,
                                    TAG.Enthalpy,
                                    TAG.Sensor,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Enthalpy],
                                    [BRICK.measures, BRICK.Outside_Air],
                                ],
                            },
                            "Return_Air_Enthalpy_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Return,
                                    TAG.Air,
                                    TAG.Enthalpy,
                                    TAG.Sensor,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Enthalpy],
                                    [BRICK.measures, BRICK.Return_Air],
                                ],
                            },
                        },
                        "tags": [TAG.Point, TAG.Air, TAG.Enthalpy, TAG.Sensor],
                    }
                },
            },
            "Fire_Sensor": {"tags": [TAG.Point, TAG.Sensor, TAG.Fire]},
            "Flow_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Flow],
                "substances": [[BRICK.measures, BRICK.Flow]],
                "subclasses": {
                    "Air_Flow_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Flow, TAG.Air],
                        "substances": [
                            [BRICK.measures, BRICK.Flow],
                            [BRICK.measures, BRICK.Air],
                        ],
                        "subclasses": {
                            "Bypass_Air_Flow_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Flow,
                                    TAG.Air,
                                    TAG.Bypass,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Flow],
                                    [BRICK.measures, BRICK.Bypass_Air],
                                ],
                            },
                            "Discharge_Air_Flow_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Flow,
                                    TAG.Air,
                                    TAG.Discharge,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Flow],
                                    [BRICK.measures, BRICK.Discharge_Air],
                                ],
                                "subclasses": {
                                    "Average_Discharge_Air_Flow_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Average,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Sensor,
                                        ],
                                    }
                                },
                            },
                            "Exhaust_Air_Flow_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Flow,
                                    TAG.Air,
                                    TAG.Exhaust,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Flow],
                                    [BRICK.measures, BRICK.Exhaust_Air],
                                ],
                                "subclasses": {
                                    "Exhaust_Air_Stack_Flow_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Exhaust,
                                            TAG.Air,
                                            TAG.Stack,
                                            TAG.Flow,
                                            TAG.Sensor,
                                        ],
                                    }
                                },
                            },
                            "Fume_Hood_Air_Flow_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Fume,
                                    TAG.Hood,
                                    TAG.Air,
                                    TAG.Flow,
                                    TAG.Sensor,
                                ],
                            },
                            "Outside_Air_Flow_Sensor": {
                                "substances": [
                                    [BRICK.measures, BRICK.Flow],
                                    [BRICK.measures, BRICK.Outside_Air],
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Flow,
                                    TAG.Air,
                                    TAG.Outside,
                                ],
                            },
                            "Return_Air_Flow_Sensor": {
                                "substances": [
                                    [BRICK.measures, BRICK.Flow],
                                    [BRICK.measures, BRICK.Return_Air],
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Flow,
                                    TAG.Air,
                                    TAG.Return,
                                ],
                            },
                            "Supply_Air_Flow_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Flow,
                                    TAG.Air,
                                    TAG.Supply,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Flow],
                                    [BRICK.measures, BRICK.Supply_Air],
                                ],
                                OWL.equivalentClass: BRICK["Discharge_Air_Flow_Sensor"],
                                "subclasses": {
                                    "Average_Supply_Air_Flow_Sensor": {
                                        OWL.equivalentClass: BRICK[
                                            "Average_Discharge_Air_Flow_Sensor"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Average,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Flow,
                                            TAG.Sensor,
                                        ],
                                    }
                                },
                            },
                        },
                    },
                    "Water_Flow_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Flow, TAG.Water],
                        "substances": [
                            [BRICK.measures, BRICK.Flow],
                            [BRICK.measures, BRICK.Water],
                        ],
                        "subclasses": {
                            "Hot_Water_Flow_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Flow,
                                    TAG.Water,
                                    TAG.Hot,
                                ],
                            },
                            "Supply_Water_Flow_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Flow,
                                    TAG.Water,
                                    TAG.Supply,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Flow],
                                    [BRICK.measures, BRICK.Supply_Water],
                                ],
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Water_Flow_Sensor"
                                ],
                                "subclasses": {
                                    "Chilled_Water_Supply_Flow_Sensor": {
                                        OWL.equivalentClass: BRICK[
                                            "Chilled_Water_Discharge_Flow_Sensor"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Sensor,
                                            TAG.Flow,
                                            TAG.Water,
                                            TAG.Supply,
                                            TAG.Chilled,
                                        ],
                                        "substances": [
                                            [BRICK.measures, BRICK.Flow],
                                            [
                                                BRICK.measures,
                                                BRICK.Supply_Chilled_Water,
                                            ],
                                        ],
                                    },
                                    "Supply_Condenser_Water_Flow_Sensor": {
                                        "substances": [
                                            [BRICK.measures, BRICK.Flow],
                                            [
                                                BRICK.measures,
                                                BRICK.Supply_Condenser_Water,
                                            ],
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Sensor,
                                            TAG.Flow,
                                            TAG.Water,
                                            TAG.Supply,
                                            TAG.Condenser,
                                        ],
                                    },
                                },
                            },
                            "Discharge_Water_Flow_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Flow,
                                    TAG.Water,
                                    TAG.Discharge,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Flow],
                                    [BRICK.measures, BRICK.Discharge_Water],
                                ],
                                "subclasses": {
                                    "Chilled_Water_Discharge_Flow_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Sensor,
                                            TAG.Flow,
                                            TAG.Water,
                                            TAG.Discharge,
                                            TAG.Chilled,
                                        ],
                                        "substances": [
                                            [BRICK.measures, BRICK.Flow],
                                            [
                                                BRICK.measures,
                                                BRICK.Discharge_Chilled_Water,
                                            ],
                                        ],
                                    }
                                },
                            },
                            "Return_Water_Flow_Sensor": {
                                "substances": [
                                    [BRICK.measures, BRICK.Flow],
                                    [BRICK.measures, BRICK.Return_Water],
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Flow,
                                    TAG.Water,
                                    TAG.Return,
                                ],
                                "subclasses": {
                                    "Return_Condenser_Water_Flow_Sensor": {
                                        "substances": [
                                            [BRICK.measures, BRICK.Flow],
                                            [
                                                BRICK.measures,
                                                BRICK.Return_Condenser_Water,
                                            ],
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Sensor,
                                            TAG.Flow,
                                            TAG.Water,
                                            TAG.Return,
                                            TAG.Condenser,
                                        ],
                                    },
                                },
                            },
                        },
                    },
                },
            },
            "Frequency_Sensor": {
                "substances": [[BRICK.measures, BRICK.Frequency]],
                "tags": [TAG.Point, TAG.Sensor, TAG.Frequency],
                "subclasses": {
                    "Output_Frequency_Sensor": {
                        "tags": [TAG.Point, TAG.Output, TAG.Frequency, TAG.Sensor],
                    }
                },
            },
            "Frost_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Frost],
                "parents": [BRICK.Temperature_Sensor],
                "substances": [
                    [BRICK.measures, BRICK.Frost],
                    [BRICK.measures, BRICK.Temperature],
                ],
            },
            "Gas_Sensor": {"tags": [TAG.Point, TAG.Sensor, TAG.Gas]},
            "Hail_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Hail],
                "substances": [[BRICK.measures, BRICK.Hail]],
            },
            "Heat_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Heat],
                "subclasses": {
                    "Trace_Heat_Sensor": {
                        # TODO: substance
                        "tags": [TAG.Point, TAG.Trace, TAG.Heat, TAG.Sensor],
                    },
                },
            },
            "Humidity_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Humidity],
                "substances": [[BRICK.measures, BRICK.Humidity]],
                "subclasses": {
                    "Relative_Humidity_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Humidity,
                            TAG.Air,
                            TAG.Relative,
                        ],
                        "substances": [
                            [BRICK.measures, BRICK.Relative_Humidity],
                            [BRICK.measures, BRICK.Air],
                        ],
                        "subclasses": {
                            "Discharge_Air_Humidity_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Humidity,
                                    TAG.Relative,
                                    TAG.Air,
                                    TAG.Discharge,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Relative_Humidity],
                                    [BRICK.measures, BRICK.Discharge_Air],
                                ],
                            },
                            "Exhaust_Air_Humidity_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Humidity,
                                    TAG.Relative,
                                    TAG.Air,
                                    TAG.Exhaust,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Relative_Humidity],
                                    [BRICK.measures, BRICK.Exhaust_Air],
                                ],
                            },
                            "Outside_Air_Humidity_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Humidity,
                                    TAG.Relative,
                                    TAG.Air,
                                    TAG.Outside,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Relative_Humidity],
                                    [BRICK.measures, BRICK.Outside_Air],
                                ],
                            },
                            "Return_Air_Humidity_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Humidity,
                                    TAG.Relative,
                                    TAG.Air,
                                    TAG.Return,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Relative_Humidity],
                                    [BRICK.measures, BRICK.Return_Air],
                                ],
                            },
                            "Supply_Air_Humidity_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Humidity,
                                    TAG.Relative,
                                    TAG.Air,
                                    TAG.Supply,
                                ],
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Air_Humidity_Sensor"
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Relative_Humidity],
                                    [BRICK.measures, BRICK.Supply_Air],
                                ],
                            },
                            "Zone_Air_Humidity_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Humidity,
                                    TAG.Relative,
                                    TAG.Air,
                                    TAG.Zone,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Relative_Humidity],
                                    [BRICK.measures, BRICK.Zone_Air],
                                ],
                            },
                            "Mixed_Air_Humidity_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Humidity,
                                    TAG.Relative,
                                    TAG.Air,
                                    TAG.Mixed,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Relative_Humidity],
                                    [BRICK.measures, BRICK.Mixed_Air],
                                ],
                            },
                        },
                    },
                },
            },
            "Illuminance_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Illuminance],
                "substances": [[BRICK.measures, BRICK.Illuminance]],
                "subclasses": {
                    "Outside_Illuminance_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Illuminance, TAG.Outside],
                    }
                },
            },
            "Luminance_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Luminance],
                "substances": [[BRICK.measures, BRICK.Luminance]],
            },
            "Motion_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Motion],
                "subclasses": {
                    "PIR_Sensor": {"tags": [TAG.Point, TAG.Sensor, TAG.PIR]}
                },
            },
            "Occupancy_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Occupancy],
                "substances": [[BRICK.measures, BRICK.Occupancy]],
                "subclasses": {
                    "PIR_Sensor": {"tags": [TAG.Point, TAG.PIR, TAG.Sensor]}
                },
            },
            "Piezoelectric_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Piezoelectric],
            },
            "Pressure_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Pressure],
                "substances": [[BRICK.measures, BRICK.Pressure]],
                "subclasses": {
                    "Differential_Pressure_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Pressure, TAG.Differential],
                        "subclasses": {
                            "Air_Differential_Pressure_Sensor": {
                                "substances": [
                                    [BRICK.measures, BRICK.Pressure],
                                    [BRICK.measures, BRICK.Air],
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Air,
                                    TAG.Sensor,
                                    TAG.Pressure,
                                    TAG.Differential,
                                ],
                                "subclasses": {
                                    "Return_Air_Differential_Pressure_Sensor": {
                                        "substances": [
                                            [BRICK.measures, BRICK.Pressure],
                                            [BRICK.measures, BRICK.Return_Air],
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Return,
                                            TAG.Air,
                                            TAG.Sensor,
                                            TAG.Pressure,
                                            TAG.Differential,
                                        ],
                                    },
                                },
                            },
                            "Chilled_Water_Differential_Pressure_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Pressure,
                                    TAG.Differential,
                                    TAG.Water,
                                    TAG.Chilled,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Pressure],
                                    [BRICK.measures, BRICK.Chilled_Water],
                                ],
                            },
                            "Filter_Differential_Pressure_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Pressure,
                                    TAG.Differential,
                                    TAG.Filter,
                                ],
                            },
                            "Hot_Water_Differential_Pressure_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Pressure,
                                    TAG.Differential,
                                    TAG.Water,
                                    TAG.Hot,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Pressure],
                                    [BRICK.measures, BRICK.Hot_Water],
                                ],
                                "subclasses": {
                                    "Medium_Temperature_Hot_Water_Differential_Pressure_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Medium,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                            TAG.Pressure,
                                            TAG.Differential,
                                            TAG.Water,
                                            TAG.Hot,
                                        ],
                                    },
                                },
                            },
                        },
                    },
                    "Static_Pressure_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Pressure, TAG.Static],
                        "subclasses": {
                            "Building_Air_Static_Pressure_Sensor": {
                                "substances": [
                                    [BRICK.measures, BRICK.Static_Pressure],
                                    [BRICK.measures, BRICK.Building_Air],
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Building,
                                    TAG.Air,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Sensor,
                                ],
                            },
                            "Discharge_Air_Static_Pressure_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Pressure,
                                    TAG.Static,
                                    TAG.Air,
                                    TAG.Discharge,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Static_Pressure],
                                    [BRICK.measures, BRICK.Discharge_Air],
                                ],
                            },
                            "Supply_Air_Static_Pressure_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Pressure,
                                    TAG.Static,
                                    TAG.Air,
                                    TAG.Supply,
                                ],
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Air_Static_Pressure_Sensor"
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Static_Pressure],
                                    [BRICK.measures, BRICK.Supply_Air],
                                ],
                            },
                            "Exhaust_Air_Static_Pressure_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Pressure,
                                    TAG.Static,
                                    TAG.Air,
                                    TAG.Exhaust,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Static_Pressure],
                                    [BRICK.measures, BRICK.Exhaust_Air],
                                ],
                                "subclasses": {
                                    "Average_Exhaust_Air_Static_Pressure_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Average,
                                            TAG.Exhaust,
                                            TAG.Air,
                                            TAG.Static,
                                            TAG.Pressure,
                                            TAG.Sensor,
                                        ],
                                    },
                                    "Lowest_Exhaust_Air_Static_Pressure_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Lowest,
                                            TAG.Exhaust,
                                            TAG.Air,
                                            TAG.Static,
                                            TAG.Pressure,
                                            TAG.Sensor,
                                        ],
                                    },
                                },
                            },
                        },
                    },
                    "Velocity_Pressure_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Pressure, TAG.Velocity],
                        "substances": [[BRICK.measures, BRICK.Velocity_Pressure]],
                        "subclasses": {
                            "Discharge_Air_Velocity_Pressure_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Pressure,
                                    TAG.Velocity,
                                    TAG.Discharge,
                                    TAG.Air,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Velocity_Pressure],
                                    [BRICK.measures, BRICK.Discharge_Air],
                                ],
                            },
                            "Exhaust_Air_Velocity_Pressure_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Pressure,
                                    TAG.Velocity,
                                    TAG.Exhaust,
                                    TAG.Air,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Velocity_Pressure],
                                    [BRICK.measures, BRICK.Exhaust_Air],
                                ],
                            },
                            "Supply_Air_Velocity_Pressure_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Pressure,
                                    TAG.Velocity,
                                    TAG.Supply,
                                    TAG.Air,
                                ],
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Air_Velocity_Pressure_Sensor"
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Velocity_Pressure],
                                    [BRICK.measures, BRICK.Supply_Air],
                                ],
                            },
                        },
                    },
                },
            },
            "Power_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Power],
                "substances": [[BRICK.measures, BRICK.Power]],
                "subclasses": {
                    "Thermal_Power_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Power, TAG.Thermal],
                        "subclasses": {
                            "Heating_Thermal_Power_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Heat,
                                    TAG.Sensor,
                                    TAG.Power,
                                    TAG.Thermal,
                                ],
                            }
                        },
                    },
                    "Electrical_Power_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Power, TAG.Electrical],
                        "subclasses": {
                            "Reactive_Power_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Power,
                                    TAG.Reactive,
                                    TAG.Electrical,
                                ],
                                "substances": [[BRICK.measures, BRICK.Reactive_Power]],
                            },
                            "Active_Power_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Power,
                                    TAG.Real,
                                    TAG.Electrical,
                                ],
                                "substances": [[BRICK.measures, BRICK.Active_Power]],
                            },
                            "Peak_Power_Demand_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Peak,
                                    TAG.Power,
                                    TAG.Demand,
                                    TAG.Sensor,
                                    TAG.Electrical,
                                ],
                                "substances": [[BRICK.measures, BRICK.Peak_Power]],
                                "parents": [BRICK.Demand_Sensor],
                            },
                        },
                    },
                },
            },
            "Rain_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Rain],
                # TODO: substances
                "substances": [[BRICK.measures, BRICK.Precipitation]],
                "subclasses": {
                    "Rain_Duration_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Rain, TAG.Duration],
                    }
                },
            },
            "Duration_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Duration],
                # TODO: substances
                "subclasses": {
                    "Rain_Duration_Sensor": {
                        "tags": [TAG.Point, TAG.Rain, TAG.Duration, TAG.Sensor],
                    },
                    "Run_Time_Sensor": {
                        "tags": [TAG.Point, TAG.Run, TAG.Time, TAG.Sensor],
                    },
                    "On_Timer_Sensor": {
                        "tags": [TAG.Point, TAG.On, TAG.Timer, TAG.Sensor],
                        OWL.equivalentClass: BRICK.Run_Time_Sensor,
                    },
                },
            },
            "Solar_Radiance_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Radiance, TAG.Solar],
                "substances": [[BRICK.measures, BRICK.Solar_Radiance]],
            },
            "Speed_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Speed],
                "substances": [[BRICK.measures, BRICK.Speed]],
                "subclasses": {
                    "Differential_Speed_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Speed, TAG.Differential],
                    },
                    "Motor_Speed_Sensor": {
                        "tags": [TAG.Point, TAG.Motor, TAG.Speed, TAG.Sensor],
                    },
                    "Wind_Speed_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Speed, TAG.Wind],
                        "substances": [[BRICK.measures, BRICK.Wind_Speed]],
                    },
                },
            },
            "Torque_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Torque],
                "substances": [[BRICK.measures, BRICK.Torque]],
                "subclasses": {
                    "Motor_Torque_Sensor": {
                        "tags": [TAG.Point, TAG.Motor, TAG.Torque, TAG.Sensor],
                    }
                },
            },
            "Voltage_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Voltage],
                "substances": [[BRICK.measures, BRICK.Voltage]],
                "subclasses": {
                    "Battery_Voltage_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Voltage, TAG.Battery],
                    },
                    "DC_Bus_Voltage_Sensor": {
                        "tags": [TAG.Point, TAG.Dc, TAG.Bus, TAG.Voltage, TAG.Sensor],
                    },
                    "Output_Voltage_Sensor": {
                        "tags": [TAG.Point, TAG.Output, TAG.Voltage, TAG.Sensor],
                    },
                },
            },
            "Water_Level_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Water, TAG.Level],
                "substances": [
                    [BRICK.measures, BRICK.Water],
                    [BRICK.measures, BRICK.Level],
                ],
                "subclasses": {
                    "Deionised_Water_Level_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Water,
                            TAG.Level,
                            TAG.Deionised,
                        ],
                        "substances": [
                            [BRICK.measures, BRICK.Deionized_Water],
                            [BRICK.measures, BRICK.Level],
                        ],
                    },
                    "Collection_Basin_Water_Level_Sensor": {
                        "tags": [
                            TAG.Collection,
                            TAG.Basin,
                            TAG.Water,
                            TAG.Level,
                            TAG.Sensor,
                            TAG.Point,
                        ],
                        "substances": [
                            [BRICK.measures, BRICK.Collection_Basin_Water],
                            [BRICK.measures, BRICK.Level],
                        ],
                    },
                },
            },
            "Usage_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Usage],
                "subclasses": {
                    "Steam_Usage_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Usage, TAG.Steam],
                    },
                    "Energy_Usage_Sensor": {
                        "parents": [BRICK.Energy_Sensor],
                        "tags": [TAG.Point, TAG.Sensor, TAG.Energy, TAG.Usage],
                    },
                    "Water_Usage_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Usage, TAG.Water],
                        "subclasses": {
                            "Hot_Water_Usage_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Usage,
                                    TAG.Hot,
                                    TAG.Water,
                                ],
                            },
                        },
                    },
                },
            },
            "Temperature_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Temperature],
                "substances": [[BRICK.measures, BRICK.Temperature]],
                "subclasses": {
                    "Air_Temperature_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Temperature, TAG.Air],
                        "substances": [
                            [BRICK.measures, BRICK.Temperature],
                            [BRICK.measures, BRICK.Air],
                        ],
                        "subclasses": {
                            "Discharge_Air_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Temperature,
                                    TAG.Air,
                                    TAG.Discharge,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Temperature],
                                    [BRICK.measures, BRICK.Discharge_Air],
                                ],
                                "subclasses": {
                                    "Preheat_Discharge_Air_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Preheat,
                                            TAG.Discharge,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                        ],
                                    }
                                },
                            },
                            "Supply_Air_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Temperature,
                                    TAG.Air,
                                    TAG.Supply,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Temperature],
                                    [BRICK.measures, BRICK.Supply_Air],
                                ],
                                OWL.equivalentClass: BRICK[
                                    "Discharge_Air_Temperature_Sensor"
                                ],
                                "subclasses": {
                                    "Preheat_Supply_Air_Temperature_Sensor": {
                                        OWL.equivalentClass: BRICK[
                                            "Preheat_Discharge_Air_Temperature_Sensor"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Preheat,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                        ],
                                    }
                                },
                            },
                            "Underfloor_Air_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Underfloor,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Sensor,
                                ],
                            },
                            "Zone_Air_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Zone,
                                    TAG.Air,
                                    TAG.Temperature,
                                    TAG.Sensor,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Temperature],
                                    [BRICK.measures, BRICK.Zone_Air],
                                ],
                                "subclasses": {
                                    "Average_Zone_Air_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Sensor,
                                            TAG.Temperature,
                                            TAG.Zone,
                                            TAG.Average,
                                            TAG.Air,
                                        ],
                                    },
                                    "Coldest_Zone_Air_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Coldest,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                        ],
                                    },
                                    "Warmest_Zone_Air_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Warmest,
                                            TAG.Zone,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                        ],
                                    },
                                },
                            },
                            "Exhaust_Air_Temperature_Sensor": {
                                "substances": [
                                    [BRICK.measures, BRICK.Temperature],
                                    [BRICK.measures, BRICK.Exhaust_Air],
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Temperature,
                                    TAG.Air,
                                    TAG.Exhaust,
                                ],
                            },
                            "Mixed_Air_Temperature_Sensor": {
                                "substances": [
                                    [BRICK.measures, BRICK.Temperature],
                                    [BRICK.measures, BRICK.Mixed_Air],
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Temperature,
                                    TAG.Air,
                                    TAG.Mixed,
                                ],
                            },
                            "Return_Air_Temperature_Sensor": {
                                "substances": [
                                    [BRICK.measures, BRICK.Temperature],
                                    [BRICK.measures, BRICK.Return_Air],
                                ],
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Temperature,
                                    TAG.Air,
                                    TAG.Return,
                                ],
                            },
                            "Outside_Air_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Temperature,
                                    TAG.Air,
                                    TAG.Outside,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Temperature],
                                    [BRICK.measures, BRICK.Outside_Air],
                                ],
                                "subclasses": {
                                    "Outside_Air_Temperature_Enable_Differential_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Outside,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Enable,
                                            TAG.Differential,
                                            TAG.Sensor,
                                        ],
                                        "subclasses": {
                                            "Low_Outside_Air_Temperature_Enable_Differential_Sensor": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Low,
                                                    TAG.Outside,
                                                    TAG.Air,
                                                    TAG.Temperature,
                                                    TAG.Enable,
                                                    TAG.Differential,
                                                    TAG.Sensor,
                                                ],
                                            },
                                        },
                                    },
                                    "Intake_Air_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Outside,
                                            TAG.Air,
                                            TAG.Temperature,
                                            TAG.Intake,
                                            TAG.Sensor,
                                        ],
                                    },
                                },
                            },
                        },
                    },
                    "Radiant_Panel_Temperature_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Temperature,
                            TAG.Radiant,
                            TAG.Panel,
                        ],
                        "substances": [
                            [BRICK.measures, BRICK.Temperature],
                            [BRICK.measures, BRICK.Radiant_Panel],
                        ],
                        "subclasses": {
                            "Inside_Face_Surface_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Inside,
                                    TAG.Face,
                                    TAG.Surface,
                                    TAG.Temperature,
                                    TAG.Sensor,
                                ],
                            },
                            "Outside_Face_Surface_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Outside,
                                    TAG.Face,
                                    TAG.Surface,
                                    TAG.Temperature,
                                    TAG.Sensor,
                                ],
                            },
                            "Embedded_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Embedded,
                                    TAG.Temperature,
                                    TAG.Sensor,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Temperature],
                                    [BRICK.measures, BRICK.Internal_Material],
                                ],
                                "subclasses": {
                                    "Core_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Core,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                        ],
                                    },
                                },
                            },
                        },
                    },
                    "Water_Temperature_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Temperature, TAG.Water],
                        "substances": [
                            [BRICK.measures, BRICK.Temperature],
                            [BRICK.measures, BRICK.Water],
                        ],
                        "subclasses": {
                            "Heat_Exchanger_Supply_Water_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Heat,
                                    TAG.Exchanger,
                                    TAG.Supply,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Sensor,
                                ],
                            },
                            "Hot_Water_Supply_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Temperature,
                                    TAG.Water,
                                    TAG.Hot,
                                    TAG.Supply,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Temperature],
                                    [BRICK.measures, BRICK.Supply_Hot_Water],
                                ],
                                "subclasses": {
                                    "Domestic_Hot_Water_Supply_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Domestic,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Supply,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                        ],
                                    },
                                    "High_Temperature_Hot_Water_Supply_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.High,
                                            TAG.Temperature,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Supply,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                        ],
                                    },
                                    "Medium_Temperature_Hot_Water_Supply_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Medium,
                                            TAG.Temperature,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Supply,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                        ],
                                    },
                                },
                            },
                            "Chilled_Water_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Temperature,
                                    TAG.Water,
                                    TAG.Chilled,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Temperature],
                                    [BRICK.measures, BRICK.Chilled_Water],
                                ],
                                "subclasses": {
                                    "Chilled_Water_Differential_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                        ],
                                    },
                                    "Chilled_Water_Supply_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Sensor,
                                            TAG.Temperature,
                                            TAG.Water,
                                            TAG.Chilled,
                                            TAG.Supply,
                                        ],
                                        "substances": [
                                            [BRICK.measures, BRICK.Temperature],
                                            [
                                                BRICK.measures,
                                                BRICK.Supply_Chilled_Water,
                                            ],
                                        ],
                                    },
                                },
                            },
                            "Discharge_Water_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Temperature,
                                    TAG.Water,
                                    TAG.Discharge,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Temperature],
                                    [BRICK.measures, BRICK.Discharge_Water],
                                ],
                            },
                            "Entering_Water_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Temperature,
                                    TAG.Water,
                                    TAG.Entering,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Temperature],
                                    [BRICK.measures, BRICK.Entering_Water],
                                ],
                            },
                            "Leaving_Water_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Temperature,
                                    TAG.Water,
                                    TAG.Leaving,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Temperature],
                                    [BRICK.measures, BRICK.Leaving_Water],
                                ],
                                "subclasses": {
                                    "Ice_Tank_Leaving_Water_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Ice,
                                            TAG.Tank,
                                            TAG.Leaving,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                        ],
                                    },
                                },
                            },
                            "Return_Water_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Temperature,
                                    TAG.Water,
                                    TAG.Return,
                                ],
                                "substances": [
                                    [BRICK.measures, BRICK.Temperature],
                                    [BRICK.measures, BRICK.Return_Water],
                                ],
                                "subclasses": {
                                    "Hot_Water_Return_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Return,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                        ],
                                        "subclasses": {
                                            "Medium_Temperature_Hot_Water_Return_Temperature_Sensor": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.Medium,
                                                    TAG.Hot,
                                                    TAG.Water,
                                                    TAG.Return,
                                                    TAG.Temperature,
                                                    TAG.Sensor,
                                                ],
                                            },
                                            "High_Temperature_Hot_Water_Return_Temperature_Sensor": {
                                                "tags": [
                                                    TAG.Point,
                                                    TAG.High,
                                                    TAG.Hot,
                                                    TAG.Water,
                                                    TAG.Return,
                                                    TAG.Temperature,
                                                    TAG.Sensor,
                                                ],
                                            },
                                        },
                                    },
                                    "Chilled_Water_Return_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Return,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                        ],
                                        "parents": [
                                            BRICK.Chilled_Water_Temperature_Sensor
                                        ],
                                    },
                                    "Differential_Supply_Return_Water_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Differential,
                                            TAG.Supply,
                                            TAG.Return,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                        ],
                                    },
                                },
                            },
                            "Collection_Basin_Water_Temperature_Sensor": {
                                "substances": [
                                    [BRICK.measures, BRICK.Temperature],
                                    [BRICK.measures, BRICK.Collection_Basin_Water],
                                ],
                                "tags": [
                                    TAG.Collection,
                                    TAG.Basin,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Sensor,
                                    TAG.Point,
                                ],
                            },
                            "Condenser_Water_Temperature_Sensor": {
                                "substances": [
                                    [BRICK.measures, BRICK.Temperature],
                                    [BRICK.measures, BRICK.Condenser_Water],
                                ],
                                "tags": [
                                    TAG.Condenser,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Sensor,
                                    TAG.Point,
                                ],
                                "subclasses": {
                                    "Supply_Condenser_Water_Temperature_Sensor": {
                                        "substances": [
                                            [BRICK.measures, BRICK.Temperature],
                                            [
                                                BRICK.measures,
                                                BRICK.Supply_Condenser_Water,
                                            ],
                                        ],
                                        "tags": [
                                            TAG.Supply,
                                            TAG.Condenser,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                            TAG.Point,
                                        ],
                                    },
                                    "Return_Condenser_Water_Temperature_Sensor": {
                                        "substances": [
                                            [BRICK.measures, BRICK.Temperature],
                                            [
                                                BRICK.measures,
                                                BRICK.Return_Condenser_Water,
                                            ],
                                        ],
                                        "tags": [
                                            TAG.Return,
                                            TAG.Condenser,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                            TAG.Point,
                                        ],
                                    },
                                },
                            },
                        },
                    },
                    "Air_Wet_Bulb_Temperature_Sensor": {
                        "substances": [
                            [BRICK.measures, BRICK.Wet_Bulb_Temperature],
                            [BRICK.measures, BRICK.Air],
                        ],
                        "parents": [BRICK.Air_Temperature_Sensor],
                        "tags": [
                            TAG.Air,
                            TAG.Wet,
                            TAG.Bulb,
                            TAG.Temperature,
                            TAG.Sensor,
                            TAG.Point,
                        ],
                        "subclasses": {
                            "Outside_Air_Wet_Bulb_Temperature_Sensor": {
                                "substances": [
                                    [BRICK.measures, BRICK.Wet_Bulb_Temperature],
                                    [BRICK.measures, BRICK.Outside_Air],
                                ],
                                "parents": [BRICK.Outside_Air_Temperature_Sensor],
                                "tags": [
                                    TAG.Outside,
                                    TAG.Air,
                                    TAG.Wet,
                                    TAG.Bulb,
                                    TAG.Temperature,
                                    TAG.Sensor,
                                    TAG.Point,
                                ],
                            },
                        },
                    },
                },
            },
        },
    },
}
