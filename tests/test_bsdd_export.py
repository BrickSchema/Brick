"""
Validates the bSDD import file produced by tools/bsdd/generate_bsdd.py.

bSDD only reports import errors by email, up to 15 minutes after an upload,
so every rule that can be checked locally is checked here instead. The codes
in parentheses refer to items in the bSDD verification checklist:
https://github.com/buildingSMART/bSDD/blob/master/Documentation/bSDD%20verification%20procedure.md
"""

import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(REPO_ROOT))
sys.path.append(str(REPO_ROOT / "tools" / "bsdd"))

from rdflib import URIRef  # noqa: E402
from rdflib.namespace import DCTERMS  # noqa: E402

from generate_bsdd import (  # noqa: E402
    ILLEGAL_CODE_CHARS,
    MAX_CODE_LENGTH,
    VERSIONED_NAMESPACE,
    build_dictionary,
    dimension_vector,
    load_graph,
    load_ifc_reference,
    load_unit_map,
    new_report,
    parse_args,
    validate_code,
)

SOURCE = REPO_ROOT / "Brick+imports.ttl"

# Fields the bSDD import model accepts, from Model/Import Model/bsdd-import-model.json.
DICTIONARY_FIELDS = {
    "ModelVersion",
    "OrganizationCode",
    "DictionaryCode",
    "DictionaryName",
    "DictionaryVersion",
    "LanguageIsoCode",
    "LanguageOnly",
    "UseOwnUri",
    "DictionaryUri",
    "License",
    "LicenseUrl",
    "ChangeRequestEmailAddress",
    "MoreInfoUrl",
    "QualityAssuranceProcedure",
    "QualityAssuranceProcedureUrl",
    "ReleaseDate",
    "Status",
    "Classes",
    "Properties",
}
CLASS_FIELDS = {
    "Code",
    "Name",
    "ClassType",
    "Definition",
    "Description",
    "ParentClassCode",
    "RelatedIfcEntityNamesList",
    "Synonyms",
    "ActivationDateUtc",
    "ReferenceCode",
    "CountriesOfUse",
    "CountryOfOrigin",
    "CreatorLanguageIsoCode",
    "DeActivationDateUtc",
    "DeprecationExplanation",
    "DocumentReference",
    "OwnedUri",
    "ReplacedObjectCodes",
    "ReplacingObjectCodes",
    "RevisionDateUtc",
    "RevisionNumber",
    "Status",
    "SubdivisionsOfUse",
    "Uid",
    "VersionDateUtc",
    "VersionNumber",
    "VisualRepresentationUri",
    "ClassProperties",
    "ClassRelations",
}
PROPERTY_FIELDS = {
    "Code",
    "Name",
    "Definition",
    "Description",
    "DataType",
    "Units",
    "Example",
    "ActivationDateUtc",
    "ConnectedPropertyCodes",
    "CountriesOfUse",
    "CountryOfOrigin",
    "CreatorLanguageIsoCode",
    "DeActivationDateUtc",
    "DeprecationExplanation",
    "Dimension",
    "DimensionLength",
    "DimensionMass",
    "DimensionTime",
    "DimensionElectricCurrent",
    "DimensionThermodynamicTemperature",
    "DimensionAmountOfSubstance",
    "DimensionLuminousIntensity",
    "DocumentReference",
    "DynamicParameterPropertyCodes",
    "IsDynamic",
    "MaxExclusive",
    "MaxInclusive",
    "MinExclusive",
    "MinInclusive",
    "MethodOfMeasurement",
    "OwnedUri",
    "Pattern",
    "PhysicalQuantity",
    "PropertyValueKind",
    "ReplacedObjectCodes",
    "ReplacingObjectCodes",
    "RevisionDateUtc",
    "RevisionNumber",
    "Status",
    "SubdivisionsOfUse",
    "TextFormat",
    "Uid",
    "VersionDateUtc",
    "VersionNumber",
    "VisualRepresentationUri",
    "PropertyRelations",
    "AllowedValues",
}
CLASS_PROPERTY_FIELDS = {
    "Code",
    "PropertyCode",
    "PropertyUri",
    "Description",
    "PropertySet",
    "Unit",
    "PredefinedValue",
    "IsRequired",
    "IsWritable",
    "MaxExclusive",
    "MaxInclusive",
    "MinExclusive",
    "MinInclusive",
    "Pattern",
    "OwnedUri",
    "PropertyType",
    "SortNumber",
    "Symbol",
    "AllowedValues",
}
CLASS_RELATION_FIELDS = {
    "RelationType",
    "RelatedClassUri",
    "RelatedClassName",
    "Fraction",
    "OwnedUri",
}

