# SHACL for Brick

The SHACL Shapes Constraint Language validates RDF graphs against conditions (called "shapes"), which are
expressed themselves as an RDF graph. This document discusses the application of SHACL to Brick. In
this document we are specifically looking at writing SHACL shapes for validating Brick *models*
(instances of buildings). Using SHACL to validate the Brick ontology deserves its own investigation.

SHACL shapes for Brick should validate the following:

- validating endpoints of Brick relationships (properties):
  - check type of subject/object: are the `brick:domain` and `brick:range` properties respected?
  - cardinality checks: with varying severity
    - floors without rooms
    - equipment missing certain points (e.g. thermostat should have a temperature sensor, at least one setpoint)
    - all named individuals should have `rdf:type`
- compatibility checking:
  - all objects of `rdf:type` should be Brick classes (subclassof, etc)
  - check for deprecated classes, relationships
- idioms, semantic checks:
  - these may be optional; users can "opt-in" to check for certain idioms
  - equipment along a chain of `brick:feeds` should all operate on the same substance

## Use SHACL to validate Brick ontology

The `generate_shacl.py` generates `BrickShape.ttl` which contains the basic shapes for the Brick Schema.

In [`brickschema`](https://github.com/BrickSchema/py-brickschema) package the `validate` sub-module
provides an API and a command line tool for validating a building ontology.  In addtion to the default
`BrickShape.ttl`, the user can add their only constraints into the validation.

## Brick SHACL shapes

Those are the rules focusing on certain type of triples in the building graph and enforcing restrictions.  The
examples below declare shapes in the `bsh` ("brickshape" ) namespace (`https://brickschema.org/schema/BrickShape#`) for clarity.

### Property Constraints

Property definitions (from the `bricksrc/properties.py` file) define inverses, domains/ranges
of properties and subproperties. The shape graph would contain one shape for
each Brick property that encodes constraints on the subject and/or object of the property.

For example, the definition of `brick:hasLocation` is

```python
{
  "hasLocation": {
    A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
    OWL.inverseOf: "isLocationOf",
    BRICK.range: BRICK.Location,
    SKOS.definition: Literal("Subject is physically located in the location given by the object"),
  },
}
```

This definition informs the following Shape for the `brick:range` property

```ttl
@prefix bsh: <https://brickschema.org/schema/{BRICK_VERSION}/BrickShape#>

bsh:HasLocationRangeShape
    a   sh:NodeShape ;
    sh:targetSubjectsOf brick:hasLocation ;
    sh:property [
        sh:class    brick:Location ;
        sh:path     brick:hasLocation ;
        sh:message "Property hasLocation has object with incorrect type"
    ] .
```

### Special Property Constraints

We will also want to define special shapes for certain properties that have additional semantics.
For example, the `feedsAir` subproperty should require that all equipments on its endpoints should
have the `brick:regulates brick:Air` property.

We can model this by requiring that all subjects of the `brick:feedsAir`
property have the `brick:Air` value for either a `brick:requlates`, `brick:hasInputSubstance`
or `brick:hasOutputSubstance` property.

```ttl
bsh:feedsAirHasInputSubstanceShape a sh:NodeShape ;
    sh:property [ sh:class brick:Air ;
            sh:message "Subject of property feedsAir has object with incorrect type" ;
            sh:path brick:hasInputSubstance ] ;
    sh:targetSubjectsOf brick:feedsAir .

bsh:feedsAirHasOutputSubstanceShape a sh:NodeShape ;
    sh:property [ sh:class brick:Air ;
            sh:message "Subject of property feedsAir has object with incorrect type" ;
            sh:path brick:hasOutputSubstance ] ;
    sh:targetSubjectsOf brick:feedsAir .

bsh:feedsAirRegulatesShape a sh:NodeShape ;
    sh:property [ sh:class brick:Air ;
            sh:message "Subject of property feedsAir has object with incorrect type" ;
            sh:path brick:regulates ] ;
    sh:targetSubjectsOf brick:feedsAir .
```
