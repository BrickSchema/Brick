from rdflib import Literal, BNode
from rdflib.collection import Collection
from brickschema.graph import Graph
from brickschema.namespaces import BRICK, BSH, A, SH

mappings = {
    "Air_Source_Heat_Pump": {
        "entity_properties": [
            {"property": BRICK.sourceSideResource, "value": BRICK.Air}
        ],
        "dependents": {
            "Air_To_Air_Heat_Pump": {
                "entity_properties": [
                    {"property": BRICK.loadSideResource, "value": BRICK.Air}
                ],
                "dependents": {
                    "Reversible_Air_To_Air_Heat_Pump": {
                        "entity_properties": [
                            {
                                "property": BRICK.reversibleHeatFlow,
                                "value": Literal("true"),
                            }
                        ],
                    },
                    "NonReversible_Air_To_Air_Heat_Pump": {
                        "entity_properties": [
                            {
                                "property": BRICK.reversibleHeatFlow,
                                "value": Literal("false"),
                            }
                        ],
                    },
                },
            },
            "Air_To_Water_Heat_Pump": {
                "entity_properties": [
                    {"property": BRICK.loadSideResource, "value": BRICK.Water}
                ],
                "dependents": {
                    "Reversible_Air_To_Water_Heat_Pump": {
                        "entity_properties": [
                            {
                                "property": BRICK.reversibleHeatFlow,
                                "value": Literal("true"),
                            }
                        ],
                    },
                    "NonReversible_Air_To_Water_Heat_Pump": {
                        "entity_properties": [
                            {
                                "property": BRICK.reversibleHeatFlow,
                                "value": Literal("false"),
                            }
                        ],
                    },
                },
            },
            "Air_To_Refrigerant_Heat_Pump": {
                "entity_properties": [
                    {"property": BRICK.loadSideResource, "value": BRICK.Refrigerant}
                ],
                "dependents": {
                    "Reversible_Air_To_Refrigerant_Heat_Pump": {
                        "entity_properties": [
                            {
                                "property": BRICK.reversibleHeatFlow,
                                "value": Literal("true"),
                            }
                        ],
                        # we leave out Heat_Recovery_Air_To_Refrigerant_Heat_Pump because
                        # it has no extra entity properties that qualify it
                    },
                    "NonReversible_Air_To_Refrigerant_Heat_Pump": {
                        "entity_properties": [
                            {
                                "property": BRICK.reversibleHeatFlow,
                                "value": Literal("false"),
                            }
                        ],
                    },
                },
            },
        },
    },
    "Water_Source_Heat_Pump": {
        "entity_properties": [
            {"property": BRICK.sourceSideResource, "value": BRICK.Water}
        ],
        "dependents": {
            "Water_To_Water_Heat_Pump": {
                "entity_properties": [
                    {"property": BRICK.loadSideResource, "value": BRICK.Water}
                ],
                "dependents": {
                    "Water_Cooled_Chiller": {
                        "entity_properties": [
                            {"property": BRICK.heatFlow, "value": Literal("cool")},
                            {
                                "property": BRICK.reversibleHeatFlow,
                                "value": Literal("false"),
                            },
                        ],
                    },
                },
            },
            "Water_To_Air_Heat_Pump": {
                "entity_properties": [
                    {"property": BRICK.loadSideResource, "value": BRICK.Air}
                ],
                "dependents": {
                    "Reversible_Water_To_Air_Heat_Pump": {
                        "entity_properties": [
                            {
                                "property": BRICK.reversibleHeatFlow,
                                "value": Literal("true"),
                            }
                        ],
                    },
                    "NonReversible_Water_To_Air_Heat_Pump": {
                        "entity_properties": [
                            {
                                "property": BRICK.reversibleHeatFlow,
                                "value": Literal("false"),
                            }
                        ],
                        "dependents": {
                            "Air_Cooled_Chiller": {
                                "entity_properties": [
                                    {
                                        "property": BRICK.heatFlow,
                                        "value": Literal("cool"),
                                    },
                                    {
                                        "property": BRICK.reversibleHeatFlow,
                                        "value": Literal("false"),
                                    },
                                ],
                            },
                        },
                    },
                },
            },
        },
    },
    "Ground_Source_Heat_Pump": {
        "entity_properties": [
            {"property": BRICK.sourceSideResource, "value": BRICK.Ground}
        ],
        "dependents": {
            "Ground_To_Air_Heat_Pump": {
                "entity_properties": [
                    {"property": BRICK.loadSideResource, "value": BRICK.Air}
                ],
                "dependents": {
                    "Reversible_Ground_To_Air_Heat_Pump": {
                        "entity_properties": [
                            {
                                "property": BRICK.reversibleHeatFlow,
                                "value": Literal("true"),
                            }
                        ],
                    },
                    "Nonreversible_Ground_To_Air_Heat_Pump": {
                        "entity_properties": [
                            {
                                "property": BRICK.reversibleHeatFlow,
                                "value": Literal("false"),
                            }
                        ],
                    },
                },
            },
            "Ground_To_Water_Heat_Pump": {
                "entity_properties": [
                    {"property": BRICK.loadSideResource, "value": BRICK.Water}
                ],
            },
        },
    },
}


