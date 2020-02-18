"""
"""
from bricksrc.namespaces import TAG, A, OWL, BRICK
from bricksrc.setpoint import setpoint_definitions
from bricksrc.sensor import sensor_definitions
from bricksrc.alarm import alarm_definitions
from bricksrc.status import status_definitions
from bricksrc.command import command_definitions
from bricksrc.parameter import parameter_definitions

base_tags = set(["Alarm", "Sensor", "Status", "Command", "Setpoint", "Parameter"])


def get_hierarchy_tags(definitions, tag):
    """
    Returns the set of tags used in a given class and in all of its
    subclasses. Uses the dictionary-based definitions
    """
    tags = _get_hierarchy_tags(definitions[tag], set())
    return tags.difference(base_tags.difference(tag))


def _get_hierarchy_tags(defns, tags):
    for tag in defns.get("tags", []):
        tags.add(tag)
    for subclass, sc_defn in defns.get("subclasses", {}).items():
        _get_hierarchy_tags(sc_defn, tags)
    return tags


alarm_tags = get_hierarchy_tags(alarm_definitions, "Alarm")
sensor_tags = get_hierarchy_tags(sensor_definitions, "Sensor")
status_tags = get_hierarchy_tags(status_definitions, "Status")
command_tags = get_hierarchy_tags(command_definitions, "Command")
setpoint_tags = get_hierarchy_tags(setpoint_definitions, "Setpoint")
parameter_tags = get_hierarchy_tags(parameter_definitions, "Parameter")


def make_exclusive_tag_groups(G):
    G.add((TAG.Alarm_Tag, A, OWL.Class))
    G.add((TAG.Status_Tag, A, OWL.Class))
    G.add((TAG.Command_Tag, A, OWL.Class))
    G.add((TAG.Setpoint_Tag, A, OWL.Class))
    G.add((TAG.Parameter_Tag, A, OWL.Class))
    G.add((TAG.Sensor_Tag, A, OWL.Class))

    for tag in alarm_tags:
        G.add((tag, A, TAG.Alarm_Tag))
    for tag in sensor_tags:
        G.add((tag, A, TAG.Sensor_Tag))
    for tag in status_tags:
        G.add((tag, A, TAG.Status_Tag))
    for tag in command_tags:
        G.add((tag, A, TAG.Command_Tag))
    for tag in setpoint_tags:
        G.add((tag, A, TAG.Setpoint_Tag))
    for tag in parameter_tags:
        G.add((tag, A, TAG.Parameter_Tag))
