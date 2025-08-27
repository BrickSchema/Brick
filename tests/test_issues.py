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
    g.expand("shacl", backend="topquadrant")

    # High_Discharge_Air_Temperature_Alarm should be a subclass of Discharge_Air_Temperature_Alarm
    res_high = list(
        g.query(
            """
        SELECT ?x WHERE {
            brick:High_Discharge_Air_Temperature_Alarm rdfs:subClassOf brick:Discharge_Air_Temperature_Alarm .
            BIND(true AS ?x)
        }
        """
        )
    )
    assert (
        len(res_high) >= 1
    ), "High_Discharge_Air_Temperature_Alarm should be a subclass of Discharge_Air_Temperature_Alarm"

    # Low_Discharge_Air_Temperature_Alarm should be a subclass of Discharge_Air_Temperature_Alarm
    res_low = list(
        g.query(
            """
        SELECT ?x WHERE {
            brick:Low_Discharge_Air_Temperature_Alarm rdfs:subClassOf brick:Discharge_Air_Temperature_Alarm .
            BIND(true AS ?x)
        }
        """
        )
    )
    assert (
        len(res_low) >= 1
    ), "Low_Discharge_Air_Temperature_Alarm should be a subclass of Discharge_Air_Temperature_Alarm"
