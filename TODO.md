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

- [ ] How to rectify confusion/complication of substances that are tags as well as classes.
      Currently, Tags are in their own ontology "BrickTag" to avoid namespace conflicts with
      the actual `Substance` classes in the Brick ontology.

      Once we figure out what the relationship for "relating" an equipment or point to a
      substance class/instance, then we can establish an inference rule that things that
      are related to that substance class must also be tagged appropriately.
