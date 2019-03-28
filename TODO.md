# TODO

Things to figure out

- [ ] Where do members of the `Substance` class become members of the class rather than subclasses?
  It makes sense for "Gas" to be a class of substance, but is "Air" a member of the class
  or is it its own class of different kinds of Air?

  Keeping this as a class means that we can instantiate an instance of "Mixed Air" and
  assign that to a section of equipment, if we want.

  Otherwise, if we turn some into members (e.g. "Air" or "Water"), then we might
  run into awkwardness later if we want to extend the hierarchy. Queries might be a little
  cleaner though

---

- [ ] How to rectify confusion/complication of substances that are tags as well as classes.
  Currently, Tags are in their own ontology "BrickTag" to avoid namespace conflicts with
  the actual `Substance` classes in the Brick ontology.

  Once we figure out what the relationship for "relating" an equipment or point to a
  substance class/instance, then we can establish an inference rule that things that
  are related to that substance class must also be tagged appropriately.

---

- [ ] Using the OWL restriction stuff, we can express that sets of tags are equivalent to
  an OWL class (for example, `cool` and `coil` tags are equivalent to the `brick:Cooling_Coil`
  class).

  This may be a little tooooo restrictive. In "vanilla" Brick, we assemble tags into valid
  class names, but it is nice to have tags distinct from classes (for example, VAV class
  should have the `equip` tag but shouldn't need to have "Equip" in the class name).

  The useful inference is from class to a set of tags

  ```
    # this is intrinsic
    :ts1   a   brick:Air_Temperature_Sensor

    # implies these extrinsic tags
    :ts1    brick:hasTag    tag:Temp
    :ts1    brick:hasTag    tag:Air
    :ts1    brick:hasTag    tag:Sensor
    :ts1    brick:hasTag    tag:Point
  ```

  Once an individual has a clear class definition (via `a` or `rdf:type`), then we can later
  find that entity using the tags.

  If we adhere to the constraint that each class has a unique set of tags (at least every super
  class; if a subtree of the class hierarchy does not have any tags, then they just inherit the
  tags of their superclass(es) ), then we can use `owl:Restriction`s to define a 1-1 mapping
  between a class and a set of tags. This is *bi-directional*.

  These two are equivalent

  ```
    # using classes
    :ts1   a   brick:Air_Temperature_Sensor

    # using tags
    :ts1    brick:hasTag    tag:Temp
    :ts1    brick:hasTag    tag:Air
    :ts1    brick:hasTag    tag:Sensor
    :ts1    brick:hasTag    tag:Point
  ```

  The following would just be a member of the `brick:Temperature_Sensor` class

  ```
    :ts1    brick:hasTag    tag:Temp
    :ts1    brick:hasTag    tag:Sensor
    :ts1    brick:hasTag    tag:Point
  ```
