"""
Generates iaq_sensor_deployment.ttl.

The spatial, asset, and equipment sections of the example are written out
verbatim because each triple says something different. The point definitions
are generated: there are ~50 of them, they differ only in name/class/unit, and
each needs a stable timeseries identifier. Deriving those identifiers with
uuid5 keeps the file reproducible -- rerunning this script produces byte
identical output.
"""

import uuid

TSDB = "postgres://iaq-data.example.com:5432/iaq"
NS = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")


def tsid(name):
    """Stable timeseries UUID for a point, so reruns don't churn the file."""
    return uuid.uuid5(NS, f"iaq_sensor_deployment/{name}")


# (suffix, brick class, unit, human-readable measurement name)
IAQ_CHANNELS = [
    ("co2", "CO2_Level_Sensor", "unit:PPM", "CO2 level"),
    ("pm2_5", "PM2.5_Sensor", "unit:MicroGM-PER-M3", "PM2.5"),
    ("pm10", "PM10_Sensor", "unit:MicroGM-PER-M3", "PM10"),
    ("tvoc", "TVOC_Level_Sensor", "unit:PPB", "TVOC level"),
    ("no2", "NO2_Level_Sensor", "unit:PPB", "NO2 level"),
    ("ozone", "Ozone_Level_Sensor", "unit:PPB", "ozone level"),
    ("temperature", "Temperature_Sensor", "unit:DEG_C", "temperature"),
    (
        "relative_humidity",
        "Relative_Humidity_Sensor",
        "unit:PERCENT_RH",
        "relative humidity",
    ),
    ("illuminance", "Illuminance_Sensor", "unit:LUX", "illuminance"),
]

# The stove device is a higher-specification model: a gas cooktop is a
# combustion source, and cooking is a major indoor formaldehyde source.
STOVE_EXTRA_CHANNELS = [
    ("co", "CO_Level_Sensor", "unit:PPM", "CO level"),
    ("formaldehyde", "Formaldehyde_Level_Sensor", "unit:PPB", "formaldehyde level"),
]

# The outdoor reference station only carries the channels that are meaningful
# as an outdoor background for the indoor measurements.
OUTDOOR_CHANNELS = [
    c
    for c in IAQ_CHANNELS
    if c[0] in ("pm2_5", "pm10", "no2", "ozone", "temperature", "relative_humidity")
]

# (point prefix, location, label prefix, channels)
POINT_GROUPS = [
    (
        "kitchen_stove",
        ":kitchen",
        "Kitchen stove",
        IAQ_CHANNELS[:5] + STOVE_EXTRA_CHANNELS + IAQ_CHANNELS[5:],
    ),
    ("kitchen_furnace", ":kitchen", "Kitchen furnace", IAQ_CHANNELS),
    ("bedroom", ":bedroom", "Bedroom", IAQ_CHANNELS),
    ("living_room", ":living_room", "Living room", IAQ_CHANNELS),
    ("outdoor", ":back_patio", "Outdoor", OUTDOOR_CHANNELS),
]

# Points that additionally demonstrate brick:aggregate and brick:resolution.
# Spelled out on a few points rather than all of them: the construct is the
# point, not the repetition.
AGGREGATED = {"kitchen_stove_co2", "kitchen_stove_pm2_5"}
RESOLUTION = {"kitchen_stove_co2": 1, "kitchen_stove_pm2_5": 1}


def render_point(name, brick_class, unit, label):
    lines = [":{} a brick:{} ;".format(name, brick_class)]
    lines.append('    rdfs:label "{}" ;'.format(label))
    if unit:
        lines.append("    brick:hasUnit {} ;".format(unit))
    lines.append("    brick:isPointOf {} ;".format(LOCATION_OF[name]))
    if name in AGGREGATED:
        lines.append('    brick:aggregate [ brick:aggregationFunction "mean" ;')
        lines.append('            brick:aggregationInterval "PT5M" ] ;')
    if name in RESOLUTION:
        lines.append(
            "    brick:resolution [ brick:value {} ] ;".format(RESOLUTION[name])
        )
    lines.append(
        '    ref:hasExternalReference [ ref:hasTimeseriesId "{}" ;'.format(tsid(name))
    )
    lines.append('            ref:storedAt "{}" ] .'.format(TSDB))
    return "\n".join(lines)


LOCATION_OF = {}
for prefix, location, _, channels in POINT_GROUPS:
    for suffix, _, _, _ in channels:
        LOCATION_OF[f"{prefix}_{suffix}"] = location


