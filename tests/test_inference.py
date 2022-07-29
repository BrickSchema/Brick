from rdflib import RDF, RDFS, OWL, Namespace, Literal
import pytest
import brickschema
from .util import make_readable
import sys

sys.path.append("..")
from bricksrc.namespaces import BRICK, TAG, A, SKOS  # noqa: E402

BLDG = Namespace("https://brickschema.org/schema/ExampleBuilding#")

g = brickschema.Graph()
g.parse("Brick.ttl", format="turtle")

# Instances
g.add((BLDG.Coil_1, A, BRICK.Heating_Coil))

g.add((BLDG.Coil_2, BRICK.hasTag, TAG.Equipment))
g.add((BLDG.Coil_2, BRICK.hasTag, TAG.Coil))
g.add((BLDG.Coil_2, BRICK.hasTag, TAG.Heat))

g.add((BLDG.AHU1, A, BRICK.AHU))
g.add((BLDG.VAV1, A, BRICK.VAV))
g.add((BLDG.AHU1, BRICK.feedsAir, BLDG.VAV1))
g.add((BLDG.CH1, A, BRICK.Chiller))

g.add((BLDG.TS1, A, BRICK.Air_Temperature_Sensor))

# add air flow sensor
g.add((BLDG.AFS1, BRICK.hasTag, TAG.Point))
g.add((BLDG.AFS1, BRICK.hasTag, TAG.Air))
g.add((BLDG.AFS1, BRICK.hasTag, TAG.Flow))
g.add((BLDG.AFS1, BRICK.hasTag, TAG.Sensor))

g.add((BLDG.S1, BRICK.hasTag, TAG.Point))
g.add((BLDG.S1, BRICK.hasTag, TAG.Sensor))

# add air flow setpoint
# g.add((BLDG.AFSP1, A, BRICK.Setpoint))
g.add((BLDG.AFSP1, BRICK.hasTag, TAG.Point))
g.add((BLDG.AFSP1, BRICK.hasTag, TAG.Air))
g.add((BLDG.AFSP1, BRICK.hasTag, TAG.Flow))
g.add((BLDG.AFSP1, BRICK.hasTag, TAG.Setpoint))

# add air flow setpoint limit
g.add((BLDG.MAFS1, BRICK.hasTag, TAG.Point))
g.add((BLDG.MAFS1, BRICK.hasTag, TAG.Max))
g.add((BLDG.MAFS1, BRICK.hasTag, TAG.Air))
g.add((BLDG.MAFS1, BRICK.hasTag, TAG.Flow))
g.add((BLDG.MAFS1, BRICK.hasTag, TAG.Setpoint))
g.add((BLDG.MAFS1, BRICK.hasTag, TAG.Limit))
g.add((BLDG.MAFS1, BRICK.hasTag, TAG.Parameter))

g.add((BLDG.AFS2, A, BRICK.Air_Flow_Sensor))

g.add((BLDG.co2s1, A, BRICK.CO2_Level_Sensor))

g.add((BLDG.standalone, A, BRICK.Temperature_Sensor))