def define_entity_property_condition(G, name, value):
    """
    Defines a SHACL condition for a Triple rule:
         sh:property [ sh:hasValue {value} ;
                     sh:path ( {name} brick:value ) ]
    Should be used as an object to sh:condition
    """
    condition = BNode()
    proplist_name = BNode()
    proplist = [name, BRICK.value]
    Collection(G, proplist_name, proplist)
    G.add((condition, SH.property, [(SH.path, proplist_name), (SH.hasValue, value)]))
    return condition


def define_entity_property_construct(G, eprops):
    """
    Define the SPARQL CONSTRUCT that adds the entity properties to an instance.
    This query has no WHERE clause because it will be used in a SHACL rule which
    already has a condition
    """
    constructions = []
    for ep in eprops:
        propname = ep["property"]
        value = ep["value"]
        constructions.append(f"$this <{propname}> [ brick:value <{value}> ]")
    construct_clause = " . ".join(constructions)
    return Literal("CONSTRUCT {" + construct_clause + "} WHERE {}")


def define_derive_shape(G, brickclass, definition, required_parent=None):
    """
    Generate the "Drive" shape graph which derives the
    given Brick class if an entity has all of the required
    entity properties
    """
    assert len(brickclass) > 0
    assert len(definition) > 0
    shape = BSH[f"Derive_{brickclass}_Shape"]
    rule = BNode()
    G.add((shape, A, SH.NodeShape))
    # choose a random entity property to act as the "trigger"; because all entity properties
    # are required for the rule to fire, we can choose any one of them as the trigger
    G.add((shape, SH.targetSubjectsOf, definition["entity_properties"][0]["property"]))
    G.add((shape, SH.rule, rule))

    # rely on the parent shape to for transitive dependencies
    if required_parent is not None:
        G.add((rule, SH.condition, required_parent))

    for ep in definition["entity_properties"]:
        condition = define_entity_property_condition(G, ep["property"], ep["value"])
        G.add((rule, SH.condition, condition))

    G.add((rule, A, SH.TripleRule))
    G.add((rule, SH.object, BRICK[brickclass]))
    G.add((rule, SH.predicate, A))
    G.add((rule, SH.subject, SH.this))

    # traverse into dependents
    for subclass, subdef in definition.get("dependents", dict()).items():
        define_derive_shape(G, subclass, subdef, shape)


def define_describe_shape(G, brickclass, definition, _eprops=None):
    """
    Generate the "Describe" shape graph which derives the properties
    given the Brick class
    """
    assert len(brickclass) > 0
    assert len(definition) > 0
    shape = BSH[f"Describe_{brickclass}_Shape"]
    rule = BNode()
    G.add((shape, A, SH.NodeShape))
    G.add((shape, SH.targetClass, BRICK[brickclass]))
    G.add((shape, SH.rule, rule))

    # inherit eprops from parents
    if _eprops is None:
        eprops = []
    else:
        eprops = _eprops[:]
    eprops.extend(definition["entity_properties"])

    G.add((rule, A, SH.SPARQLRule))
    G.add((rule, SH.construct, define_entity_property_construct(G, eprops)))

    # traverse into dependents
    for subclass, subdef in definition.get("dependents", dict()).items():
        define_describe_shape(G, subclass, subdef, eprops)


def generate(G, mappings):
    for brickclass, definition in mappings.items():
        # define the "derive" shape
        define_derive_shape(G, brickclass, definition)
        define_describe_shape(G, brickclass, definition)
        pass


if __name__ == "__main__":
    g = Graph().load_file("../Brick.ttl")
    generate(g, mappings)
    g.serialize("Brick+heat_pump_shapes.ttl", format="ttl")

    g.load_file("data.ttl")
    g.expand("brick")

    print("-" * 10, "brick:Air_Source_Heat_Pump")
    q = "SELECT DISTINCT ?x WHERE { ?x a brick:Air_Source_Heat_Pump }"
    for row in g.query(q):
        print(row)

    print("-" * 10, "brick:Air_To_Air_Heat_Pump")

    q = "SELECT DISTINCT ?x WHERE { ?x a brick:Air_To_Air_Heat_Pump }"
    for row in g.query(q):
        print(row)

    print("-" * 10, "source-side resource is air")

    q = "SELECT DISTINCT ?x WHERE { ?x brick:sourceSideResource/brick:value brick:Air }"
    for row in g.query(q):
        print(row)

    print("-" * 10, "load-side resource is air")

    q = "SELECT DISTINCT ?x WHERE { ?x brick:loadSideResource/brick:value brick:Air }"
    for row in g.query(q):
        print(row)
