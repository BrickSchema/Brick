from .namespaces import TAG, OWL, BRICK

"""
Set up subclasses of the loop superclass
"""
loop_subclasses = {
    "Water_Loop": {
        "tags": [TAG.Loop, TAG.Water],
        "subclasses": {
            "Chilled_Water_Loop": {"tags": [TAG.Chilled, TAG.Water, TAG.Loop]},
            "Hot_Water_Loop": {"tags": [TAG.Hot, TAG.Water, TAG.Loop]},
            "Condenser_Water_Loop": {"tags": [TAG.Condenser, TAG.Water, TAG.Loop]},
        },
    },
    "Air_Loop": {"tags": [TAG.Loop, TAG.Air]},
}