def render_group(prefix, label_prefix, channels):
    out = []
    for suffix, brick_class, unit, measurement in channels:
        name = f"{prefix}_{suffix}"
        out.append(
            render_point(
                name, brick_class, unit, f"{label_prefix} {measurement} sensor"
            )
        )
    return "\n\n".join(out)


HEADER = """\
####################################################################################
# Residential indoor air quality (IAQ) sensor deployment
#
# This example models a complete IAQ monitoring deployment in a single-family
# home. It is a broad demonstration of how Brick and RealEstateCore (REC) are
# used together:
#
#   * REC models the real estate: the site, building, levels, rooms, postal
#     address, and floor areas.
#   * REC also models asset identity for every piece of equipment: model and
#     serial numbers, and network identity (IP and MAC address).
#   * Brick models the operational layer: the equipment taxonomy, the points
#     each device exposes, the units and quantities being measured, the
#     ventilation equipment whose behavior the IAQ data explains, and the
#     external references connecting points to their timeseries data.
#
# Sections:
#   1.  Ontology header
#   2.  Site, building, levels, and rooms
#   3.  Zones
#   4.  Network infrastructure
#   5.  IAQ sensor devices
#   6.  IAQ points
#   7.  Ventilation and HVAC equipment
#   8.  Ventilation control points
#   9.  Deployment collection
#
# Only one direction of each relationship is asserted below; Brick defines the
# inverses (brick:hasPoint/brick:isPointOf, brick:hosts/brick:isHostedBy,
# brick:hasPart/brick:isPartOf, ...) and a reasoner materializes the other.
#
# This file is generated by generate.py.
####################################################################################

@prefix : <http://example.com/iaq_sensor_deployment#> .
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rec: <https://w3id.org/rec#> .
@prefix ref: <https://brickschema.org/schema/Brick/ref#> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

####################################################################################
# 1. Ontology header
####################################################################################

<http://example.com/iaq_sensor_deployment> a owl:Ontology ;
    rdfs:label "Residential IAQ sensor deployment" ;
    owl:imports <https://brickschema.org/schema/1.5/Brick> .

####################################################################################
# 2. Site, building, levels, and rooms
#
# rec:Site is the parcel of land, rec:Building the structure. Addresses and
# floor areas are modeled as named REC entities so they carry structured values
# rather than literals. Room floor areas are what turn raw concentrations into
# interpretable quantities such as air changes per hour or per-area emission
# rates. The outdoor space hosts the reference station: indoor concentrations
# only mean something relative to the outdoor background.
####################################################################################

:site_1 a rec:Site ;
    rdfs:label "123 Alder Street parcel" ;
    rec:hasPart :home_1 .

:home_1 a rec:Building ;
    rdfs:label "Home 1" ;
    rec:hasPart :floor_1,
        :roof ;
    rec:address :home_1_address ;
    rec:area :home_1_area ;
    brick:buildingPrimaryFunction "Single Family Home" ;
    brick:yearBuilt 1978 .

:home_1_address a rec:PostalAddress ;
    rec:addressLine1 "123 Alder Street" ;
    rec:city "Golden" ;
    rec:region "CO" ;
    rec:postalCode "80401" ;
    rec:country "US" .

:home_1_area a rec:ArchitectureArea ;
    rec:grossArea "165.0"^^xsd:float ;
    rec:netArea "148.0"^^xsd:float .

:floor_1 a rec:Level ;
    rdfs:label "First Floor" ;
    rec:levelNumber 1 ;
    rec:hasPart :kitchen,
        :bedroom,
        :living_room .

:kitchen a rec:CookingRoom ;
    rdfs:label "Kitchen" ;
    rec:area :kitchen_area .

:kitchen_area a rec:ArchitectureArea ;
    rec:netArea "14.0"^^xsd:float .

:bedroom a rec:Bedroom ;
    rdfs:label "Bedroom" ;
    rec:area :bedroom_area .

:bedroom_area a rec:ArchitectureArea ;
    rec:netArea "16.0"^^xsd:float .

:living_room a rec:LivingRoom ;
    rdfs:label "Living Room" ;
    rec:area :living_room_area .

:living_room_area a rec:ArchitectureArea ;
    rec:netArea "28.0"^^xsd:float .

:back_patio a rec:OutdoorSpace ;
    rdfs:label "Back patio" ;
    rec:isPartOf :site_1 .

:roof a rec:RoofLevel ;
    rdfs:label "Roof" ;
    rec:levelNumber 2 .

####################################################################################
# 3. Zones
#
# All three rooms are served by one thermostat, so they form a single HVAC
# zone. The zone is the granularity at which ventilation can actually be
# controlled, which is what makes per-room IAQ differences within it
# interesting.
####################################################################################

:home_hvac_zone a rec:HVACZone ;
    rdfs:label "Whole-home HVAC zone" ;
    rec:hasPart :kitchen,
        :bedroom,
        :living_room .

####################################################################################
# 4. Network infrastructure
#
# These are wireless devices on a home network, so the model says so. REC asset
# properties carry network identity (rec:IPAddress, rec:MACAddress), and Brick's
# ICT equipment shapes add rec:numberOfPorts. This is what makes a deployment
# model useful during commissioning: when a sensor stops reporting, the graph
# already records which access point it associates with and which gateway
# forwards its data.
####################################################################################

:home_router a brick:Network_Router ;
    rdfs:label "Home router" ;
    rec:locatedIn :living_room ;
    rec:IPAddress "192.168.1.1" ;
    rec:MACAddress "9C:8E:CD:00:11:22" ;
    rec:numberOfPorts 4 ;
    rec:modelNumber "RT-2400" .

:home_wifi_ap a brick:Wireless_Access_Point ;
    rdfs:label "Home Wi-Fi access point" ;
    rec:locatedIn :living_room ;
    brick:isPartOf :home_router ;
    rec:IPAddress "192.168.1.2" ;
    rec:MACAddress "9C:8E:CD:00:11:23" .

:iaq_gateway a brick:Gateway ;
    rdfs:label "IAQ data collection gateway" ;
    rec:locatedIn :living_room ;
    rec:IPAddress "192.168.1.10" ;
    rec:MACAddress "9C:8E:CD:00:11:24" .

####################################################################################
# 5. IAQ sensor devices
#
# The kitchen stove device is a higher-specification model with additional CO,
# formaldehyde, and occupancy channels; the rest are the base model.
# Heterogeneous hardware within one deployment is the normal case, and it is
# captured through the points each device hosts rather than through the
# equipment class.
####################################################################################

:kitchen_stove_iaq_device a brick:IAQ_Sensor_Equipment ;
    rdfs:label "Kitchen IAQ sensor equipment near stove" ;
    rec:locatedIn :kitchen ;
    rec:modelNumber "AS-9000" ;
    rec:serialNumber "AS9000-0001" ;
    rec:IPAddress "192.168.1.101" ;
    rec:MACAddress "A4:CF:12:00:00:01" ;
    brick:hosts :kitchen_stove_co2,
        :kitchen_stove_pm2_5,
        :kitchen_stove_pm10,
        :kitchen_stove_tvoc,
        :kitchen_stove_no2,
        :kitchen_stove_co,
        :kitchen_stove_formaldehyde,
        :kitchen_stove_ozone,
        :kitchen_stove_temperature,
        :kitchen_stove_relative_humidity,
        :kitchen_stove_illuminance,
        :kitchen_occupancy .

:kitchen_furnace_iaq_device a brick:IAQ_Sensor_Equipment ;
    rdfs:label "Kitchen IAQ sensor equipment near furnace" ;
    rec:locatedIn :kitchen ;
    rec:modelNumber "AS-9000" ;
    rec:serialNumber "AS9000-0002" ;
    rec:IPAddress "192.168.1.102" ;
    rec:MACAddress "A4:CF:12:00:00:02" ;
    brick:hosts :kitchen_furnace_co2,
        :kitchen_furnace_pm2_5,
        :kitchen_furnace_pm10,
        :kitchen_furnace_tvoc,
        :kitchen_furnace_no2,
        :kitchen_furnace_ozone,
        :kitchen_furnace_temperature,
        :kitchen_furnace_relative_humidity,
        :kitchen_furnace_illuminance .

:bedroom_iaq_device a brick:IAQ_Sensor_Equipment ;
    rdfs:label "Bedroom IAQ sensor equipment" ;
    rec:locatedIn :bedroom ;
    rec:modelNumber "AS-9000" ;
    rec:serialNumber "AS9000-0003" ;
    rec:IPAddress "192.168.1.103" ;
    rec:MACAddress "A4:CF:12:00:00:03" ;
    brick:hosts :bedroom_co2,
        :bedroom_pm2_5,
        :bedroom_pm10,
        :bedroom_tvoc,
        :bedroom_no2,
        :bedroom_ozone,
        :bedroom_temperature,
        :bedroom_relative_humidity,
        :bedroom_illuminance .

:living_room_iaq_device a brick:IAQ_Sensor_Equipment ;
    rdfs:label "Living room IAQ sensor equipment" ;
    rec:locatedIn :living_room ;
    rec:modelNumber "AS-9000" ;
    rec:serialNumber "AS9000-0004" ;
    rec:IPAddress "192.168.1.104" ;
    rec:MACAddress "A4:CF:12:00:00:04" ;
    brick:hosts :living_room_co2,
        :living_room_pm2_5,
        :living_room_pm10,
        :living_room_tvoc,
        :living_room_no2,
        :living_room_ozone,
        :living_room_temperature,
        :living_room_relative_humidity,
        :living_room_illuminance .

# Outdoor reference station. Indoor/outdoor ratios are the standard way to
# separate indoor sources (cooking, cleaning, occupants) from infiltration of
# outdoor pollution, so a deployment without one is hard to interpret.
:outdoor_iaq_device a brick:IAQ_Sensor_Equipment ;
    rdfs:label "Outdoor reference IAQ sensor equipment" ;
    rec:locatedIn :back_patio ;
    rec:modelNumber "AS-9000-OD" ;
    rec:serialNumber "AS9000OD-0001" ;
    rec:IPAddress "192.168.1.105" ;
    rec:MACAddress "A4:CF:12:00:00:05" ;
    brick:hosts :outdoor_pm2_5,
        :outdoor_pm10,
        :outdoor_no2,
        :outdoor_ozone,
        :outdoor_temperature,
        :outdoor_relative_humidity .

####################################################################################
# 6. IAQ points
#
# Every point carries its unit and a reference to where its data is actually
# stored. The kitchen stove points additionally show constructs that apply
# equally to the rest but are spelled out once here:
#
#   * brick:aggregate  -- how the stored data was reduced
#   * brick:resolution -- the smallest change the sensor can distinguish
####################################################################################
"""

