"""
Tests for the Point unit / quantity kind / substance compatibility shapes
defined in bricksrc/rules.ttl:

    bsh:PointUnitIsCompatibleWithQuantityKind
    bsh:PointAnnotationMatchesClassAnnotation
"""

import brickschema

prefixes = """
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix qudtqk: <http://qudt.org/vocab/quantitykind/> .
@prefix : <http://example.com/test#> .
"""

# each of these should be accepted by the compatibility shapes
VALID_CASES = {
    # the unit is an applicable unit of the quantity kind of the class
    "airtemp_degc": "a brick:Air_Temperature_Sensor ; brick:hasUnit unit:DEG_C",
    "airtemp_degf": "a brick:Air_Temperature_Sensor ; brick:hasUnit unit:DEG_F",
    "co2_ppm": "a brick:CO2_Sensor ; brick:hasUnit unit:PPM",
    "airflow_m3perhr": "a brick:Air_Flow_Sensor ; brick:hasUnit unit:M3-PER-HR",
    # the class quantity kind (brick:Air_Quality) has no applicable units of its
    # own; unit:PPM is applicable to one of its skos:narrower quantity kinds
    "airquality_ppm": "a brick:Air_Quality_Sensor ; brick:hasUnit unit:PPM",
    # brick:Warm_Cool_Adjust_Sensor overrides the qudtqk:DimensionlessRatio of
    # its parent brick:Adjust_Sensor with brick:Differential_Temperature; only
    # the most specific annotation should be used
    "warmcool_degc": "a brick:Warm_Cool_Adjust_Sensor ; brick:hasUnit unit:DEG_C",
    # brick:Occupancy_Count and qudtqk:Count list count units directly
    "occupancy_count_num": "a brick:Occupancy_Count_Sensor ; brick:hasUnit unit:NUM",
    "power_cycle_count_num": "a brick:Power_Cycle_Count_Sensor ; brick:hasUnit unit:NUM",
    "rh_percent_rh": "a brick:Relative_Humidity_Sensor ; brick:hasUnit unit:PERCENT_RH",
    # instance quantity kind refines/matches the one on the class
    "qk_refines": "a brick:Air_Quality_Sensor ; brick:hasQuantity brick:CO2_Concentration",
    # instance substance refines/matches the one on the class
    "substance_refines": "a brick:Air_Temperature_Sensor ; brick:hasSubstance brick:Outside_Air",
    "substance_equal": "a brick:Outside_Air_Temperature_Sensor ; brick:hasSubstance brick:Outside_Air",
    # brick:Supply_Air owl:sameAs brick:Discharge_Air
    "substance_sameas": "a brick:Supply_Air_Temperature_Sensor ; brick:hasSubstance brick:Discharge_Air",
}

