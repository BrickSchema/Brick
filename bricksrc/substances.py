from .namespaces import TAG, BRICK, OWL

# Defining substances
substances = {
    "Fluid": {
        "tags": [TAG.Fluid],
        "subclasses": {
            "Gas": {"tags": [TAG.Fluid, TAG.Gas],
                "subclasses": {
                    "Hydrocarbon_Refrigerant": {
                        "tags": [TAG.Fluid, TAG.Gas, TAG.Hydrocarbon_Refrigerant],
                        "subclasses": {
                            "Air": {
                                "tags": [TAG.Fluid, TAG.Gas, TAG.Hydrocarbon_Refrigerant, TAG.Air],
                                "subclasses": {
                                    "Bypass_Air": {
                                        "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Hydrocarbon_Refrigerant, TAG.Bypass],
                                    },
                                    "Outside_Air": {
                                        "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Hydrocarbon_Refrigerant, TAG.Outside],
                                    },
                                    "Zone_Air": {
                                        "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Hydrocarbon_Refrigerant, TAG.Zone],
                                    },
                                    "Building_Air": {
                                        "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Hydrocarbon_Refrigerant, TAG.Building],
                                    },
                                    "Mixed_Air": {
                                        "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Hydrocarbon_Refrigerant, TAG.Mixed],
                                    },
                                    "Return_Air": {
                                        "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Hydrocarbon_Refrigerant, TAG.Return],
                                    },
                                    "Exhaust_Air": {
                                        "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Hydrocarbon_Refrigerant, TAG.Exhaust],
                                    },
                                    "Supply_Air": {
                                        OWL.equivalentClass: BRICK["Discharge_Air"],
                                        "tags": [TAG.Fluid, TAG.Gas, TAG.Hydrocarbon_Refrigerant, TAG.Air, TAG.Supply],
                                    },
                                    "Discharge_Air": {
                                        "tags": [TAG.Fluid, TAG.Gas, TAG.Hydrocarbon_Refrigerant, TAG.Air, TAG.Discharge],
                                    },
                                },
                            },
                            "CO2": {"tags": [TAG.Fluid, TAG.Gas, TAG.Hydrocarbon_Refrigerant, TAG.CO2]},
                            "CO": {"tags": [TAG.Fluid, TAG.Gas, TAG.Hydrocarbon_Refrigerant, TAG.CO]},
                            "Steam": {"tags": [TAG.Fluid, TAG.Gas, TAG.Hydrocarbon_Refrigerant, TAG.Steam]},
                            "Natural_Gas": {"tags": [TAG.Fluid, TAG.Gas, TAG.Hydrocarbon_Refrigerant, TAG.Natural]},
                        },
                    },
                    "Fluorocarbon_Refrigerant": {
                        "tags": [TAG.Fluid, TAG.Gas, TAG.Fluorocarbon_Refrigerant],
                        "subclasses": {
                            "CFC": { "tags": [TAG.Fluid, TAG.Gas, TAG.Fluorocarbon_Refrigerant, TAG.CFC]},
                            "HCFC": {"tags": [TAG.Fluid, TAG.Gas, TAG.Fluorocarbon_Refrigerant, TAG.HCFC]},
                            "HFC": {
                                "tags": [TAG.Fluid, TAG.Gas, TAG.Fluorocarbon_Refrigerant, TAG.HFC],
                                "subclasses": {
                                    "R410A": {
                                        "tags": [TAG.Fluid, TAG.Gas, TAG.Fluorocarbon_Refrigerant, TAG.HFC, TAG.R410A],
                                    },
                                    "R134a": {
                                        "tags": [TAG.Fluid, TAG.Gas, TAG.Fluorocarbon_Refrigerant, TAG.HFC, TAG.R134a],
                                    },
                                },
                            },
                            "HFO": {
                                "tags": [TAG.Fluid, TAG.Gas, TAG.Fluorocarbon_Refrigerant, TAG.HFO],
                                "subclasses": {
                                    "R1234yf": {
                                        "tags": [TAG.Fluid, TAG.Gas, TAG.Fluorocarbon_Refrigerant, TAG.HFO, TAG.R1234yf],
                                    },
                                },
                            },
                        },
                    },
                },
            },
            "Liquid": {
                "tags": [TAG.Fluid, TAG.Liquid],
                "subclasses":{
                    "Liquid_Hydrocarbon_Refrigerant": {
                        "tags": [TAG.Fluid, TAG.Liquid, TAG.Hydrocarbon_Refrigerant],
                        "subclasses": {
                            "Gasoline": {"tags": [TAG.Fluid, TAG.Liquid, TAG.Hydrocarbon_Refrigerant, TAG.Gasoline]},
                            "Liquid_CO2": {"tags": [TAG.Fluid, TAG.Liquid, TAG.Hydrocarbon_Refrigerant, TAG.CO2]},
                            "Glycol": {"tags": [TAG.Fluid, TAG.Liquid, TAG.Hydrocarbon_Refrigerant, TAG.Glycol]},
                            "Oil": {
                                "tags": [TAG.Fluid, TAG.Liquid, TAG.Hydrocarbon_Refrigerant, TAG.Oil],
                                "subclasses": {
                                    "Fuel_Oil": {
                                        "tags": [TAG.Fluid, TAG.Liquid, TAG.Hydrocarbon_Refrigerant, TAG.Oil, TAG.Fuel]
                                    }
                                },
                            },
                            "Water": {
                                "tags": [TAG.Fluid, TAG.Liquid, TAG.Hydrocarbon_Refrigerant, TAG.Water],
                                "subclasses": {
                                    "Deionized_Water": {
                                        "tags": [
                                            TAG.Fluid,
                                            TAG.Liquid,
                                            TAG.Deionized,
                                            TAG.Hydrocarbon_Refrigerant,
                                            TAG.Water,
                                        ],
                                    },
                                    "Bypass_Water": {
                                        "tags": [TAG.Fluid, TAG.Liquid, TAG.Hydrocarbon_Refrigerant, TAG.Water, TAG.Bypass],
                                    },
                                    "Chilled_Water": {
                                        "tags": [TAG.Fluid, TAG.Liquid, TAG.Hydrocarbon_Refrigerant, TAG.Water, TAG.Chilled],
                                        "subclasses": {
                                            "Discharge_Chilled_Water": {
                                                "tags": [
                                                    TAG.Fluid,
                                                    TAG.Liquid,
                                                    TAG.Hydrocarbon_Refrigerant,
                                                    TAG.Water,
                                                    TAG.Chilled,
                                                    TAG.Discharge,
                                                ],
                                                "parents": [BRICK.Discharge_Water],
                                            },
                                            "Supply_Chilled_Water": {
                                                OWL.equivalentClass: BRICK[
                                                    "Discharge_Chilled_Water"
                                                ],
                                                "tags": [
                                                    TAG.Fluid,
                                                    TAG.Liquid,
                                                    TAG.Hydrocarbon_Refrigerant,
                                                    TAG.Water,
                                                    TAG.Chilled,
                                                    TAG.Supply,
                                                ],
                                                "parents": [BRICK.Supply_Water],
                                            },
                                        },
                                    },
                                    "Collection_Basin_Water": {
                                        "tags": [
                                            TAG.Fluid,
                                            TAG.Liquid,
                                            TAG.Hydrocarbon_Refrigerant,
                                            TAG.Water,
                                            TAG.Collection,
                                            TAG.Basin,
                                        ]
                                    },
                                    "Blowdown_Water": {
                                        "tags": [
                                            TAG.Fluid,
                                            TAG.Liquid,
                                            TAG.Hydrocarbon_Refrigerant,
                                            TAG.Water,
                                            TAG.Blowdown,
                                        ],
                                    },
                                    "Condenser_Water": {
                                        "tags": [
                                            TAG.Fluid,
                                            TAG.Liquid,
                                            TAG.Hydrocarbon_Refrigerant,
                                            TAG.Water,
                                            TAG.Condenser,
                                        ],
                                        "subclasses": {
                                            "Supply_Condenser_Water": {
                                                "tags": [
                                                    TAG.Fluid,
                                                    TAG.Liquid,
                                                    TAG.Hydrocarbon_Refrigerant,
                                                    TAG.Water,
                                                    TAG.Condenser,
                                                    TAG.Supply,
                                                ],
                                            },
                                            "Return_Condenser_Water": {
                                                "tags": [
                                                    TAG.Fluid,
                                                    TAG.Liquid,
                                                    TAG.Hydrocarbon_Refrigerant,
                                                    TAG.Water,
                                                    TAG.Condenser,
                                                    TAG.Return,
                                                ],
                                            },
                                        },
                                    },
                                    "Domestic_Water": {
                                        "tags": [
                                            TAG.Fluid,
                                            TAG.Liquid,
                                            TAG.Hydrocarbon_Refrigerant,
                                            TAG.Water,
                                            TAG.Domestic,
                                        ],
                                    },
                                    "Potable_Water": {
                                        "tags": [
                                            TAG.Fluid,
                                            TAG.Liquid,
                                            TAG.Hydrocarbon_Refrigerant,
                                            TAG.Water,
                                            TAG.Potable,
                                        ],
                                    },
                                    "Discharge_Water": {
                                        "tags": [
                                            TAG.Fluid,
                                            TAG.Liquid,
                                            TAG.Hydrocarbon_Refrigerant,
                                            TAG.Water,
                                            TAG.Discharge,
                                        ],
                                    },
                                    "Entering_Water": {
                                        "tags": [
                                            TAG.Fluid,
                                            TAG.Liquid,
                                            TAG.Hydrocarbon_Refrigerant,
                                            TAG.Water,
                                            TAG.Entering,
                                        ],
                                    },
                                    "Leaving_Water": {
                                        "tags": [TAG.Fluid, TAG.Liquid, TAG.Hydrocarbon_Refrigerant, TAG.Water, TAG.Leaving],
                                    },
                                    "Return_Water": {
                                        "tags": [TAG.Fluid, TAG.Liquid, TAG.Hydrocarbon_Refrigerant, TAG.Water, TAG.Return],
                                    },
                                    "Supply_Water": {
                                        "tags": [TAG.Fluid, TAG.Liquid, TAG.Hydrocarbon_Refrigerant, TAG.Water, TAG.Supply],
                                        OWL.equivalentClass: BRICK["Discharge_Water"],
                                    },
                                    "Hot_Water": {
                                        "tags": [TAG.Fluid, TAG.Liquid, TAG.Hydrocarbon_Refrigerant, TAG.Water, TAG.Hot],
                                        "subclasses": {
                                            "Supply_Hot_Water": {
                                                "tags": [
                                                    TAG.Fluid,
                                                    TAG.Liquid,
                                                    TAG.Hydrocarbon_Refrigerant,
                                                    TAG.Water,
                                                    TAG.Hot,
                                                    TAG.Supply,
                                                ],
                                                "parents": [BRICK.Supply_Water],
                                                OWL.equivalentClass: BRICK[
                                                    "Discharge_Hot_Water"
                                                ],
                                            },
                                            "Discharge_Hot_Water": {
                                                "tags": [
                                                    TAG.Fluid,
                                                    TAG.Liquid,
                                                    TAG.Hydrocarbon_Refrigerant,
                                                    TAG.Water,
                                                    TAG.Hot,
                                                    TAG.Discharge,
                                                ],
                                                "parents": [BRICK.Discharge_Water],
                                            },
                                            "Return_Hot_Water": {
                                                "tags": [
                                                    TAG.Fluid,
                                                    TAG.Liquid,
                                                    TAG.Hydrocarbon_Refrigerant,
                                                    TAG.Water,
                                                    TAG.Hot,
                                                    TAG.Return,
                                                ],
                                                "parents": [BRICK.Return_Water],
                                            },
                                        },
                                    },
                                    "Makeup_Water": {
                                        "tags": [TAG.Fluid, TAG.Liquid, TAG.Hydrocarbon_Refrigerant, TAG.Water, TAG.Makeup],
                                    },
                                },
                            },
                        },
                    },
                    "Liquid_Fluorocarbon_Refrigerant": {
                        "tags": [TAG.Fluid, TAG.Liquid, TAG.Fluorocarbon_Refrigerant],
                        "subclasses": {
                            "Liquid_CFC": { "tags": [TAG.Fluid, TAG.Liquid, TAG.Fluorocarbon_Refrigerant, TAG.CFC]},
                            "Liquid_HCFC": {"tags": [TAG.Fluid, TAG.Liquid, TAG.Fluorocarbon_Refrigerant, TAG.HCFC]},
                            "Liquid_HFC": {
                                "tags": [TAG.Fluid, TAG.Liquid, TAG.Fluorocarbon_Refrigerant, TAG.HFC],
                                "subclasses": {
                                    "Liquid_R410A": {
                                        "tags": [TAG.Fluid, TAG.Liquid, TAG.Fluorocarbon_Refrigerant, TAG.HFC, TAG.R410A],
                                    },
                                    "Liquid_R134a": {
                                        "tags": [TAG.Fluid, TAG.Liquid, TAG.Fluorocarbon_Refrigerant, TAG.HFC, TAG.R134a],
                                    },
                                },
                            },
                            "Liquid_HFO": {
                                "tags": [TAG.Fluid, TAG.Liquid, TAG.Fluorocarbon_Refrigerant, TAG.HFO],
                                "subclasses": {
                                    "Liquid_R1234yf": {
                                        "tags": [TAG.Fluid, TAG.Liquid, TAG.Fluorocarbon_Refrigerant, TAG.HFO, TAG.R1234yf],
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    },
    "Solid": {
        "tags": [TAG.Solid],
        "subclasses": {
            "Ice": {"tags": [TAG.Solid, TAG.Ice]},
            "Frost": {"tags": [TAG.Solid, TAG.Frost]},
            "Hail": {"tags": [TAG.Solid, TAG.Hail]},
        },
    },
}
