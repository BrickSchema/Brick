# Brick

Brick is an open-source, BSD-licensed development effort to create a uniform schema for representing metadata in buildings. Brick has three components:

* An RDF class hierarchy describing the various building subsystems and the entities and equipment therein
* A minimal, principled set of relationships for connecting these entities together into a directed graph representing a building
* A method of encapsulation for composing complex components from a set of lower-level ones

The official Brick website, [http://brickschema.org/](http://brickschema.org/), contains documentation and other information about the Brick schema.

This repository tracks the main schema development of Brick.

## Structure

* `dist/` contains the Brick Turtle files containing the class structure, tagsets and relationships
* `src/` contains the necessary tools for creating the Brick Turtle files

## Schema Compilation

1. Update information in ``config.json`` if needed.
2. Run ``./build.sh`` at the root dir of the project. It consists of two steps.
    1. Compile schema files from ``src/Tags.csv`` and ``src/TagSets.csv``.
    2. Test if the generated files are correct with a couple of predefined rules. (It's currently very naive. If you have ideas to check, please add to the code or create an issue to discuss.)

## Discussion

Discussion takes place primarily on the Brick User Form: [https://groups.google.com/forum/#!forum/brickschema](https://groups.google.com/forum/#!forum/brickschema)

## Questions and Issues

If you have an issue with Brick's coverage, utility or usability, or any other Brick-related question:

1. First check the [Brick user form](https://groups.google.com/forum/#!forum/brickschema) and the [Brick issue tracker](https://github.com/BuildSysUniformMetadata/Brick/issues)
   to check if anyone has asked your question already.
2. If you find a previously submitted issue that closely mirrors your own, feel free to jump in on the conversation. Otherwise, please file a new issue or submit a new thread on the forum.

## How To Contribute

0. Read the [RFC guide](https://github.com/BuildSysUniformMetadata/Brick/issues/25)
1. Fork the [Brick repository](https://github.com/BuildSysUniformMetadata/Brick)
2. Make your changes in a branch on your own fork.
3. Send a pull request containing your changes.
    * If you are making several independent changes, please submit separate, independent pull requests.
    * Make sure to note if your change will cause any current Brick files to be broken (i.e. if you are changing class names)
4. Wait for your pull request to be merged by one of the maintainers
