# Brick

[![Build Status](https://github.com/BrickSchema/Brick/workflows/Build/badge.svg)](https://github.com/BrickSchema/Brick/actions)
[![Python 3.6](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/)

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

- `example1`: getting familiar with RDFlib, namespaces, Brick models and when and when not to import the Brick ontology definition
- `simple_apartment`: uses Python to programmatically build a Brick model of a small apartment
- `g36`: contains Brick implementations of several figures from ASHRAE Guideline 36

## Versioning

Brick uses a semantic versioning scheme for its version numbers: `major.minor.patch`. The [releases page](https://github.com/BrickSchema/Brick/releases) contains links to each published Brick release for easy download.

We target a minor version release (e.g. `1.1`, `1.2`, `1.3`) roughly every 6 months. Minor releases will contain largely backwards-compatible extensions and new features to the ontology. Due to the significance of these changes, minor releases will be developed in their own branch; PRs for those releases will be merged into the minor version branch, and then ultimately merged into the main branch when the minor release is published.

Patch releases (e.g. `1.2.1`, `1.2.2`) contain smaller, incremental, backwards-compatible changes to the ontology. Commits and PRs for the next patch release will be merged directly into `master`. Every evening, a `nightly` build is produced containing the latest commits. **There may be bugs or errors in the nightly release**, however these bugs will be removed by the time a patch release is published.

## How To Contribute

See [CONTRIBUTING.md](https://github.com/BrickSchema/Brick/blob/master/CONTRIBUTING.md)

## Tests

Tests go in the `tests/` directory and should be implemented using [pytest](https://pytest.readthedocs.io/en/latest/getting-started.html#getstarted).
[`tests/test_inference.py`](https://github.com/BrickSchema/Brick/blob/master/tests/test_inference.py) is a good example.

Run tests by executing `pytest` in the top-level directory of this repository.

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
