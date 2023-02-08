from .namespaces import TAG, BRICK, OWL, SKOS

# Defining substances
substances = {
    "Fluid": {
        "tags": [TAG.Fluid],
        SKOS.narrower: {
            "Refrigerant": {
                "tags": [TAG.Fluid, TAG.Refrigerant],
            },
            "Gas": {
                "tags": [TAG.Fluid, TAG.Gas],
                SKOS.narrower: {
                    "Air": {
                        "tags": [TAG.Fluid, TAG.Gas, TAG.Air],
                        SKOS.narrower: {
                            "Bypass_Air": {
                                "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Bypass],
                            },
                            "Outside_Air": {
                                "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Outside],
                            },
                            "Zone_Air": {
                                "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Zone],
                            },
                            "Building_Air": {
                                "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Building],
                            },
                            "Mixed_Air": {
                                "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Mixed],
                            },
                            "Return_Air": {
                                "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Return],
                            },
                            "Exhaust_Air": {
                                "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Exhaust],
                            },
                            "Supply_Air": {
                                "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Supply],
                            },
                            "Discharge_Air": {
                                "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Discharge],
                            },
                        },
                    },
                    "CO2": {"tags": [TAG.Fluid, TAG.Gas, TAG.CO2]},
                    "CO": {"tags": [TAG.Fluid, TAG.Gas, TAG.CO]},
                    "Steam": {"tags": [TAG.Fluid, TAG.Gas, TAG.Steam]},
                    "Natural_Gas": {"tags": [TAG.Fluid, TAG.Gas, TAG.Natural]},
                },
            },
            "Liquid": {
                "tags": [TAG.Fluid, TAG.Liquid],
                SKOS.narrower: {
                    "Gasoline": {"tags": [TAG.Fluid, TAG.Liquid, TAG.Gasoline]},
                    "Liquid_CO2": {"tags": [TAG.Fluid, TAG.Liquid, TAG.CO2]},
                    "Glycol": {"tags": [TAG.Fluid, TAG.Liquid, TAG.Glycol]},
                    "Oil": {
                        "tags": [TAG.Fluid, TAG.Liquid, TAG.Oil],
                        SKOS.narrower: {
                            "Fuel_Oil": {
                                "tags": [TAG.Fluid, TAG.Liquid, TAG.Oil, TAG.Fuel]
                            }
                        },
                    },
                    "Water": {
                        "tags": [TAG.Fluid, TAG.Liquid, TAG.Water],
                        SKOS.narrower: {
                            "Deionized_Water": {
                                "tags": [
                                    TAG.Fluid,
                                    TAG.Liquid,
                                    TAG.Deionized,
                                    TAG.Water,
                                ],
                            },
                            "Bypass_Water": {
                                "tags": [TAG.Fluid, TAG.Liquid, TAG.Water, TAG.Bypass],
                            },
                            "Chilled_Water": {
                                "tags": [TAG.Fluid, TAG.Liquid, TAG.Water, TAG.Chilled],
                                SKOS.narrower: {
                                    "Entering_Chilled_Water": {
                                        "tags": [
                                            TAG.Fluid,
                                            TAG.Liquid,
                                            TAG.Water,
                                            TAG.Chilled,
                                            TAG.Entering,
                                        ],
                                        "parents": [BRICK.Entering_Water],
                                    },
                                    "Leaving_Chilled_Water": {
                                        "tags": [
                                            TAG.Fluid,
                                            TAG.Liquid,
                                            TAG.Water,
                                            TAG.Chilled,
                                            TAG.Leaving,
                                        ],
                                        "parents": [BRICK.Leaving_Water],
                                    },
                                },
                            },
                            "Collection_Basin_Water": {
                                "tags": [
                                    TAG.Fluid,
                                    TAG.Liquid,
                                    TAG.Water,
                                    TAG.Collection,
                                    TAG.Basin,
                                ]
                            },
                            "Blowdown_Water": {
                                "tags": [
                                    TAG.Fluid,
                                    TAG.Liquid,
                                    TAG.Water,
                                    TAG.Blowdown,
                                ],
                            },
                            "Condenser_Water": {
                                "tags": [
                                    TAG.Fluid,
                                    TAG.Liquid,
                                    TAG.Water,
                                    TAG.Condenser,
                                ],
                                SKOS.narrower: {
                                    "Entering_Condenser_Water": {
                                        "tags": [
                                            TAG.Fluid,
                                            TAG.Liquid,
                                            TAG.Water,
                                            TAG.Condenser,
                                            TAG.Entering,
                                        ],
                                    },
                                    "Leaving_Condenser_Water": {
                                        "tags": [
                                            TAG.Fluid,
                                            TAG.Liquid,
                                            TAG.Water,
                                            TAG.Condenser,
                                            TAG.Leaving,
                                        ],
                                    },
                                },
                            },
                            "Domestic_Water": {
                                "tags": [
                                    TAG.Fluid,
                                    TAG.Liquid,
                                    TAG.Water,
                                    TAG.Domestic,
                                ],
                            },
                            "Potable_Water": {
                                "tags": [
                                    TAG.Fluid,
                                    TAG.Liquid,
                                    TAG.Water,
                                    TAG.Potable,
                                ],
                            },
                            "Leaving_Water": {
                                "tags": [TAG.Fluid, TAG.Liquid, TAG.Water, TAG.Leaving],
                            },
                            "Entering_Water": {
                                "tags": [
                                    TAG.Fluid,
                                    TAG.Liquid,
                                    TAG.Water,
                                    TAG.Entering,
                                ],
                            },
                            "Hot_Water": {
                                "tags": [TAG.Fluid, TAG.Liquid, TAG.Water, TAG.Hot],
                                SKOS.narrower: {
                                    "Entering_Hot_Water": {
                                        "tags": [
                                            TAG.Fluid,
                                            TAG.Liquid,
                                            TAG.Water,
                                            TAG.Hot,
                                            TAG.Entering,
                                        ],
                                        "parents": [BRICK.Entering_Water],
                                    },
                                    "Leaving_Hot_Water": {
                                        "tags": [
                                            TAG.Fluid,
                                            TAG.Liquid,
                                            TAG.Water,
                                            TAG.Hot,
                                            TAG.Leaving,
                                        ],
                                        "parents": [BRICK.Leaving_Water],
                                    },
                                },
                            },
                            "Makeup_Water": {
                                "tags": [TAG.Fluid, TAG.Liquid, TAG.Water, TAG.Makeup],
                            },
                        },
                    },
                },
            },
        },
    },
    "Solid": {
        "tags": [TAG.Solid],
        SKOS.narrower: {
            "Ice": {"tags": [TAG.Solid, TAG.Ice]},
            "Frost": {"tags": [TAG.Solid, TAG.Frost]},
            "Hail": {"tags": [TAG.Solid, TAG.Hail]},
            "Soil": {"tags": [TAG.Solid, TAG.Soil]},
        },
    },
}
