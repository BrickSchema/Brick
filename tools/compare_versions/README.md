## Brick Version Comparison

# How to use it?

- `python tools/compare_versions/compare_versions.py --help` for getting help
- `python --oldbrick 1.0.3 https://brickschema.org/schema/1.0.3/Brick.ttl --newbrick 1.1.0 ./Brick.ttl
  - This will produce the comparison results inside `./history/{old_version}-{new_version}`.
