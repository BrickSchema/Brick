from brickschema.inference import TagInferenceSession, \
    HaystackInferenceSession, RDFSInferenceSession, OWLRLInferenceSession, \
    InverseEdgeInferenceSession, ManualBrickInferenceSession
from brickschema.namespaces import RDF, RDFS, BRICK, TAG
from rdflib import Namespace
import json
import pkgutil
import pytest


def test_lookup_tagset():
    session = TagInferenceSession(approximate=False)
    assert session is not None

    tagsets = session.lookup_tagset(['AHU', 'Equipment'])
    assert tagsets[0][0] == set(['AHU'])

    tagsets = session.lookup_tagset(['Air', 'Flow', 'Sensor'])
    assert tagsets[0][0] == set(['Air_Flow_Sensor'])

    tagsets = session.lookup_tagset(['Air', 'Flow', 'Sensor', 'Equipment'])
    assert len(tagsets) == 0

    tagsets = session.lookup_tagset(['Air', 'Flow', 'Setpoint'])
    assert tagsets[0][0] == set(['Air_Flow_Setpoint'])

    tagsets = session.lookup_tagset(['Air', 'Flow', 'Setpoint', 'Limit',
                                     'Parameter'])
    assert tagsets[0][0] == set(['Air_Flow_Setpoint_Limit'])

    tagsets = session.lookup_tagset(['Max', 'Air', 'Flow', 'Setpoint',
                                     'Limit', 'Parameter'])
    assert tagsets[0][0] == set(['Max_Air_Flow_Setpoint_Limit'])


def test_most_likely_tagsets():
    session = TagInferenceSession(approximate=True)
    assert session is not None

    tagset1 = ['AHU', 'Equipment']
    inferred, leftover = session.most_likely_tagsets(tagset1)
    assert inferred == ['AHU']
    assert len(leftover) == 0

    tagset2 = ['Air', 'Flow', 'Sensor']
    inferred, leftover = session.most_likely_tagsets(tagset2)
    assert inferred == ['Air_Flow_Sensor']
    assert len(leftover) == 0

    tagset3 = ['Air', 'Flow', 'Sensor', 'Equipment']
    inferred, leftover = session.most_likely_tagsets(tagset3)
    assert inferred == ['Air_Flow_Sensor']
    assert len(leftover) == 1

    tagset4 = ['Air', 'Flow', 'Setpoint']
    inferred, leftover = session.most_likely_tagsets(tagset4, num=1)
    assert inferred == ['Air_Flow_Setpoint']
    assert len(leftover) == 0

    tagset5 = ['Air', 'Flow', 'Setpoint', 'Limit']
    inferred, leftover = session.most_likely_tagsets(tagset5, num=1)
    assert inferred == ['Air_Flow_Setpoint_Limit']
    assert len(leftover) == 0

    tagset6 = ['Max', 'Air', 'Flow', 'Setpoint', 'Limit']
    inferred, leftover = session.most_likely_tagsets(tagset6, num=1)
    assert inferred == ['Max_Air_Flow_Setpoint_Limit']
    assert len(leftover) == 0


def test_haystack_inference():
    session = HaystackInferenceSession("http://example.org/carytown")
    assert session is not None
    data = pkgutil.get_data(__name__, "data/carytown.json").decode()
    raw_model = json.loads(data)
    brick_model = session.infer_model(raw_model)
    points = brick_model.query("""SELECT ?p WHERE {
        ?p rdf:type/rdfs:subClassOf* brick:Point
    }""")
    assert len(points) == 17

    equips = brick_model.query("""SELECT ?e WHERE {
        ?e rdf:type/rdfs:subClassOf* brick:Equipment
    }""")
    assert len(equips) == 2


def test_rdfs_inference_subclass():
    session = RDFSInferenceSession()
    assert session is not None

    EX = Namespace("http://example.com/building#")
    graph = [
        (EX["a"], RDF.type, BRICK.Temperature_Sensor)
    ]
    expanded_graph = session.expand(graph)

    res1 = expanded_graph.query(f"""SELECT ?type WHERE {{
        <{EX["a"]}> rdf:type ?type
    }}""")

    expected = [
        BRICK.Point,
        BRICK.Class,
        BRICK.Sensor,
        RDFS.Resource,
        BRICK.Temperature_Sensor,
    ]

    assert len(res1) == len(expected), f"Results were {res1}"
    for expected_class in expected:
        assert (expected_class, ) in res1,\
            f"{expected_class} not found in {res1}"


@pytest.mark.slow
def test_owl_inference_tags():
    session = OWLRLInferenceSession()
    assert session is not None

    EX = Namespace("http://example.com/building#")
    graph = [
        (EX["a"], BRICK.hasTag, TAG.Air),
        (EX["a"], BRICK.hasTag, TAG.Flow),
        (EX["a"], BRICK.hasTag, TAG.Setpoint)
    ]
    expanded_graph = session.expand(graph)

    res1 = expanded_graph.query(f"""SELECT ?type WHERE {{
        <{EX["a"]}> rdf:type ?type
    }}""")

    expected = [
        BRICK.Point,
        BRICK.Class,
        BRICK.Setpoint,
        RDFS.Resource,
        BRICK.Air_Flow_Setpoint,
    ]

    assert len(res1) == len(expected), f"Results were {res1}"
    for expected_class in expected:
        assert (expected_class, ) in res1,\
            f"{expected_class} not found in {res1}"


def test_inverse_edge_inference():
    session = InverseEdgeInferenceSession()
    assert session is not None

    EX = Namespace("http://example.com/building#")
    graph = [
        (EX["vav1"], RDF.type, BRICK.VAV),
        (EX["ahu1"], RDF.type, BRICK.AHU),
        (EX["ahu1"], BRICK.feeds, EX["vav1"]),
    ]
    expanded_graph = session.expand(graph)

    res1 = expanded_graph.query(f"""SELECT ?a ?b WHERE {{
        ?a brick:isFedBy ?b
    }}""")
    expected = [
        (EX["vav1"], EX["ahu1"])
    ]

    assert len(res1) == len(expected), f"Results were {res1}"
    for expected_row in expected:
        assert expected_row in res1,\
            f"{expected_row} not found in {res1}"


def test_manual_brick_inference_tags():
    session = ManualBrickInferenceSession()
    assert session is not None

    EX = Namespace("http://example.com/building#")
    graph = [
        (EX["a"], BRICK.hasTag, TAG.Air),
        (EX["a"], BRICK.hasTag, TAG.Flow),
        (EX["a"], BRICK.hasTag, TAG.Setpoint)
    ]
    expanded_graph = session.expand(graph)

    res1 = expanded_graph.query(f"""SELECT ?type WHERE {{
        <{EX["a"]}> rdf:type ?type
    }}""")

    expected = [
        BRICK.Setpoint,
        BRICK.Flow_Setpoint,
        BRICK.Air_Flow_Setpoint,
    ]

    assert len(res1) == len(expected), f"Results were {res1}"
    for expected_class in expected:
        assert (expected_class, ) in res1,\
            f"{expected_class} not found in {res1}"