FOOTER = """\
####################################################################################
# 7. Ventilation and HVAC equipment
#
# IAQ measurements are only actionable next to the equipment that can change
# them. A packaged rooftop unit conditions and filters the air for the whole
# zone; a gas wall furnace heats the kitchen directly; the range hood is local
# exhaust for the largest indoor source in the house. Note brick:feeds from a
# space to equipment: that is the return/exhaust path, i.e. the kitchen
# supplies the air the range hood removes.
####################################################################################

:home_hvac_system a brick:HVAC_System ;
    rdfs:label "Home forced-air HVAC system" ;
    rec:includes :rtu,
        :kitchen_wall_furnace,
        :range_hood .

:rtu a brick:Rooftop_Unit ;
    rdfs:label "Packaged rooftop unit" ;
    rec:locatedIn :roof ;
    brick:feeds :home_hvac_zone ;
    brick:hasPart :air_filter ;
    rec:modelNumber "RTU-3T" ;
    rec:serialNumber "RTU3T-77213" ;
    brick:hasPoint :rtu_fan_command,
        :rtu_supply_air_flow .

:air_filter a brick:Filter ;
    rdfs:label "RTU MERV 13 filter" ;
    rec:modelNumber "MERV13-20x25x1" ;
    brick:hasPoint :air_filter_status,
        :change_filter_alarm .

# A vented gas wall furnace: the second combustion source in the kitchen, and
# the reason the second kitchen device sits where it does. NO2 and CO next to a
# gas appliance are the measurements that catch a failing burner or a blocked
# flue.
:kitchen_wall_furnace a brick:Space_Heater ;
    rdfs:label "Kitchen gas wall furnace" ;
    rec:locatedIn :kitchen ;
    brick:feeds :kitchen ;
    rec:modelNumber "WF-25" ;
    brick:hasPoint :kitchen_wall_furnace_command .

:range_hood a brick:Exhaust_Fan ;
    rdfs:label "Kitchen range hood exhaust fan" ;
    rec:locatedIn :kitchen ;
    brick:isControlledBy :iaq_controller ;
    rec:modelNumber "RH-400" ;
    brick:hasPoint :range_hood_command,
        :range_hood_speed_setpoint .

# Exhaust path: the kitchen supplies the air the range hood removes.
:kitchen brick:feeds :range_hood .

:thermostat a brick:Thermostat ;
    rdfs:label "Living room thermostat" ;
    rec:locatedIn :living_room ;
    rec:modelNumber "TS-3" ;
    rec:IPAddress "192.168.1.60" ;
    rec:MACAddress "9C:8E:CD:00:11:60" ;
    brick:hasPoint :thermostat_zone_air_temperature,
        :thermostat_air_temperature_setpoint .

####################################################################################
# 8. Ventilation control points
#
# The CO2 setpoint closes the loop between the measurements above and the
# ventilation equipment, which is the reason the deployment exists.
####################################################################################

:iaq_controller a brick:Controller ;
    rdfs:label "Demand-controlled ventilation controller" ;
    rec:locatedIn :kitchen ;
    rec:IPAddress "192.168.1.50" ;
    rec:MACAddress "9C:8E:CD:00:11:50" ;
    brick:hasPoint :kitchen_co2_setpoint .

:kitchen_co2_setpoint a brick:CO2_Setpoint ;
    rdfs:label "Kitchen CO2 setpoint" ;
    brick:hasUnit unit:PPM ;
    brick:isPointOf :kitchen .

:kitchen_wall_furnace_command a brick:On_Off_Command ;
    rdfs:label "Kitchen wall furnace on/off command" .

:range_hood_command a brick:On_Off_Command ;
    rdfs:label "Range hood on/off command" .

:range_hood_speed_setpoint a brick:Speed_Setpoint ;
    rdfs:label "Range hood speed setpoint" ;
    brick:hasUnit unit:PERCENT .

:rtu_fan_command a brick:On_Off_Command ;
    rdfs:label "RTU fan on/off command" .

:rtu_supply_air_flow a brick:Air_Flow_Sensor ;
    rdfs:label "RTU supply air flow sensor" ;
    brick:hasUnit unit:M3-PER-HR .

:air_filter_status a brick:Filter_Status ;
    rdfs:label "Air filter status" .

:change_filter_alarm a brick:Change_Filter_Alarm ;
    rdfs:label "Change filter alarm" .

:thermostat_zone_air_temperature a brick:Zone_Air_Temperature_Sensor ;
    rdfs:label "Thermostat zone air temperature sensor" ;
    brick:hasUnit unit:DEG_C .

:thermostat_air_temperature_setpoint a brick:Air_Temperature_Setpoint ;
    rdfs:label "Thermostat air temperature setpoint" ;
    brick:hasUnit unit:DEG_C .

####################################################################################
# 9. Deployment collection
#
# The instruments are a logical grouping that cuts across rooms and corresponds
# to no HVAC system, which is what a brick:Automation_Collection is for. Note
# that collections relate to their members with rec:includes, not
# brick:hasPart. Brick encourages subclassing Automation_Collection for a
# specific kind of grouping; the base class is used directly here.
####################################################################################

:iaq_deployment a brick:Automation_Collection ;
    rdfs:label "Home 1 IAQ instrument deployment" ;
    rec:includes :kitchen_stove_iaq_device,
        :kitchen_furnace_iaq_device,
        :bedroom_iaq_device,
        :living_room_iaq_device,
        :outdoor_iaq_device,
        :iaq_gateway .
"""

