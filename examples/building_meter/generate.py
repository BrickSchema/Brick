import brickschema
from brickschema.namespaces import A, OWL, BRICK, UNIT
from rdflib import Namespace, Literal

# our entities will live in this namespace
BLDG = Namespace("urn:example#")

# create a graph for our model
g = brickschema.Graph()
g.bind("bldg", BLDG)

# define a building in a site
g.add((BLDG["mysite"], A, BRICK.Site))
g.add((BLDG["mybldg"], A, BRICK.Building))
g.add((BLDG["mysite"], BRICK.hasPart, BLDG["mybldg"]))

# add a full building meter to the building
g.add((BLDG["main-meter"], A, BRICK.Building_Electrical_Meter))
g.add((BLDG["mybldg"], BRICK.isMeteredBy, BLDG["main-meter"]))

# add sensors to the building meter

# energy sensor
g.add((BLDG["building_energy_sensor"], A, BRICK.Energy_Sensor))
g.add((BLDG["building_energy_sensor"], BRICK.isPointOf, BLDG["main-meter"]))
g.add((BLDG["building_energy_sensor"], BRICK.hasUnit, UNIT["KiloW-HR"]))
timeseries_props = [
    (BRICK.hasTimeseriesId, Literal("a7523b08-7bc7-4a9d-8e88-8c0cd8084be0"))
]
g.add((BLDG["building_energy_sensor"], BRICK.timeseries, timeseries_props))

# power sensor
g.add((BLDG["building_power_sensor"], A, BRICK.Electric_Power_Sensor))
g.add((BLDG["building_power_sensor"], BRICK.isPointOf, BLDG["main-meter"]))
g.add((BLDG["building_power_sensor"], BRICK.hasUnit, UNIT["KiloW"]))
timeseries_props = [
    (BRICK.hasTimeseriesId, Literal("fd64fbc8-0742-4e1e-8f88-e2cd8a3d78af"))
]
g.add((BLDG["building_power_sensor"], BRICK.timeseries, timeseries_props))

# peak demand sensor
g.add((BLDG["building_peak_demand"], A, BRICK.Peak_Power_Demand_Sensor))
g.add((BLDG["building_peak_demand"], BRICK.isPointOf, BLDG["main-meter"]))
g.add((BLDG["building_peak_demand"], BRICK.hasUnit, UNIT["KiloW"]))
other_props = [
    (BRICK.aggregationFunction, Literal("max")),
    (BRICK.aggregationInterval, Literal("RP1D")),
]
g.add((BLDG["building_peak_demand"], BRICK.aggregate, other_props))
timeseries_props = [
    (BRICK.hasTimeseriesId, Literal("bcf9a85d-696c-446a-a2ac-97207ecfbc56"))
]
g.add((BLDG["building_peak_demand"], BRICK.timeseries, timeseries_props))

# add some submeters
submeters = [
    {
        "name": "submeter-floor1",
        "floor": "floor1",
        "power_sensor_id": "647654d4-56ee-11ec-bf02-3dcb0419df3b",
    },
    {
        "name": "submeter-floor2",
        "floor": "floor2",
        "power_sensor_id": "7a5e3870-56ee-11ec-bf02-3dcb0419df3b",
    },
    {
        "name": "submeter-floor3",
        "floor": "floor3",
        "power_sensor_id": "82332722-56ee-11ec-bf02-3dcb0419df3b",
    },
]
for submeter in submeters:
    g.add((BLDG[submeter["name"]], A, BRICK.Electrical_Meter))
    g.add((BLDG[submeter["name"]], BRICK.meters, BLDG[submeter["floor"]]))
    g.add((BLDG[submeter["name"]], BRICK.isSubMeterOf, BLDG["main-meter"]))
    g.add((BLDG[submeter["floor"]], A, BRICK.Floor))
    g.add((BLDG[submeter["floor"]], BRICK.isPartOf, BLDG["mybldg"]))

    # each of them has a power sensor w/ a provided UUID
    g.add((BLDG[f"submeter-{submeter['name']}-power"], A, BRICK.Electric_Power_Sensor))
    g.add(
        (
            BLDG[f"submeter-{submeter['name']}-power"],
            BRICK.isPointOf,
            BLDG[submeter["name"]],
        )
    )
    g.add((BLDG[f"submeter-{submeter['name']}-power"], BRICK.hasUnit, UNIT["KiloW"]))
    timeseries_props = [(BRICK.hasTimeseriesId, Literal(submeter["power_sensor_id"]))]
    g.add(
        (BLDG[f"submeter-{submeter['name']}-power"], BRICK.timeseries, timeseries_props)
    )

# monitored equipment


# save the file
g.serialize("building_meter.ttl", format="ttl")
