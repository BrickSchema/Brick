from .namespaces import BRICK, TAG, OWL

"""
Location class structure
"""
location_subclasses = {
    "Building": {
        "tags": [TAG.Building, TAG.Location],
        "subclasses": {
            "Parking_Structure": {
                "tags": [TAG.Location, TAG.Parking, TAG.Structure, TAG.Building]
            },
        },
        "constraints": {
            BRICK.hasPart: [
                BRICK.Floor,
                BRICK.Room,
                BRICK.Space,
                BRICK.Zone,
                BRICK.Wing,
            ],
        },
    },
    "Floor": {
        "tags": [TAG.Floor, TAG.Location],
        "subclasses": {
            "Basement": {"tags": [TAG.Basement, TAG.Location, TAG.Floor]},
            "Rooftop": {"tags": [TAG.Rooftop, TAG.Location, TAG.Floor]},
            "Parking_Level": {
                "tags": [TAG.Parking, TAG.Level, TAG.Location, TAG.Floor]
            },
        },
        OWL.equivalentClass: BRICK["Storey"],
        "constraints": {
            BRICK.hasPart: [
                BRICK.Room,
                BRICK.Space,
                BRICK.Zone,
            ],
        },
    },
    "Storey": {
        "tags": [TAG.Storey, TAG.Location],
        OWL.equivalentClass: BRICK["Floor"],
    },
    "Outdoor_Area": {
        "tags": [TAG.Location, TAG.Outdoor, TAG.Area],
        "subclasses": {
            "Bench_Space": {"tags": [TAG.Location, TAG.Outdoor, TAG.Area, TAG.Bench]},
            "Field_Of_Play": {
                "tags": [TAG.Location, TAG.Outdoor, TAG.Area, TAG.Field, TAG.Play]
            },
            "Information_Area": {
                "tags": [TAG.Location, TAG.Outdoor, TAG.Area, TAG.Information]
            },
        },
    },
    "Outside": {"tags": [TAG.Outside, TAG.Location]},
    "Region": {"tags": [TAG.Location, TAG.Region]},
    "Site": {
        "tags": [TAG.Site, TAG.Location],
        "constraints": {
            BRICK.hasPart: [
                BRICK.Building,
                BRICK.Region,
                BRICK.Site,
                BRICK.Space,
                BRICK.Room,
            ],
        },
    },
    "Wing": {"tags": [TAG.Wing, TAG.Location]},
    "Space": {
        "tags": [TAG.Space, TAG.Location],
        "subclasses": {
            "Common_Space": {
                "tags": [TAG.Common, TAG.Space, TAG.Location],
                "subclasses": {
                    "Auditorium": {
                        "tags": [TAG.Auditorium, TAG.Common, TAG.Space, TAG.Location]
                    },
                    "Atrium": {
                        "tags": [TAG.Atrium, TAG.Common, TAG.Space, TAG.Location]
                    },
                    "Cafeteria": {
                        "tags": [TAG.Cafeteria, TAG.Common, TAG.Space, TAG.Location]
                    },
                    "Hallway": {
                        "tags": [TAG.Hallway, TAG.Common, TAG.Space, TAG.Location]
                    },
                    "Lobby": {
                        "tags": [TAG.Lobby, TAG.Common, TAG.Space, TAG.Location],
                        "subclasses": {
                            "Employee_Entrance_Lobby": {
                                "tags": [
                                    TAG.Employee,
                                    TAG.Entrance,
                                    TAG.Lobby,
                                    TAG.Common,
                                    TAG.Space,
                                    TAG.Location,
                                ]
                            },
                            "Visitor_Lobby": {
                                "tags": [
                                    TAG.Visitor,
                                    TAG.Lobby,
                                    TAG.Common,
                                    TAG.Space,
                                    TAG.Location,
                                ]
                            },
                        },
                    },
                    "Lounge": {
                        "tags": [TAG.Lounge, TAG.Common, TAG.Space, TAG.Location],
                        "subclasses": {
                            "Majlis": {
                                "tags": [
                                    TAG.Majlis,
                                    TAG.Lounge,
                                    TAG.Common,
                                    TAG.Space,
                                    TAG.Location,
                                ]
                            },
                        },
                    },
                },
            },
            "Entrance": {"tags": [TAG.Entrance, TAG.Space, TAG.Location]},
            "Gatehouse": {"tags": [TAG.Gatehouse, TAG.Space, TAG.Location]},
            "Media_Hot_Desk": {"tags": [TAG.Media, TAG.Desk, TAG.Space, TAG.Location]},
            "Parking_Space": {"tags": [TAG.Parking, TAG.Space, TAG.Location]},
            "Room": {
                "tags": [TAG.Room, TAG.Location],
                "subclasses": {
                    "Ablutions_Room": {
                        "tags": [TAG.Ablutions, TAG.Room, TAG.Space, TAG.Location]
                    },
                    "Breakroom": {
                        "tags": [TAG.Breakroom, TAG.Room, TAG.Space, TAG.Location],
                        OWL.equivalentClass: BRICK["Break_Room"],
                    },
                    "Break_Room": {
                        "tags": [TAG.Break, TAG.Room, TAG.Space, TAG.Location],
                        OWL.equivalentClass: BRICK["Breakroom"],
                    },
                    "Conference_Room": {
                        "tags": [TAG.Conference, TAG.Room, TAG.Space, TAG.Location]
                    },
                    "Control_Room": {
                        "tags": [TAG.Control, TAG.Room, TAG.Space, TAG.Location]
                    },
                    "Copy_Room": {
                        "tags": [TAG.Copy, TAG.Room, TAG.Space, TAG.Location]
                    },
                    "Exercise_Room": {
                        "tags": [TAG.Exercise, TAG.Room, TAG.Space, TAG.Location]
                    },
                    "Food_Service_Room": {
                        "tags": [
                            TAG.Food,
                            TAG.Service,
                            TAG.Room,
                            TAG.Space,
                            TAG.Location,
                        ],
                        "subclasses": {
                            "Concession": {
                                "tags": [
                                    TAG.Concessions,
                                    TAG.Food,
                                    TAG.Service,
                                    TAG.Room,
                                    TAG.Space,
                                    TAG.Location,
                                ]
                            },
                        },
                    },
                    "Hospitality_Box": {
                        "tags": [
                            TAG.Hospitality,
                            TAG.Box,
                            TAG.Room,
                            TAG.Space,
                            TAG.Location,
                        ]
                    },
                    "Janitor_Room": {
                        "tags": [TAG.Janitor, TAG.Room, TAG.Space, TAG.Location]
                    },
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
                    "Library": {
                        "tags": [TAG.Library, TAG.Room, TAG.Space, TAG.Location]
                    },
                    "Loading_Dock": {
                        "tags": [
                            TAG.Loading,
                            TAG.Dock,
                            TAG.Room,
                            TAG.Space,
                            TAG.Location,
                        ]
                    },
                    "Mail_Room": {
                        "tags": [TAG.Mail, TAG.Room, TAG.Space, TAG.Location]
                    },
                    "Massage_Room": {
                        "tags": [TAG.Massage, TAG.Room, TAG.Space, TAG.Location]
                    },
                    "Media_Room": {
                        "tags": [TAG.Media, TAG.Room, TAG.Space, TAG.Location],
                        "subclasses": {
                            "Broadcast_Room": {
                                "tags": [
                                    TAG.Broadcast,
                                    TAG.Media,
                                    TAG.Room,
                                    TAG.Space,
                                    TAG.Location,
                                ]
                            },
                            "Media_Production_Room": {
                                "tags": [
                                    TAG.Production,
                                    TAG.Media,
                                    TAG.Room,
                                    TAG.Space,
                                    TAG.Location,
                                ]
                            },
                            "Studio": {
                                "tags": [
                                    TAG.Studio,
                                    TAG.Media,
                                    TAG.Room,
                                    TAG.Space,
                                    TAG.Location,
                                ]
                            },
                        },
                    },
                    "Medical_Room": {
                        "tags": [TAG.Medical, TAG.Room, TAG.Space, TAG.Location],
                        "subclasses": {
                            "First_Aid_Room": {
                                "tags": [
                                    TAG.First,
                                    TAG.Aid,
                                    TAG.Meidcal,
                                    TAG.Room,
                                    TAG.Space,
                                    TAG.Location,
                                ]
                            },
                        },
                    },
                    "Office": {
                        "tags": [TAG.Office, TAG.Room, TAG.Space, TAG.Location],
                        "subclasses": {
                            "Cubicle": {
                                "tags": [
                                    TAG.Cubicle,
                                    TAG.Office,
                                    TAG.Room,
                                    TAG.Space,
                                    TAG.Location,
                                ]
                            },
                            "Enclosed_Office": {
                                "tags": [
                                    TAG.Enclosed,
                                    TAG.Office,
                                    TAG.Room,
                                    TAG.Space,
                                    TAG.Location,
                                ],
                                "subclasses": {
                                    "Private_Office": {
                                        "tags": [
                                            TAG.Private,
                                            TAG.Enclosed,
                                            TAG.Office,
                                            TAG.Room,
                                            TAG.Space,
                                            TAG.Location,
                                        ]
                                    },
                                    "Shared_Office": {
                                        "tags": [
                                            TAG.Shared,
                                            TAG.Enclosed,
                                            TAG.Office,
                                            TAG.Room,
                                            TAG.Space,
                                            TAG.Location,
                                        ]
                                    },
                                    "Team_Room": {
                                        "tags": [
                                            TAG.Team,
                                            TAG.Enclosed,
                                            TAG.Office,
                                            TAG.Room,
                                            TAG.Space,
                                            TAG.Location,
                                        ]
                                    },
                                },
                            },
                            "Open_Office": {
                                "tags": [
                                    TAG.Open,
                                    TAG.Office,
                                    TAG.Room,
                                    TAG.Space,
                                    TAG.Location,
                                ]
                            },
                        },
                    },
                    "Office_Kitchen": {
                        "tags": [
                            TAG.Office,
                            TAG.Kitchen,
                            TAG.Room,
                            TAG.Space,
                            TAG.Location,
                        ]
                    },
                    "Prayer_Room": {
                        "tags": [TAG.Prayer, TAG.Room, TAG.Space, TAG.Location]
                    },
                    "Reception": {
                        "tags": [TAG.Reception, TAG.Room, TAG.Space, TAG.Location]
                    },
                    "Restroom": {
                        "tags": [TAG.Restroom, TAG.Room, TAG.Space, TAG.Location],
                        OWL.equivalentClass: BRICK["Rest_Room"],
                    },
                    "Rest_Room": {
                        "tags": [TAG.Rest, TAG.Room, TAG.Space, TAG.Location],
                        OWL.equivalentClass: BRICK["Restroom"],
                    },
                    "Retail_Room": {
                        "tags": [TAG.Retail, TAG.Room, TAG.Space, TAG.Location]
                    },
                    "Security_Service_Room": {
                        "tags": [
                            TAG.Security,
                            TAG.Service,
                            TAG.Room,
                            TAG.Space,
                            TAG.Location,
                        ],
                        "subclasses": {
                            "Detention_Room": {
                                "tags": [
                                    TAG.Detention,
                                    TAG.Room,
                                    TAG.Space,
                                    TAG.Location,
                                ]
                            },
                        },
                    },
                    "Server_Room": {"tags": [TAG.Server, TAG.Room, TAG.Location]},
                    "Service_Room": {
                        "tags": [TAG.Service, TAG.Room, TAG.Space, TAG.Location],
                        "subclasses": {
                            "Electrical_Room": {
                                "tags": [
                                    TAG.Electrical,
                                    TAG.Service,
                                    TAG.Room,
                                    TAG.Space,
                                    TAG.Location,
                                ],
                                "subclasses": {
                                    "Battery_Room": {
                                        "tags": [
                                            TAG.Battery,
                                            TAG.Electrical,
                                            TAG.Service,
                                            TAG.Room,
                                            TAG.Space,
                                            TAG.Location,
                                        ]
                                    },
                                    "Generator_Room": {
                                        "tags": [
                                            TAG.Generator,
                                            TAG.Electrical,
                                            TAG.Service,
                                            TAG.Room,
                                            TAG.Space,
                                            TAG.Location,
                                        ]
                                    },
                                    "Transformer_Room": {
                                        "tags": [
                                            TAG.Transformer,
                                            TAG.Electrical,
                                            TAG.Service,
                                            TAG.Room,
                                            TAG.Space,
                                            TAG.Location,
                                        ]
                                    },
                                },
                            },
                            "Mechanical_Room": {
                                "tags": [
                                    TAG.Mechanical,
                                    TAG.Service,
                                    TAG.Room,
                                    TAG.Space,
                                    TAG.Location,
                                ],
                                "subclasses": {
                                    "Pump_Room": {
                                        "tags": [
                                            TAG.Pump,
                                            TAG.Mechanical,
                                            TAG.Service,
                                            TAG.Room,
                                            TAG.Space,
                                            TAG.Location,
                                        ]
                                    },
                                },
                            },
                            "Plumbing_Room": {
                                "tags": [
                                    TAG.Plumbing,
                                    TAG.Service,
                                    TAG.Room,
                                    TAG.Space,
                                    TAG.Location,
                                ]
                            },
                        },
                    },
                    "Shower": {"tags": [TAG.Shower, TAG.Room, TAG.Space, TAG.Location]},
                    "Sports_Service_Room": {
                        "tags": [
                            TAG.Sports,
                            TAG.Service,
                            TAG.Room,
                            TAG.Space,
                            TAG.Location,
                        ]
                    },
                    "Storage_Room": {
                        "tags": [TAG.Storage, TAG.Room, TAG.Space, TAG.Location],
                        "subclasses": {
                            "Hazardous_Materials_Storage": {
                                "tags": [
                                    TAG.Hazardous,
                                    TAG.Materials,
                                    TAG.Storage,
                                    TAG.Room,
                                    TAG.Space,
                                    TAG.Location,
                                ]
                            },
                            "Waste_Storage": {
                                "tags": [
                                    TAG.Waste,
                                    TAG.Storage,
                                    TAG.Room,
                                    TAG.Space,
                                    TAG.Location,
                                ]
                            },
                        },
                    },
                    "Telecom_Room": {
                        "tags": [TAG.Telecom, TAG.Room, TAG.Space, TAG.Location],
                        "subclasses": {
                            "Equipment_Room": {
                                "tags": [
                                    TAG.Equipment,
                                    TAG.Telecom,
                                    TAG.Room,
                                    TAG.Space,
                                    TAG.Location,
                                ]
                            },
                            "Switch_Room": {
                                "tags": [
                                    TAG.Switch,
                                    TAG.Telecom,
                                    TAG.Room,
                                    TAG.Space,
                                    TAG.Location,
                                ]
                            },
                            "Distribution_Frame": {
                                "tags": [
                                    TAG.Distribution,
                                    TAG.Frame,
                                    TAG.Telecom,
                                    TAG.Room,
                                    TAG.Space,
                                    TAG.Location,
                                ],
                                "subclasses": {
                                    "IDF": {
                                        "tags": [
                                            TAG.IDF,
                                            TAG.Distribution,
                                            TAG.Frame,
                                            TAG.Telecom,
                                            TAG.Room,
                                            TAG.Space,
                                            TAG.Location,
                                        ]
                                    },
                                    "MDF": {
                                        "tags": [
                                            TAG.MDF,
                                            TAG.Distribution,
                                            TAG.Frame,
                                            TAG.Telecom,
                                            TAG.Room,
                                            TAG.Space,
                                            TAG.Location,
                                        ]
                                    },
                                },
                            },
                            "TETRA_Room": {
                                "tags": [
                                    TAG.TETRA,
                                    TAG.Telecom,
                                    TAG.Room,
                                    TAG.Space,
                                    TAG.Location,
                                ]
                            },
                        },
                    },
                    "Wardrobe": {
                        "tags": [TAG.Wardrobe, TAG.Room, TAG.Space, TAG.Location]
                    },
                    "Workshop": {
                        "tags": [TAG.Workshop, TAG.Room, TAG.Space, TAG.Location]
                    },
                },
            },
            "Ticketing_Booth": {
                "tags": [TAG.Ticketing, TAG.Booth, TAG.Space, TAG.Location]
            },
            "Tunnel": {"tags": [TAG.Tunnel, TAG.Space, TAG.Location]},
            "Vertical_Space": {
                "tags": [TAG.Vertical, TAG.Space, TAG.Location],
                "subclasses": {
                    "Elevator_Space": {
                        "tags": [TAG.Elevator, TAG.Vertical, TAG.Space, TAG.Location],
                        OWL.equivalentClass: BRICK["Elevator_Shaft"],
                    },
                    "Elevator_Shaft": {
                        "tags": [
                            TAG.Elevator,
                            TAG.Vertical,
                            TAG.Shaft,
                            TAG.Space,
                            TAG.Location,
                        ],
                        OWL.equivalentClass: BRICK["Elevator_Space"],
                    },
                    "Riser": {
                        "tags": [TAG.Riser, TAG.Vertical, TAG.Space, TAG.Location]
                    },
                    "Staircase": {
                        "tags": [TAG.Staircase, TAG.Vertical, TAG.Space, TAG.Location]
                    },
                },
            },
            "Water_Tank": {"tags": [TAG.Water, TAG.Tank, TAG.Space, TAG.Location]},
        },
    },
    "Zone": {
        "tags": [TAG.Zone, TAG.Location],
        "subclasses": {
            "Energy_Zone": {"tags": [TAG.Energy, TAG.Zone, TAG.Location]},
            "HVAC_Zone": {"tags": [TAG.HVAC, TAG.Zone, TAG.Location]},
            "Lighting_Zone": {"tags": [TAG.Lighting, TAG.Zone, TAG.Location]},
            "Fire_Zone": {"tags": [TAG.Fire, TAG.Zone, TAG.Location]},
        },
        "constraints": {
            BRICK.hasPart: [
                BRICK.Room,
                BRICK.Space,
            ],
        },
    },
}