@pytest.mark.slow
def test_tag_inference():

    # Apply reasoner
    g.load_file("extensions/brick_extension_shacl_tag_inference.ttl")
    g.expand(profile="shacl+shacl+shacl")

    g.bind("rdf", RDF)
    g.bind("owl", OWL)
    g.bind("rdfs", RDFS)
    g.bind("skos", SKOS)
    g.bind("brick", BRICK)
    g.bind("tag", TAG)
    g.bind("bldg", BLDG)

    print("expanded:", len(g))

    res1 = make_readable(
        g.query(
            "SELECT DISTINCT ?co2tag WHERE {\
                                   bldg:co2s1 brick:hasTag ?co2tag\
                                  }"
        )
    )
    res1 = [x[0] for x in res1]
    assert set(res1) == {"CO2", "Level", "Sensor", "Point", "Air", "Quality"}

    # test_sensors_measure_co2
    res2 = make_readable(
        g.query(
            "SELECT DISTINCT ?sensor WHERE {\
                    ?sensor rdf:type/brick:hasQuantity brick:CO2_Concentration\
                                  }"
        )
    )
    assert len(res2) == 1

    # test_sensors_measure_air
    res3 = make_readable(
        g.query(
            "SELECT DISTINCT ?sensor WHERE {\
                    ?sensor rdf:type/brick:hasSubstance brick:Air\
                                  }"
        )
    )
    assert len(res3) == 5

    # test_sensors_measure_air_temp
    # sensors that measure air temperature
    res4 = make_readable(
        g.query(
            "SELECT DISTINCT ?sensor WHERE {\
                ?sensor rdf:type ?type .\
                ?type brick:hasSubstance brick:Air .\
                ?type rdfs:subClassOf* brick:Temperature_Sensor\
          }"
        )
    )
    assert len(res4) == 1

    # air flow sensors
    res = make_readable(
        g.query(
            "SELECT DISTINCT ?sensor WHERE {\
                                    ?sensor rdf:type brick:Air_Flow_Sensor\
                                 }"
        )
    )
    assert len(res) == 2

    # air flow setpoints
    res = make_readable(
        g.query(
            "SELECT DISTINCT ?sp WHERE {\
                                    ?sp rdf:type brick:Air_Flow_Setpoint\
                                 }"
        )
    )
    assert len(res) == 1

    # setpoints
    res = make_readable(
        g.query(
            "SELECT DISTINCT ?sp WHERE {\
                    ?sp rdf:type/rdfs:subClassOf* brick:Setpoint\
                                 }"
        )
    )
    assert len(res) == 1

    # air flow setpoints
    res = make_readable(
        g.query(
            "SELECT DISTINCT ?sp WHERE {\
                                    ?sp rdf:type brick:Max_Air_Flow_Setpoint_Limit\
                                 }"
        )
    )
    assert len(res) == 1

    # air flow sensors
    res = make_readable(
        g.query(
            "SELECT DISTINCT ?sensor WHERE {\
                                    ?sensor brick:hasTag tag:Air .\
                                    ?sensor brick:hasTag tag:Sensor .\
                                    ?sensor brick:hasTag tag:Flow\
                                 }"
        )
    )
    assert len(res) == 2


def test_owl_inverse():
    g = brickschema.Graph()
    g.parse("Brick.ttl", format="turtle")
    g.add((BLDG.vav1, BRICK.hasPoint, BLDG.AFS2))
    g.add((BLDG.vav1, A, BRICK.VAV))
    g.add((BLDG.AFS2, A, BRICK.Air_Flow_Sensor))
    g.expand("shacl")

    res = make_readable(g.query("SELECT ?x ?y WHERE { ?x brick:hasPoint ?y }"))
    assert len(res) == 1

    res = make_readable(g.query("SELECT ?x ?y WHERE { ?x brick:isPointOf ?y }"))
    assert len(res) == 1


def test_shacl_owl_equivalentclass():
    g = brickschema.Graph()
    g.load_file("Brick.ttl")
    g.add((BLDG.VAV1, A, BRICK.VAV))
    g.add((BLDG.VAV2, A, BRICK.Variable_Air_Volume_Box))
    g.serialize("/tmp/x.ttl", format="turtle")
    g.expand("shacl")
    g.serialize("/tmp/y.ttl", format="turtle")
    res = g.query("SELECT ?vav WHERE { ?vav rdf:type brick:VAV }")
    assert len(list(res)) == 2, "VAV should be equivalent to Variable_Air_Volume_Box"

    res = g.query("SELECT ?vav WHERE { ?vav rdf:type brick:Variable_Air_Volume_Box }")
    assert len(list(res)) == 2, "VAV should be equivalent to Variable_Air_Volume_Box"


def test_meter_inference():
    g = brickschema.Graph()
    g.load_file("Brick.ttl")
    g.add((BLDG.abcdef, A, BRICK.Electrical_Meter))
    g.add((BLDG.abcdef, BRICK.meters, BLDG.bldg))
    g.add((BLDG.bldg, A, BRICK.Building))
    g.expand("shacl")
    assert (BLDG.abcdef, A, BRICK.Building_Electrical_Meter) in g


def test_virtual_meter():
    g = brickschema.Graph()
    g.load_file("Brick.ttl")
    g.add((BLDG.abcdef, A, BRICK.Electrical_Meter))
    g.add((BLDG.abcdef, BRICK.isVirtualMeter, [(BRICK.value, Literal(True))]))
    valid, _, report = g.validate()
    assert valid, report

    g = brickschema.Graph()
    g.load_file("Brick.ttl")
    g.add((BLDG.abcdef, A, BRICK.Building))
    g.add((BLDG.abcdef, BRICK.isVirtualMeter, [(BRICK.value, Literal(True))]))
    valid, _, report = g.validate()
    assert not valid, "Virtual meter should not be allowed on a building"

    g = brickschema.Graph()
    g.load_file("Brick.ttl")
    g.add((BLDG.abcdef, A, BRICK.Building))
    g.add((BLDG.abcdef, BRICK.isVirtualMeter, [(BRICK.value, Literal(False))]))
    valid, _, report = g.validate()
    assert valid, report
