import argparse
import json
import os
from collections import defaultdict
from pathlib import Path

import semver
from rdflib import Graph, OWL, RDF, RDFS, Namespace
from tqdm import tqdm


def get_short_version(version):
    version = semver.parse_version_info(version)
    if version.major >= 1 and version.minor >= 1:
        return ".".join([str(version.major), str(version.minor)])
    return version


def get_root(version):
    short_version = get_short_version(version)
    if short_version == "1.3":
        return "https://brickschema.org/schema/Brick#Class"
    if semver.compare(version, "1.0.3") > 0:  # if current version is newer than 1.0.3
        return f"https://brickschema.org/schema/{short_version}/Brick#Class"
    return f"https://brickschema.org/schema/{short_version}/BrickFrame#TagSet"


argparser = argparse.ArgumentParser()
argparser.add_argument(
    "--oldbrick",
    nargs=2,
    metavar=("VERSION", "PATH"),
    help=(
        "The version of and the path to the old Brick. The path can be either a "
        "URL or filesystem path."
    ),
    default=[
        "1.0.3",
        "https://brickschema.org/schema/1.0.3/Brick.ttl",
    ],
)
argparser.add_argument(
    "--newbrick",
    nargs=2,
    metavar=("VERSION", "PATH"),
    help=(
        "The version of, and the path to the new Brick. The path can be either a "
        "URL or filesystem path."
    ),
    default=["1.3.0", "./Brick.ttl"],
)
argparser.add_argument(
    "--serialize",
    action="store_true",
    help="Save the graph containing both ontologies as a turtle file.",
)
args = argparser.parse_args()

old_ver = args.oldbrick[0]
old_ttl = args.oldbrick[1]
new_ver = args.newbrick[0]
new_ttl = args.newbrick[1]

OLD_BRICK = Namespace(f"https://brickschema.org/schema/{old_ver}/Brick#")
NEW_BRICK = Namespace(f"https://brickschema.org/schema/{new_ver}/Brick#")
OLD_ROOT = get_root(old_ver)
NEW_ROOT = get_root(new_ver)

g = Graph()
g.parse(old_ttl, format="turtle")
g.parse(new_ttl, format="turtle")
g.bind("old_brick", OLD_BRICK)
g.bind("new_brick", NEW_BRICK)
g.bind("rdfs", RDFS)
g.bind("rdf", RDF)
g.bind("owl", OWL)


def get_tag_sets(root):
    tag_sets = {}
    qstr_allclasses = """
    select ?class where {{
      ?class rdfs:subClassOf+ <{0}>.
    }}
    """
    for row in g.query(qstr_allclasses.format(root)):
        klass = row[0].split("#")[-1]
        tag_set = klass.split("_")  # Tags inside the class name.
        tag_sets[klass] = set(tag_set)
    print(root, len(tag_sets))
    return tag_sets


old_tag_sets = get_tag_sets(OLD_ROOT)
new_tag_sets = get_tag_sets(NEW_ROOT)

history_dir = Path(f"history/{old_ver}-{new_ver}")
os.makedirs(history_dir, exist_ok=True)

old_classes = set(old_tag_sets.keys())
new_classes = set(new_tag_sets.keys())

with open(history_dir / "removed_classes.txt", "w") as fp:
    fp.write("\n".join(sorted(old_classes - new_classes)))

with open(history_dir / "added_classes.txt", "w") as fp:
    fp.write("\n".join(sorted(new_classes - old_classes)))

if args.serialize:
    g.serialize(history_dir / "graph.ttl", format="turtle")


# List possible matches for removed classes
mapping_candidates = defaultdict(list)
for old_class, old_tag_set in tqdm(old_tag_sets.items()):
    if old_class in new_tag_sets:
        continue
    for new_class, new_tag_set in new_tag_sets.items():
        # If the delimited tags are similar in the old class and this new class,
        # they might be mappable across the version.
        if (
            len(old_tag_set.intersection(new_tag_set))
            / len(old_tag_set.union(new_tag_set))
            > 0.7
        ):
            mapping_candidates[old_class].append(new_class)

with open(history_dir / "possible_mapping.json", "w") as fp:
    json.dump(mapping_candidates, fp, indent=2)
