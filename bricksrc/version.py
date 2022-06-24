# Major version: increment for backwards compatible changes
BRICK_MAJOR_VERSION = 1

# Minor version: increment for substantial additions to the ontology that
# are backwards compatible
BRICK_MINOR_VERSION = 3

# Patch version: increment for minor additions/changes to the ontology that
# are largely backwards compatible (bug-fixes exempted)
BRICK_PATCH_VERSION = 0

# the simplified (no patch version) version number for Brick. Intended for
# inclusion in the Brick namespace URI
BRICK_VERSION = f"{BRICK_MAJOR_VERSION}.{BRICK_MINOR_VERSION}"

# the full "semantic verersion" including the patch number
BRICK_FULL_VERSION = f"{BRICK_VERSION}.{BRICK_PATCH_VERSION}"