# each of these should be rejected, by the shape named in the value
INVALID_CASES = {
    "airtemp_m3perhr": (
        "a brick:Air_Temperature_Sensor ; brick:hasUnit unit:M3-PER-HR",
        "PointUnitIsCompatibleWithQuantityKind",
    ),
    # unit:PERCENT is dimensionless, temperature is not
    "airtemp_percent": (
        "a brick:Air_Temperature_Sensor ; brick:hasUnit unit:PERCENT",
        "PointUnitIsCompatibleWithQuantityKind",
    ),
    "co2_degc": (
        "a brick:CO2_Sensor ; brick:hasUnit unit:DEG_C",
        "PointUnitIsCompatibleWithQuantityKind",
    ),
    # Same-dimension mismatches: the shape accepts only applicable units, never
    # merely a shared dimension vector. unit:LUX measures illuminance, not
    # luminance; unit:MACH is dimensionless, like unit:PPM, but is no
    # concentration.
    "luminance_in_lux": (
        "a brick:Luminance_Sensor ; brick:hasUnit unit:LUX",
        "PointUnitIsCompatibleWithQuantityKind",
    ),
    "co2_mach": (
        "a brick:CO2_Sensor ; brick:hasUnit unit:MACH",
        "PointUnitIsCompatibleWithQuantityKind",
    ),
    # qudtqk:NonActivePower is only qudt:organizedUnder qudtqk:ElectricPower, so
    # its reactive power units must not apply to an electric power point
    "electric_power_kilovar": (
        "a brick:Electric_Power_Sensor ; brick:hasUnit unit:KiloVAR",
        "PointUnitIsCompatibleWithQuantityKind",
    ),
    "qk_unrelated": (
        "a brick:Air_Temperature_Sensor ; brick:hasQuantity qudtqk:VolumeFlowRate",
        "PointAnnotationMatchesClassAnnotation",
    ),
    # brick:Return_Air is a sibling of brick:Outside_Air, not a specialization
    "substance_sibling": (
        "a brick:Outside_Air_Temperature_Sensor ; brick:hasSubstance brick:Return_Air",
        "PointAnnotationMatchesClassAnnotation",
    ),
    "substance_unrelated": (
        "a brick:Air_Temperature_Sensor ; brick:hasSubstance brick:Chilled_Water",
        "PointAnnotationMatchesClassAnnotation",
    ),
    # Masking canaries. Only the *most specific* class annotation counts; if a
    # parent's broader annotation were allowed to leak through, both of these
    # would wrongly pass. brick:Air_Flow_Deadband_Setpoint declares only
    # qudtqk:VolumeFlowRate while an ancestor contributes a dimensionless kind
    # that would accept unit:PERCENT; brick:Water_Temperature_Sensor declares
    # brick:Water (which subsumes brick:Hot_Water) but
    # brick:Chilled_Water_Temperature_Sensor overrides it with brick:Chilled_Water.
    "masked_parent_quantity": (
        "a brick:Air_Flow_Deadband_Setpoint ; brick:hasUnit unit:PERCENT",
        "PointUnitIsCompatibleWithQuantityKind",
    ),
    # the same for a Sensor: brick:Humidity_Sensor's qudtqk:PressureRatio accepts
    # unit:PERCENT, but brick:Relative_Humidity_Sensor declares
    # qudtqk:RelativeHumidity, whose only applicable unit is unit:PERCENT_RH
    "masked_parent_sensor_quantity": (
        "a brick:Relative_Humidity_Sensor ; brick:hasUnit unit:PERCENT",
        "PointUnitIsCompatibleWithQuantityKind",
    ),
    "masked_parent_substance": (
        "a brick:Chilled_Water_Temperature_Sensor ; brick:hasSubstance brick:Hot_Water",
        "PointAnnotationMatchesClassAnnotation",
    ),
}

SHAPE_NAMES = [
    "PointUnitIsCompatibleWithQuantityKind",
    "PointAnnotationMatchesClassAnnotation",
]


def _validate(brick, body):
    g = brickschema.Graph().parse(data=prefixes + body, format="turtle")
    return g.validate(extra_graphs=[brick], engine="topquadrant")


def _results_for(report, focus):
    """Returns the report blocks mentioning the given focus node"""
    return [
        block
        for block in report.split("--- Result")
        if f"http://example.com/test#{focus}>" in block
        and any(s in block for s in SHAPE_NAMES)
    ]


def test_compatible_units_quantities_and_substances(brick_with_imports):
    data = "\n".join(":%s %s ." % (name, body) for name, body in VALID_CASES.items())
    _, _, report = _validate(brick_with_imports, data)
    for name in VALID_CASES:
        assert not _results_for(
            report, name
        ), "%s should be accepted by the compatibility shapes:\n" % name + "\n".join(
            _results_for(report, name)
        )


def test_incompatible_units_quantities_and_substances(brick_with_imports):
    data = "\n".join(
        ":%s %s ." % (name, body) for name, (body, _) in INVALID_CASES.items()
    )
    conforms, _, report = _validate(brick_with_imports, data)
    assert not conforms, report
    for name, (_, shape) in INVALID_CASES.items():
        blocks = _results_for(report, name)
        assert blocks, "%s should have been flagged by bsh:%s" % (name, shape)
        assert any(
            shape in block for block in blocks
        ), "%s should have been flagged by bsh:%s, got:\n" % (name, shape) + "\n".join(
            blocks
        )


# ---------------------------------------------------------------------------
# The path expressions in the compatibility shapes are deliberately minimal.
# Each simplification below is valid only because of a property of the Brick
# data. These tests assert those properties directly, so that a change to the
# ontology which invalidates one fails loudly here rather than quietly
# weakening the shapes.
# ---------------------------------------------------------------------------


