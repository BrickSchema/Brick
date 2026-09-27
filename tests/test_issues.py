import sys

import pyshacl
import pytest
from rdflib import Graph

sys.path.append("..")
# Keeping import pattern consistent with existing tests
from bricksrc.namespaces import BRICK, SH, OWL, A  # noqa: E402


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
    assert (
        res_high.askAnswer
    ), "High_Discharge_Air_Temperature_Alarm should be a subclass of Discharge_Air_Temperature_Alarm"

    # Low_Discharge_Air_Temperature_Alarm should be a subclass of Discharge_Air_Temperature_Alarm
    res_low = g.query(
        """
        ASK {
            brick:Low_Discharge_Air_Temperature_Alarm rdfs:subClassOf brick:Discharge_Air_Temperature_Alarm .
        }
        """
    )
    assert (
        res_low.askAnswer
    ), "Low_Discharge_Air_Temperature_Alarm should be a subclass of Discharge_Air_Temperature_Alarm"


# Points whose brick:hasQuantity must be accepted: Brick quantities and QUDT
# quantity kinds (which deprecated Brick quantities point users to), on
# brick:Point and on subclasses that carry their own shapes
ISSUE_804_EXAMPLES = """
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix : <urn:issue804#> .

:point_qudt_kind a brick:Point ;
    brick:hasQuantity qk:Power .

:point_brick_quantity a brick:Point ;
    brick:hasQuantity brick:Volume .

:point_deprecated_replacement a brick:Point ;
    brick:hasQuantity qk:ElectricEnergy .

:sensor_qudt_kind a brick:Power_Sensor ;
    brick:hasQuantity qk:Power .

:setpoint_qudt_kind a brick:Temperature_Setpoint ;
    brick:hasQuantity qk:Temperature .
"""


@pytest.fixture()
def issue_804_shapes(brick):
    """Every property shape in Brick that constrains brick:hasQuantity, on
    whichever class declares it"""
    shapes = Graph()
    for klass, ps in brick.subject_objects(SH.property):
        if (ps, SH.path, BRICK.hasQuantity) in brick:
            shapes.add((klass, A, SH.NodeShape))
            shapes.add((klass, A, OWL.Class))
            shapes.add((klass, SH.property, ps))
            shapes += brick.cbd(ps)
    return shapes


@pytest.fixture()
def issue_804_data(brick_with_imports):
    data = Graph()
    data += brick_with_imports
    data.parse(data=ISSUE_804_EXAMPLES, format="turtle")
    return data


def test_issue_804(issue_804_shapes, issue_804_data):
    """
    Ensure Brick issue #804 stays fixed: no shape may restrict
    brick:hasQuantity to brick:Quantity alone, which rejected QUDT
    quantity kinds.
    """
    examples = Graph().parse(data=ISSUE_804_EXAMPLES, format="turtle")
    points = set(examples.subjects(BRICK.hasQuantity, None))
    assert points, "no examples found"
    for point in sorted(points):
        conforms, _, report = pyshacl.validate(
            issue_804_data,
            shacl_graph=issue_804_shapes,
            focus_nodes=[point],
            inference="none",
        )
        assert conforms, f"{point} should validate\n{report}"
