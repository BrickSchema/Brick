import sys

sys.path.append("..")
# Keeping import pattern consistent with existing tests
from bricksrc.namespaces import BRICK  # noqa: E402


def test_issue_719(brick_with_imports):
    """
    Ensure reasoning respects Brick issue #719:
    High/Low Discharge Air Temperature Alarm should be recognized as subclasses
    of Discharge_Air_Temperature_Alarm via equivalence with Supply_Air_Temperature_Alarm.
    """
    g = brick_with_imports

    # High_Discharge_Air_Temperature_Alarm should be a subclass of Discharge_Air_Temperature_Alarm
    res_high = g.query(
            """
        ASK {
            brick:High_Discharge_Air_Temperature_Alarm rdfs:subClassOf brick:Discharge_Air_Temperature_Alarm .
        }
        """
        )
    assert res_high.askAnswer, "High_Discharge_Air_Temperature_Alarm should be a subclass of Discharge_Air_Temperature_Alarm"

    # Low_Discharge_Air_Temperature_Alarm should be a subclass of Discharge_Air_Temperature_Alarm
    res_low = g.query(
            """
        ASK {
            brick:Low_Discharge_Air_Temperature_Alarm rdfs:subClassOf brick:Discharge_Air_Temperature_Alarm .
        }
        """
        )
    assert res_low.askAnswer, "Low_Discharge_Air_Temperature_Alarm should be a subclass of Discharge_Air_Temperature_Alarm"
