import brickschema

from bricksrc.namespaces import BRICK, OWL, RDF, RDFS


def test_lighting_aliases_and_entity_properties(brick):
    assert (
        BRICK.Start_Stop_Counter,
        BRICK.aliasOf,
        BRICK.Power_Cycle_Count_Sensor,
    ) in brick

    assert (BRICK.ratedLuminousFlux, RDF.type, BRICK.EntityProperty) in brick
    assert (
        BRICK.ratedCorrelatedColorTemperature,
        RDF.type,
        BRICK.EntityProperty,
    ) in brick
    assert (BRICK.ratedApparentPower, RDF.type, BRICK.EntityProperty) in brick


def test_lighting_component_classes(brick):
    assert brick.query(
        "ASK { brick:Light_Source rdfs:subClassOf+ brick:Lighting_Equipment }"
    ).askAnswer
    assert brick.query(
        "ASK { brick:Luminaire_Driver rdfs:subClassOf+ brick:Lighting_Equipment }"
    ).askAnswer
    assert (BRICK.expectedLifetime, RDF.type, OWL.DatatypeProperty) in brick


def test_lighting_component_modeling(brick_with_imports):
    data = """
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix : <urn:ex#> .

:luminaire a brick:Luminaire ;
    brick:hasPart :driver, :light_source .

:driver a brick:Luminaire_Driver ;
    brick:expectedLifetime "PT50000H"^^xsd:duration ;
    brick:ratedPowerInput [
        brick:hasUnit unit:W ;
        brick:value "32"^^xsd:decimal
    ] .

:light_source a brick:Light_Source ;
    brick:expectedLifetime "PT25000H"^^xsd:duration ;
    brick:ratedVoltageInput [
        brick:hasUnit unit:V ;
        brick:value "12"^^xsd:decimal
    ] .
"""
    graph = brickschema.Graph().parse(data=data, format="turtle")

    valid, _, report = graph.validate(
        extra_graphs=[brick_with_imports], engine="topquadrant"
    )
    assert valid, report
