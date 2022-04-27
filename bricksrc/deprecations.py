from .namespaces import BRICK

deprecations = {
    BRICK.Supply_Water_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.Entering_Water_Temperature_Sensor,
    },
    BRICK.Discharge_Water_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.Entering_Water_Temperature_Sensor,
    },
    BRICK.Supply_Water_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.Entering_Water_Flow_Sensor,
    },
    BRICK.Discharge_Water_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.Entering_Water_Flow_Sensor,
    },
    BRICK.Chilled_Water_Supply_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.Chilled_Water_Entering_Flow_Sensor,
    },
    BRICK.Chilled_Water_Discharge_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.Chilled_Water_Entering_Flow_Sensor,
    },
    BRICK.Supply_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.Entering_Water,
    },
    BRICK.Supply_Chilled_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.Entering_Chilled_Water,
    },
    BRICK.Discharge_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.Entering_Water,
    },
    BRICK.Discharge_Chilled_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.Entering_Chilled_Water,
    },
    BRICK.Supply_Hot_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.Entering_Hot_Water,
    },
    BRICK.Discharge_Hot_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.Entering_Hot_Water,
    },
    BRICK.Return_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.Leaving_Water,
    },
    BRICK.Return_Hot_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.Leaving_Hot_Water,
    },
    BRICK.Supply_Condenser_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.Entering_Condenser_Water,
    },
    BRICK.Discharge_Condenser_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.Entering_Condenser_Water,
    },
    BRICK.Return_Condenser_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.Leaving_Condenser_Water,
    },
    BRICK.Heat_Exchanger_Supply_Water_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        # "replace_with": BRICK.Leaving_Condenser_Water,
    },
    BRICK.Heat_Exchanger_Discharge_Water_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        # "replace_with": BRICK.Leaving_Condenser_Water,
    },
    BRICK.Hot_Water_Supply_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.Hot_Water_Entering_Temperature_Sensor,
    },
    BRICK.Hot_Water_Discharge_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.Hot_Water_Entering_Temperature_Sensor,
    },
    BRICK.Domestic_Hot_Water_Discharge_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.Domestic_Hot_Water_Entering_Temperature_Sensor,
    },
    BRICK.High_Temperature_Hot_Water_Discharge_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.High_Temperature_Hot_Water_Entering_Temperature_Sensor,
    },
    BRICK.Medium_Temperature_Hot_Water_Discharge_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related poitns",
        "replace_with": BRICK.Medium_Temperature_Hot_Water_Entering_Temperature_Sensor,
    },
}
