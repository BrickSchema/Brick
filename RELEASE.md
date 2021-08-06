# Release Notes

This document contains the items that need to be done to prepare Brick for a release.

## Branch

Create a new branch to centralize the final changes for the release; something like `v1.2.1-release` is appropriate. Push this branch to GitHub and use it as the merge target for any outstanding PRs.

## Version Number

Change the version number in `bricksrc/version.py`; this will usually involve changing either the **patch** version or the **minor** version.
