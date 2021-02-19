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
                    "Office": {
                        "tags": [
                            TAG.Office,
                            TAG.Location,
                        ],
                        "subclasses": {
                            "Private_Office": {
                                "tags": [TAG.Private, TAG.Office, TAG.Location],
                            },
                            "Open_Office": {
                                "tags": [
                                    TAG.Open,
                                    TAG.Office,
                                    TAG.Location,
                                ],
                            },
                        },
                    },
                    "Meeting_Room": {
                        "tags": [
                            TAG.Meeting,
                            TAG.Room,
                            TAG.Location,
                        ],
                        "subclasses": {
                            "Conference_Room": {
                                "tags": [
                                    TAG.Conference,
                                    TAG.Room,
                                    TAG.Location,
                                ],
                            },
                            "Classroom": {
                                "tags": [TAG.Class, TAG.Room, TAG.Location],
                                "subclasses": {
                                    "Training_Room": {
                                        "tags": [
                                            TAG.Training,
                                            TAG.Room,
                                            TAG.Location,
                                        ],
                                    },
                                },
                            },
                            "Work_Room": {
                                "tags": [
                                    TAG.Work,
                                    TAG.Room,
                                    TAG.Location,
                                ],
                            },
                            "Auditorium": {
                                "tags": [
                                    TAG.Auditorium,
                                    TAG.Location,
                                ],
                            },
                        },
                    },
                    "Break_Room": {
                        "tags": [
                            TAG.Break,
                            TAG.Room,
                            TAG.Location,
                        ],
                    },
                    "Cafeteria": {
                        "tags": [
                            TAG.Cafeteria,
                            TAG.Location,
                        ],
                    },
                    "Kitchen": {
                        "tags": [
                            TAG.Kitchen,
                            TAG.Location,
                        ],
                    },
                    "Support_Room": {
                        "tags": [
                            TAG.Support,
                            TAG.Room,
                            TAG.Location,
                        ],
                        "subclasses": {
                            "Storage_Room": {
                                "tags": [
                                    TAG.Storage,
                                    TAG.Room,
                                    TAG.Location,
                                ],
                            },
                            "Passageway": {
                                "tags": [
                                    TAG.Passageway,
                                    TAG.Location,
                                ],
                                "subclasses": {
                                    "Hallway": {
                                        "tags": [
                                            TAG.Hallway,
                                            TAG.Location,
                                        ],
                                    },
                                    "Corridor": {
                                        "tags": [
                                            TAG.Corridor,
                                            TAG.Location,
                                        ],
                                        OWL.equivalentClass: BRICK["Hallway"],
                                    },
                                },
                            },
                            "Lobby": {
                                "tags": [
                                    TAG.Lobby,
                                    TAG.Location,
                                ],
                                "subclasses": {
                                    "Reception_Area": {
                                        "tags": [
                                            TAG.Reception,
                                            TAG.Area,
                                            TAG.Location,
                                        ],
                                    },
                                },
                            },
                            "Foyer": {
                                "tags": [
                                    TAG.Foyer,
                                    TAG.Location,
                                ],
                                "subclasses": {
                                    "Waiting_Room": {
                                        "tags": [
                                            TAG.Waiting,
                                            TAG.Room,
                                            TAG.Location,
                                        ],
                                    },
                                },
                            },
                            "Restroom": {
                                "tags": [
                                    TAG.Restroom,
                                    TAG.Room,
                                    TAG.Location,
                                ],
                            },
                            "Showers": {
                                "tags": [
                                    TAG.Showers,
                                    TAG.Location,
                                ],
                            },
                        },
                    },
                    "Information_Communications_Room": {
                        "tags": [
                            TAG.Information,
                            TAG.Communications,
                            TAG.Room,
                            TAG.Location,
                        ],
                        "subclasses": {
                            "IT_Closet": {
                                "tags": [
                                    TAG.IT,
                                    TAG.Closet,
                                    TAG.Location,
                                ],
                            },
                            "Server_Room": {
                                "tags": [
                                    TAG.Server,
                                    TAG.Room,
                                    TAG.Location,
                                ],
                            },
                            "Telephone_Room": {
                                "tags": [
                                    TAG.Telephone,
                                    TAG.Room,
                                    TAG.Location,
                                ],
                            },
                            "Mail_Room": {
                                "tags": [
                                    TAG.Mail,
                                    TAG.Room,
                                    TAG.Location,
                                ],
                            },
                        },
                    },
                    "Library": {
                        "tags": [
                            TAG.Library,
                            TAG.Location,
                        ],
                    },
                    "Mechanical_Room": {
                        "tags": [
                            TAG.Mechanical,
                            TAG.Room,
                            TAG.Location,
                        ],
                    },
                    "Electrical_Room": {
                        "tags": [
                            TAG.Electrical,
                            TAG.Room,
                            TAG.Location,
                        ],
                    },
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
