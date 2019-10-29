import sys
sys.path.append('./')  # Assume that this file is run at the root of the repo.
import os
from collections import defaultdict
import json
import argparse
import semver

from tqdm import tqdm
import rdflib
from rdflib import Namespace, URIRef, RDF, RDFS, OWL
from bricksrc.namespaces import BRICK_VERSION


def get_root(version):
    if semver.compare(version, '1.0.3') > 0:  # if the current version is newer than 1.0.3
        root_template = 'https://brickschema.org/schema/{0}/Brick#Class'
    else:
        root_template = 'https://brickschema.org/schema/{0}/BrickFrame#TagSet'
    return root_template.format(version)


argparser = argparse.ArgumentParser()
argparser.add_argument('--oldbrick',
                       nargs=2,
                       metavar=('VERSION', 'PATH'),
                       help='The version of and the path to the old Brick. The path can be either a URL or filesystem path.',
                       default=['1.0.3', 'https://github.com/BrickSchema/Brick/releases/download/v1.0.3/Brick.ttl'],
                       )
argparser.add_argument('--newbrick',
                       nargs=2,
                       metavar=('VERSION', 'PATH'),
                       help='The version of, and the path to the new Brick. The path can be either a URL or filesystem path.',
                       default=['1.1.0', './Brick.ttl'],
                       )
args = argparser.parse_args()


old_ver = args.oldbrick[0]
old_ttl = args.oldbrick[1]
new_ver = args.newbrick[0]
new_ttl = args.newbrick[1]

brick_ns_template = 'https://brickschema.org/schema/{0}/Brick#'
OLD_BRICK = Namespace(brick_ns_template.format(old_ver))
NEW_BRICK = Namespace(brick_ns_template.format(new_ver))
OLD_ROOT = get_root(old_ver)
NEW_ROOT = get_root(new_ver)

g = rdflib.Graph()
g.parse(old_ttl, format='turtle')
g.parse(new_ttl, format='turtle')
g.bind('old_brick', OLD_BRICK)
g.bind('new_brick', NEW_BRICK)
g.bind('rdfs', RDFS)
g.bind('rdf', RDF)
g.bind('owl', OWL)

g.serialize('test.ttl', format='turtle')


def get_tag_sets(root):
    tag_sets = {}
    qstr_allclasses = """
    select ?class where {{
      ?class rdfs:subClassOf+ <{0}>.
    }}
    """
    for row in g.query(qstr_allclasses.format(root)):
        klass = row[0].split('#')[-1]
        tag_set = klass.split('_')  # Tags inside the class name.
        tag_sets[klass] = set(tag_set)
    return tag_sets


old_tag_sets = get_tag_sets(OLD_ROOT)
new_tag_sets = get_tag_sets(NEW_ROOT)

history_dir = 'history/{0}'.format(new_ver)
if not os.path.exists(history_dir):
    os.makedirs(history_dir)

old_classes = set(old_tag_sets.keys())
new_classes = set(new_tag_sets.keys())

with open(history_dir + '/removed_classes.txt', 'w') as fp:
    fp.write('\n'.join(sorted(old_classes - new_classes)))

with open(history_dir + '/added_classes.txt', 'w') as fp:
    fp.write('\n'.join(sorted(new_classes - old_classes)))


# List possible matches for removed classes
mapping_candidates = defaultdict(list)
for old_class, old_tag_set in tqdm(old_tag_sets.items()):
    if old_class in new_tag_sets:
        continue
    for new_class, new_tag_set in new_tag_sets.items():
        # If the delimited tags are similar in the old class and this new class,
        # They might be mappable across the version.
        if len(old_tag_set.intersection(new_tag_set)) / len(old_tag_set.union(new_tag_set)) > 0.7:
            mapping_candidates[old_class].append(new_class)
with open(history_dir + '/possible_mapping.json', 'w') as fp:
    json.dump(mapping_candidates, fp, indent=2)