VALID_CLASS_TYPES = {"Class", "Material", "GroupOfProperties", "AlternativeUse"}
VALID_DATATYPES = {"Boolean", "Character", "Integer", "Real", "String", "Time"}
VALID_VALUE_KINDS = {"Single", "Range", "List", "Complex", "ComplexList"}
VALID_RELATION_TYPES = {
    "HasMaterial",
    "HasReference",
    "IsEqualTo",
    "IsSimilarTo",
    "IsParentOf",
    "IsChildOf",
    "HasPart",
    "IsPartOf",
}


@pytest.fixture(scope="module")
def graph():
    if not SOURCE.exists():
        pytest.skip(f"{SOURCE.name} not built, run `make Brick.ttl` first")
    return load_graph(SOURCE)


@pytest.fixture(scope="module")
def dictionary(graph):
    return build_dictionary(graph, parse_args([]), new_report())


@pytest.fixture(scope="module")
def class_codes(dictionary):
    return {entry["Code"] for entry in dictionary["Classes"]}


@pytest.fixture(scope="module")
def property_codes(dictionary):
    return {entry["Code"] for entry in dictionary["Properties"]}


def test_dictionary_required_fields(dictionary):
    """GEN-01: required at dictionary level, plus the extras verification wants."""
    for field in (
        "OrganizationCode",
        "DictionaryCode",
        "DictionaryName",
        "DictionaryVersion",
        "LanguageIsoCode",
        "QualityAssuranceProcedure",
        "ChangeRequestEmailAddress",
        "License",
        "LicenseUrl",
    ):
        assert dictionary.get(field), f"dictionary is missing {field}"

    assert dictionary["Classes"], "dictionary has no classes"
    assert dictionary["Properties"], "dictionary has no properties"


def test_dictionary_uploads_as_preview(dictionary):
    """Activation is irreversible, so generated files must never claim Active."""
    assert dictionary["Status"] == "Preview"


def test_release_date_comes_from_brick_metadata(dictionary, graph):
    brick_ontology = URIRef(VERSIONED_NAMESPACE)
    modified = [str(value) for value in graph.objects(brick_ontology, DCTERMS.modified)]
    assert modified
    assert dictionary["ReleaseDate"] == modified[0]


def test_own_uris_are_declared(dictionary):
    """UseOwnUri requires DictionaryUri and an OwnedUri on every concept."""
    assert dictionary["UseOwnUri"] is True
    assert dictionary["DictionaryUri"]
    for entry in dictionary["Classes"]:
        assert entry.get("OwnedUri"), f"{entry['Code']} has no OwnedUri"
    for entry in dictionary["Properties"]:
        assert entry.get("OwnedUri"), f"{entry['Code']} has no OwnedUri"

    for collection in ("Classes", "Properties"):
        for entry in dictionary[collection]:
            assert entry["OwnedUri"].startswith(
                dictionary["DictionaryUri"]
            ), f"{entry['Code']} OwnedUri falls outside DictionaryUri"

    owned_uris = [
        entry["OwnedUri"]
        for collection in ("Classes", "Properties")
        for entry in dictionary[collection]
    ]
    assert len(owned_uris) == len(set(owned_uris)), "OwnedUri values must be unique"


def test_known_fields_only(dictionary):
    """Unknown keys are rejected on import, so catch typos here."""
    assert set(dictionary) <= DICTIONARY_FIELDS

    for entry in dictionary["Classes"]:
        assert set(entry) <= CLASS_FIELDS, entry["Code"]
        for class_property in entry.get("ClassProperties", []):
            assert set(class_property) <= CLASS_PROPERTY_FIELDS, entry["Code"]
        for relation in entry.get("ClassRelations", []):
            assert set(relation) <= CLASS_RELATION_FIELDS, entry["Code"]

    for entry in dictionary["Properties"]:
        assert set(entry) <= PROPERTY_FIELDS, entry["Code"]


