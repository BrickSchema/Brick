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


def test_case_insensitive_property_collision_fails(graph):
    with pytest.raises(
        ValueError, match="Case-insensitive bSDD property-code collision"
    ):
        build_dictionary(graph)


@pytest.mark.parametrize(
    ("code", "children"),
    [
        (
            "aggregate",
            ["aggregate.aggregationFunction", "aggregate.aggregationInterval"],
        ),
        ("coordinates", ["coordinates.latitude", "coordinates.longitude"]),
        (
            "deprecation",
            [
                "deprecation.deprecatedInVersion",
                "deprecation.deprecationMitigationMessage",
                "deprecation.deprecationMitigationRule",
            ],
        ),
        ("lastKnownValue", ["lastKnownValue.timestamp", "lastKnownValue.value"]),
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
