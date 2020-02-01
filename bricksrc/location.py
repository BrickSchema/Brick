from .namespaces import TAG

"""
Location class structure
"""
location_subclasses = {
    "Building": {
        "tags": [TAG.Site],
    },
    "Floor": {
        "tags": [TAG.Floor, TAG.Location],
    },
    "Roof": {
        "tags": [TAG.Roof, TAG.Location],
    },
    "Basement": {
        "tags": [TAG.Basement, TAG.Location],
    },
    "Outside": {
        "tags": [TAG.Outside, TAG.Location],
    },
    "City": {
        "tags": [TAG.City, TAG.Location],
    },
    "Wing": {
        "tags": [TAG.Wing, TAG.Location],
    },
    "Space": {
        "tags": [TAG.Space, TAG.Location],
    },
    "Zone": {
        "tags": [TAG.Zone, TAG.Location],
        "subclasses": {
            "HVAC_Zone": {
                "tags": [TAG.HVAC, TAG.Zone, TAG.Location],
            },
            "Lighting_Zone": {
                "tags": [TAG.Lighting, TAG.Zone, TAG.Location],
            },
            "Fire_Zone": {
                "tags": [TAG.Fire, TAG.Zone, TAG.Location],
            },
        },
    },
    "Room": {
        "tags": [TAG.Room, TAG.Location],
        "subclasses": {
            "Laboratory": {
                "tags": [TAG.Laboratory, TAG.Room, TAG.Location],
                "subclasses": {
                    "Freezer": {
                        "tags": [TAG.Freezer, TAG.Laboratory, TAG.Room, TAG.Location],
                    },
                    "Cold_Box": {
                        "tags": [TAG.Cold, TAG.Box, TAG.Laboratory, TAG.Room, TAG.Location],
                    },
                    "Hot_Box": {
                        "tags": [TAG.Hot, TAG.Box, TAG.Laboratory, TAG.Room, TAG.Location],
                    },
                    "Environment_Box": {
                        "tags": [TAG.Environment, TAG.Box, TAG.Laboratory, TAG.Room, TAG.Location],
                    },
                },
            },
            "Server_Room": {
                "tags": [TAG.Server, TAG.Room, TAG.Location],
            },
        },
    },
}