def test_codes_are_valid(dictionary):
    """Code format rules, and CLS-05/PRP-03 reserved prefixes."""
    for collection in ("Classes", "Properties"):
        for entry in dictionary[collection]:
            code = entry["Code"]
            assert code, f"empty code in {collection}"
            assert len(code) <= MAX_CODE_LENGTH, code
            assert not set(code) & ILLEGAL_CODE_CHARS, code
            assert code[:3].lower() != "ifc", f"{code} uses the reserved Ifc prefix"


def test_codes_are_unique(dictionary):
    """Codes identify terms within a dictionary and are not case-sensitive."""
    for collection in ("Classes", "Properties"):
        codes = [entry["Code"].lower() for entry in dictionary[collection]]
        duplicates = {code for code in codes if codes.count(code) > 1}
        assert not duplicates, f"duplicate {collection} codes: {sorted(duplicates)}"


def test_classes_have_required_fields(dictionary):
    for entry in dictionary["Classes"]:
        assert entry.get("Name"), f"{entry['Code']} has no Name"
        assert entry.get("ClassType") in VALID_CLASS_TYPES, entry["Code"]


def test_parent_class_codes_resolve(dictionary, class_codes):
    """ParentClassCode must exist in the delivered data."""
    for entry in dictionary["Classes"]:
        parent = entry.get("ParentClassCode")
        if parent is not None:
            assert parent in class_codes, f"{entry['Code']} -> missing parent {parent}"


def test_replacing_object_codes_resolve(dictionary, class_codes):
    for entry in dictionary["Classes"]:
        for code in entry.get("ReplacingObjectCodes", []):
            assert code in class_codes, f"{entry['Code']} -> missing {code}"


def test_class_hierarchy_is_acyclic(dictionary):
    """CLS-02, REL-01: ParentClassCode must form a tree, not a cycle."""
    parents = {
        entry["Code"]: entry.get("ParentClassCode") for entry in dictionary["Classes"]
    }
    for code in parents:
        seen = set()
        current = code
        while current is not None:
            assert current not in seen, f"cycle in hierarchy through {code}"
            seen.add(current)
            current = parents.get(current)


def test_no_material_semantics(dictionary):
    """
    A Brick substance is what an entity observes, not what it is made of --
    brick:Substance is rdfs:subClassOf sosa:FeatureOfInterest. Material and
    HasMaterial both mean composition, which Brick never states, so neither
    may appear. Guards the substance mapping against regression.
    """
    for entry in dictionary["Classes"]:
        assert entry["ClassType"] != "Material", f"{entry['Code']} typed as Material"
        for relation in entry.get("ClassRelations", []):
            assert relation["RelationType"] != "HasMaterial", entry["Code"]


def test_class_relations_are_valid(dictionary):
    for entry in dictionary["Classes"]:
        for relation in entry.get("ClassRelations", []):
            assert relation["RelationType"] in VALID_RELATION_TYPES, entry["Code"]
            assert relation.get("RelatedClassUri"), entry["Code"]


def test_class_properties_resolve(dictionary, property_codes):
    """CPR-01/CPR-02: properties must exist, and carry a property set name."""
    for entry in dictionary["Classes"]:
        for class_property in entry.get("ClassProperties", []):
            code = class_property.get("PropertyCode")
            assert code in property_codes, f"{entry['Code']} -> missing {code}"
            property_set = class_property.get("PropertySet")
            assert property_set, f"{entry['Code']}.{code} has no PropertySet"
            assert not property_set.lower().startswith(
                "pset_"
            ), f"{property_set} uses the reserved Pset_ prefix"


def test_properties_have_required_fields(dictionary):
    """GEN-01 and PRP-04."""
    for entry in dictionary["Properties"]:
        assert entry.get("Name"), f"{entry['Code']} has no Name"
        assert entry.get("DataType") in VALID_DATATYPES, entry["Code"]
        kind = entry.get("PropertyValueKind")
        assert kind is None or kind in VALID_VALUE_KINDS, entry["Code"]


