"""Focused invariants for the direct Brick-to-bSDD mapping."""

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.extend((str(REPO_ROOT), str(REPO_ROOT / "tools" / "bsdd")))

from generate_bsdd import (
    export_entity_properties,
    load_graph,
    load_unit_map,
    build_dictionary,
)  # noqa: E402

SOURCE = REPO_ROOT / "Brick+imports.ttl"


@pytest.fixture(scope="module")
def graph():
    if not SOURCE.exists():
        pytest.skip("run `make Brick.ttl` first")
    return load_graph(SOURCE)


def test_entity_properties_are_namespaced_from_quantity_kinds(graph):
    properties = {entry["Code"] for entry in build_dictionary(graph)["Properties"]}
    assert "Volume" in properties
    assert "entityPropertyVolume" in properties
    assert "volume" not in properties


def test_ifc_mappings_are_taken_directly_from_the_static_csv(graph):
    classes = {entry["Code"]: entry for entry in build_dictionary(graph)["Classes"]}
    assert classes["Chiller"]["RelatedIfcEntityNamesList"] == ["IfcChiller"]
    assert "RelatedIfcEntityNamesList" not in classes["Supply_Fan"]


@pytest.mark.parametrize(
    ("code", "children"),
    [
        (
            "entityPropertyAggregate",
            [
                "entityPropertyAggregate.aggregationFunction",
                "entityPropertyAggregate.aggregationInterval",
            ],
        ),
        (
            "entityPropertyCoordinates",
            [
                "entityPropertyCoordinates.latitude",
                "entityPropertyCoordinates.longitude",
            ],
        ),
        (
            "entityPropertyDeprecation",
            [
                "entityPropertyDeprecation.deprecatedInVersion",
                "entityPropertyDeprecation.deprecationMitigationMessage",
                "entityPropertyDeprecation.deprecationMitigationRule",
            ],
        ),
        (
            "entityPropertyLastKnownValue",
            [
                "entityPropertyLastKnownValue.timestamp",
                "entityPropertyLastKnownValue.value",
            ],
        ),
    ],
)
def test_complex_entity_properties_have_namespaced_scalar_children(
    graph, code, children
):
    properties = {
        entry["Code"]: entry
        for entry in export_entity_properties(graph, load_unit_map())
    }
    complex_property = properties[code]
    assert complex_property["PropertyValueKind"] == "Complex"
    assert complex_property["ConnectedPropertyCodes"] == children
    assert all(properties[child]["PropertyValueKind"] == "Single" for child in children)
