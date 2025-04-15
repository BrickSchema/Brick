"""
Generates tests automatically
"""
import pytest
from rdflib import Namespace
import ontoenv
from ontoenv import OntoEnv, Config
import brickschema
import glob
import sys

sys.path.append("..")
from bricksrc.namespaces import QUDT, RDF, RDFS, BRICK  # noqa: E402
from bricksrc.namespaces import TAG, SKOS, A, OWL  # noqa: E402


def pytest_generate_tests(metafunc):
    """
    Generates Brick tests for a variety of contexts
    """

    # validates that example files pass validation
    if "filename" in metafunc.fixturenames:
        # example_files_1 = glob.glob("examples/*.ttl")
        example_files = glob.glob("examples/*/*.ttl")
        # example_files = set(example_files_1 + example_files_2)
        metafunc.parametrize("filename", example_files)


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "slow: mark tests as slow (deselect w/ '-m \"not slow\"')"
    )

@pytest.fixture()
def brick():
    g = brickschema.Graph()
    g.load_file("Brick.ttl")
    g.bind("qudt", QUDT)
    g.bind("rdf", RDF)
    g.bind("rdfs", RDFS)
    g.bind("brick", BRICK)
    g.remove((None, OWL.imports, None))
    return g

@pytest.fixture()
def brick_with_imports():
    cfg = Config(["Brick.ttl", "support/", "extensions/", "rec/Source/SHACL/RealEstateCore"], strict=False, offline=True, temporary=True)
    env = OntoEnv(cfg)
    g = brickschema.Graph()
    g.load_file("Brick.ttl")
    g.bind("qudt", QUDT)
    g.bind("rdf", RDF)
    g.bind("rdfs", RDFS)
    g.bind("brick", BRICK)
    env.import_dependencies(g)
    # remove all imports
    g.remove((None, OWL.imports, None))
    return g


@pytest.fixture()
def simple_brick_model():
    BLDG = Namespace("https://brickschema.org/schema/ExampleBuilding#")

    g = brickschema.Graph()
    g.load_file("Brick.ttl")
    g.bind("rdf", RDF)
    g.bind("owl", OWL)
    g.bind("rdfs", RDFS)
    g.bind("skos", SKOS)
    g.bind("brick", BRICK)
    g.bind("tag", TAG)
    g.bind("bldg", BLDG)

    # Create instances
    g.add((BLDG.Coil_1, A, BRICK.Heating_Coil))
    g.add((BLDG.AHU1, A, BRICK.Air_Handler_Unit))
    g.add((BLDG.VAV1, A, BRICK.Variable_Air_Volume_Box))
    g.add((BLDG.CH1, A, BRICK.Chiller))

    # locations
    g.add((BLDG.Zone1, A, BRICK.HVAC_Zone))
    g.add((BLDG.Room1, A, BRICK.Room))
    g.add((BLDG.Room2, A, BRICK.Room))

    # points
    g.add((BLDG.TS1, A, BRICK.Air_Temperature_Sensor))
    g.add((BLDG.TS2, A, BRICK.Air_Temperature_Sensor))
    g.add((BLDG.AFS1, A, BRICK.Air_Flow_Sensor))
    g.add((BLDG.co2s1, A, BRICK.CO2_Level_Sensor))

    g.add((BLDG.AFSP1, A, BRICK.Air_Flow_Setpoint))

    g.add((BLDG.MAFS1, A, BRICK.Max_Air_Flow_Setpoint_Limit))

    # establishing some relationships
    g.add((BLDG.CH1, BRICK.feeds, BLDG.AHU1))
    g.add((BLDG.AHU1, BRICK.feeds, BLDG.VAV1))
    g.add((BLDG.VAV1, BRICK.hasPoint, BLDG.TS2))
    g.add((BLDG.VAV1, BRICK.hasPoint, BLDG.AFS1))
    g.add((BLDG.VAV1, BRICK.hasPoint, BLDG.AFSP1))

    g.add((BLDG.VAV1, BRICK.feeds, BLDG.Zone1))
    g.add((BLDG.Zone1, BRICK.hasPart, BLDG.Room1))
    g.add((BLDG.Zone1, BRICK.hasPart, BLDG.Room2))

    g.add((BLDG.TS1, BRICK.hasLocation, BLDG.Room1))

    # lets us use both relationships
    g.expand(profile="shacl")
    return g