def test_numeric_properties_declare_a_dimension(dictionary):
    """PRP-01: every numeric property needs a Dimension, dimensionless ones
    included -- those state '0 0 0 0 0 0 0' rather than leaving it blank."""
    missing = [
        entry["Code"]
        for entry in dictionary["Properties"]
        if entry["DataType"] in ("Integer", "Real") and not entry.get("Dimension")
    ]
    assert missing == [], missing


def test_dimensions_are_well_formed(dictionary):
    """Seven space-separated exponents: length, mass, time, current,
    temperature, amount of substance, luminous intensity."""
    for entry in dictionary["Properties"]:
        dimension = entry.get("Dimension")
        if dimension is None:
            continue
        parts = dimension.split(" ")
        assert len(parts) == 7, f"{entry['Code']}: {dimension}"
        for part in parts:
            float(part)


def test_units_agree_with_dimension(dictionary, graph):
    """
    PRP-01: every unit on a property must match that property's dimension.

    Checked against QUDT rather than trusting the generator: each bSDD unit
    code is mapped back to its QUDT unit, whose own dimension vector must
    convert to the Dimension the property declares.
    """
    reverse_units = {code: iri for iri, code in load_unit_map().items()}

    for entry in dictionary["Properties"]:
        dimension = entry.get("Dimension")
        if not dimension or not entry.get("Units"):
            continue
        for unit_code in entry["Units"]:
            iri = reverse_units.get(unit_code)
            if iri is None:
                continue
            actual = dimension_vector(graph, URIRef(iri))
            assert actual == dimension, (
                f"{entry['Code']} declares {dimension} but unit {unit_code} "
                f"({iri}) is {actual}"
            )


def test_allowed_values_are_well_formed(dictionary):
    """AllowedValue requires Code and Value; PRP-06 forbids them on booleans."""
    for entry in dictionary["Properties"]:
        values = entry.get("AllowedValues", [])
        if values:
            assert entry["DataType"] != "Boolean", entry["Code"]
        codes = [value["Code"].lower() for value in values]
        assert len(codes) == len(set(codes)), f"duplicate values in {entry['Code']}"
        for value in values:
            assert value.get("Code"), entry["Code"]
            assert value.get("Value"), entry["Code"]
            assert (
                validate_code(value["Code"]) is None
            ), f"{entry['Code']} has invalid value code {value['Code']}"


def test_substance_property_is_enumerated(dictionary, property_codes):
    """
    Substances become the values of one property rather than classes: they are
    instances of brick:Substance organised by skos:broader, not a class tree.
    """
    assert "Substance" in property_codes
    substance = next(p for p in dictionary["Properties"] if p["Code"] == "Substance")
    assert substance["DataType"] == "String"
    assert len(substance["AllowedValues"]) > 50

    allowed = {value["Code"] for value in substance["AllowedValues"]}
    predefined = [
        class_property["PredefinedValue"]
        for entry in dictionary["Classes"]
        for class_property in entry.get("ClassProperties", [])
        if class_property.get("PropertyCode") == "Substance"
    ]
    assert predefined, "no class carries a substance"
    assert set(predefined) <= allowed, "substance values outside the allowed list"


def test_only_brick_terms_are_published(dictionary):
    """
    The dictionary publishes Brick's own namespace and nothing else. Brick
    imports its location classes from RealEstateCore, but UseOwnUri would force
    them under Brick identifiers, which is republishing another vocabulary's
    content. Nothing imported may leak in through a URI or a relation.
    """
    for entry in dictionary["Classes"]:
        assert entry["OwnedUri"].startswith(
            dictionary["DictionaryUri"] + "#"
        ), f"{entry['Code']} is published under a foreign URI"
        for relation in entry.get("ClassRelations", []):
            assert "w3id.org/rec" not in relation.get(
                "RelatedClassUri", ""
            ), f"{entry['Code']} relates to a RealEstateCore term"


def test_no_rec_location_terms(class_codes):
    """The location subtree is RealEstateCore's to publish, not Brick's."""
    for code in ("Room", "Space", "Level", "Site", "AdmittingRoom"):
        assert code not in class_codes, f"RealEstateCore term {code} was published"


