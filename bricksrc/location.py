from .namespaces import BRICK, TAG, OWL

"""
Location class structure
"""
location_subclasses = {
    "Building": {"tags": [TAG.Building, TAG.Location]},
    "Floor": {
        "tags": [TAG.Floor, TAG.Location],
        "subclasses": {
            "Basement": {"tags": [TAG.Basement, TAG.Location, TAG.Floor]},
            "Rooftop": {"tags": [TAG.Rooftop, TAG.Location, TAG.Floor]},
        },
        OWL.equivalentClass: BRICK["Storey"],
    },
    "Storey": {
        "tags": [TAG.Storey, TAG.Location],
        OWL.equivalentClass: BRICK["Floor"],
    },
    "Outside": {"tags": [TAG.Outside, TAG.Location]},
    "Site": {"tags": [TAG.Site, TAG.Location]},
    "Wing": {"tags": [TAG.Wing, TAG.Location]},
    "Space": {
        "tags": [TAG.Space, TAG.Location],
        "subclasses": {
            "Room": {
                "tags": [TAG.Room, TAG.Location],
                "subclasses": {
                    "Laboratory": {
                        "tags": [TAG.Laboratory, TAG.Room, TAG.Location],
                        "subclasses": {
                            "Freezer": {
                                "tags": [
                                    TAG.Freezer,
                                    TAG.Laboratory,
                                    TAG.Room,
                                    TAG.Location,
                                ],
                            },
                            "Cold_Box": {
                                "tags": [
                                    TAG.Cold,
                                    TAG.Box,
                                    TAG.Laboratory,
                                    TAG.Room,
                                    TAG.Location,
                                ],
                            },
                            "Hot_Box": {
                                "tags": [
                                    TAG.Hot,
                                    TAG.Box,
                                    TAG.Laboratory,
                                    TAG.Room,
                                    TAG.Location,
                                ],
                            },
                            "Environment_Box": {
                                "tags": [
                                    TAG.Environment,
                                    TAG.Box,
                                    TAG.Laboratory,
                                    TAG.Room,
                                    TAG.Location,
                                ],
                            },
                        },
                    },
                    "Server_Room": {"tags": [TAG.Server, TAG.Room, TAG.Location]},
                },
            },
        },
    },
    "Zone": {
        "tags": [TAG.Zone, TAG.Location],
        "subclasses": {
            "HVAC_Zone": {"tags": [TAG.HVAC, TAG.Zone, TAG.Location]},
            "Lighting_Zone": {"tags": [TAG.Lighting, TAG.Zone, TAG.Location]},
            "Fire_Zone": {"tags": [TAG.Fire, TAG.Zone, TAG.Location]},
        },
    },
}
