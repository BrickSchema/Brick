from .namespaces import BRICK, RDFS

deprecations = {
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
        "replace_with": BRICK.Chilled_Water_Leaving_Flow_Sensor,
        RDFS.subClassOf: [
            BRICK.Discharge_Water_Flow_Sensor,
            BRICK.Chilled_Water_Flow_Sensor,
        ],
    },
    BRICK.Chilled_Water_Supply_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Chilled_Water_Leaving_Flow_Sensor,
        RDFS.subClassOf: [
            BRICK.Supply_Water_Flow_Sensor,
            BRICK.Chilled_Water_Flow_Sensor,
        ],
    },
    BRICK.Chilled_Water_Discharge_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Chilled_Water_Leaving_Flow_Sensor,
        RDFS.subClassOf: [
            BRICK.Discharge_Water_Flow_Sensor,
            BRICK.Chilled_Water_Flow_Sensor,
        ],
    },
    BRICK.Supply_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Water,
        RDFS.subClassOf: BRICK.Water,
    },
    BRICK.Supply_Chilled_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water,
        RDFS.subClassOf: BRICK.Chilled_Water,
    },
    BRICK.Discharge_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Water,
        RDFS.subClassOf: BRICK.Water,
    },
    BRICK.Discharge_Chilled_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water,
        RDFS.subClassOf: BRICK.Chilled_Water,
    },
    BRICK.Supply_Hot_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water,
        RDFS.subClassOf: BRICK.Hot_Water,
    },
    BRICK.Discharge_Hot_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water,
        RDFS.subClassOf: BRICK.Hot_Water,
    },
    BRICK.Return_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Water,
        RDFS.subClassOf: BRICK.Water,
    },
    BRICK.Return_Hot_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Hot_Water,
        RDFS.subClassOf: BRICK.Hot_Water,
    },
    BRICK.Supply_Condenser_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Condenser_Water,
        RDFS.subClassOf: BRICK.Condenser_Water,
    },
    BRICK.Discharge_Condenser_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Condenser_Water,
        RDFS.subClassOf: BRICK.Condenser_Water,
    },
    BRICK.Return_Condenser_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Condenser_Water,
        RDFS.subClassOf: BRICK.Condenser_Water,
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
        "replace_with": BRICK.Chilled_Water_Entering_Flow_Sensor,
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
        "replace_with": BRICK.Chilled_Water_Leaving_Flow_Setpoint,
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
        "replace_with": BRICK.Chilled_Water_Leaving_Flow_Setpoint,
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
        "replace_with": BRICK.Differential_Leaving_Return_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Water_Differential_Temperature_Sensor,
    },
    BRICK.Differential_Discharge_Return_Water_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Differential_Leaving_Return_Water_Temperature_Sensor,
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
        RDFS.subClassOf: BRICK.Condenser_Water,
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
