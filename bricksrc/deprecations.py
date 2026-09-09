from .namespaces import BRICK, RDFS, SKOS, A, QUDTQK, REC

deprecations = {
    BRICK.Collection: {
        "version": "1.5.0",
        "mitigation_message": "Brick Collection is deprecated in favor of REC Collection to remove redundancy between the two ontologies.",
        "replace_with": REC.Collection,
        RDFS.subClassOf: BRICK.Entity,
    },
    BRICK.Speed_Status: {
        "version": "1.4.0",
        "mitigation_message": "Speed Status is no longer necessary. Use Speed Mode Status for motors with various categorical speed settings, such as low, medium, and high. To further clarify, points representing the current speed of a variable speed fan as an analog value or input, use Speed Sensor.",
        "replace_with": BRICK.Speed_Mode_Status,
        RDFS.subClassOf: BRICK.Status,
    },
    BRICK.Condenser: {
        "version": "1.3.0",
        "mitigation_message": "'Condenser' and 'Condensing Unit' are interchangable terms. Renaming class to 'Condensing_Unit' to further aligns with ASHRAE's terminology.",
        "replace_with": BRICK.Condensing_Unit,
    },
    BRICK.Heat_Sensor: {
        "version": "1.4.0",
        "mitigation_message": "This class has a poor definition is supplanted by Temperature_Sensor",
        "replace_with": BRICK.Temperature_Sensor,
        RDFS.subClassOf: BRICK.Sensor,
    },
    BRICK.Trace_Heat_Sensor: {
        "version": "1.4.0",
        "mitigation_message": "Removed due to unclear definition",
        "replace_with": BRICK.Sensor,
    },
    BRICK.Solar_Radiance_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "The class 'Solar_Radiance_Sensor' is deprecated in favor of 'Solar_Irradiance_Sensor'. The new name better reflects the standard unit of measurement, watts per square meter (W/m²), and aligns with the terminology commonly used in solar applications.",
        "replace_with": BRICK.Solar_Irradiance_Sensor,
        RDFS.subClassOf: BRICK.Sensor,
    },
    BRICK.Occupied_Air_Temperature_Cooling_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "'Occupied_Air_Temperature_Cooling_Setpoint' is deprecated in favor of further specifying that it is a zone air setpoint.",
        "replace_with": BRICK.Occupied_Cooling_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Occupied_Air_Temperature_Setpoint,
    },
    BRICK.Occupied_Air_Temperature_Heating_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "'Occupied_Air_Temperature_Heating_Setpoint' is deprecated in favor of further specifying that it is a zone air setpoint.",
        "replace_with": BRICK.Occupied_Heating_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Occupied_Air_Temperature_Setpoint,
    },
    BRICK.Unoccupied_Air_Temperature_Cooling_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "'Unoccupied_Air_Temperature_Cooling_Setpoint' is deprecated in favor of further specifying that it is a zone air setpoint.",
        "replace_with": BRICK.Unoccupied_Cooling_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Unoccupied_Air_Temperature_Setpoint,
    },
    BRICK.Unoccupied_Air_Temperature_Heating_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "'Unoccupied_Air_Temperature_Heating_Setpoint' is deprecated in favor of further specifying that it is a zone air setpoint.",
        "replace_with": BRICK.Unoccupied_Heating_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Unoccupied_Air_Temperature_Setpoint,
    },
    BRICK.Effective_Air_Temperature_Cooling_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "The class 'Effective_Air_Temperature_Cooling_Setpoint' is deprecated in favor of further specifying that it is a zone air setpoint.",
        "replace_with": BRICK.Effective_Cooling_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Effective_Air_Temperature_Setpoint,
    },
    BRICK.Effective_Air_Temperature_Heating_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "The class 'Effective_Air_Temperature_Heating_Setpoint' is deprecated in favor of further specifying that it is a zone air setpoint.",
        "replace_with": BRICK.Effective_Heating_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Effective_Air_Temperature_Setpoint,
    },
    BRICK.Zone_Air_Temperature_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "The class 'Zone_Air_Temperature_Setpoint' is deprecated in favor of more explicit class names to distinguish target and cooling/heating setpoints.",
        SKOS.definition: "Sets temperature of zone air",
        "replace_with": BRICK.Target_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Air_Temperature_Setpoint,
    },
    BRICK.Effective_Zone_Air_Temperature_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "The class 'Effective_Zone_Air_Temperature_Setpoint' is deprecated and replaced to better represent its function as a target setpoint",
        "replace_with": BRICK.Effective_Target_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Zone_Air_Temperature_Setpoint,
    },
    BRICK.Occupied_Zone_Air_Temperaure_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "'Occupied_Zone_Air_Temperature_Setpoint' is deprecated in favor of further specifying that it is a target setpoint",
        "replace_with": BRICK.Occupied_Target_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Zone_Air_Temperature_Setpoint,
    },
    BRICK.Unoccupied_Zone_Air_Temperature_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "'Unoccupied_Zone_Air_Temperature_Setpoint' is deprecated in favor of further specifying that it is a target setpoint",
        "replace_with": BRICK.Unoccupied_Target_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Zone_Air_Temperature_Setpoint,
    },
    BRICK.Zone_Air_Cooling_Temperature_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "'Zone_Air_Cooling_Temperature_Setpoint' is deprecated to support new naming convention, which reorders intended behaviour (cooling) before the substance (zone air).",
        SKOS.definition: "The upper (cooling) setpoint for zone air temperature",
        "replace_with": BRICK.Cooling_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Zone_Air_Temperature_Setpoint,
    },
    BRICK.Zone_Air_Heating_Temperature_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "'Zone_Air_Heating_Temperature_Setpoint' is deprecated to support new naming convention, whic reorders intended behaviour (heating) before the substance (zone air)",
        SKOS.definition: "The lower (heating) setpoint for zone air temperature",
        "replace_with": BRICK.Heating_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Zone_Air_Temperature_Setpoint,
    },
    BRICK.Fresh_Air_Fan: {
        "version": "1.3.0",
        "mitigation_message": "Fresh Air Fan is deprecated in favor of Outside Fan because the latter is a more accurate representation",
        "replace_with": BRICK.Outside_Fan,
        RDFS.subClassOf: BRICK.Fan,
    },
    BRICK.Exhaust_Fan_Disable_Command: {
        "version": "1.3.0",
        "mitigation_message": "Exhaust_Fan_Disable_Command is deprecated as a point name should not include more specific equipment names than top level equipment names",
        "replace_with": BRICK.Disable_Command,
        RDFS.subClassOf: BRICK.Command,
    },
    BRICK.Exhaust_Fan_Enable_Command: {
        "version": "1.3.0",
        "mitigation_message": "Exhaust_Fan_Enable_Command is deprecated as a point name should not include more specific equipment names than top level equipment names",
        "replace_with": BRICK.Enable_Command,
    },
    BRICK.Light_Command: {
        "version": "1.3.1",
        "mitigation_message": "Replaced with Lighting_Command to represent its function more precisely.",
        "replace_with": BRICK.Lighting_Level_Command,
        RDFS.subClassOf: BRICK.Command,
    },
    BRICK.Supply_Water_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Water_Temperature_Sensor,
        RDFS.subClassOf: BRICK.Water_Temperature_Sensor,
    },
    BRICK.Discharge_Water_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Water_Temperature_Sensor,
        RDFS.subClassOf: BRICK.Water_Temperature_Sensor,
    },
    BRICK.Supply_Water_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Water_Flow_Sensor,
        RDFS.subClassOf: BRICK.Water_Flow_Sensor,
    },
    BRICK.Discharge_Water_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Water_Flow_Sensor,
        RDFS.subClassOf: BRICK.Water_Flow_Sensor,
    },
    BRICK.Chilled_Water_Discharge_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water_Flow_Sensor,
        RDFS.subClassOf: [
            BRICK.Discharge_Water_Flow_Sensor,
            BRICK.Chilled_Water_Flow_Sensor,
        ],
    },
    BRICK.Chilled_Water_Supply_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water_Flow_Sensor,
        RDFS.subClassOf: [
            BRICK.Supply_Water_Flow_Sensor,
            BRICK.Chilled_Water_Flow_Sensor,
        ],
    },
    BRICK.Chilled_Water_Discharge_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water_Flow_Sensor,
        RDFS.subClassOf: [
            BRICK.Discharge_Water_Flow_Sensor,
            BRICK.Chilled_Water_Flow_Sensor,
        ],
    },
    BRICK.Discharge_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Water,
        SKOS.broader: BRICK.Water,
        A: BRICK.Substance,
    },
    BRICK.Discharge_Chilled_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water,
        SKOS.broader: BRICK.Chilled_Water,
        A: BRICK.Substance,
    },
    BRICK.Discharge_Hot_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water,
        SKOS.broader: BRICK.Hot_Water,
        A: BRICK.Substance,
    },
    BRICK.Supply_Condenser_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Condenser_Water,
        SKOS.broader: BRICK.Condenser_Water,
        A: BRICK.Substance,
    },
    BRICK.Discharge_Condenser_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Condenser_Water,
        SKOS.broader: BRICK.Condenser_Water,
        A: BRICK.Substance,
    },
    BRICK.Return_Condenser_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Condenser_Water,
        SKOS.broader: BRICK.Condenser_Water,
        A: BRICK.Substance,
    },
    BRICK.Heat_Exchanger_Supply_Water_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Heat_Exchanger_Leaving_Water_Temperature_Sensor,
        RDFS.subClassOf: BRICK.Water_Temperature_Sensor,
    },
    BRICK.Heat_Exchanger_Discharge_Water_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Heat_Exchanger_Leaving_Water_Temperature_Sensor,
        RDFS.subClassOf: BRICK.Water_Temperature_Sensor,
    },
    BRICK.Hot_Water_Supply_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water_Flow_Sensor,
        RDFS.subClassOf: [BRICK.Hot_Water_Flow_Sensor, BRICK.Supply_Water_Flow_Sensor],
    },
    BRICK.Hot_Water_Discharge_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water_Flow_Sensor,
        RDFS.subClassOf: [
            BRICK.Hot_Water_Flow_Sensor,
            BRICK.Discharge_Water_Flow_Sensor,
        ],
    },
    BRICK.Hot_Water_Supply_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water_Temperature_Sensor,
        RDFS.subClassOf: [
            BRICK.Supply_Water_Temperature_Sensor,
        ],
    },
    BRICK.Hot_Water_Discharge_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water_Temperature_Sensor,
        RDFS.subClassOf: [
            BRICK.Discharge_Water_Temperature_Sensor,
        ],
    },
    BRICK.Domestic_Hot_Water_Discharge_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Domestic_Hot_Water_Temperature_Sensor,
        RDFS.subClassOf: BRICK.Domestic_Hot_Water_Temperature_Sensor,
    },
    BRICK.High_Temperature_Hot_Water_Discharge_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_High_Temperature_Hot_Water_Temperature_Sensor,
        RDFS.subClassOf: BRICK.Hot_Water_Discharge_Temperature_Sensor,
    },
    BRICK.Medium_Temperature_Hot_Water_Discharge_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Medium_Temperature_Hot_Water_Temperature_Sensor,
        RDFS.subClassOf: BRICK.Hot_Water_Discharge_Temperature_Sensor,
    },
    BRICK.Return_Water_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Water_Flow_Sensor,
        RDFS.subClassOf: BRICK.Water_Flow_Sensor,
    },
    BRICK.Chilled_Water_Return_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Chilled_Water_Flow_Sensor,
        RDFS.subClassOf: [
            BRICK.Chilled_Water_Flow_Sensor,
            BRICK.Return_Water_Flow_Sensor,
        ],
    },
    BRICK.Hot_Water_Return_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Hot_Water_Flow_Sensor,
        RDFS.subClassOf: [BRICK.Hot_Water_Flow_Sensor, BRICK.Return_Water_Flow_Sensor],
    },
    BRICK.Return_Condenser_Water_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Condenser_Water_Flow_Sensor,
        RDFS.subClassOf: [
            BRICK.Condenser_Water_Flow_Sensor,
            BRICK.Return_Water_Flow_Sensor,
        ],
    },
    BRICK.Chilled_Water_Discharge_Flow_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water_Flow_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Chilled_Water_Flow_Setpoint,
            BRICK.Discharge_Water_Flow_Setpoint,
        ],
    },
    BRICK.Chilled_Water_Return_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Chilled_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Chilled_Water_Temperature_Sensor,
            BRICK.Return_Water_Temperature_Sensor,
        ],
    },
    BRICK.Chilled_Water_Supply_Flow_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water_Flow_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Chilled_Water_Flow_Setpoint,
            BRICK.Supply_Water_Flow_Setpoint,
        ],
    },
    BRICK.Chilled_Water_Supply_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Chilled_Water_Temperature_Sensor,
            BRICK.Supply_Water_Temperature_Sensor,
        ],
    },
    BRICK.Chilled_Water_Discharge_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Chilled_Water_Temperature_Sensor,
            BRICK.Discharge_Water_Temperature_Sensor,
        ],
    },
    BRICK.Differential_Supply_Return_Water_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Differential_Entering_Leaving_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Water_Differential_Temperature_Sensor,
    },
    BRICK.Differential_Discharge_Return_Water_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Differential_Entering_Leaving_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Water_Differential_Temperature_Sensor,
    },
    BRICK.Domestic_Hot_Water_Supply_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Domestic_Hot_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Hot_Water_Supply_Temperature_Sensor,
    },
    BRICK.Domestic_Hot_Water_Supply_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Domestic_Hot_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Supply_Hot_Water_Temperature_Setpoint,
    },
    BRICK.Domestic_Hot_Water_Discharge_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Domestic_Hot_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Discharge_Hot_Water_Temperature_Setpoint,
    },
    BRICK.High_Temperature_Hot_Water_Return_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_High_Temperature_Hot_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Hot_Water_Return_Temperature_Sensor,
    },
    BRICK.High_Temperature_Hot_Water_Supply_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_High_Temperature_Hot_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Hot_Water_Supply_Temperature_Sensor,
    },
    BRICK.Hot_Water_Discharge_Flow_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water_Flow_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Discharge_Water_Flow_Setpoint,
            BRICK.Hot_Water_Flow_Setpoint,
        ],
    },
    BRICK.Discharge_Water_Flow_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Water_Flow_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Water_Flow_Setpoint,
        ],
    },
    BRICK.Supply_Water_Flow_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Water_Flow_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Water_Flow_Setpoint,
        ],
    },
    BRICK.Hot_Water_Return_Flow_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Hot_Water_Flow_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: [BRICK.Return_Water_Flow_Sensor, BRICK.Hot_Water_Flow_Sensor],
    },
    BRICK.Hot_Water_Return_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Hot_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Return_Water_Temperature_Sensor,
        ],
    },
    BRICK.Hot_Water_Supply_Flow_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water_Flow_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Supply_Water_Flow_Setpoint,
            BRICK.Hot_Water_Flow_Setpoint,
        ],
    },
    BRICK.Hot_Water_Supply_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Supply_Water_Temperature_Sensor,
        ],
    },
    BRICK.Medium_Temperature_Hot_Water_Return_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Medium_Temperature_Hot_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Hot_Water_Return_Temperature_Sensor,
    },
    BRICK.Medium_Temperature_Hot_Water_Supply_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Medium_Temperature_Hot_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Hot_Water_Supply_Temperature_Sensor,
    },
    BRICK.Return_Chilled_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Chilled_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Chilled_Water_Temperature_Setpoint,
            BRICK.Return_Water_Temperature_Setpoint,
        ],
    },
    BRICK.Return_Condenser_Water_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Condenser_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Condenser_Water_Temperature_Sensor,
    },
    BRICK.Return_Condenser_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Condenser_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Return_Water_Temperature_Setpoint,
    },
    BRICK.Return_Hot_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Hot_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Return_Water_Temperature_Setpoint,
        ],
    },
    BRICK.Return_Water_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Water_Temperature_Sensor,
    },
    BRICK.Return_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Water_Temperature_Setpoint,
    },
    BRICK.Supply_Chilled_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Chilled_Water_Temperature_Setpoint,
        ],
    },
    BRICK.Discharge_Chilled_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Chilled_Water_Temperature_Setpoint,
        ],
    },
    BRICK.Supply_Condenser_Water: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Condenser_Water,
        "version": "1.3.0",
        SKOS.broader: BRICK.Condenser_Water,
        A: BRICK.Substance,
    },
    BRICK.Supply_Condenser_Water_Flow_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Condenser_Water_Flow_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Condenser_Water_Flow_Sensor,
            BRICK.Supply_Water_Flow_Sensor,
        ],
    },
    BRICK.Discharge_Condenser_Water_Flow_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Condenser_Water_Flow_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Condenser_Water_Flow_Sensor,
            BRICK.Discharge_Water_Flow_Sensor,
        ],
    },
    BRICK.Supply_Condenser_Water_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Condenser_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Condenser_Water_Temperature_Sensor,
            BRICK.Supply_Water_Temperature_Sensor,
        ],
    },
    BRICK.Discharge_Condenser_Water_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Condenser_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Condenser_Water_Temperature_Sensor,
            BRICK.Discharge_Water_Temperature_Sensor,
        ],
    },
    BRICK.Supply_Condenser_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Condenser_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Leaving_Condenser_Water_Temperature_Setpoint,
        ],
    },
    BRICK.Discharge_Condenser_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Condenser_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Leaving_Condenser_Water_Temperature_Setpoint,
        ],
    },
    BRICK.Supply_Hot_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Leaving_Hot_Water_Temperature_Setpoint,
            BRICK.Hot_Water_Temperature_Setpoint,
        ],
    },
    BRICK.Discharge_Hot_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Leaving_Hot_Water_Temperature_Setpoint,
            BRICK.Hot_Water_Temperature_Setpoint,
        ],
    },
    BRICK.Electric_Current: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Electric_Current' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/ElectricCurrent' directly.",
        "replace_with": QUDTQK.ElectricCurrent,
    },
    BRICK.Voltage: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Voltage' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/Voltage' directly.",
        "replace_with": QUDTQK.Voltage,
    },
    BRICK.Thermal_Energy: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Thermal_Energy' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/ThermalEnergy' directly.",
        "replace_with": QUDTQK.ThermalEnergy,
    },
    BRICK.Frequency: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Frequency' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/Frequency' directly.",
        "replace_with": QUDTQK.Frequency,
    },
    BRICK.Irradiance: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Irradiance' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/Irradiance' directly. For specific solar irradiance, use brick:Solar_Irradiance.",
        "replace_with": QUDTQK.Irradiance,
    },
    BRICK.Power_Factor: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Power_Factor' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/PowerFactor' directly.",
        "replace_with": QUDTQK.PowerFactor,
    },
    BRICK.Pressure: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined generic quantity 'Pressure' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/Pressure' directly, or more specific QUDT/Brick quantities like qudt:QuantityKind/StaticPressure, qudt:QuantityKind/AtmosphericPressure, brick:Differential_Pressure, etc.",
        "replace_with": QUDTQK.Pressure,
    },
    BRICK.Atmospheric_Pressure: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Atmospheric_Pressure' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/AtmosphericPressure' directly.",
        "replace_with": QUDTQK.AtmosphericPressure,
    },
    BRICK.Gauge_Pressure: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Gauge_Pressure' is deprecated. Use the QUDT quantity 'qudt:QuantityKind/Pressure' and indicate contextually that it is gauge pressure if necessary.",
        "replace_with": QUDTQK.Pressure,
    },
    BRICK.Static_Pressure: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Static_Pressure' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/StaticPressure' directly.",
        "replace_with": QUDTQK.StaticPressure,
    },
    BRICK.Dynamic_Pressure: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Dynamic_Pressure' (also referred to as Velocity_Pressure) is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/DynamicPressure' directly.",
        "replace_with": QUDTQK.DynamicPressure,
    },
    BRICK.Velocity_Pressure: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Velocity_Pressure' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/DynamicPressure' directly.",
        "replace_with": QUDTQK.DynamicPressure,
    },
    BRICK.Radiance: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Radiance' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/Radiance' directly. For specific solar radiance, use brick:Solar_Radiance.",
        "replace_with": QUDTQK.Radiance,
    },
    BRICK.Temperature: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined generic quantity 'Temperature' is deprecated for direct use. Use the equivalent QUDT quantity 'qudt:QuantityKind/Temperature' directly, or more specific Brick quantities like brick:Dry_Bulb_Temperature, brick:Wet_Bulb_Temperature, etc., which now subclass the QUDT quantity.",
        "replace_with": QUDTQK.Temperature,
    },
    BRICK.Time: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Time' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/Time' directly.",
        "replace_with": QUDTQK.Time,
    },
    BRICK.Energy: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Energy' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/Energy' directly.",
        "replace_with": QUDTQK.Energy,
    },
    BRICK.Electric_Energy: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Electric_Energy' is deprecated. Use QUDT quantitykind:ElectricEnergy directly.",
        "replace_with": QUDTQK.ElectricEnergy,
    },
    BRICK.Active_Energy: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Active_Energy' is deprecated. Use QUDT quantitykind:ActiveEnergy directly.",
        "replace_with": QUDTQK.ActiveEnergy,
    },
    BRICK.Reactive_Energy: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Reactive_Energy' is deprecated. Use QUDT quantitykind:ReactiveEnergy directly.",
        "replace_with": QUDTQK.ReactiveEnergy,
    },
    BRICK.Apparent_Energy: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Apparent_Energy' is deprecated. Use QUDT quantitykind:ApparentEnergy directly.",
        "replace_with": QUDTQK.ApparentEnergy,
    },
    BRICK.Level: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Level' is deprecated. Use QUDT quantitykind:LiquidLevel directly for liquid level measurements.",
    },
    BRICK.Current_Imbalance: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Current_Imbalance' is deprecated. Use QUDT quantitykind:ElectricCurrentImbalance directly.",
        "replace_with": QUDTQK.ElectricCurrentImbalance,
    },
    BRICK.Voltage_Imbalance: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Voltage_Imbalance' is deprecated. Use QUDT quantitykind:VoltageImbalance directly.",
        "replace_with": QUDTQK.VoltageImbalance,
    },
    BRICK.GrainsOfMoisture: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'GrainsOfMoisture' is deprecated. Use QUDT quantitykind:SpecificHumidity directly.",
        "replace_with": QUDTQK.SpecificHumidity,
    },
    BRICK.Deceleration_Time: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Deceleration_Time' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/Time' directly.",
        "replace_with": QUDTQK.Time,
    },
    BRICK.Acceleration_Time: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Acceleration_Time' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/Time' directly.",
        "replace_with": QUDTQK.Time,
    },
    BRICK.Radioactivity_Concentration_Sensor: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Radioactivity_Concentration_Sensor' is deprecated. Use Air_Quality_Sensor instead, or the provided sensor class for the specific kind or source of radioactivity (e.g. Radon gas)",
        "replace_with": BRICK.Air_Quality_Sensor,
    },
    BRICK.Phasor: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Phasor' is deprecated.",
    },
    BRICK.Radioactivity_Concentration: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Radioactivity_Concentration' is deprecated.",
    },
    BRICK.Weather_Condition: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Weather_Condition' is deprecated.",
    },
}

