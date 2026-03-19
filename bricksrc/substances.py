from .namespaces import BRICK, OWL, SKOS, TAG

# Defining substances
substances = {
    "Light": {
        "tags": [TAG.Light],
    },
    "Fluid": {
        SKOS.narrower: {
            "Refrigerant": {},
            "Gas": {
                SKOS.narrower: {
                    "Air": {
                        SKOS.narrower: {
                            "Bypass_Air": {},
                            "Outside_Air": {},
                            "Zone_Air": {},
                            "Room_Air": {},
                            "Building_Air": {},
                            "Mixed_Air": {},
                            "Return_Air": {},
                            "Exhaust_Air": {},
                            "Supply_Air": {
                                OWL.sameAs: BRICK.Discharge_Air,
                            },
                            "Discharge_Air": {
                                OWL.sameAs: BRICK.Supply_Air,
                            },
                        },
                    },
                    "Formaldehyde": {},
                    "Methane": {},
                    "CO": {}, # Carbon Monoxide
                    "CO2": {}, # Carbon Dioxide
                    "Natural_Gas": {},
                    "Ammonia": {},
                    "NO2": {}, # Nitrogen Dioxide
                    "Ozone": {},
                    "Radon": {},
                    "Steam": {},
                    "TVOC": {}, # Total Volatile Organic Compounds
                },
            },
            "Liquid": {
                SKOS.narrower: {
                    "Gasoline": {},
                    "Liquid_CO2": {},
                    "Glycol": {},
                    "Oil": {
                        SKOS.narrower: {"Fuel_Oil": {}},
                    },
                    "Water": {
                        SKOS.narrower: {
                            "Deionized_Water": {},
                            "Bypass_Water": {},
                            "Chilled_Water": {
                                SKOS.narrower: {
                                    "Entering_Chilled_Water": {
                                        "parents": [BRICK.Entering_Water],
                                    },
                                    "Leaving_Chilled_Water": {
                                        "parents": [BRICK.Leaving_Water],
                                    },
                                    "Return_Chilled_Water": {
                                        "parents": [BRICK.Return_Water],
                                    },
                                    "Supply_Chilled_Water": {
                                        "parents": [BRICK.Supply_Water],
                                    },
                                },
                            },
                            "Collection_Basin_Water": {},
                            "Blowdown_Water": {},
                            "Condenser_Water": {
                                SKOS.narrower: {
                                    "Entering_Condenser_Water": {},
                                    "Leaving_Condenser_Water": {},
                                },
                            },
                            "Domestic_Water": {
                                SKOS.narrower: {
                                    "Domestic_Hot_Water": {
                                        "parents": [BRICK.Hot_Water],
                                        SKOS.narrower: {
                                            "Entering_Domestic_Hot_Water": {
                                                "parents": [BRICK.Entering_Water],
                                            },
                                            "Leaving_Domestic_Hot_Water": {
                                                "parents": [BRICK.Leaving_Water],
                                            },
                                        },
                                    },
                                }
                            },
                            "Potable_Water": {},
                            "Leaving_Water": {},
                            "Return_Water": {},
                            "Supply_Water": {},
                            "Entering_Water": {},
                            "Hot_Water": {
                                SKOS.narrower: {
                                    "Entering_Hot_Water": {
                                        "parents": [BRICK.Entering_Water],
                                    },
                                    "Return_Hot_Water": {
                                        "parents": [BRICK.Return_Water],
                                    },
                                    "Leaving_Hot_Water": {
                                        "parents": [BRICK.Leaving_Water],
                                    },
                                    "High_Temperature_Hot_Water": {
                                        SKOS.narrower: {
                                            "Entering_High_Temperature_Hot_Water": {
                                                "parents": [BRICK.Entering_Water],
                                            },
                                            "Leaving_High_Temperature_Hot_Water": {
                                                "parents": [BRICK.Leaving_Water],
                                            },
                                        },
                                    },
                                    "Medium_Temperature_Hot_Water": {
                                        SKOS.narrower: {
                                            "Entering_Medium_Temperature_Hot_Water": {
                                                "parents": [BRICK.Entering_Water],
                                            },
                                            "Leaving_Medium_Temperature_Hot_Water": {
                                                "parents": [BRICK.Leaving_Water],
                                            },
                                        },
                                    },
                                },
                            },
                            "Makeup_Water": {},
                        },
                    },
                },
            },
        },
    },
    "Solid": {
        SKOS.narrower: {
            "Ice": {},
            "Frost": {},
            "Hail": {},
            "Soil": {},
        },
    },
    "Particulate_Matter": {
        SKOS.narrower: {
            "PM1": {},
            "PM2.5": {},
            "PM10": {},
        },
    },
}
