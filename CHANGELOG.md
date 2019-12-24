# Changelog
-----------

## Brick v1.1
-------------

### Release Notes

Brick v1.1 represents the latest release of Brick since v1.0.3.
The class hierarchy in v1.0.3 has been refined to eliminate redundant, misleading or unnecessary classes.
The class hierarchy has also been extended to cover Substances and Quantities, which are can be used to model aspects of equipment and point behavior.
An expanded set of properties complements the class hierarchy: `measures`, `regulates`, `hasInputSubstance`, `hasOutputSubstance` and so on.
This release also incorporates an improved Python-based framework for editing and generating the Brick ontology so that the Turtle file does not have to be edited directly.
Finally, Brick v1.1 incorporates a set of tags --- atomic identifiers --- which can be used to annotate and infer classes.

For technical details on these changes, we refer the reader to a [recent publication in BuildSys 2019](https://brickschema.org/papers/HouseOfSticks-BuildSys-2019-Fierro.pdf).

Changes:
- addition of unit test framework under `tests/`
- Brick ontology now fits under OWL RL ontology profile

Backwards incompatible changes:
- the Brick namespace URI has changed from `https://brickschema.org/schema/1.0.3/Brick#` to `https://brickschema.org/schema/1.1/Brick#`

Added classes:
- **TODO**

Removed classes:
- **TODO**


### Contributors

Thanks to all of the contributors!

- [@gtfierro](https://github.com/gtfierro)
- [@jbkoh](https://github.com/jbkoh)
- [@shreyasnagare](https://github.com/shreyasnagare)
- [@JoelBender](https://github.com/JoelBender)
- [@blip2](https://github.com/blip2)
