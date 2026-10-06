# Major version: increment for backwards incompatible changes
BRICK_MAJOR_VERSION = 1

# Minor version: increment for substantial additions to the ontology that
# are backwards compatible
BRICK_MINOR_VERSION = 5

# Patch version: increment for minor additions/changes to the ontology that
# are largely backwards compatible (bug-fixes exempted)
BRICK_PATCH_VERSION = 0

# the simplified (no patch version) version number for Brick. Intended for
# inclusion in the Brick namespace URI
BRICK_VERSION = f"{BRICK_MAJOR_VERSION}.{BRICK_MINOR_VERSION}"

# the full "semantic version" including the patch number
BRICK_FULL_VERSION = f"{BRICK_VERSION}.{BRICK_PATCH_VERSION}"

# Pre-release label appended to the full version in the ontology's
# owl:versionInfo (e.g. "rc.2" gives "1.5.0-rc.2"). Set to "" for a final release.
# Semver requires we use the "." to delineate "rc" from the version,
# else "rc10" would come before "rc2"
BRICK_PRERELEASE = "rc.2"

# the full version as published in owl:versionInfo, including any pre-release label
BRICK_VERSION_INFO = (
    f"{BRICK_FULL_VERSION}-{BRICK_PRERELEASE}"
    if BRICK_PRERELEASE
    else BRICK_FULL_VERSION
)
