# Release Notes

This document contains the items that need to be done to prepare Brick for a release.

## Version Number

Change the version number in `bricksrc/version.py`; this will usually involve changing either the **patch** version or the **minor** version.

## Branch

Create a new branch to centralize the final changes for the release; something like `v1.2.1` or `v1.2.1-release` is appropriate. Push this branch to GitHub and use it as the merge target for any outstanding PRs.

When the branch is finished and the release is ready, merge it into the `master` branch on GitHub.

## Release Notes

Now the release notes can be prepared.

Use the output of the `tools/compare_versions` tool to generate a list of what has changed since the last release of Brick. This *can* be a URL, and in fact this is the easist way of comparing the current build with the previous build: specifically, what classes/concepts are added or removed. Take a look at the bottom of https://github.com/BrickSchema/Brick/releases/tag/v1.2.0 as an example for what this should look like in the release.

Due to a limitation of the `compare_versions` tool, it is currently necessary to download all Brick.ttl files that will be compared and to manually adjust the namespaces so that they are versioned, e.g. `https://brickschema.org/schema/Brick#` becomes `https://brickschema.org/schema/1.2.1/Brick#`.

After this is done, the tool can be run as follows

```bash
$ make # generate Brick
$ python tools/compare_versions/compare_versions.py --oldbrick 1.2.0 Brick120.ttl --newbrick 1.2.1 Brick.ttl
```

This will generate a `history/` directory containing files with the added and removed class lists.

Put together the release notes. This should summarize the changes to Brick since the last release. Be sure to thank all contributors since the previous release.  This can be computed by the following git command:

```
git shortlog <last version>..HEAD -n -s
```

for example, using the git tag for the `v1.2.0` release:

```
git shortlog v1.2.0..HEAD -n -s
```

Include the added/removed classes at the bottom of the release notes. Be sure to tag the release following the usual naming schema `vMAJOR.MINOR.PATCH`.

## Update `brickschema`

Checkout the [brickschema repository](https://github.com/BrickSchema/py-brickschema). Edit `tools/update_auxiliary.sh` to identify the internal folder where the copy of Brick should go. Usually this will just involve changing the version number at the end.

Then, run `update_auxiliary.sh` from the root directory of the repository:

```bash
$ ./tools/update_auxiliary.sh
```

Update the version number of the package (`poetry version <new version>`), build and publish.


## Update Website

Instructions coming soon...
