# SHACL for Brick

The SHACL Shapes Constraint Language validates RDF graphs against conditions (called "shapes"), which are expressed themselves as an RDF graph. This document discusses the application of SHACL to Brick. In this document we are specifically looking at writing SHACL shapes for validating Brick *models* (instances of buildings). Using SHACL to validate the Brick ontology deserves its own investigation.

SHACL shapes for Brick should validate the following:

- validating endpoints of Brick relationships (properties):
  - check type of subject/object: are the `rdfs:range`, `rdfs:domain` properties respected?
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
  - proper relationships exist between equipment: e.g. thermostat should have `controls` relationship to RTU

## Getting Started

Install `pyshacl` from pip.

`generate_shacl.py` uses `bricksrc/` to generate a Shapes graph that is serialized to `shacl_test.ttl`.

To validate a graph, use [pySHACL](https://github.com/RDFLib/pySHACL):

```bash
pyshacl -s shacl_test.ttl -m -e Brick.ttl -f human sample_graph.ttl
```

You may want to expand a graph before validating it. In that case, run

```bash
python expand_graph.py sample_graph.ttl
```

which will drop the expanded graph into `output.ttl` in the same directory.

## Brick SHACL shapes

Going through what the SHACL shapes would look for for different tests. The examples below declare shapes in the `bsh` ("brickshape") namespace for clarity

### Property Constraints

Property definitions (from the `bricksrc/properties.py` file) define inverses, domains/ranges of properties and subproperties. The shape graph would contain one shape for each Brick property that encodes constraints on the domain and/or range of the property.

**TODO**: so far, I'm only sure how to encode the `rdfs:range` property

For example, the definition of `brick:hasLocation` is

```python
{
  "hasLocation": {
    A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
    OWL.inverseOf: "isLocationOf",
    RDFS.range: BRICK.Location,
    SKOS.definition: Literal("Subject is physically located in the location given by the object"),
  },
}
```

This definition informs the following Shape for the `rdfs:range` property

```ttl
bsh:HasLocationRangeShape
    a   sh:NodeShape ;
    sh:targetObjectsOf brick:hasLocation ;
    sh:property [
        sh:class    brick:Location ;
        sh:path     brick:hasLocation ;
        sh:nodeKind sh:IRI ;
    ] .
```

For properties with both a domain and a range, we will need both a "domain" Shape and a "range" Shape; however, at this time I'm not sure how to encode constraints for `rdfs:domain`.

### Special Property Constraints

We will also want to define special shapes for certain properties that have additional semantics. For example, the `feedsAir` subproperty should require that all equipment on its endpoints should have the `brick:regulates brick:Air` property.

We can model this by requiring that all subjects *and* objects of the `brick:feedsAir` property have the `brick:Air` value for either a `brick:requlates` or `brick:measures` property.

```ttl
bsh:FeedsAirSubjectShape a sh:NodeShape ;
    sh:targetSubjectsOf brick:feedsAir ;
    sh:or (
        sh:property [
            sh:path brick:regulates ;
            sh:class brick:Air ;
        ]
        sh:property [
            sh:path brick:measures ;
            sh:class brick:Air ;
        ]
    ) .

bsh:FeedsAirObjectShape a sh:NodeShape ;
    sh:targetObjectsOf brick:feedsAir ;
    sh:or (
        sh:property [
            sh:path brick:regulates ;
            sh:class brick:Air ;
        ]
        sh:property [
            sh:path brick:measures ;
            sh:class brick:Air ;
        ]
    ) .
```
