from rdflib import Literal
from .namespaces import TAG, BRICK, SKOS

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
                                SKOS.definition: Literal(
                                    "air in a bypass duct, used to relieve static pressure"
                                ),
                            },
                            "Outside_Air": {
                                "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Outside],
                                SKOS.definition: Literal(
                                    "air external to a defined zone (e.g., corridors)."
                                ),
                            },
                            "Zone_Air": {
                                "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Zone],
                                SKOS.definition: Literal(
                                    "air inside a defined zone (e.g., corridors)."
                                ),
                            },
                            "Building_Air": {
                                "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Building],
                                SKOS.definition: Literal(
                                    "air contained within a building"
                                ),
                            },
                            "Mixed_Air": {
                                "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Mixed],
                                SKOS.definition: Literal(
                                    "(1) air that contains two or more streams of air. (2) combined outdoor air and recirculated air."
                                ),
                            },
                            "Return_Air": {
                                "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Return],
                                SKOS.definition: Literal(
                                    "air removed from a space to be recirculated or exhausted. Air extracted from a space and totally or partially returned to an air conditioner, furnace, or other heating, cooling, or ventilating system."
                                ),
                            },
                            "Exhaust_Air": {
                                "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Exhaust],
                                SKOS.definition: Literal(
                                    "air that must be removed from a space due to contaminants, regardless of pressurization"
                                ),
                            },
                            "Supply_Air": {
                                "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Supply],
                                SKOS.definition: Literal(
                                    "(1) air delivered by mechanical or natural ventilation to a space, composed of any combination of outdoor air, recirculated air, or transfer air. (2) air entering a space from an air-conditioning, heating, or ventilating apparatus for the purpose of comfort conditioning. Supply air is generally filtered, fan forced, and either heated, cooled, humidified, or dehumidified as necessary to maintain specified conditions. Only the quantity of outdoor air within the supply airflow may be used as replacement air."
                                ),
                            },
                            "Discharge_Air": {
                                "tags": [TAG.Fluid, TAG.Gas, TAG.Air, TAG.Discharge],
                            },
                        },
                    },
                    "CO2": {
                        "tags": [TAG.Fluid, TAG.Gas, TAG.CO2],
                        SKOS.definition: Literal("Carbon Dioxide in the vapor phase"),
                    },
                    "Steam": {
                        "tags": [TAG.Fluid, TAG.Gas, TAG.Steam],
                        SKOS.definition: Literal("water in the vapor phase."),
                    },
                    "Natural_Gas": {
                        "tags": [TAG.Fluid, TAG.Gas, TAG.Natural],
                        SKOS.definition: Literal(
                            "Fossil fuel energy source consisting largely of methane and other hydrocarbons"
                        ),
                    },
                },
            },
            "Liquid": {
                "tags": [TAG.Fluid, TAG.Liquid],
                "subclasses": {
                    "Gasoline": {
                        "tags": [TAG.Fluid, TAG.Liquid, TAG.Gasoline],
                        SKOS.definition: Literal(
                            "Petroleum derived liquid used as a fuel source"
                        ),
                    },
                    "Liquid_CO2": {
                        "tags": [TAG.Fluid, TAG.Liquid, TAG.CO2],
                        SKOS.definition: Literal("Carbon Dioxide in the liquid phase"),
                    },
                    "Oil": {
                        "tags": [TAG.Fluid, TAG.Liquid, TAG.Oil],
                        "subclasses": {
                            "Fuel_Oil": {
                                "tags": [TAG.Liquid, TAG.Oil, TAG.Fuel],
                                SKOS.definition: Literal(
                                    "Petroleum based oil burned for energy"
                                ),
                            }
                        },
                    },
                    "Water": {
                        "tags": [TAG.Fluid, TAG.Liquid, TAG.Water],
                        SKOS.definition: Literal(
                            "transparent, odorless, tasteless liquid; a compound of hydrogen and oxygen (H2O), containing 11.188% hydrogen and 88.812% oxygen by mass; freezing at 32°F (0°C); boiling near 212°F (100°C)."
                        ),
                        "subclasses": {
                            "Deionized_Water": {
                                "tags": [
                                    TAG.Fluid,
                                    TAG.Liquid,
                                    TAG.Deionized,
                                    TAG.Water,
                                ],
                                SKOS.definition: Literal(
                                    "Water which has been purified by removing its ions (constituting the majority of non-particulate contaminants)"
                                ),
                            },
                            "Chilled_Water": {
                                "tags": [TAG.Fluid, TAG.Liquid, TAG.Water, TAG.Chilled],
                                SKOS.definition: Literal(
                                    "water used as a cooling medium (particularly in air-conditioning systems or in processes) at below ambient temperature."
                                ),
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
                                SKOS.definition: Literal(
                                    "Water expelled from a system to remove mineral build up"
                                ),
                            },
                            "Condenser_Water": {
                                "tags": [
                                    TAG.Fluid,
                                    TAG.Liquid,
                                    TAG.Water,
                                    TAG.Condenser,
                                ],
                                SKOS.definition: Literal(
                                    "Water used used to remove heat through condensation"
                                ),
                            },
                            "Domestic_Water": {
                                "tags": [
                                    TAG.Fluid,
                                    TAG.Liquid,
                                    TAG.Water,
                                    TAG.Domestic,
                                ],
                                SKOS.definition: Literal(
                                    "Tap water for drinking, washing, cooking, and flushing of toliets"
                                ),
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
                                SKOS.definition: Literal(
                                    "Hot water used for HVAC heating or supply to hot taps"
                                ),
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
                                SKOS.definition: Literal(
                                    "Water used used to makeup water loss through leaks, evaporation, or blowdown"
                                ),
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
            "Ice": {
                "tags": [TAG.Solid, TAG.Ice],
                SKOS.definition: Literal("Water in its solid form"),
            },
            "Frost": {"tags": [TAG.Solid, TAG.Frost]},
            "Hail": {"tags": [TAG.Solid, TAG.Hail]},
        },
    },
}
