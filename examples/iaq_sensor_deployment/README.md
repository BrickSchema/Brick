# Residential IAQ sensor deployment

A single-family home instrumented with five indoor air quality monitors (two in
the kitchen, one each in the bedroom and living room, plus an outdoor reference
station), modeled with Brick 1.5 and RealEstateCore together.

The example is deliberately broad — it is meant to show what a *complete*
Brick + REC deployment model looks like rather than the minimum needed to
describe a sensor:

| Concern | Modeled with |
| --- | --- |
| Site, building, levels, rooms, outdoor space | `rec:Site`, `rec:Building`, `rec:Level`, `rec:CookingRoom`/`rec:Bedroom`/`rec:LivingRoom`, `rec:OutdoorSpace` |
| Address and floor areas | `rec:PostalAddress`, `rec:ArchitectureArea` |
| Building metadata | `brick:buildingPrimaryFunction`, `brick:yearBuilt` |
| Asset identity | `rec:modelNumber`, `rec:serialNumber` |
| Network identity | `rec:IPAddress`, `rec:MACAddress`, `rec:numberOfPorts` |
| Network topology | `brick:Network_Router`, `brick:Wireless_Access_Point`, `brick:Gateway` |
| Measurements | `brick:CO2_Level_Sensor`, `brick:PM2.5_Sensor`, `brick:PM10_Sensor`, `brick:TVOC_Level_Sensor`, `brick:NO2_Level_Sensor`, `brick:Ozone_Level_Sensor`, `brick:CO_Level_Sensor`, `brick:Formaldehyde_Level_Sensor`, `brick:Temperature_Sensor`, `brick:Relative_Humidity_Sensor`, `brick:Illuminance_Sensor`, `brick:Occupancy_Sensor` |
| Data handling | `brick:hasUnit`, `brick:aggregate`, `brick:resolution`, `ref:hasExternalReference` |
| Ventilation context | `rec:HVACZone`, `brick:HVAC_System`, `brick:Rooftop_Unit`, `brick:Space_Heater`, `brick:Filter`, `brick:Exhaust_Fan`, `brick:Thermostat`, `brick:Controller`, `brick:CO2_Setpoint` |
| Deployment grouping | `brick:Automation_Collection` + `rec:includes` |

## Regenerating

`iaq_sensor_deployment.ttl` is produced by `generate.py`, which writes the
prose sections verbatim and generates the ~50 point definitions from a channel
table. Timeseries identifiers are derived with `uuid5`, so reruns are byte
identical:

```
python generate.py
```
