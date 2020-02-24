# Brick

[![Build Status](https://travis-ci.org/BrickSchema/Brick.svg?branch=master)](https://travis-ci.org/BrickSchema/Brick)

Brick is an open-source, BSD-licensed development effort to create a uniform schema for representing metadata in buildings. Brick has three components:

* An RDF class hierarchy describing the various building subsystems and the entities and equipment therein
* A minimal, principled set of relationships for connecting these entities together into a directed graph representing a building
* A method of encapsulation for composing complex components from a set of lower-level ones

The official Brick website, [http://brickschema.org/](http://brickschema.org/), contains documentation and other information about the Brick schema.

This repository tracks the main schema development of Brick.

## Discussion

Discussion takes place primarily on the Brick User Form: [https://groups.google.com/forum/#!forum/brickschema](https://groups.google.com/forum/#!forum/brickschema)

## Questions and Issues

If you have an issue with Brick's coverage, utility or usability, or any other Brick-related question:

1. First check the [Brick user form](https://groups.google.com/forum/#!forum/brickschema) and the [Brick issue tracker](https://github.com/BuildSysUniformMetadata/Brick/issues)
   to check if anyone has asked your question already.
2. If you find a previously submitted issue that closely mirrors your own, feel free to jump in on the conversation. Otherwise, please file a new issue or submit a new thread on the forum.

## Examples

The `examples/` directory contains executable code samples with extensive documentation that introduce Brick concepts and idioms.

- `simple_example_1.py`: getting familiar with RDFlib, namespaces, Brick models and when and when not to import the Brick ontology definition

## How To Contribute

See [CONTRIBUTING.md](https://github.com/BrickSchema/Brick/blob/master/CONTRIBUTING.md)

## Tests

Tests go in the `tests/` directory and should be implemented using [pytest](https://pytest.readthedocs.io/en/latest/getting-started.html#getstarted).
[`tests/test_inference.py`](https://github.com/BrickSchema/Brick/blob/master/tests/test_inference.py) is a good example.

Run tests by executing `pytest` in the top-level directory of this repository.

## Ontology Implementation

### Complexity

Almost everything we are using falls under [OWL Lite](https://www.w3.org/TR/owl-ref/#Sublanguage-def) with the exception of the `owl:hasValue` property which we use to define a 1-1 mapping between sets of tags and names of classes.
Because of this, the current solution falls under [OWL DL](https://www.w3.org/TR/owl-ref/#hasValue-def).

This also means that we need a reasoner, but thankfully not one that supports OWL Full :).
[OWL-RL](https://owl-rl.readthedocs.io/en/latest/owlrl.html) is a nice choice that works with [RDFlib](https://github.com/RDFLib/rdflib).


```python
# G is our RDFlib Graph

# apply reasoning to expand all of the inferred triples
import owlrl
owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(G)

# get namespaces
print(list(G.namespaces()))

G.query("SELECT ?x WHERE { ?x brick:hasTag tag:Equipment }")
```

We can serialize the expanded form of the graph to disk if we need to use a SPARQL query processor that does not support reasoning.

### Classes

- The Brick class namespace is `https://brickschema.org/schema/1.1/Brick#`
- Classes belong to `owl:Class` and are arranged into a hierarchy with `rdfs:subClassOf`
- Equivalent classes (the members of the classes are the same) are related with the `owl:equivalentClass` property
- Definitions given with `skos:definition`
- We are eliminating equipment-flavored classes where it makes sense
    - e.g. `brick:AHU_Average_Exhaust_Air_Static_Pressure_Sensor` is just a `Average_Exhaust_Air_Static_Pressure_Sensor` that is a point of an AHU.
- Classes are equivalent to a set of tags (see below)

The root classes we have defined are:

- `Equipment`
- `Location`
- `Point`
- `Tag`
- `Measurable` (containing the `Substance` and `Quantity` classes)

### Relationships

(Relationships are the Brick term for owl ObjectProperties between instances of classes)

At the surface level, relationship work the same as they did in the original Brick.
All the same relationships still exist (where I remembered to define them), and they have their
inverses defined using `owl:inverseOf`.

Domains and ranges are defined in terms of classes. Stating that the `rdfs:range` of a relationship
is of class `brick:Equipment` means that the object of the relationship should be an instance of the
`brick:Equipment` class.

This prototype includes sub-relationships in addition to relationships.
Sub-relationships can be used in place of the super-relationship to add more detail to the nature of that relationship.
The only example so far is `feedsAir` being a subproperty of `feeds`.

Something to figure out is how we could infer the `feedsAir` relationship; maybe if the two endpoint equipment have the `air` tag and a `feeds` relationship?
This may be something that needs to be explicitly specified rather than inferred.

### Tags

Brick is a "concept-first" ontology, which means that it focuses on modeling the definition and behavior of concepts (equipment, points, locations, and so on) and the relationships between them. This stands in contrast to efforts like Project Haystack, which use combinations of tags (short, atomic words and phrases) to hint at concepts. To facilitate the use of Brick's formal model over existing tag-based models and the use of tag-based "annotations", the Brick v1.1 release includes a mapping between Brick's classes and a set of tags.

Like all entities in Brick, tags are URIs with a consistent prefix (namespace); in the case of tags, the namespace is `https://brickschema.org/schema/1.1/BrickTag#`, commonly abbreviated as `tag:`. Examples of tags are `tag:Air`, `tag:Temperature` and `tag:Sensor`. Many of the Brick tags are drawn from Haystack.

The equivalency of a class to a set of tags is accomplished by modeling a Brick class (e.g. `Air_Temperature_Sensor`) a subclass of an anonymous class which is the intersection of entities that have the required tags. If we instantiate a class directly, an OWL reasoner will infer the correct tags for that entity.

Here is the Brick "class-to-tag" mapping definition for the `Temperature_Sensor` class:

```
# in turtle format
brick:Temperature_Sensor a owl:Class ;
    rdfs:subClassOf brick:Sensor ;
    rdfs:subClassOf [ owl:intersectionOf (
                            [ a owl:Restriction ;
                                owl:hasValue tag:Sensor ;
                                owl:onProperty brick:hasTag
                            ]
                            [ a owl:Restriction ;
                                owl:hasValue tag:Temperature ;
                                owl:onProperty brick:hasTag
                            ]
                            [ a owl:Restriction ;
                                owl:hasValue tag:Point ;
                                owl:onProperty brick:hasTag
                            ]
                        ) ] .
```


The first `owl:Restriction` is the set of all classes that have `tag:Sensor` as the value for one of their `brick:hasTag` properties.
Through a reasoning process, all instances of `brick:Temperature_Sensor` will inherit the tag annotations.
```
# input Brick model has an instance of brick:Temperature_Sensor
:ts1   a   brick:Temperature_Sensor

# the reasoner infers these tags and adds them to the model
:ts1    brick:hasTag    tag:Temp
:ts1    brick:hasTag    tag:Sensor
:ts1    brick:hasTag    tag:Point
```


To perform the inference of a class from a set of tags (the inverse of the process above), use the `TagInferenceSession` from the `brickschema` package (this cannot currently be performed by an OWL reasoner)

For a sample entity modeled with tags:

```turtle
# myfile.ttl
@prefix brick: <https://brickschema.org/schema/1.1.0/Brick#> .
@prefix tag: <https://brickschema.org/schema/1.1.0/BrickTag#> .
@prefix bldg: <https://example.org/example#> .

bldg:my_entity  brick:hasTag    tag:Air, tag:Flow, tag:Setpoint, tag:Point .
```

Load the graph into a `brickschema.Graph` and run the TagInferenceSession:

```python
import brickschema
g = brickschema.graph.Graph()
g.load_file("myfile.ttl")
g = brickschema.inference.TagInferenceSession(approximate=False).expand(g)

print(g.query("SELECT ?type WHERE { bldg:my_entity a ?type }"))
# => ['Brick:Air_Flow_Setpoint']
```

### Substances

Brick now defines a hierarchy of substances (`bricksrc/substances.py`) and a hierarchy of quantities (`bricksrc/quantities.py`).
Substances and quantities can be related to equipment and points.

Not all of this is implemented. In the current prototype, sensors are related to substances and quantities
through the `brick:measures` relationship.

```
:ts1    a       brick:Temperature_Sensor
:ts1    brick:measures      :Air

# this implies the following
:ts1    a       brick:Air_Temperature_Sensor
```

We can further subclass substances to provide system- or process-level context to their definitions:

```
:ts1    a       brick:Sensor
:ts1    brick:measures      brick:Return_Air
:ts1    brick:measures      brick:Temperature

# implies...

:ts1    a       brick:Return_Air_Temperature_Sensor
```

Brick uses OWL restrictions to refine classes based on such relationships.
For this example, because `:ts1` measures Air (specifically the `brick:Air` class), OWL infers our sensor as a `brick:Air_Temperature_Sensor`.

Here's what that the definition looks like in turtle:

```
brick:Air_Temperature_Sensor a owl:Class ;
    rdfs:subClassOf brick:Temperature_Sensor ;
    owl:equivalentClass [ owl:intersectionOf ( [ a owl:Restriction ;
                        owl:hasValue brick:Temperature ;
                        owl:onProperty brick:measures ] [ a owl:Restriction ;
                        owl:hasValue brick:Air ;
                        owl:onProperty brick:measures ] ) ] .
```

**Note**: we are using classes as values here, which is different than the rest of Brick. This is called ["punning"](https://www.w3.org/2007/OWL/wiki/Punning#Using_Classes_as_Property_Values). This is to avoid having to create instances of substances for our sensors to measure and so on, but reserves the possibility to implement this in the future. Instances of substances can model regions/chunks of "stuff" in a stage of a process, e.g. the water entering a chiller or the mixed air region of an air handling unit.

## Python Framework

Rather than getting lost in the Sisyphean bikeshedding of how to format everything as YAML, we're
just using Python dictionaries so we don't have to worry about any (well, not that much) parsing logic.

For now, the code is the documentation. Look at `bricksrc/equipment.py`, `bricksrc/point.py`, etc. for examples and how to add to each of the class hierarchies.

## Other Tools

### Version Comparison

We can track the different classes between versions. The below scripts produces comparison files.
- `python tools/compare_versions/compare_versions.py --oldbrick 1.0.3 https://github.com/BrickSchema/Brick/releases/download/v1.0.3/Brick.ttl --newbrick 1.1.0 ./Brick.ttl`

It will produce three files inside `history/{current_version}`.
- `added_classes.txt`: A list of new classes introduced in the current version compared to the previous version.
- `removed_classes.txt`: A list of old classes removed in the current version compared to the previous version.
- `possible_mapping.json`: A map of candidate classes that can replace removed classes. Keys are removed classes and the values are candidate correspondants in the new vesion.