def test_collection_subclasses_survive_as_roots(dictionary):
    """
    System, Loop and the other rec:Collection subclasses lose their parent when
    REC is excluded. They must still be published, as roots -- dropping them
    would take Brick's own classes out with the import.
    """
    entries = {entry["Code"]: entry for entry in dictionary["Classes"]}
    for code in ("System", "Loop", "PV_Array", "Point_Collection"):
        assert code in entries, f"{code} was dropped with the REC hierarchy"
        assert (
            "ParentClassCode" not in entries[code]
        ), f"{code} unexpectedly has a parent"


def test_deprecated_terms_are_excluded_by_default(class_codes):
    """brick:Location and its subtree are deprecated as of Brick 1.5."""
    assert "Location" not in class_codes


def test_known_term_round_trips(dictionary):
    """A representative sensor should carry its quantity and its substance."""
    entry = next(
        c for c in dictionary["Classes"] if c["Code"] == "Air_Temperature_Sensor"
    )
    assert entry["ParentClassCode"] == "Temperature_Sensor"
    assert entry["Definition"]
    assert entry["OwnedUri"].endswith("#Air_Temperature_Sensor")

    linked = {
        class_property["PropertyCode"]: class_property
        for class_property in entry["ClassProperties"]
    }
    assert "Temperature" in linked
    assert linked["Substance"]["PredefinedValue"] == "Air"


def test_ifc_entities_are_inherited_by_subclasses(dictionary):
    """
    mappings/ifc.csv curates `Fan -> IfcFan`; every Brick fan is an IfcFan, so
    the subclasses carry it too (CLS-01). Without this the file would name an
    entity for 30 classes and leave 1,370 empty.
    """
    entities = {
        c["Code"]: c.get("RelatedIfcEntityNamesList") for c in dictionary["Classes"]
    }
    for code in ("Fan", "Supply_Fan", "Cooling_Tower_Fan"):
        assert entities[code] == ["IfcFan"], code
    assert entities["Air_Temperature_Sensor"] == ["IfcSensor"]


def test_ifc_entities_follow_equivalent_classes(dictionary):
    """
    Brick's abbreviations are owl:equivalentClass of the spelled-out term but
    sit under a generic parent, so subclass inheritance alone never reaches
    them.
    """
    entities = {
        c["Code"]: c.get("RelatedIfcEntityNamesList") for c in dictionary["Classes"]
    }
    assert entities["AHU"] == entities["Air_Handling_Unit"] == ["IfcUnitaryEquipment"]
    assert entities["HX"] == entities["Heat_Exchanger"] == ["IfcHeatExchanger"]
    assert entities["VAV"] == ["IfcAirTerminalBox"]


def test_curated_ifc_entity_overrides_the_inherited_one(dictionary):
    """A subclass with its own row keeps it, rather than taking its parent's."""
    entities = {
        c["Code"]: c.get("RelatedIfcEntityNamesList") for c in dictionary["Classes"]
    }
    assert entities["Heat_Exchanger"] == ["IfcHeatExchanger"]
    assert entities["Coil"] == ["IfcCoil"]  # Coil is a Heat_Exchanger in Brick
    assert entities["Heating_Coil"] == ["IfcCoil"]


def test_points_inherit_no_ifc_entity(dictionary):
    """
    IFC models physical products, not telemetry. Sensors are the exception --
    IfcSensor is a real device -- but setpoints and commands must stay empty
    rather than borrow an entity from anywhere.
    """
    entities = {
        c["Code"]: c.get("RelatedIfcEntityNamesList") for c in dictionary["Classes"]
    }
    for code in ("Point", "Setpoint", "Command", "Parameter"):
        assert not entities.get(code), code


def test_ifc_entity_names_exist_in_ifc_4_3(dictionary):
    """
    Every name must be one bSDD's own IFC dictionary carries, or it will not
    resolve once Brick is published alongside it.
    """
    known = {row["code"] for row in load_ifc_reference()}
    assert known, "reference/ifc-4.3-classes.csv is missing"
    for entry in dictionary["Classes"]:
        for name in entry.get("RelatedIfcEntityNamesList", []):
            assert name in known, f"{entry['Code']} -> unknown IFC entity {name}"


def test_output_is_json_serialisable(dictionary):
    """The deliverable is a single JSON file; nothing may leak rdflib types."""
    json.dumps(dictionary)
