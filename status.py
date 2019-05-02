from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.collection import Collection
from rdflib.extras.infixowl import Restriction

BRICK = Namespace("https://brickschema.org/schema/1.0.3/Brick#")
TAG = Namespace("https://brickschema.org/schema/1.0.3/BrickTag#")
BLDG = Namespace("https://brickschema.org/schema/1.0.3/ExampleBuilding#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
A = RDF.type

status_definitions = {
    "Status": {
        "tagvalues": [
            [BRICK.hasTag, TAG.Status]
        ],
        "subclasses": {
            "Direction_Status": {
                "subclasses": {
                    "Motor_Direction_Status": {},
                    "Run_Direction_Status": {},
                },
            },
            "Disable_Status": {},
            "Drive_Ready_Status": {},
            "Emergency_Air_Flow_Status": {},
            "Emergency_Generator_Status": {},
            "Emergency_Power_Off_Status": {
                "subclasses": {
                    "Emergency_Power_Off_Activated_By_High_Temperature_Status": {},
                    "Emergency_Power_Off_Activated_By_Leak_Detection_System_Status": {},
                    "Emergency_Power_Off_Enable_Status": {},
                    "Emergency_Power_Off_System_Enable_Status": {},
                },
            },
            "Emergency_Push_Button_Status": {},
            "Enable_Status": {
                "subclasses": {
                    "Heat_Exchanger_System_Enable_Status": {},
                    "Run_Enable_Status": {},
                },
            },
            "Even_Month_Status": {},
            "Fan_Status": {},
            "Fault_Indicator_Status": {},
            "Fault_Status": {
                "subclasses": {
                    "Humidifier_Fault_Status": {},
                },
            },
            "Filter_Status": {
                "subclasses": {
                    "Pre_Filter_Status": {},
                },
            },
            "Freeze_Status": {},
            "Hand_Auto_Status": {},
            "Hold_Status": {},
            "Last_Fault_Code_Status": {},
            "Load_Shed_Status": {
                "subclasses": {
                    "Differential_Pressure_Load_Shed_Status": {
                        "subclasses": {
                            "Chilled_Water_Differential_Pressure_Load_Shed_Reset_Status": {},
                            "Chilled_Water_Differential_Pressure_Load_Shed_Status": {},
                            "Hot_Water_Differential_Pressure_Load_Shed_Reset_Status": {},
                            "Hot_Water_Differential_Pressure_Load_Shed_Status": {},
                            "Hot_Water_Discharge_Temperature_Load_Shed_Status": {},
                            "Hot_Water_Supply_Temperature_Load_Shed_Status": {},
                        },
                    },
                },
            },
            "Manual_Auto_Status": {},
            "Mode_Status": {
                "subclasses": {
                    "Occupied_Mode_Status": {},
                    "System_Mode_Status": {},
                    "Operating_Mode_Status": {
                        "subclasses": {
                            "Vent_Operating_Mode_Status": {},
                        },
                    },
                },
            },
            "Occupancy_Status": {
                "subclasses": {
                    "Temporary_Occupancy_Status": {},
                },
            },
            "Off_Status": {},
            "On_Status": {},
            "On_Off_Status": {
                "subclasses": {
                    "Cooling_On_Off_Status": {},
                    "Dehumidification_On_Off_Status": {},
                    "EconCycle_On_Off_Status": {},
                    "Heating_On_Off_Status": {},
                    "Humidification_On_Off_Status": {},
                    "Locally_On_Off_Status": {},
                    "Remotely_On_Off_Status": {},
                    "Standby_Glycool_Unit_On_Off_Status": {},
                    "Standby_Unit_On_Off_Status": {},
                },
            },
            "Overridden_Status": {
                "subclasses": {
                    "Overridden_Off_Status": {},
                    "Overridden_On_Status": {},
                },
            },
            "Pressure_Status": {
                "subclasses": {
                    "Discharge_Air_Duct_Pressure_Status": {},
                    "Supply_Air_Duct_Pressure_Status": {},
                },
            },
            "Lead_Lag_Status": {},
            "Stages_Status": {},
            "Start_Stop_Status": {
                "subclasses": {
                    "Fan_Start_Stop_Status": {},
                    "Motor_Start_Stop_Status": {},
                    "Pump_Start_Stop_Status": {},
                    "Run_Status": {},
                },
            },
            "System_Shutdown_Status": {},
            "System_Status": {},
            "Turn_Off_Status": {},
            "Speed_Status": {},
        },
    },
}

