# Entity Properties

Entity Properties are attributes or characteristics of Brick entities. Entity Properties should change rarely, if ever. Entity Properties are identified by an RDF property name and related SHACL shapes.

Entity Properties are categorized broadly by the following dimensions:
- **Inherent** vs **Configurable** (mutually exclusive):
    - an Inherent Property is one that is a permanent and/or characteristic property of the entity. The dimensions of a room, max rated power of a motor, tonnage of an RTU are all examples of Inherent Properties.
    - Configurable Properties are temporary or actuatable properties of an entity
- **Physical** vs **Virtual** vs **Identity** (not mutually exclusive):
    - a Physical Property is a characteristic that exists in the physical world ("meatspace")
    - a Virtual Property is a characteristic that has a digital representation. May be a property of the virtual representation of an entity, or a computed property of the entity
    - an Identity Property is a characteristic that identifies the device

The properties themselves are *instances* of Entity Properties; a shallow hierarchy of properties is defined with `rdfs:subPropertyOf`.

**Example**: here are some Physical Properties defined in the ontology which define the following hierarchy:
- `prop:hasArea`:
    - `prop:hasGrossArea`
    - `prop:hasNetArea`
- `prop:hasVolume`
- `prop:hasHeight`
- `prop:hasWidth`
- `prop:hasLength`

```ttl
prop:hasArea    a  prop:PhysicalProperty ;
    skos:definition "Entity has 2-dimensional area" ;
    rdfs:range  prop:AreaShape .

prop:hasGrossArea    rdfs:subPropertyOf  prop:hasArea ;
    skos:definition "Entity has gross 2-dimensional area" ;
    rdfs:range  prop:AreaShape .

prop:hasNetArea    rdfs:subPropertyOf  prop:hasArea ;
    skos:definition "Entity has gross 2-dimensional area" ;
    rdfs:range  prop:AreaShape .

prop:hasVolume  a  prop:PhysicalProperty ;
    skos:definition "Entity has 3-dimensional volume" ;
    rdfs:range  prop:VolumeShape .

prop:hasHeight a prop:PhysicalProperty ;
    skos:definition "Entity has height" ;
    rdfs:range  prop:OneDimensionalMagnitudeShape .

prop:hasWidth a prop:PhysicalProperty ;
    skos:definition "Entity has width" ;
    rdfs:range  prop:OneDimensionalMagnitudeShape .

prop:hasLength a prop:PhysicalProperty ;
    skos:definition "Entity has length" ;
    rdfs:range  prop:OneDimensionalMagnitudeShape .
```

The subject of each property will be a Brick entity; the value is an anonymous class which is goverened by a SHACL Shape. Note that the use of SHACL is optional here. We don't need SHACL inference for anything; we can use the SHACL shapes for "type checking" on the properties. That kind of SHACL validation is fairly easy to find implementations of.

```ttl
prop:AreaShape a sh:NodeShape ;
    rdfs:range qudt:Quantity ;
    sh:property [
        sh:path brick:hasUnit ;
        sh:in   (unit:FT2 unit:M2) ;
        sh:minCount 1 ;
    ] .


prop:VolumeShape    a   sh:NodeShape ;
    rdfs:range qudt:Quantity ;
    sh:property [
        sh:path brick:hasUnit ;
        sh:in   (unit:FT3 unit:M3) ;
        sh:minCount 1 ;
    ] .


prop:OneDimensionalMagnitudeShape   a   sh:NodeShape ;
    rdfs:range qudt:Quantity ;
    sh:property [
        sh:path brick:hasUnit ;
        sh:in   (unit:FT unit:M) ;
        sh:minCount 1 ;
    ] .
```

## Example 1: Room and Floor Geometry

Here's an example of how the above properties would be used to describe the net area of a floor, and the height and area of a room. Benefits of this approach:
- easy to add other metadata to the value itself (precision, timestamp, etc)
- semantics are in the property name -- this will simplify queries (see below)
- compatible with (and based on) QUDT
- (*if we need it*) multiple Brick entities can refer to the same property value but with different relationships

```ttl
:floor1 a   brick:Floor ;
    prop:hasNetArea    [
        prop:value  "100"^^xsd:integer ;
        brick:hasUnit   unit:FT2 ;
    ] .


:room1  a   brick:Room ;
    prop:hasArea    [
        prop:value  "35"^^xsd:integer ;
        brick:hasUnit   unit:FT2 ;
    ] ;
    prop:hasHeight [
        prop:value  "7"^^xsd:integer ;
        brick:hasUnit   unit:F ;
    ] .

```

Here's a sample SPARQL query to get the room names and areas for all rooms on the 4th floor. I think this is a fair "trade" syntactically for the additional expressive power we get out of the feature. I'm having a hard time figuring out what else we can remove from the model to make it simpler, without giving up the ability to add things like units.

```sparql
SELECT ?room ?area ?unit WHERE {
    ?room a brick:Room .
    ?room brick:isPartOf bldg:Floor_4 .
    ?room brick:hasArea/prop:value  ?area .
    ?room brick:hasArea/prop:unit   ?unit
}
```

## Example 2: Electrical Metering Points

An example of an single-phase active power sensor that measures net power, and a daily energy usage meter

```ttl
:meter1 a   brick:Power_Sensor ;
    brick:hasUnit   unit:KiloW ;
    prop:hasComplexity   [
        prop:value  "active" ;
    ] ;
    prop:hasPowerFlow   [
        prop:value  "net" ;
    ] ;
    prop:hasPhaseCount   [
        prop:value  "1"^^xsd:integer ;
    ] ;
    prop:hasIP6Address  [
        prop:value  "fe80::1",
    ] .

:daily_energy_usage_meter   a   brick:Energy_Sensor ;
    brick:hasUnit   unit:KiloW-HR ;
    prop:aggregate [
        prop:aggregationFunction    "sum" ;
        prop:aggregationInterval    "1d" ;
    ] ;
    prop:hasComplexity [
        prop:value  "active" ;
    ] ;
    prop:hasPowerFlow [
        prop:value  "net" ;
    ]
.

:hourly_peak_real_power_meter   a   brick:Power_Sensor ;
    brick:hasUnit   unit:KiloW-HR ;
    prop:aggregate [
        prop:aggregationFunction    "max" ;
        prop:aggregationInterval    "1h" ;
    ] ;
    prop:hasComplexity [
        prop:value  "real" ;
    ]
.
```
