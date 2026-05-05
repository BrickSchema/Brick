from collections import defaultdict

BRICK_PREFIX = "https://brickschema.org/schema/Brick#"


def _brick_name(value):
    return value.toPython().replace(BRICK_PREFIX, "")


def _query_class_relations(g, query):
    relations = defaultdict(list)
    for row in g.query(query):
        class_name = _brick_name(row.c)
        if row.p:
            relations[class_name].append(_brick_name(row.p))
    return relations


def _query_class_names(g, query):
    return {_brick_name(row.c) for row in g.query(query)}


def _all_non_deprecated_class_relations(g):
    # This is the shared universe of active Brick class names for the
    # name-pair checks below. The relation values are only needed for the
    # supply/discharge equivalence check.
    return _query_class_relations(
        g,
        """
        SELECT DISTINCT ?c ?p
        WHERE {
            ?c (rdfs:subClassOf | owl:equivalentClass)+ ?p .
            FILTER NOT EXISTS { ?c owl:deprecated true } .
            FILTER NOT EXISTS { ?p owl:deprecated true } .
        }
        """,
    )


def _explicit_equivalent_classes(g):
    # The supply/discharge naming convention is not enough by itself: those
    # class pairs should also be connected with an explicit equivalentClass.
    return _query_class_relations(
        g,
        """
        SELECT DISTINCT ?c ?p
        WHERE {
            ?c (rdfs:subClassOf | owl:equivalentClass)* brick:Class .
            ?c owl:equivalentClass ?p .
            FILTER NOT EXISTS { ?c owl:deprecated true } .
        }
        """,
    )


def _supply_discharge_air_classes(g):
    # Water supply/return terminology is distinct from air supply/discharge.
    # Limit this check to classes tied to the aliased air substances.
    return _query_class_names(
        g,
        """
        SELECT DISTINCT ?c
        WHERE {
            ?c (owl:equivalentClass|^owl:equivalentClass)* ?e .
            ?e brick:hasSubstance ?s .
            FILTER (?s IN (brick:Supply_Air, brick:Discharge_Air)) .
            FILTER NOT EXISTS { ?c owl:deprecated true } .
        }
        """,
    )


def _assert_matching_name_pairs(classes, left, right, *, allowed=None):
    # For every active class containing one side of a conventional name pair,
    # make sure the corresponding class name also exists.
    classes_to_check = set(classes)
    if allowed is not None:
        classes_to_check &= set(allowed)

    missing_right = []
    missing_left = []
    for class_name in classes_to_check:
        if left in class_name:
            counterpart = class_name.replace(left, right)
            if counterpart not in classes:
                missing_right.append((class_name, counterpart))
        if right in class_name:
            counterpart = class_name.replace(right, left)
            if counterpart not in classes:
                missing_left.append((class_name, counterpart))

    assert (
        not missing_left
    ), "Missing {left} counterparts for {right} classes: {missing}".format(
        left=left,
        right=right,
        missing=sorted(missing_left),
    )
    assert (
        not missing_right
    ), "Missing {right} counterparts for {left} classes: {missing}".format(
        left=left,
        right=right,
        missing=sorted(missing_right),
    )


def _assert_supply_discharge_equivalence(classes, equivalent_classes, allowed):
    # Supply/Discharge air class names are aliases, so the ontology should
    # encode that aliasing explicitly instead of only relying on similar names.
    classes_to_check = set(classes) & set(allowed)
    missing_equivalence = {}

    for class_name in classes_to_check:
        if "Discharge" in class_name:
            counterpart = class_name.replace("Discharge", "Supply")
            if counterpart in classes:
                if class_name not in equivalent_classes.get(
                    counterpart, []
                ) and counterpart not in equivalent_classes.get(class_name, []):
                    missing_equivalence[class_name] = counterpart

    assert not missing_equivalence, (
        "Missing Supply/Discharge owl:equivalentClass definitions: "
        f"{missing_equivalence}"
    )


def test_min_max_classes_have_matching_counterparts(brick_with_imports):
    relations = _all_non_deprecated_class_relations(brick_with_imports)
    _assert_matching_name_pairs(relations, "Min", "Max")


def test_occupied_unoccupied_classes_have_matching_counterparts(brick_with_imports):
    relations = _all_non_deprecated_class_relations(brick_with_imports)
    _assert_matching_name_pairs(relations, "Occupied", "Unoccupied")


def test_supply_discharge_air_classes_have_matching_equivalent_counterparts(
    brick_with_imports,
):
    relations = _all_non_deprecated_class_relations(brick_with_imports)
    supply_discharge_air_classes = _supply_discharge_air_classes(brick_with_imports)

    _assert_matching_name_pairs(
        relations,
        "Discharge",
        "Supply",
        allowed=supply_discharge_air_classes,
    )
    _assert_supply_discharge_equivalence(
        relations,
        _explicit_equivalent_classes(brick_with_imports),
        supply_discharge_air_classes,
    )
