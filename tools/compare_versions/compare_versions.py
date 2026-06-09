import argparse
import numpy as np
from sentence_transformers import SentenceTransformer
from scipy.optimize import linear_sum_assignment
import json
import os
from collections import defaultdict
from pathlib import Path
import sys

dirname = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(dirname))

import semver
from rdflib import Graph, OWL, RDF, RDFS, Namespace, SKOS
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
    if semver.compare(version, "1.0.3") <= 0:  # if current version is older than 1.0.3
        return f"https://brickschema.org/schema/{short_version}/BrickFrame#TagSet"
    # 1.4 and later
    return "https://brickschema.org/schema/Brick#Entity"


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

old_brick = Graph()
old_brick.parse(old_ttl, format="turtle")

new_brick = Graph()
new_brick.parse(new_ttl, format="turtle")


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


def get_concepts(graph):
    # return everything in the brick: namespace
    qstr = """SELECT ?s WHERE {
        FILTER(STRSTARTS(STR(?s), "https://brickschema.org/schema"))
        { ?s a owl:Class }
        UNION
        { ?s a owl:ObjectProperty }
        UNION
        { ?s a owl:DatatypeProperty }
        UNION
        { ?s a brick:Quantity }
        UNION
        { ?s a brick:EntityPropertyValue }
        UNION
        { ?s a brick:EntityProperty }
    }"""
    return set([row[0] for row in graph.query(qstr)])


old_classes = get_concepts(old_brick)
new_classes = get_concepts(new_brick)

print(f"Old classes: {len(old_classes)}")
print(f"New classes: {len(new_classes)}")

history_dir = Path(f"history/{old_ver}-{new_ver}")
os.makedirs(history_dir, exist_ok=True)

# old_classes = set(old_tag_sets.keys())
# new_classes = set(new_tag_sets.keys())

print(f"Common classes: {len(old_classes & new_classes)}")

with open(history_dir / "removed_classes.txt", "w") as fp:
    fp.write("\n".join(sorted(old_classes - new_classes)))

with open(history_dir / "added_classes.txt", "w") as fp:
    fp.write("\n".join(sorted(new_classes - old_classes)))

if args.serialize:
    g.serialize(history_dir / "graph.ttl", format="turtle")


def prep_concept(graph, concept):
    # remove BRICK namespace from concept, change '_' in to ' '
    name = concept.split("#")[-1].replace("_", " ")
    definition = graph.value(concept, RDFS.comment) or graph.value(
        concept, SKOS.definition
    )
    # get the cbd of the concept
    sentence = f"{name} - {definition}"
    return sentence


THRESHOLD = 0.7

model = SentenceTransformer("all-MiniLM-L6-v2")
old_classes = list(old_classes)
old_classes_sentences = [prep_concept(old_brick, c) for c in old_classes]
old_embeddings = model.encode(old_classes_sentences)

new_classes = list(new_classes)
new_classes_sentences = [prep_concept(new_brick, c) for c in new_classes]
new_embeddings = model.encode(new_classes_sentences)
similarities = np.dot(old_embeddings, new_embeddings.T)
distance_matrix = 1 - similarities
row_ind, col_ind = linear_sum_assignment(distance_matrix)

# fetch all deprecations from Brick
deprecations = {}
qstr = """
SELECT ?s ?version ?message ?replacement WHERE {
    ?s owl:deprecated true .
    ?s brick:deprecatedInVersion ?version .
    ?s brick:deprecationMitigationMessage ?message .
    ?s brick:isReplacedBy ?replacement .
}
"""
for row in new_brick.query(qstr):
    deprecations[row[0]] = {
        "version": row[1],
        "message": row[2],
        "replacement": row[3],
    }

mapping = {}
for i, j in zip(row_ind, col_ind):
    score = similarities[i, j]
    if score < THRESHOLD:
        continue
    if old_classes[i] == new_classes[j]:
        continue
    if old_classes[i] in deprecations:
        continue
    mapping[old_classes[i]] = new_classes[j]

with open(history_dir / "mapping.json", "w") as fp:
    json.dump(mapping, fp)

# remove deprecations that are not new
for row in old_brick.query(qstr):
    if row[0] in deprecations:
        del deprecations[row[0]]

# output the Markdown-formatted release notes

# output added classes
with open(history_dir / "release_notes.md", "w") as fp:
    fp.write("## Added Concepts\n\n```\n")
    for c in sorted(set(new_classes) - set(old_classes)):
        fp.write(f"{c}\n")
    fp.write("\n```\n")

    fp.write("\n\n## Removed Concepts\n\n```\n")
    for c in sorted(set(old_classes) - set(new_classes)):
        fp.write(f"{c}\n")
    fp.write("\n```\n")

    fp.write("\n\n## Deprecations\n\n")
    fp.write("<details>\n<summary>Deprecations JSON</summary>\n\n```json\n")
    json.dump(deprecations, fp, indent=2)
    fp.write("\n```\n")