# Definitions (and optional rdfs:seeAlso) for deprecated terms whose deprecation
# metadata is declared in Turtle (bricksrc/recpatches.ttl) rather than in the
# `deprecations` dict above. Terms in `deprecations` carry SKOS.definition inline.
deprecated_definitions = {
    BRICK.Ablutions_Room: {
        SKOS.definition: "A room for performing cleansing rituals before prayer",
    },
    BRICK.Atrium: {
        SKOS.definition: "a large open-air or skylight covered space surrounded by a building.",
        RDFS.seeAlso: "https://en.wikipedia.org/wiki/Atrium_(architecture)",
    },
    BRICK.Auditorium: {
        SKOS.definition: "A space for performances or larger gatherings",
    },
    BRICK.Basement: {
        SKOS.definition: "The floor of a building which is partly or entirely below ground level.",
    },
    BRICK.Battery_Room: {
        SKOS.definition: "A room used to hold batteries for backup power",
    },
    BRICK.Bench_Space: {
        SKOS.definition: "For areas of play in a stadium, the area for partcipants and referees by the side of the field",
    },
    BRICK.Break_Room: {
        SKOS.definition: "A space for people to relax while not working",
    },
    BRICK.Broadcast_Room: {
        SKOS.definition: "A space to organize and manage a broadcast. Separate from studio",
    },
    BRICK.Building: {
        SKOS.definition: "An independent unit of the built environment with a characteristic spatial structure, intended to serve at least one function or user activity [ISO 12006-2:2013]",
    },
    BRICK.Cafeteria: {
        SKOS.definition: "A space to serve food and beverages",
    },
    BRICK.Cold_Box: {
        SKOS.definition: "in a gas separation unit, the insulated section that contains the low-temperature heat exchangers and distillation columns.",
    },
    BRICK.Common_Space: {
        SKOS.definition: "A class of spaces that are used by multiple people at the same time",
    },
    BRICK.Concession: {
        SKOS.definition: "A space to sell food and beverages. Usually embedded in a larger space and does not include a space where people consume their purchases",
    },
    BRICK.Conference_Room: {
        SKOS.definition: "A space dedicated in which to hold a meetings",
    },
    BRICK.Control_Room: {
        SKOS.definition: "A space from which operations are managed",
    },
    BRICK.Copy_Room: {
        SKOS.definition: "A room set aside for common office equipment, including printers and copiers",
    },
    BRICK.Cubicle: {
        SKOS.definition: "A smaller space set aside for an individual, but not with a door and without full-height walls",
    },
    BRICK.Detention_Room: {
        SKOS.definition: "A space for the temporary involuntary confinement of people",
    },
    BRICK.Distribution_Frame: {
        SKOS.definition: "A class of spaces where the cables carrying signals meet and connect, e.g. a wiring closet or a broadcast downlink room",
    },
    BRICK.Electrical_Room: {
        SKOS.definition: "A class of service rooms that house electrical equipment for a building",
    },
    BRICK.Elevator_Shaft: {
        SKOS.definition: "The vertical space in which an elevator ascends and descends",
    },
    BRICK.Employee_Entrance_Lobby: {
        SKOS.definition: "An open space near an entrance that is typicaly only used for employees",
    },
    BRICK.Enclosed_Office: {
        SKOS.definition: "A space for individuals to work with walls and a door",
    },
    BRICK.Energy_Zone: {
        SKOS.definition: "A space or group of spaces that are managed or monitored as one unit for energy purposes",
    },
    BRICK.Entrance: {
        SKOS.definition: "The location and space of a building where people enter and exit the building",
    },
    BRICK.Environment_Box: {
        SKOS.definition: "(also known as climatic chamber), enclosed space designed to create a particular environment.",
    },
    BRICK.Equipment_Room: {
        SKOS.definition: "A telecommunications room where equipment that serves the building is stored",
    },
    BRICK.Exercise_Room: {
        SKOS.definition: "An indoor room used for exercise and physical activities",
    },
    BRICK.Field_Of_Play: {
        SKOS.definition: "The area of a stadium where athletic events occur, e.g. the soccer pitch",
    },
    BRICK.Fire_Zone: {
        SKOS.definition: "A logical subdivision of a building that is monitored for fire; may also have a classification for the type of fire hazard that can occur",
    },
    BRICK.First_Aid_Room: {
        SKOS.definition: "A room for a person with minor injuries can be treated or temporarily treated until transferred to a more advanced medical facility",
    },
    BRICK.Floor: {
        SKOS.definition: "A level, typically representing a horizontal aggregation of spaces that are vertically bound. (referring to IFC)",
    },
    BRICK.Food_Service_Room: {
        SKOS.definition: "A space used in the production, storage, serving, or cleanup of food and beverages",
    },
    BRICK.Freezer: {
        SKOS.definition: "cold chamber usually kept at a temperature of 22°F to 31°F (–5°C to –1°C), with high-volume air circulation.",
    },
    BRICK.Furniture: {
        SKOS.definition: "Movable objects intended to support various human activities such as seating, eating and sleeping",
        RDFS.seeAlso: "https://en.wikipedia.org/wiki/Furniture",
    },
    BRICK.Gatehouse: {
        SKOS.definition: "The standalone building used to manage the entrance to a campus or building grounds",
    },
    BRICK.Generator_Room: {
        SKOS.definition: "A room for electrical equipment, specifically electrical generators.",
    },
    BRICK.HVAC_Zone: {
        SKOS.definition: "a space or group of spaces, within a building with heating, cooling, and ventilating requirements, that are sufficiently similar so that desired conditions (e.g., temperature) can be maintained throughout using a single sensor (e.g., thermostat or temperature sensor).",
    },
    BRICK.Hallway: {
        SKOS.definition: "A common space, used to connect other parts of a building",
    },
    BRICK.Hazardous_Materials_Storage: {
        SKOS.definition: "A storage space set aside (usually with restricted access) for the storage of materials that can be hazardous to living beings or the environment",
    },
    BRICK.Hospitality_Box: {
        SKOS.definition: "A room at a stadium, usually overlooking the field of play, that is physical separate from the other seating at the venue",
    },
    BRICK.Hot_Box: {
        SKOS.definition: "hot air chamber forming part of an air handler.",
    },
    BRICK.IDF: {
        SKOS.definition: "An room for an intermediate distribution frame, where cables carrying signals from the main distrubtion frame terminate and then feed out to endpoints",
    },
    BRICK.Information_Area: {
        SKOS.definition: "An information booth or kiosk where visitors would look for information",
    },
    BRICK.Janitor_Room: {
        SKOS.definition: "A room set aside for the storage of cleaning equipment and supplies",
    },
    BRICK.Laboratory: {
        SKOS.definition: "facility acceptable to the local, national, or international recognized authority having jurisdiction and which provides uniform testing and examination procedures and standards for meeting design, manufacturing, and factory testing requirements.",
    },
    BRICK.Library: {
        SKOS.definition: "A place for the storage and/or consumption of physical media, e.g. books, periodicals, and DVDs/CDs",
    },
    BRICK.Loading_Dock: {
        SKOS.definition: "A part of a facility where delivery trucks can load and unload. Usually partially enclosed with specific traffic lanes leading to the dock",
    },
    BRICK.Lobby: {
        SKOS.definition: "A space just after the entrance to a building or other space of a building, where visitors can wait",
    },
    BRICK.Lounge: {
        SKOS.definition: "A room for lesiure activities or relaxing",
    },
    BRICK.MDF: {
        SKOS.definition: "A room for the Main Distribution Frame, the central place of a building where cables carrying signals meet and connect to the outside world",
    },
    BRICK.Mail_Room: {
        SKOS.definition: "A room where mail is recieved and sorted for distribution to the rest of the building",
    },
    BRICK.Majlis: {
        SKOS.definition: "In Arab countries, an Majlis is a private lounge where visitors are recieved and entertained",
    },
    BRICK.Massage_Room: {
        SKOS.definition: "Usually adjunct to an athletic facility, a private/semi-private space where massages are performed",
    },
    BRICK.Mechanical_Room: {
        SKOS.definition: "A class of service rooms where mechanical equipment (HVAC) operates",
    },
    BRICK.Media_Hot_Desk: {
        SKOS.definition: "A non-enclosed space used by members of the media temporarily to cover an event while they are present at a venue",
    },
    BRICK.Media_Production_Room: {
        SKOS.definition: "A enclosed space used by media professionals for the production of media",
    },
    BRICK.Media_Room: {
        SKOS.definition: "A class of spaces related to the creation of media",
    },
    BRICK.Medical_Room: {
        SKOS.definition: "A class of rooms used for medical purposes",
    },
    BRICK.Office: {
        SKOS.definition: "A class of rooms dedicated for work or study",
    },
    BRICK.Office_Kitchen: {
        SKOS.definition: "A common space, usually near or in a breakroom, where minor food preperation occurs",
    },
    BRICK.Open_Office: {
        SKOS.definition: "An open space used for work or study by mulitple people. Usuaully subdivided into cubicles or desks",
    },
    BRICK.Outdoor_Area: {
        SKOS.definition: "A class of spaces that exist outside of a building",
    },
    BRICK.Parking_Level: {
        SKOS.definition: "A floor of a parking structure",
    },
    BRICK.Parking_Space: {
        SKOS.definition: "An area large enough to park an individual vehicle",
    },
    BRICK.Parking_Structure: {
        SKOS.definition: "A building or part of a building devoted to vehicle parking",
    },
    BRICK.Photovoltaic_Array: {
        SKOS.definition: "A collection of photovoltaic panels",
    },
    BRICK.Plumbing_Room: {
        SKOS.definition: "A service room devoted to the operation and routing of water in a building. Usually distinct from the HVAC subsystems.",
    },
    BRICK.Portfolio: {
        SKOS.definition: "A collection of sites",
    },
    BRICK.Prayer_Room: {
        SKOS.definition: "A room set aside for prayer",
    },
    BRICK.Private_Office: {
        SKOS.definition: "An office devoted to a single individual, with walls and door",
    },
    BRICK.Pump_Room: {
        SKOS.definition: "A mechanical room that houses pumps",
    },
    BRICK.Reception: {
        SKOS.definition: "A space, usually in a lobby, where visitors to a building or space can go to after arriving at a building and inform building staff that they have arrived",
    },
    BRICK.Region: {
        SKOS.definition: "A unit of geographic space, usually contigious or somehow related to a geopolitical feature",
    },
    BRICK.Restroom: {
        SKOS.definition: "A room that provides toilets and washbowls.",
    },
    BRICK.Retail_Room: {
        SKOS.definition: "A space set aside for retail in a larger establishment, e.g. a gift shop in a hospital",
    },
    BRICK.Riser: {
        SKOS.definition: "A vertical shaft indented for installing building infrastructure e.g., electrical wire, network communication wire, plumbing, etc",
    },
    BRICK.Room: {
        SKOS.definition: "Base class for all more specific room types.",
    },
    BRICK.Security_Service_Room: {
        SKOS.definition: "A class of spaces used by the security staff of a facility",
    },
    BRICK.Service_Room: {
        SKOS.definition: "A class of spaces related to the operations of building subsystems, e.g. HVAC, electrical, IT, plumbing, etc",
    },
    BRICK.Shared_Office: {
        SKOS.definition: "An office used by multiple people",
    },
    BRICK.Shower: {
        SKOS.definition: "A space containing showers, usually adjacent to an athletic or execise area",
    },
    BRICK.Site: {
        SKOS.definition: "A geographic region containing 0 or more buildings. Typically used as the encapsulating location for a collection of Brick entities through the hasPart/isPartOf relationships",
    },
    BRICK.Space: {
        SKOS.definition: "A part of the physical world or a virtual world whose 3D spatial extent is bounded actually or theoretically, and provides for certain functions within the zone it is contained in.",
    },
    BRICK.Sports_Service_Room: {
        SKOS.definition: "A class of spaces used in the support of sports",
    },
    BRICK.Stage_Riser: {
        SKOS.definition: "A low platform in a space or on a stage",
    },
    BRICK.Staircase: {
        SKOS.definition: "A vertical space containing stairs",
    },
    BRICK.Storage_Room: {
        SKOS.definition: "A class of spaces used for storage",
    },
    BRICK.Studio: {
        SKOS.definition: "A room used for the production or media, usually with either a specialized set or a specialized sound booth for recording",
    },
    BRICK.Switch_Room: {
        SKOS.definition: "A telecommuncations room housing network switches",
    },
    BRICK.TETRA_Room: {
        SKOS.definition: "A room used for local two-way radio networks, e.g. the portable radios carried by facilities staff",
    },
    BRICK.Team_Room: {
        SKOS.definition: "An office used by multiple team members for specific work tasks. Distinct from Conference Room",
    },
    BRICK.Telecom_Room: {
        SKOS.definition: "A class of spaces used to support telecommuncations and IT equipment",
    },
    BRICK.Ticketing_Booth: {
        SKOS.definition: "A room or space used to sell or distribute tickets to events at a venue",
    },
    BRICK.Transformer_Room: {
        SKOS.definition: "An electrical room where electricity enters and is transformed to different voltages and currents by the equipment contained in the room",
    },
    BRICK.Tunnel: {
        SKOS.definition: "An enclosed space that connects buildings. Often underground",
    },
    BRICK.Vertical_Space: {
        SKOS.definition: "A class of spaces used to connect multiple floors or levels..",
    },
    BRICK.Visitor_Lobby: {
        SKOS.definition: "A lobby for visitors to the building. Sometimes used to distinguish from an employee entrance looby",
    },
    BRICK.Wardrobe: {
        SKOS.definition: "Storage for clothing, costumes, or uniforms",
    },
    BRICK.Waste_Storage: {
        SKOS.definition: "A room used for storing waste such as trash or recycling",
    },
    BRICK.Water_Tank: {
        SKOS.definition: "A space used to hold water. This will likely be deprecated in future releases of Brick for the sake of clarity w.r.t. equipment classification of tanks",
    },
    BRICK.Wing: {
        SKOS.definition: "A wing is part of a building – or any feature of a building – that is subordinate to the main, central structure.",
    },
    BRICK.Workshop: {
        SKOS.definition: "A space used to house equipment that can be used to repair or fabricate things",
    },
    BRICK.Zone: {
        SKOS.definition: "(1) a separately controlled heated or cooled space. (2) one occupied space or several occupied spaces with similar occupancy category, occupant density, zone air distribution effectiveness, and zone primary airflow per unit area. (3) space or group of spaces within a building for which the heating, cooling, or lighting requirements are sufficiently similar that desired conditions can be maintained throughout by a single controlling device.",
    },
}
