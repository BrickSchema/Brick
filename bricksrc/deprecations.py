from .namespaces import BRICK, RDFS, SKOS, A

deprecations = {
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
        "replace_with": BRICK.Cooling_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Zone_Air_Temperature_Setpoint,
    },
    BRICK.Zone_Air_Heating_Temperature_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "'Zone_Air_Heating_Temperature_Setpoint' is deprecated to support new naming convention, whic reorders intended behaviour (heating) before the substance (zone air)",
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
    BRICK.Supply_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Water,
        SKOS.broader: BRICK.Water,
        A: BRICK.Substance,
    },
    BRICK.Supply_Chilled_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water,
        SKOS.broader: BRICK.Chilled_Water,
        A: BRICK.Substance,
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
    BRICK.Supply_Hot_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water,
        SKOS.broader: BRICK.Hot_Water,
        A: BRICK.Substance,
    },
    BRICK.Discharge_Hot_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water,
        SKOS.broader: BRICK.Hot_Water,
        A: BRICK.Substance,
    },
    BRICK.Return_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Water,
        SKOS.broader: BRICK.Water,
        A: BRICK.Substance,
    },
    BRICK.Return_Hot_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Hot_Water,
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
        "replace_with": BRICK.Hot_Water_Leaving_Flow_Sensor,
        RDFS.subClassOf: [BRICK.Hot_Water_Flow_Sensor, BRICK.Supply_Water_Flow_Sensor],
    },
    BRICK.Hot_Water_Discharge_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Hot_Water_Leaving_Flow_Sensor,
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
        "replace_with": BRICK.Hot_Water_Entering_Flow_Sensor,
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
        "replace_with": BRICK.Leaving_Chilled_Water__Flow_Setpoint,
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
        "replace_with": BRICK.Hot_Water_Leaving_Flow_Setpoint,
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
        "replace_with": BRICK.Hot_Water_Entering_Flow_Sensor,
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
        "replace_with": BRICK.Hot_Water_Leaving_Flow_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Supply_Water_Temperature_Sensor,
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
            BRICK.Supply_Water_Temperature_Sensor,
        ],
    },
    BRICK.Discharge_Condenser_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Condenser_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Discharge_Water_Temperature_Sensor,
        ],
    },
    BRICK.Supply_Hot_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Supply_Water_Temperature_Sensor,
        ],
    },
    BRICK.Discharge_Hot_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Discharge_Water_Temperature_Sensor,
        ],
    },
}
