"""
Concepts used by the point attribute annotations that are being added to
Brick point classes ahead of Brick 2.0 (see the point-attributes drafts in
BrickSchema/Brick2-specification-drafting).

Each dictionary is a SKOS concept hierarchy; the concepts are instances of
the class named in generate_brick.py (Phenomenon, Process, Mode,
EnumerationKind).
"""

from .namespaces import BRICK, SKOS

# values of brick:ofProcess
processes = {
    "Heating": {
        SKOS.narrower: {
            "Preheat": {},
            "Reheat": {},
        },
    },
    "Cooling": {},
    "Humidification": {},
    "Dehumidification": {},
    "Load_Shed": {},
    "Run": {},
    "Acceleration": {},
    "Deceleration": {},
    "Smoke_Detection": {},
    "Liquid_Detection": {},
}

# values of brick:hasPhenomenon. In Brick 2.0, Phenomenon is expected to
# become the supertype of Substance.
phenomena = {
    "Solar": {},
    "Wind": {},
    "Fire": {},
    "People": {},
}
# existing Brick 1.x substances that are also phenomena; they stay Substances
# for backwards compatibility and are additionally typed as Phenomenon
substance_phenomena = [BRICK.Hail, BRICK.Frost]

# values of brick:inMode
modes = {
    "Occupied": {},
    "Unoccupied": {},
}

# values of brick:hasEnumeration
# TODO(Brick 2.0): enumerate the members of each EnumerationKind (only On_Off
# has members so far); several of these are open questions for the community
# (see questions-for-community.md in the drafting repo).
enumeration_kinds = {
    "EnumerationKind-Automatic_Mode": {},
    "EnumerationKind-Availability": {},
    "EnumerationKind-CommunicationState": {},
    "EnumerationKind-Conditioning_Mode": {},
    "EnumerationKind-Forward_Reverse": {},
    "EnumerationKind-Maintenance_Mode": {},
    "EnumerationKind-Maintenance_Required": {},
    "EnumerationKind-Manual_Auto": {},
    "EnumerationKind-Mode": {},
    "EnumerationKind-Motion": {},
    "EnumerationKind-Occupancy": {},
    "EnumerationKind-On_Off": {
        SKOS.narrower: {
            "On_Off-On": {},
            "On_Off-Off": {},
        },
    },
    "EnumerationKind-Open_Close": {},
    "EnumerationKind-Operating_Mode": {},
    "EnumerationKind-Shutdown": {},
    "EnumerationKind-Speed_Mode": {},
    "EnumerationKind-Stage": {},
    "EnumerationKind-Start_Stop": {},
}
