import brickschema
from rdflib import Namespace

BLDG = Namespace("urn:bldg#")
ttl_file = """
@prefix : <urn:bldg#> .
@prefix brick: <https://brickschema.org/schema/Brick#> .

:hvac_system    a   brick:HVAC_System .
:air_loop_1 a   brick:Air_Loop ;
    brick:isPartOf  :hvac_system .

:ahu1   a   brick:AHU ;
    brick:feeds     :vav1 ;
    brick:isPartOf :hvac_system, :air_loop_1 .

:vav1   a   brick:VAV ;
    brick:hasPart :dmp1 ;
    brick:hasPoint  :sats1 ;
    brick:feeds     :zone1 ;
    brick:isPartOf :hvac_system, :air_loop_1 .

:zone1  a   brick:HVAC_Zone .
:dmp1 a brick:Damper ;
    brick:hasPoint  :pos1 .
:pos1   a brick:Position_Command .
:sats1   a brick:Supply_Air_Temperature_Sensor .
"""


def test_collections_rules():
    g = brickschema.Graph()
    g.load_file("Brick.ttl")
    g.parse(data=ttl_file, format="turtle")
    g.bind("", BLDG)

    valid, _, report = g.validate()
    assert valid, report

    g.expand("brick")

    valid, _, report = g.validate()
    assert valid, report

    res = set(g.query("SELECT ?x WHERE { ?x brick:isPartOf :hvac_system }"))
    expected = [
        BLDG["air_loop_1"],
        BLDG["ahu1"],
        BLDG["vav1"],
        BLDG["dmp1"],
        BLDG["pos1"],
        BLDG["sats1"],
    ]
    for entity in expected:
        assert (entity,) in res
    assert len(expected) == len(res)

    res = set(g.query("SELECT ?x WHERE { ?x brick:isPartOf :air_loop_1 }"))
    expected = [BLDG["ahu1"], BLDG["vav1"], BLDG["dmp1"], BLDG["pos1"], BLDG["sats1"]]
    for entity in expected:
        assert (entity,) in res
    assert len(expected) == len(res)
