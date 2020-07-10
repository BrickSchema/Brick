from rdflib import Literal
from .namespaces import TAG, BRICK

# Defining substances
substances = {
    "Fluid": {
        "tags": [TAG.Fluid],
        "subclasses": {
            "Gas": {
                "tags": [TAG.Fluid, TAG.Gas],
                "subclasses": {
                    "Air": {
                        "tags": [TAG.Fluid, TAG.Gas, TAG.Air],
                        "subclasses": {
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
                    "Steam": {"tags": [TAG.Fluid, TAG.Gas, TAG.Steam]},
                    "Natural_Gas": {"tags": [TAG.Fluid, TAG.Gas, TAG.Natural]},
                },
            },
            "Liquid": {
                "tags": [TAG.Fluid, TAG.Liquid],
                "subclasses": {
                    "Gasoline": {"tags": [TAG.Fluid, TAG.Liquid, TAG.Gasoline]},
                    "Liquid_CO2": {"tags": [TAG.Fluid, TAG.Liquid, TAG.CO2]},
                    "Oil": {
                        "tags": [TAG.Fluid, TAG.Liquid, TAG.Oil],
                        "subclasses": {
                            "Fuel_Oil": {"tags": [TAG.Liquid, TAG.Oil, TAG.Fuel]}
                        },
                    },
                    "Water": {
                        "tags": [TAG.Fluid, TAG.Liquid, TAG.Water],
                        "subclasses": {
                            "Deionized_Water": {
                                "tags": [
                                    TAG.Fluid,
                                    TAG.Liquid,
                                    TAG.Deionized,
                                    TAG.Water,
                                ],
                            },
                            "Chilled_Water": {
                                "tags": [TAG.Fluid, TAG.Liquid, TAG.Water, TAG.Chilled],
                                "subclasses": {
                                    "Discharge_Chilled_Water": {
                                        "tags": [
                                            TAG.Fluid,
                                            TAG.Liquid,
                                            TAG.Water,
                                            TAG.Chilled,
                                            TAG.Discharge,
                                        ],
                                        "parents": [BRICK.Discharge_Water],
                                    },
                                    "Supply_Chilled_Water": {
                                        "tags": [
                                            TAG.Fluid,
                                            TAG.Liquid,
                                            TAG.Water,
                                            TAG.Chilled,
                                            TAG.Supply,
                                        ],
                                        "parents": [BRICK.Supply_Water],
                                    },
                                },
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
                            },
                            "Domestic_Water": {
                                "tags": [
                                    TAG.Fluid,
                                    TAG.Liquid,
                                    TAG.Water,
                                    TAG.Domestic,
                                ],
                            },
                            "Discharge_Water": {
                                "tags": [
                                    TAG.Fluid,
                                    TAG.Liquid,
                                    TAG.Water,
                                    TAG.Discharge,
                                ],
                            },
                            "Entering_Water": {
                                "tags": [
                                    TAG.Fluid,
                                    TAG.Liquid,
                                    TAG.Water,
                                    TAG.Entering,
                                ],
                            },
                            "Leaving_Water": {
                                "tags": [TAG.Fluid, TAG.Liquid, TAG.Water, TAG.Leaving],
                            },
                            "Return_Water": {
                                "tags": [TAG.Fluid, TAG.Liquid, TAG.Water, TAG.Return],
                            },
                            "Supply_Water": {
                                "tags": [TAG.Fluid, TAG.Liquid, TAG.Water, TAG.Supply],
                                "subclasses": {
                                    "Supply_Chilled_Water": {
                                        "tags": [
                                            TAG.Fluid,
                                            TAG.Liquid,
                                            TAG.Water,
                                            TAG.Chilled,
                                            TAG.Supply,
                                        ],
                                    },
                                    "Supply_Hot_Water": {
                                        "tags": [
                                            TAG.Fluid,
                                            TAG.Liquid,
                                            TAG.Water,
                                            TAG.Hot,
                                            TAG.Supply,
                                        ],
                                    },
                                },
                            },
                            "Hot_Water": {
                                "tags": [TAG.Fluid, TAG.Liquid, TAG.Water, TAG.Hot],
                                "subclasses": {
                                    "Supply_Hot_Water": {
                                        "tags": [
                                            TAG.Fluid,
                                            TAG.Liquid,
                                            TAG.Water,
                                            TAG.Hot,
                                            TAG.Supply,
                                        ],
                                    }
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
        "subclasses": {
            "Ice": {"tags": [TAG.Solid, TAG.Ice]},
            "Frost": {"tags": [TAG.Solid, TAG.Frost]},
            "Hail": {"tags": [TAG.Solid, TAG.Hail]},
        },
    },
}