# Occupancy is what makes CO2 interpretable: 1200 ppm in an empty kitchen means
# something very different from 1200 ppm in an occupied one. It is hosted by the
# stove device but is a property of the room, not of the air.
# Its data arrives over MQTT rather than landing in the timeseries database
# with the rest, which is what ref:storedAt is there to record.
OCCUPANCY = """\
:kitchen_occupancy a brick:Occupancy_Sensor ;
    rdfs:label "Kitchen occupancy sensor" ;
    brick:isPointOf :kitchen ;
    ref:hasExternalReference [ ref:hasTimeseriesId "{}" ;
            ref:storedAt "mqtt://iaq-gateway.example.com:1883\
/home1/kitchen/occupancy" ] .""".format(
    tsid("kitchen_occupancy")
)

SECTION_HEADINGS = {
    "kitchen_stove": "# --- Kitchen, near stove ---",
    "kitchen_furnace": "# --- Kitchen, near furnace ---",
    "bedroom": "# --- Bedroom ---",
    "living_room": "# --- Living room ---",
    "outdoor": "# --- Outdoor reference station ---",
}


def main():
    parts = [HEADER]
    for prefix, _, label_prefix, channels in POINT_GROUPS:
        parts.append(f"\n{SECTION_HEADINGS[prefix]}\n")
        parts.append(render_group(prefix, label_prefix, channels))
        if prefix == "kitchen_stove":
            parts.append("")
            parts.append(OCCUPANCY)
        parts.append("")
    parts.append("")
    parts.append(FOOTER)
    with open("iaq_sensor_deployment.ttl", "w") as f:
        f.write("\n".join(parts))


if __name__ == "__main__":
    main()
