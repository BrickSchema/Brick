# Brick 2 Electric Boogaloo


Here's the gist of how I'm doing things and what kinds of inference/modeling are enabled

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

G.query("SELECT ?x WHERE { ?x brick:hasTag tag:Equip }")
```

We can serialize the expanded form of the graph to disk if we need to use a SPARQL query processor that does not support reasoning.

### Classes

- The Brick class namespace is `https://brickschema.org/schema/1.0.3/Brick#`
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
- `Substance`
- `Quantity`

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

- Tag ontology namespace is `https://brickschema.org/schema/1.0.3/BrickTag#`
- We use Haystack tags and define our own set including them
- Tags should have definitions, but this is not included yet
- Sets of tags have a 1-1 mapping with a class name
- definitions given using the `skos:definition` property

This is accomplished by declaring a Brick class (e.g. `Air_Temperature_Sensor`) as equivalent to an anonymous class, which is an `owl:Restriction` that is the intersection of entities that have certain tags.

```
# in turtle format
brick:Temperature_Sensor a owl:Class ;
    rdfs:subClassOf brick:Sensor ;
    owl:equivalentClass [ owl:intersectionOf (
                            [ a owl:Restriction ;
                                owl:hasValue tag:Sensor ;
                                owl:onProperty brick:hasTag
                            ]
                            [ a owl:Restriction ;
                                owl:hasValue tag:Temperature ;
                                owl:onProperty brick:hasTag
                            ]
                        ) ] .
```

The first `owl:Restriction` is the set of all classes that have `tag:Sensor` as the value for one of their `brick:hasTag` properties.

This means that a temperature sensor `:ts1` could be defined in two different ways and the reasoner would infer the other triples:

```
# using classes
:ts1   a   brick:Temperature_Sensor

# using tags
:ts1    brick:hasTag    tag:Temp
:ts1    brick:hasTag    tag:Sensor
```

### Substances

Brick now defines a hierarchy of substances (`substances.py`) and a hierarchy of quantities (`quantities.py`).
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

```python
definitions = {
    "Lighting_System": {
        "tagvalues": [   # Lighting_System class is equivalent to the Lighting tag
            (BRICK.hasTag, TAG.Lighting),
            # if you have more required tags add them as their own tuple in the list
        ],
        # defining subclasses. This can be nested ad-infinitum
        "subclasses": {
            "Lighting": {
                "subclasses": {
                    "Luminaire": {},
                    "Luminaire_Driver": {},
                },
            },
            "Interface": {
                "subclasses": {
                    "Switch": {
                        "subclasses": {
                            "Dimmer": {},
                        },
                    },
                    "Touchpanel": {},
                },
            },
        },
    }
}
define_subclasses(definitions, BRICK.Equipment)
```

For now, the code is the documentation. Look at `equipment.py`, `point.py`, etc for examples and how to add to each of the class hierarchies.

## TODOs

- [ ] pull all tags from haystack
- [ ] add Tag definitions
- [ ] add alarms, other setpoints and the rest of the Brick points

---

**Authors: Gabe Fierro**
