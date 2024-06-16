"""
Tests all example files. See tests/conftest.py for the fixture that generates each of the individual test cases
"""
import ontoenv

env = ontoenv.OntoEnv(read_only=True)


def test_example_file_with_reasoning(brick_with_imports, filename):
    g = brick_with_imports
    g.load_file(filename)
    env.import_dependencies(g)
    g.expand("shacl", backend="topquadrant")

    valid, _, report = g.validate(engine="topquadrant")
    assert valid, report


# specific unit test for the 'evse.ttl' example file
def test_evse_example_file_with_reasoning(brick_with_imports):
    g = brick_with_imports
    g.load_file("examples/evse/evse.ttl")
    env.import_dependencies(g)
    g.expand("shacl", backend="topquadrant")

    # test that all Electric_Vehicle_Charging_Ports in the model
    # have a brick:electricVehicleChargerDirectionality property
    q = """
    SELECT ?evcp WHERE {
        ?evcp a/rdfs:subClassOf* brick:Electric_Vehicle_Charging_Port .
        FILTER NOT EXISTS {
            ?evcp brick:electricVehicleChargerDirectionality ?dir .
        }
    }"""
    res = list(g.query(q))
    assert len(res) == 0, "All EVCPs must have a directionality property"
