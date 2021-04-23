import brickschema
from brickschema.namespaces import A, OWL, BRICK, UNIT
from rdflib import Namespace, Literal

# our entities will live in this namespace
BLDG = Namespace("urn:example#")

# create a graph for our model
g = brickschema.Graph()
g.bind("bldg", BLDG)

g.add((BLDG["pv_generation_system"], A, BRICK.PV_Generation_System))

arrays = {
    "array1": {
        "panels": ["panel11", "panel12", "panel13"],
        "orientation": 0,  # relative to south
        "tilt": 20,
        "panel_area": 5,  # sqm
    },
    "array2": {
        "panels": ["panel21", "panel22", "panel23"],
        "orientation": 2,  # relative to south
        "tilt": 23,
        "panel_area": 5,  # sqm
    },
}

# programmatically build up the arrays
for arrayname, defn in arrays.items():
    g.add((BLDG[arrayname], A, BRICK.Photovoltaic_Array))
    g.add((BLDG["pv_generation_system"], BRICK.hasPart, BLDG[arrayname]))

    orientation_props = [
        (BRICK.hasUnit, UNIT.DEG),
        (BRICK.value, Literal(defn["orientation"])),
        (BRICK.orientationRelativeTo, Literal("South")),
    ]
    g.add((BLDG[arrayname], BRICK.orientation, orientation_props))

    tilt_props = [(BRICK.hasUnit, UNIT.DEG), (BRICK.value, Literal(defn["tilt"]))]
    g.add((BLDG[arrayname], BRICK.tilt, tilt_props))

    for panel in defn["panels"]:
        g.add((BLDG[panel], A, BRICK.PV_Panel))
        g.add((BLDG[panel], BRICK.isPartOf, BLDG[arrayname]))
        area_props = [
            (BRICK.value, Literal(defn["panel_area"])),
            (BRICK.hasUnit, UNIT.M2),
        ]
        g.add((BLDG[panel], BRICK.panelArea, area_props))

# save the file
g.serialize("solar_array.ttl", format="ttl")
