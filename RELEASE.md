# Release Notes

This document contains the items that need to be done to prepare Brick for a release.

## Branch

Create a new branch to centralize the final changes for the release; something like `v1.2.1` or `v1.2.1-release` is appropriate. Push this branch to GitHub and use it as the merge target for any outstanding PRs.

## Updating Documentation

TODO...

## Update `brickschema`

TODO...

## Version Number

Change the version number in `bricksrc/version.py`; this will usually involve changing either the **patch** version or the **minor** version.

## Release Notes

Use the output of the `tools/compare_versions` tool to generate a list of what has changed since the last release of Brick. This *can* be a URL, and in fact this is the easist way of comparing the current build with the previous build: specifically, what classes/concepts are added or removed. This should be one of the last items done. Take a look at the bottom of https://github.com/BrickSchema/Brick/releases/tag/v1.2.0 as an example for what this should look like in the release.

This can be done as follows:

```bash
$ make # generate Brick
$ python tools/compare_versions/compare_versions.py --oldbrick 1.2.0 https://github.com/BrickSchema/Brick/releases/download/v1.2.0/Brick.ttl --newbrick 1.2.1 Brick.ttl
```
