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
                    "CO2": {},
                    "CO": {},
                    "Steam": {},
                    "Natural_Gas": {},
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
                                    },
                                }
                            },
                            "Potable_Water": {},
                            "Leaving_Water": {},
                            "Entering_Water": {},
                            "Hot_Water": {
                                SKOS.narrower: {
                                    "Entering_Hot_Water": {
                                        "parents": [BRICK.Entering_Water],
                                    },
                                    "Leaving_Hot_Water": {
                                        "parents": [BRICK.Leaving_Water],
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
}
