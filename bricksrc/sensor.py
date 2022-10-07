from rdflib import Literal
from .namespaces import BRICK, TAG, OWL, RDFS, QUDT

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
                    "Temperature_Adjust_Sensor": {
                        BRICK.hasQuantity: BRICK.Differential_Temperature,
                        "tags": [TAG.Point, TAG.Sensor, TAG.Adjust, TAG.Temperature],
                    },
                },
            },
            "Air_Quality_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Air, TAG.Quality],
                "subclasses": {
                    "Ammonia_Sensor": {
                        "tags": [TAG.Point, TAG.Ammonia, TAG.Sensor],
                        BRICK.hasQuantity: BRICK.Ammonia_Concentration,
                        BRICK.hasSubstance: BRICK.Air,
                    },
                    "CO_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.CO],
                        BRICK.hasQuantity: BRICK.CO_Concentration,
                        BRICK.hasSubstance: BRICK.Air,
                        "subclasses": {
                            "CO_Level_Sensor": {
                                "tags": [TAG.Point, TAG.CO, TAG.Level, TAG.Sensor],
                            },
                            "CO_Differential_Sensor": {
                                BRICK.hasQuantity: BRICK.Differential_CO_Concentration,
                                BRICK.hasSubstance: BRICK.Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.CO,
                                    TAG.Differential,
                                    TAG.Sensor,
                                ],
                            },
                            "Outside_Air_CO_Sensor": {
                                BRICK.hasQuantity: BRICK.CO_Concentration,
                                BRICK.hasSubstance: BRICK.Outside_Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Outside,
                                    TAG.Air,
                                    TAG.CO,
                                    TAG.Sensor,
                                ],
                            },
                            "Return_Air_CO_Sensor": {
                                BRICK.hasQuantity: BRICK.CO_Concentration,
                                BRICK.hasSubstance: BRICK.Return_Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Return,
                                    TAG.Air,
                                    TAG.CO,
                                    TAG.Sensor,
                                ],
                            },
                        },
                    },
                    "CO2_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.CO2],
                        BRICK.hasQuantity: BRICK.CO2_Concentration,
                        BRICK.hasSubstance: BRICK.Air,
                        "subclasses": {
                            "CO2_Differential_Sensor": {
                                BRICK.hasQuantity: BRICK.Differential_CO2_Concentration,
                                BRICK.hasSubstance: BRICK.Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.CO2,
                                    TAG.Differential,
                                    TAG.Sensor,
                                ],
                            },
                            "CO2_Level_Sensor": {
                                BRICK.hasQuantity: BRICK.CO2_Concentration,
                                BRICK.hasSubstance: BRICK.Air,
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
                                BRICK.hasQuantity: BRICK.CO2_Concentration,
                                BRICK.hasSubstance: BRICK.Outside_Air,
                            },
                            "Return_Air_CO2_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Return,
                                    TAG.Air,
                                    TAG.CO2,
                                    TAG.Sensor,
                                ],
                                BRICK.hasQuantity: BRICK.CO2_Concentration,
                                BRICK.hasSubstance: BRICK.Return_Air,
                            },
                        },
                    },
                    "NO2_Level_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Level, TAG.NO2],
                        BRICK.hasQuantity: BRICK.NO2_Concentration,
                        BRICK.hasSubstance: BRICK.Air,
                    },
                    "Formaldehyde_Level_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Level, TAG.Formaldehyde],
                        BRICK.hasSubstance: BRICK.Air,
                        BRICK.hasQuantity: BRICK.Formaldehyde_Concentration,
                    },
                    "Ozone_Level_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Level, TAG.Ozone],
                        BRICK.hasSubstance: BRICK.Air,
                        BRICK.hasQuantity: BRICK.Ozone_Concentration,
                    },
                    "Methane_Level_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Level, TAG.Methane],
                        BRICK.hasSubstance: BRICK.Air,
                        BRICK.hasQuantity: BRICK.Methane_Concentration,
                    },
                    "Radioactivity_Concentration_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Radioactivity,
                            TAG.Concentration,
                        ],
                        BRICK.hasSubstance: BRICK.Air,
                        BRICK.hasQuantity: BRICK.Radioactivity_Concentration,
                        "subclasses": {
                            "Radon_Concentration_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Radon,
                                    TAG.Concentration,
                                ],
                                BRICK.hasSubstance: BRICK.Air,
                                BRICK.hasQuantity: BRICK.Radon_Concentration,
                            },
                        },
                    },
                    "Particulate_Matter_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Particulate, TAG.Matter],
                        BRICK.hasSubstance: BRICK.Air,
                        BRICK.hasQuantity: BRICK.Air_Quality,
                        "subclasses": {
                            "PM1_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Particulate,
                                    TAG.Matter,
                                    TAG.PM1,
                                ],
                                BRICK.hasSubstance: BRICK.Air,
                                BRICK.hasQuantity: BRICK.PM1_Concentration,
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
                                BRICK.hasSubstance: BRICK.Air,
                                BRICK.hasQuantity: BRICK.PM10_Concentration,
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
                                BRICK.hasSubstance: BRICK.Air,
                                BRICK.hasQuantity: BRICK["PM2.5_Concentration"],
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
                                BRICK.hasSubstance: BRICK.Air,
                                BRICK.hasQuantity: BRICK["TVOC_Concentration"],
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
                BRICK.hasSubstance: BRICK.Air,
                BRICK.hasQuantity: BRICK.GrainsOfMoisture,
                "subclasses": {
                    "Outside_Air_Grains_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Outside,
                            TAG.Air,
                            TAG.Grains,
                            TAG.Sensor,
                        ],
                        BRICK.hasSubstance: BRICK.Outside_Air,
                        BRICK.hasQuantity: BRICK.GrainsOfMoisture,
                    },
                    "Return_Air_Grains_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Return,
                            TAG.Air,
                            TAG.Grains,
                            TAG.Sensor,
                        ],
                        BRICK.hasSubstance: BRICK.Return_Air,
                        BRICK.hasQuantity: BRICK.GrainsOfMoisture,
                    },
                },
            },
            "Angle_Sensor": {
                BRICK.hasQuantity: BRICK.Angle,
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
                BRICK.hasQuantity: BRICK.Capacity,
            },
            "Contact_Sensor": {"tags": [TAG.Point, TAG.Sensor, TAG.Contact]},
            "Conductivity_Sensor": {
                # IFC ConductanceSensor
                # TODO: pull from
                # https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/
                "tags": [TAG.Point, TAG.Sensor, TAG.Conductivity],
                BRICK.hasQuantity: BRICK.Conductivity,
                "subclasses": {
                    "Deionised_Water_Conductivity_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Conductivity,
                            TAG.Water,
                            TAG.Deionised,
                        ],
                        BRICK.hasQuantity: BRICK.Conductivity,
                        BRICK.hasSubstance: BRICK.Deionized_Water,
                    }
                },
            },
            "Current_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Current],
                BRICK.hasQuantity: BRICK.Electric_Current,
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
                BRICK.hasQuantity: BRICK.Position,
                "tags": [TAG.Point, TAG.Position, TAG.Sensor],
                "subclasses": {
                    "Sash_Position_Sensor": {
                        BRICK.hasQuantity: BRICK.Position,
                        "tags": [TAG.Point, TAG.Sash, TAG.Position, TAG.Sensor],
                    },
                    "Damper_Position_Sensor": {
                        BRICK.hasQuantity: BRICK.Position,
                        "tags": [TAG.Point, TAG.Damper, TAG.Position, TAG.Sensor],
                    },
                    "Valve_Position_Sensor": {
                        BRICK.hasQuantity: BRICK.Position,
                        "tags": [TAG.Point, TAG.Valve, TAG.Position, TAG.Sensor],
                    },
                },
            },
            "Demand_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Demand],
                "subclasses": {
                    "Peak_Demand_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Peak,
                            TAG.Power,
                            TAG.Demand,
                            TAG.Sensor,
                            TAG.Electric,
                        ],
                        BRICK.hasQuantity: BRICK.Peak_Power,
                    },
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
                BRICK.hasQuantity: BRICK.Dewpoint,
                "subclasses": {
                    "Outside_Air_Dewpoint_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Dewpoint,
                            TAG.Air,
                            TAG.Outside,
                        ],
                        BRICK.hasQuantity: BRICK.Dewpoint,
                        BRICK.hasSubstance: BRICK.Outside_Air,
                    },
                    "Return_Air_Dewpoint_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Dewpoint,
                            TAG.Air,
                            TAG.Return,
                        ],
                        BRICK.hasQuantity: BRICK.Dewpoint,
                        BRICK.hasSubstance: BRICK.Return_Air,
                    },
                    "Exhaust_Air_Dewpoint_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Dewpoint,
                            TAG.Air,
                            TAG.Exhaust,
                        ],
                        BRICK.hasQuantity: BRICK.Dewpoint,
                        BRICK.hasSubstance: BRICK.Exhaust_Air,
                    },
                    "Supply_Air_Dewpoint_Sensor": {
                        OWL.equivalentClass: BRICK["Discharge_Air_Dewpoint_Sensor"],
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Dewpoint,
                            TAG.Air,
                            TAG.Supply,
                        ],
                        "substances": [
                            [BRICK.measures, BRICK.Dewpoint],
                            [BRICK.measures, BRICK.Supply_Air],
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
                        BRICK.hasQuantity: BRICK.Dewpoint,
                        BRICK.hasSubstance: BRICK.Discharge_Air,
                    },
                    "Zone_Air_Dewpoint_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Dewpoint,
                            TAG.Air,
                            TAG.Zone,
                        ],
                        BRICK.hasQuantity: BRICK.Dewpoint,
                        BRICK.hasSubstance: BRICK.Zone_Air,
                    },
                },
            },
            "Direction_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Direction],
                BRICK.hasQuantity: BRICK.Direction,
                "subclasses": {
                    "Wind_Direction_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Direction, TAG.Wind],
                        BRICK.hasQuantity: BRICK.Wind_Direction,
                    }
                },
            },
            "Energy_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Energy],
                BRICK.hasQuantity: BRICK.Energy,
                "subclasses": {
                    "Electric_Energy_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Energy, TAG.Electric],
                        BRICK.hasQuantity: BRICK.Electric_Energy,
                        "subclasses": {
                            "Reactive_Energy_Sensor": {
                                BRICK.hasQuantity: BRICK.Reactive_Energy,
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Energy,
                                    TAG.Electric,
                                    TAG.Reactive,
                                ],
                            }
                        },
                    }
                },
            },
            "Enthalpy_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Enthalpy],
                BRICK.hasQuantity: BRICK.Enthalpy,
                "subclasses": {
                    "Air_Enthalpy_Sensor": {
                        BRICK.hasQuantity: BRICK.Enthalpy,
                        BRICK.hasSubstance: BRICK.Air,
                        "subclasses": {
                            "Outside_Air_Enthalpy_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Outside,
                                    TAG.Air,
                                    TAG.Enthalpy,
                                    TAG.Sensor,
                                ],
                                BRICK.hasQuantity: BRICK.Enthalpy,
                                BRICK.hasSubstance: BRICK.Outside_Air,
                            },
                            "Return_Air_Enthalpy_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Return,
                                    TAG.Air,
                                    TAG.Enthalpy,
                                    TAG.Sensor,
                                ],
                                BRICK.hasQuantity: BRICK.Enthalpy,
                                BRICK.hasSubstance: BRICK.Return_Air,
                            },
                        },
                        "tags": [TAG.Point, TAG.Air, TAG.Enthalpy, TAG.Sensor],
                    }
                },
            },
            "Fire_Sensor": {"tags": [TAG.Point, TAG.Sensor, TAG.Fire]},
            "Flow_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Flow],
                BRICK.hasQuantity: BRICK.Flow,
                "subclasses": {
                    "Natural_Gas_Flow_Sensor": {
                        BRICK.hasSubstance: BRICK.Natural_Gas,
                        BRICK.hasQuantity: BRICK.Flow,
                        "tags": [TAG.Point, TAG.Sensor, TAG.Natural, TAG.Gas, TAG.Flow],
                    },
                    "Air_Flow_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Flow, TAG.Air],
                        BRICK.hasQuantity: BRICK.Flow,
                        BRICK.hasSubstance: BRICK.Air,
                        "subclasses": {
                            "Bypass_Air_Flow_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Flow,
                                    TAG.Air,
                                    TAG.Bypass,
                                ],
                                BRICK.hasQuantity: BRICK.Flow,
                                BRICK.hasSubstance: BRICK.Bypass_Air,
                            },
                            "Discharge_Air_Flow_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Flow,
                                    TAG.Air,
                                    TAG.Discharge,
                                ],
                                BRICK.hasQuantity: BRICK.Flow,
                                BRICK.hasSubstance: BRICK.Discharge_Air,
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
                                BRICK.hasQuantity: BRICK.Flow,
                                BRICK.hasSubstance: BRICK.Exhaust_Air,
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
                            "Mixed_Air_Flow_Sensor": {
                                BRICK.hasQuantity: BRICK.Flow,
                                BRICK.hasSubstance: BRICK.Mixed_Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Flow,
                                    TAG.Air,
                                    TAG.Mixed,
                                ],
                            },
                            "Outside_Air_Flow_Sensor": {
                                BRICK.hasQuantity: BRICK.Flow,
                                BRICK.hasSubstance: BRICK.Outside_Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Flow,
                                    TAG.Air,
                                    TAG.Outside,
                                ],
                            },
                            "Return_Air_Flow_Sensor": {
                                BRICK.hasQuantity: BRICK.Flow,
                                BRICK.hasSubstance: BRICK.Return_Air,
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
                                BRICK.hasQuantity: BRICK.Flow,
                                BRICK.hasSubstance: BRICK.Supply_Air,
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
                        BRICK.hasQuantity: BRICK.Flow,
                        BRICK.hasSubstance: BRICK.Water,
                        "subclasses": {
                            "Condenser_Water_Flow_Sensor": {
                                BRICK.hasQuantity: BRICK.Flow,
                                BRICK.hasSubstance: BRICK.Condenser_Water,
                                "tags": [
                                    TAG.Condenser,
                                    TAG.Water,
                                    TAG.Flow,
                                    TAG.Sensor,
                                    TAG.Point,
                                ],
                            },
                            "Entering_Water_Flow_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Entering,
                                    TAG.Water,
                                    TAG.Flow,
                                    TAG.Sensor,
                                ],
                                BRICK.hasQuantity: BRICK.Flow,
                                BRICK.hasSubstance: BRICK.Entering_Water,
                                "subclasses": {
                                    "Entering_Chilled_Water_Flow_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Sensor,
                                            TAG.Flow,
                                            TAG.Water,
                                            TAG.Entering,
                                            TAG.Chilled,
                                        ],
                                        BRICK.hasQuantity: BRICK.Flow,
                                        BRICK.hasSubstance: BRICK.Entering_Chilled_Water,
                                        "parents": [BRICK.Chilled_Water_Flow_Sensor],
                                    },
                                    "Entering_Hot_Water_Flow_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Entering,
                                            TAG.Flow,
                                            TAG.Sensor,
                                        ],
                                        BRICK.hasQuantity: BRICK.Flow,
                                        BRICK.hasSubstance: BRICK.Entering_Hot_Water,
                                        "parents": [BRICK.Hot_Water_Flow_Sensor],
                                    },
                                    "Entering_Condenser_Water_Flow_Sensor": {
                                        BRICK.hasQuantity: BRICK.Flow,
                                        BRICK.hasSubstance: BRICK.Entering_Condenser_Water,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Sensor,
                                            TAG.Flow,
                                            TAG.Water,
                                            TAG.Entering,
                                            TAG.Condenser,
                                        ],
                                    },
                                },
                            },
                            "Bypass_Water_Flow_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Bypass,
                                    TAG.Water,
                                    TAG.Flow,
                                    TAG.Sensor,
                                ],
                                BRICK.hasQuantity: BRICK.Flow,
                                BRICK.hasSubstance: BRICK.Bypass_Water,
                            },
                            "Hot_Water_Flow_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Flow,
                                    TAG.Water,
                                    TAG.Hot,
                                ],
                                BRICK.hasQuantity: BRICK.Flow,
                                BRICK.hasSubstance: BRICK.Hot_Water,
                            },
                            "Chilled_Water_Flow_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.Flow,
                                    TAG.Sensor,
                                ],
                                BRICK.hasQuantity: BRICK.Flow,
                                BRICK.hasSubstance: BRICK.Chilled_Water,
                            },
                            "Leaving_Water_Flow_Sensor": {
                                BRICK.hasQuantity: BRICK.Flow,
                                BRICK.hasSubstance: BRICK.Leaving_Water,
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Flow,
                                    TAG.Water,
                                    TAG.Leaving,
                                ],
                                "subclasses": {
                                    "Leaving_Chilled_Water_Flow_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Sensor,
                                            TAG.Flow,
                                            TAG.Water,
                                            TAG.Leaving,
                                            TAG.Chilled,
                                        ],
                                        BRICK.hasQuantity: BRICK.Flow,
                                        BRICK.hasSubstance: BRICK.Leaving_Chilled_Water,
                                        "parents": [BRICK.Chilled_Water_Flow_Sensor],
                                    },
                                    "Leaving_Hot_Water_Flow_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Sensor,
                                            TAG.Flow,
                                            TAG.Water,
                                            TAG.Leaving,
                                            TAG.Hot,
                                        ],
                                        BRICK.hasQuantity: BRICK.Flow,
                                        BRICK.hasSubstance: BRICK.Leaving_Hot_Water,
                                        "parents": [BRICK.Hot_Water_Flow_Sensor],
                                    },
                                    "Leaving_Condenser_Water_Flow_Sensor": {
                                        BRICK.hasQuantity: BRICK.Flow,
                                        BRICK.hasSubstance: BRICK.Leaving_Condenser_Water,
                                        "parents": [BRICK.Condenser_Water_Flow_Sensor],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Sensor,
                                            TAG.Flow,
                                            TAG.Water,
                                            TAG.Leaving,
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
                BRICK.hasQuantity: BRICK.Frequency,
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
                BRICK.hasQuantity: BRICK.Temperature,
                BRICK.hasSubstance: BRICK.Frost,
            },
            "Gas_Sensor": {"tags": [TAG.Point, TAG.Sensor, TAG.Gas]},
            "Hail_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Hail],
                BRICK.hasSubstance: BRICK.Hail,
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
                BRICK.hasQuantity: BRICK.Humidity,
                "subclasses": {
                    "Relative_Humidity_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Humidity,
                            TAG.Air,
                            TAG.Relative,
                        ],
                        BRICK.hasQuantity: BRICK.Relative_Humidity,
                        BRICK.hasSubstance: BRICK.Air,
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
                                BRICK.hasQuantity: BRICK.Relative_Humidity,
                                BRICK.hasSubstance: BRICK.Discharge_Air,
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
                                BRICK.hasQuantity: BRICK.Relative_Humidity,
                                BRICK.hasSubstance: BRICK.Exhaust_Air,
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
                                BRICK.hasQuantity: BRICK.Relative_Humidity,
                                BRICK.hasSubstance: BRICK.Outside_Air,
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
                                BRICK.hasQuantity: BRICK.Relative_Humidity,
                                BRICK.hasSubstance: BRICK.Return_Air,
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
                                BRICK.hasQuantity: BRICK.Relative_Humidity,
                                BRICK.hasSubstance: BRICK.Supply_Air,
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
                                BRICK.hasQuantity: BRICK.Relative_Humidity,
                                BRICK.hasSubstance: BRICK.Zone_Air,
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
                                BRICK.hasQuantity: BRICK.Relative_Humidity,
                                BRICK.hasSubstance: BRICK.Mixed_Air,
                            },
                        },
                    },
                },
            },
            "Illuminance_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Illuminance],
                BRICK.hasQuantity: BRICK.Illuminance,
                "subclasses": {
                    "Outside_Illuminance_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Illuminance, TAG.Outside],
                    }
                },
            },
            "Imbalance_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Imbalance],
                "subclasses": {
                    "Current_Imbalance_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Imbalance, TAG.Current],
                        BRICK.hasQuantity: BRICK.Current_Imbalance,
                    },
                    "Voltage_Imbalance_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Imbalance, TAG.Voltage],
                        BRICK.hasQuantity: BRICK.Voltage_Imbalance,
                    },
                },
            },
            "Luminance_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Luminance],
                BRICK.hasQuantity: BRICK.Luminance,
            },
            "Motion_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Motion],
                "subclasses": {
                    "PIR_Sensor": {"tags": [TAG.Point, TAG.Sensor, TAG.PIR]}
                },
            },
            "Occupancy_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Occupancy],
                BRICK.hasQuantity: BRICK.Occupancy,
            },
            "Occupancy_Count_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Occupancy, TAG.Count],
                BRICK.hasQuantity: BRICK.Occupancy_Count,
            },
            "Piezoelectric_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Piezoelectric],
            },
            "Pressure_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Pressure],
                BRICK.hasQuantity: BRICK.Pressure,
                "subclasses": {
                    "Differential_Pressure_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Pressure, TAG.Differential],
                        BRICK.hasQuantity: BRICK.Differential_Pressure,
                        "subclasses": {
                            "Air_Differential_Pressure_Sensor": {
                                BRICK.hasQuantity: BRICK.Differential_Pressure,
                                BRICK.hasSubstance: BRICK.Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Air,
                                    TAG.Sensor,
                                    TAG.Pressure,
                                    TAG.Differential,
                                ],
                                "subclasses": {
                                    "Exhaust_Air_Differential_Pressure_Sensor": {
                                        BRICK.hasQuantity: BRICK.Differential_Pressure,
                                        BRICK.hasSubstance: BRICK.Exhaust_Air,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Exhaust,
                                            TAG.Air,
                                            TAG.Sensor,
                                            TAG.Pressure,
                                            TAG.Differential,
                                        ],
                                    },
                                    "Return_Air_Differential_Pressure_Sensor": {
                                        BRICK.hasQuantity: BRICK.Differential_Pressure,
                                        BRICK.hasSubstance: BRICK.Return_Air,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Return,
                                            TAG.Air,
                                            TAG.Sensor,
                                            TAG.Pressure,
                                            TAG.Differential,
                                        ],
                                    },
                                    "Supply_Air_Differential_Pressure_Sensor": {
                                        BRICK.hasQuantity: BRICK.Differential_Pressure,
                                        BRICK.hasSubstance: BRICK.Supply_Air,
                                        OWL.equivalentClass: BRICK[
                                            "Discharge_Air_Differential_Pressure_Sensor"
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Supply,
                                            TAG.Air,
                                            TAG.Sensor,
                                            TAG.Pressure,
                                            TAG.Differential,
                                        ],
                                    },
                                    "Discharge_Air_Differential_Pressure_Sensor": {
                                        "substances": [
                                            [
                                                BRICK.measures,
                                                BRICK.Differential_Pressure,
                                            ],
                                            [BRICK.measures, BRICK.Discharge_Air],
                                        ],
                                        "tags": [
                                            TAG.Point,
                                            TAG.Discharge,
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
                                BRICK.hasQuantity: BRICK.Differential_Pressure,
                                BRICK.hasSubstance: BRICK.Chilled_Water,
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
                                BRICK.hasQuantity: BRICK.Differential_Pressure,
                                BRICK.hasSubstance: BRICK.Hot_Water,
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
                                BRICK.hasQuantity: BRICK.Static_Pressure,
                                BRICK.hasSubstance: BRICK.Building_Air,
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
                                BRICK.hasQuantity: BRICK.Static_Pressure,
                                BRICK.hasSubstance: BRICK.Discharge_Air,
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
                                BRICK.hasQuantity: BRICK.Static_Pressure,
                                BRICK.hasSubstance: BRICK.Supply_Air,
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
                                BRICK.hasQuantity: BRICK.Static_Pressure,
                                BRICK.hasSubstance: BRICK.Exhaust_Air,
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
                            "Underfloor_Air_Plenum_Static_Pressure_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Underfloor,
                                    TAG.Air,
                                    TAG.Plenum,
                                    TAG.Static,
                                    TAG.Pressure,
                                    TAG.Sensor,
                                ]
                            },
                        },
                    },
                    "Velocity_Pressure_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Pressure, TAG.Velocity],
                        BRICK.hasQuantity: BRICK.Velocity_Pressure,
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
                                BRICK.hasQuantity: BRICK.Velocity_Pressure,
                                BRICK.hasSubstance: BRICK.Discharge_Air,
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
                                BRICK.hasQuantity: BRICK.Velocity_Pressure,
                                BRICK.hasSubstance: BRICK.Exhaust_Air,
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
                                BRICK.hasQuantity: BRICK.Velocity_Pressure,
                                BRICK.hasSubstance: BRICK.Supply_Air,
                            },
                        },
                    },
                },
            },
            "Power_Factor_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Power, TAG.Factor],
                BRICK.hasQuantity: BRICK.Power_Factor,
            },
            "Power_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Power],
                BRICK.hasQuantity: BRICK.Power,
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
                    "Electric_Power_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Power, TAG.Electric],
                        BRICK.hasQuantity: BRICK.Electric_Power,
                        "subclasses": {
                            "Reactive_Power_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Power,
                                    TAG.Reactive,
                                    TAG.Electric,
                                ],
                                BRICK.hasQuantity: BRICK.Reactive_Power,
                            },
                            "Active_Power_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Power,
                                    TAG.Real,
                                    TAG.Electric,
                                ],
                                BRICK.hasQuantity: BRICK.Active_Power,
                            },
                        },
                    },
                },
            },
            "Rain_Level_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Rain],
                # TODO: substances
                BRICK.hasQuantity: BRICK.Precipitation,
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
            "Refrigerant_Level_Sensor": {
                BRICK.hasQuantity: BRICK.Level,
                BRICK.hasSubstance: BRICK.Refrigerant,
                "tags": [TAG.Point, TAG.Sensor, TAG.Refrigerant, TAG.Level],
            },
            "Solar_Radiance_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Radiance, TAG.Solar],
                BRICK.hasQuantity: BRICK.Solar_Radiance,
            },
            "Speed_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Speed],
                BRICK.hasQuantity: BRICK.Speed,
                "subclasses": {
                    "Differential_Speed_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Speed, TAG.Differential],
                    },
                    "Motor_Speed_Sensor": {
                        "tags": [TAG.Point, TAG.Motor, TAG.Speed, TAG.Sensor],
                    },
                    "Wind_Speed_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Speed, TAG.Wind],
                        BRICK.hasQuantity: BRICK.Linear_Speed,
                    },
                },
            },
            "Torque_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Torque],
                BRICK.hasQuantity: BRICK.Torque,
                "subclasses": {
                    "Motor_Torque_Sensor": {
                        "tags": [TAG.Point, TAG.Motor, TAG.Torque, TAG.Sensor],
                    }
                },
            },
            "Voltage_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Voltage],
                BRICK.hasQuantity: BRICK.Voltage,
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
                BRICK.hasQuantity: BRICK.Level,
                BRICK.hasSubstance: BRICK.Water,
                "subclasses": {
                    "Deionised_Water_Level_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Water,
                            TAG.Level,
                            TAG.Deionised,
                        ],
                        BRICK.hasQuantity: BRICK.Level,
                        BRICK.hasSubstance: BRICK.Deionized_Water,
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
                        BRICK.hasQuantity: BRICK.Level,
                        BRICK.hasSubstance: BRICK.Collection_Basin_Water,
                    },
                },
            },
            "Generation_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Generation],
                "subclasses": {
                    "Energy_Generation_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Generation, TAG.Energy]
                    }
                },
            },
            "Usage_Sensor": {
                "tags": [TAG.Point, TAG.Sensor, TAG.Usage],
                "subclasses": {
                    "Natural_Gas_Usage_Sensor": {
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Usage,
                            TAG.Natural,
                            TAG.Gas,
                        ],
                    },
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
                BRICK.hasQuantity: BRICK.Temperature,
                "subclasses": {
                    "Soil_Temperature_Sensor": {
                        BRICK.hasSubstance: BRICK.Soil,
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Temperature,
                            TAG.Soil,
                        ],
                    },
                    "Natural_Gas_Temperature_Sensor": {
                        BRICK.hasSubstance: BRICK.Natural_Gas,
                        "tags": [
                            TAG.Point,
                            TAG.Sensor,
                            TAG.Temperature,
                            TAG.Natural,
                            TAG.Gas,
                        ],
                    },
                    "Heat_Sink_Temperature_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Temperature, TAG.Heat_Sink]
                    },
                    "Air_Temperature_Sensor": {
                        "tags": [TAG.Point, TAG.Sensor, TAG.Temperature, TAG.Air],
                        BRICK.hasQuantity: BRICK.Temperature,
                        BRICK.hasSubstance: BRICK.Air,
                        "subclasses": {
                            "Discharge_Air_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Temperature,
                                    TAG.Air,
                                    TAG.Discharge,
                                ],
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: BRICK.Discharge_Air,
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
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: BRICK.Supply_Air,
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
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: BRICK.Zone_Air,
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
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: BRICK.Exhaust_Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Temperature,
                                    TAG.Air,
                                    TAG.Exhaust,
                                ],
                            },
                            "Mixed_Air_Temperature_Sensor": {
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: BRICK.Mixed_Air,
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Temperature,
                                    TAG.Air,
                                    TAG.Mixed,
                                ],
                            },
                            "Return_Air_Temperature_Sensor": {
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: BRICK.Return_Air,
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
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: BRICK.Outside_Air,
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
                        "constraints": {
                            BRICK.isPointOf: [BRICK.Radiant_Panel],
                        },
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
                        BRICK.hasQuantity: BRICK.Temperature,
                        BRICK.hasSubstance: BRICK.Water,
                        "subclasses": {
                            "Water_Differential_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Temperature,
                                    TAG.Sensor,
                                ],
                                BRICK.hasQuantity: BRICK.Differential_Temperature,
                                BRICK.hasSubstance: BRICK.Water,
                            },
                            "Domestic_Hot_Water_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Domestic,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Sensor,
                                ],
                            },
                            "Entering_Hot_Water_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Temperature,
                                    TAG.Water,
                                    TAG.Hot,
                                    TAG.Entering,
                                ],
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: BRICK.Entering_Hot_Water,
                                "subclasses": {
                                    "Hot_Water_Differential_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                        ],
                                        "parents": [
                                            BRICK.Water_Differential_Temperature_Sensor,
                                        ],
                                    },
                                    "Entering_Domestic_Hot_Water_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Domestic,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Entering,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                        ],
                                        "parents": [
                                            BRICK.Domestic_Hot_Water_Temperature_Sensor
                                        ],
                                    },
                                    "Entering_High_Temperature_Hot_Water_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.High,
                                            TAG.Temperature,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Entering,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                        ],
                                    },
                                    "Entering_Medium_Temperature_Hot_Water_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Medium,
                                            TAG.Temperature,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Entering,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                        ],
                                    },
                                },
                            },
                            "Leaving_Hot_Water_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Temperature,
                                    TAG.Water,
                                    TAG.Hot,
                                    TAG.Leaving,
                                ],
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: BRICK.Leaving_Hot_Water,
                                "subclasses": {
                                    "Hot_Water_Differential_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                        ],
                                        "parents": [
                                            BRICK.Water_Differential_Temperature_Sensor,
                                        ],
                                    },
                                    "Leaving_Domestic_Hot_Water_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Domestic,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Leaving,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                        ],
                                        "parents": [
                                            BRICK.Domestic_Hot_Water_Temperature_Sensor
                                        ],
                                    },
                                    "Leaving_High_Temperature_Hot_Water_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.High,
                                            TAG.Temperature,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Leaving,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                        ],
                                    },
                                    "Leaving_Medium_Temperature_Hot_Water_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Medium,
                                            TAG.Temperature,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Leaving,
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
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: BRICK.Chilled_Water,
                                "subclasses": {
                                    "Chilled_Water_Differential_Temperature_Sensor": {
                                        BRICK.hasQuantity: BRICK.Differential_Temperature,
                                        BRICK.hasSubstance: BRICK.Chilled_Water,
                                        "tags": [
                                            TAG.Point,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                        ],
                                        "parents": [
                                            BRICK.Water_Differential_Temperature_Sensor
                                        ],
                                    },
                                    "Entering_Chilled_Water_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Sensor,
                                            TAG.Temperature,
                                            TAG.Water,
                                            TAG.Chilled,
                                            TAG.Entering,
                                        ],
                                        BRICK.hasQuantity: BRICK.Temperature,
                                        BRICK.hasSubstance: BRICK.Entering_Chilled_Water,
                                    },
                                    "Leaving_Chilled_Water_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Sensor,
                                            TAG.Temperature,
                                            TAG.Water,
                                            TAG.Chilled,
                                            TAG.Leaving,
                                        ],
                                        "substances": [
                                            [BRICK.measures, BRICK.Temperature],
                                            [
                                                BRICK.measures,
                                                BRICK.Leaving_Chilled_Water,
                                            ],
                                        ],
                                    },
                                    "Differential_Entering_Leaving_Water_Temperature_Sensor": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Sensor,
                                            TAG.Temperature,
                                            TAG.Water,
                                            TAG.Chilled,
                                            TAG.Leaving,
                                            TAG.Entering,
                                            TAG.Differential,
                                        ],
                                        BRICK.hasSubstance: [
                                            BRICK.Leaving_Chilled_Water,
                                            BRICK.Entering_Chilled_Water,
                                        ],
                                        BRICK.hasQuantity: BRICK.Temperature,
                                    },
                                },
                            },
                            "Entering_Water_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Temperature,
                                    TAG.Water,
                                    TAG.Entering,
                                ],
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: BRICK.Entering_Water,
                            },
                            "Leaving_Water_Temperature_Sensor": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Sensor,
                                    TAG.Temperature,
                                    TAG.Water,
                                    TAG.Leaving,
                                ],
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: BRICK.Leaving_Water,
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
                                    "Heat_Exchanger_Leaving_Water_Temperature_Sensor": {
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
                            "Collection_Basin_Water_Temperature_Sensor": {
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: BRICK.Collection_Basin_Water,
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
                                BRICK.hasQuantity: BRICK.Temperature,
                                BRICK.hasSubstance: BRICK.Condenser_Water,
                                "tags": [
                                    TAG.Condenser,
                                    TAG.Water,
                                    TAG.Temperature,
                                    TAG.Sensor,
                                    TAG.Point,
                                ],
                                "subclasses": {
                                    "Leaving_Condenser_Water_Temperature_Sensor": {
                                        BRICK.hasQuantity: BRICK.Temperature,
                                        BRICK.hasSubstance: BRICK.Leaving_Condenser_Water,
                                        "tags": [
                                            TAG.Leaving,
                                            TAG.Condenser,
                                            TAG.Water,
                                            TAG.Temperature,
                                            TAG.Sensor,
                                            TAG.Point,
                                        ],
                                    },
                                    "Entering_Condenser_Water_Temperature_Sensor": {
                                        "substances": [
                                            [BRICK.measures, BRICK.Temperature],
                                            [
                                                BRICK.measures,
                                                BRICK.Entering_Condenser_Water,
                                            ],
                                        ],
                                        "tags": [
                                            TAG.Entering,
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
                        BRICK.hasQuantity: BRICK.Wet_Bulb_Temperature,
                        BRICK.hasSubstance: BRICK.Air,
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
                                BRICK.hasQuantity: BRICK.Wet_Bulb_Temperature,
                                BRICK.hasSubstance: BRICK.Outside_Air,
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
