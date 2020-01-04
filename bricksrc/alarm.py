from .namespaces import TAG, BRICK

alarm_definitions = {
    "Alarm": {
        "tags": [TAG.Alarm],
        "subclasses": {
            "CO2_Alarm": {
                "tags": [TAG.CO2, TAG.Alarm],
                "subclasses": {
                    "High_CO2_Alarm": {
                        "tags": [TAG.High, TAG.CO2, TAG.Alarm],
                    },
                },
            },
            "Change_Filter_Alarm": {
                "tags": [TAG.Change, TAG.Filter, TAG.Alarm],
            },
            "Communication_Loss_Alarm": {
                "tags": [TAG.Communication, TAG.Loss, TAG.Alarm],
            },
            "Failure_Alarm": {
                "tags": [TAG.Failure, TAG.Alarm],
            },
            "Leak_Alarm": {
                "tags": [TAG.Leak, TAG.Alarm],
                "subclasses": {
                    "Condensate_Leak_Alarm": {
                        "tags": [TAG.Condensate, TAG.Leak, TAG.Alarm],
                    },
                },
            },
            "Overload_Alarm": {
                "tags": [TAG.Overload, TAG.Alarm],
            },
            "Temperature_Alarm": {
                "tags": [TAG.Temperature, TAG.Alarm],
                "subclasses": {
                    "Water_Temperature_Alarm": {
                        "tags": [TAG.Water, TAG.Temperature, TAG.Alarm],
                        "parents": [BRICK.Water_Alarm],
                        "subclasses": {
                            "Discharge_Water_Temperature_Alarm": {
                                "tags": [TAG.Discharge, TAG.Water,
                                         TAG.Temperature, TAG.Alarm],
                            },
                            "Supply_Water_Temperature_Alarm": {
                                "tags": [TAG.Supply, TAG.Water,
                                         TAG.Temperature, TAG.Alarm],
                            },
                        },
                    },
                }
            },
            "Water_Alarm": {
                "tags": [TAG.Water, TAG.Alarm],
                "subclasses": {
                    "Deionized_Water_Alarm": {
                        "tags": [TAG.Deionized, TAG.Water, TAG.Alarm],
                    },
                },
            },
        },
    },
}
