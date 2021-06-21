# VBIS / Brick Alignment

Aligns concepts in Brick with concepts in VBIS v3 (https://vbis.com.au/classification-and-tags).

Use the alignment file `Brick-VBIS-alignment.ttl`; import this into your RDF graph in order to realize the mappings between concepts in VBIS and Brick.
Specifically, the file encodes which VBIS search tags are relevant for many different Brick equipment classes.
The VBIS search tags are encoded as string literals and are related to Brick classes through the `https://brickschema.org/schema/Brick/alignments/vbis#hasTag` property.

## Example 1: Adding VBIS Tags to a Brick Model



## Example 2: Validating VBIS Tags in a Brick model

Consider a Brick model with two entities, each with a VBIS tag

```ttl
@prefix : <urn:example#> .
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix vbis: <https://brickschema.org/schema/Brick/alignments/vbis#> .

# correct
:chiller1   a   brick:Absorption_Chiller ;
    vbis:hasTag vbis:ME-Chr-Ab-DF .

# incorrect
:chiller2   a   brick:Absorption_Chiller ;
    vbis:hasTag vbis:ME-Chr-AC-Sc .
```

One has a correct VBIS tag (given the Brick class) and the other does not. We can use the following Python code to check:

```python
import brickschema

g = brickschema.Graph(load_brick_nightly=True)
g.load_file("example.ttl")
g.load_file("Brick-VBIS-alignment.ttl")

valid, _, report = g.validate()
if not valid:
    print(report)
```

which will give us the following report:

```
Validation Report
Conforms: False
Results (1):
Constraint Violation in InConstraintComponent (http://www.w3.org/ns/shacl#InConstraintComponent):
        Severity: sh:Violation
        Source Shape: [ sh:in ( vbis:ME-Chr-Ab-St vbis:ME-Chr-Ab-DF vbis:ME-Chr-Ab-WH vbis:ME-Chr-Ab ) ; sh:maxCount Literal("1", datatype=xsd:integer) ; sh:message Literal("Brick class brick:Absorption_Chiller does not match the provided tag") ; sh:path vbis:hasTag ]
        Focus Node: :chiller2
        Value Node: vbis:ME-Chr-AC-Sc
        Result Path: vbis:hasTag
        Message: Brick class brick:Absorption_Chiller does not match the provided tag
```
