from rdflib import OWL, RDF, RDFS

from bricksrc.namespaces import BRICK


def test_section2_relationships(brick):
    assert (BRICK.hasParameter, RDF.type, OWL.ObjectProperty) in brick
    assert (BRICK.hasParameter, RDFS.domain, BRICK.Point) in brick
    assert (BRICK.hasParameter, RDFS.range, BRICK.Parameter) in brick

    assert (BRICK.hasTrigger, RDF.type, OWL.ObjectProperty) in brick
    assert (BRICK.hasTrigger, RDFS.domain, BRICK.Point) in brick
    assert (BRICK.hasTrigger, RDFS.range, BRICK.TriggerDirection) in brick


def test_trigger_direction_classes(brick):
    # TriggerDirection is a punned enumeration: each class is an instance of itself
    assert (BRICK.TriggerDirection, RDF.type, OWL.Class) in brick
    assert (BRICK.EnumerationKind, RDFS.subClassOf, BRICK.Entity) in brick
    assert (BRICK.TriggerDirection, RDFS.subClassOf, BRICK.EnumerationKind) in brick
    assert (BRICK.TriggerDirection, RDF.type, BRICK.TriggerDirection) in brick

    # Rising/Falling hierarchy
    for trigger in [
        BRICK["TriggerDirection-Rising"],
        BRICK["TriggerDirection-Falling"],
    ]:
        assert (trigger, RDF.type, OWL.Class) in brick
        assert (trigger, RDFS.subClassOf, BRICK.TriggerDirection) in brick
        assert (trigger, RDF.type, trigger) in brick

    # Cooling/Heating subconcepts
    assert (
        BRICK["TriggerDirection-Cooling"],
        RDFS.subClassOf,
        BRICK["TriggerDirection-Rising"],
    ) in brick
    assert (
        BRICK["TriggerDirection-Heating"],
        RDFS.subClassOf,
        BRICK["TriggerDirection-Falling"],
    ) in brick


def test_new_point_class_parentage(brick):
    assert (BRICK.Threshold, RDFS.subClassOf, BRICK.Setpoint) in brick
    assert (BRICK.Threshold, RDFS.subClassOf, BRICK.Point) not in brick
    assert (BRICK.Alarm_Threshold, RDFS.subClassOf, BRICK.Parameter) in brick

    assert (BRICK.Limit, RDFS.subClassOf, BRICK.Point) in brick
    assert (BRICK.Request, RDFS.subClassOf, BRICK.Point) in brick

    # Deadband and Deadband_Shift are sibling Parameter subclasses
    assert (BRICK.Deadband, RDFS.subClassOf, BRICK.Parameter) in brick
    assert (BRICK.Deadband_Shift, RDFS.subClassOf, BRICK.Parameter) in brick


def test_cooling_heating_setpoints_are_thresholds(brick):
    # Cooling temperature setpoints are Thresholds with Cooling trigger
    assert (
        BRICK.Cooling_Temperature_Setpoint,
        RDFS.subClassOf,
        BRICK.Threshold,
    ) in brick
    assert (
        BRICK.Cooling_Temperature_Setpoint,
        BRICK.hasTrigger,
        BRICK["TriggerDirection-Cooling"],
    ) in brick

    assert (
        BRICK.Cooling_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf,
        BRICK.Threshold,
    ) in brick
    assert (
        BRICK.Cooling_Zone_Air_Temperature_Setpoint,
        BRICK.hasTrigger,
        BRICK["TriggerDirection-Cooling"],
    ) in brick

    # Heating temperature setpoints are Thresholds with Heating trigger
    assert (
        BRICK.Heating_Temperature_Setpoint,
        RDFS.subClassOf,
        BRICK.Threshold,
    ) in brick
    assert (
        BRICK.Heating_Temperature_Setpoint,
        BRICK.hasTrigger,
        BRICK["TriggerDirection-Heating"],
    ) in brick

    assert (
        BRICK.Heating_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf,
        BRICK.Threshold,
    ) in brick
    assert (
        BRICK.Heating_Zone_Air_Temperature_Setpoint,
        BRICK.hasTrigger,
        BRICK["TriggerDirection-Heating"],
    ) in brick


def test_deadband_setpoints_are_not_thresholds(brick):
    # Deadband setpoints represent the size of a deadband, not a threshold
    for cls in [
        BRICK.Occupied_Cooling_Temperature_Deadband_Setpoint,
        BRICK.Occupied_Heating_Temperature_Deadband_Setpoint,
        BRICK.Unoccupied_Cooling_Temperature_Deadband_Setpoint,
        BRICK.Unoccupied_Heating_Temperature_Deadband_Setpoint,
    ]:
        assert (cls, RDFS.subClassOf, BRICK.Threshold) not in brick
