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
g.add((BLDG["meter"], A, BRICK.Building_Electrical_Meter))
g.add((BLDG["mybldg"], BRICK.isLocationOf, BLDG["meter"]))

# add sensors to the meter...

# energy sensor
g.add((BLDG["building_energy_sensor"], A, BRICK.Energy_Sensor))
g.add((BLDG["building_energy_sensor"], BRICK.isPointOf, BLDG["meter"]))
g.add((BLDG["building_energy_sensor"], BRICK.hasUnit, UNIT["KiloW-HR"]))
timeseries_props = [
    (BRICK.hasTimeseriesId, Literal("a7523b08-7bc7-4a9d-8e88-8c0cd8084be0"))
]
g.add((BLDG["building_energy_sensor"], BRICK.timeseries, timeseries_props))

# power sensor
g.add((BLDG["building_power_sensor"], A, BRICK.Electrical_Power_Sensor))
g.add((BLDG["building_power_sensor"], BRICK.isPointOf, BLDG["meter"]))
g.add((BLDG["building_power_sensor"], BRICK.hasUnit, UNIT["KiloW"]))
timeseries_props = [
    (BRICK.hasTimeseriesId, Literal("fd64fbc8-0742-4e1e-8f88-e2cd8a3d78af"))
]
g.add((BLDG["building_power_sensor"], BRICK.timeseries, timeseries_props))

# peak demand sensor
g.add((BLDG["building_peak_demand"], A, BRICK.Peak_Power_Demand_Sensor))
g.add((BLDG["building_peak_demand"], BRICK.isPointOf, BLDG["meter"]))
g.add((BLDG["building_peak_demand"], BRICK.hasUnit, UNIT["KiloW"]))
other_props = [
    (BRICK.aggregationFunction, Literal("max")),
    (BRICK.aggregationWindow, Literal("RP1D")),
]
g.add((BLDG["building_peak_demand"], BRICK.aggregate, other_props))
timeseries_props = [
    (BRICK.hasTimeseriesId, Literal("bcf9a85d-696c-446a-a2ac-97207ecfbc56"))
]
g.add((BLDG["building_peak_demand"], BRICK.timeseries, timeseries_props))

# save the file
g.serialize("building_meter.ttl", format="ttl")