def test_brick_quantity_broader_always_has_inverse_narrower(brick_with_imports):
    """Justifies walking Brick's narrower quantities with skos:narrower alone."""
    missing = list(
        brick_with_imports.query(
            "SELECT ?x ?y WHERE { ?x skos:broader ?y . "
            "?x a brick:Quantity . ?y a brick:Quantity . "
            "FILTER(STRSTARTS(STR(?x), STR(brick:))) "
            "FILTER(STRSTARTS(STR(?y), STR(brick:))) "
            "FILTER NOT EXISTS { ?y skos:narrower ?x } }"
        )
    )
    assert not missing, (
        "Brick quantity skos:broader pairs lacking the inverse narrower: %s"
        % missing[:5]
    )


def test_no_skos_narrower_on_qudt_quantity_kinds(brick_with_imports):
    """
    Justifies walking skos:narrower in the unit shape: it must never enter
    QUDT's hierarchy, whose skos:broader includes the non-commensurable
    qudt:organizedUnder groupings. QUDT kinds are walked only along
    qudt:specializationOf and qudt:exactMatch.
    """
    found = list(
        brick_with_imports.query(
            "SELECT ?x ?y WHERE { ?x skos:narrower ?y . "
            "FILTER(STRSTARTS(STR(?x), 'http://qudt.org/')) }"
        )
    )
    assert not found, "skos:narrower from QUDT quantity kinds: %s" % found[:5]


def test_nothing_reachable_only_via_inverse_narrower(brick_with_imports):
    """Justifies using skos:broader* instead of (skos:broader|^skos:narrower)*."""
    extra = list(
        brick_with_imports.query(
            "SELECT ?x ?y WHERE { ?x skos:narrower ?y . "
            "FILTER NOT EXISTS { ?x skos:broader ?y } "
            "FILTER NOT EXISTS { ?y skos:broader ?x } }"
        )
    )
    assert not extra, "pairs reachable only via ^skos:narrower: %s" % extra[:5]


def test_sameas_is_materialized_symmetrically(brick_with_imports):
    """Justifies dropping ^owl:sameAs from the substance compatibility path."""
    asymmetric = list(
        brick_with_imports.query(
            "SELECT ?x ?y WHERE { ?x owl:sameAs ?y . "
            "FILTER NOT EXISTS { ?y owl:sameAs ?x } }"
        )
    )
    assert not asymmetric, "owl:sameAs pairs lacking the reverse: %s" % asymmetric[:5]


def test_qudt_reference_pairs_share_a_dimension_vector(brick_with_imports):
    """
    Justifies dropping brick:hasQUDTReference from the quantity kind
    compatibility path: the shared-dimension-vector fallback already covers it.
    """
    unshared = list(
        brick_with_imports.query(
            "SELECT ?x ?y WHERE { ?x brick:hasQUDTReference ?y . "
            "FILTER NOT EXISTS { ?x qudt:hasDimensionVector ?d . "
            "?y qudt:hasDimensionVector ?d } }"
        )
    )
    assert not unshared, (
        "brick:hasQUDTReference pairs not sharing a dimension vector: %s" % unshared[:5]
    )


def test_every_point_class_carries_its_effective_annotation(brick_with_imports):
    """
    The shapes read brick:hasQuantity / brick:hasSubstance straight off the
    instance's own rdf:type, with no hierarchy walk. That is only correct
    because generate_brick.py materializes the effective annotation onto every
    Point class (materialize_inherited_class_annotations). If that ever stops
    happening, points typed with the affected classes would silently go
    unchecked, so assert it here.
    """
    for prop in ("brick:hasQuantity", "brick:hasSubstance"):
        missing = list(
            brick_with_imports.query(
                """SELECT ?class WHERE {
                    ?class rdfs:subClassOf* brick:Point .
                    ?ancestor %(prop)s ?value .
                    ?class rdfs:subClassOf+ ?ancestor .
                    FILTER NOT EXISTS { ?class %(prop)s ?own }
                    FILTER NOT EXISTS { ?class owl:deprecated true }
                }"""
                % {"prop": prop}
            )
        )
        assert (
            not missing
        ), "Point classes inheriting %s but not carrying it directly: %s" % (
            prop,
            [str(r[0]).split("#")[-1] for r in missing[:5]],
        )
