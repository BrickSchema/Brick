import sys
sys.path.append('./')  # Assume that this file is run at the root of the repo.
import os
import pdb
from collections import defaultdict
import json

from tqdm import tqdm
import rdflib
from rdflib import Namespace, URIRef, RDF, RDFS, OWL
from bricksrc.namespaces import BRICK_VERSION

OLD_VERSION = '1.0.3'
NEW_VERSION = BRICK_VERSION

old_ttl = 'https://github.com/BrickSchema/Brick/releases/download/v{0}/Brick.ttl'.format(OLD_VERSION)
new_ttl = 'Brick.ttl'  # The current dev version.
OLD_BRICK = Namespace('https://brickschema.org/schema/{0}/Brick#'.format(OLD_VERSION))
OLD_ROOT = URIRef('https://brickschema.org/schema/{0}/BrickFrame#TagSet'.format(OLD_VERSION))
NEW_BRICK = Namespace('https://brickschema.org/schema/{0}/Brick#'.format(NEW_VERSION))
NEW_ROOT = NEW_BRICK.Class

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

history_dir = 'history/{0}'.format(NEW_VERSION)
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
