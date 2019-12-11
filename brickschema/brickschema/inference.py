# This file provides inference of Brick entities from sets of tags.
# Currently assumes that all tags are Brick tags

import pkgutil
from .namespaces import BRICK, A
from .graph import Graph
from collections import defaultdict
from rdflib import Namespace


class TagInferenceSession:
    """
    Provides methods and an interface for inferring Brick classes from
    sets of Brick tags. If you want to work with non-Brick tags, you
    will need to use a wrapper class (see HaystackInferenceSession)
    """

    def __init__(self):
        """
        Creates new Tag Inference session
        """
        self.g = Graph(load_brick=True)
        self.lookup = defaultdict(set)
        self._make_tag_lookup()

    def _make_tag_lookup(self):
        import pickle
        # get ontology data from package
        data = pkgutil.get_data(__name__, "ontologies/taglookup.pickle")
        self.lookup = pickle.loads(data)
        return

        res = self.g.query("""SELECT ?class ?p ?o ?restrictions WHERE {
          ?class rdfs:subClassOf+ brick:Class.
          ?class owl:equivalentClass ?restrictions.
          ?restrictions owl:intersectionOf ?inter.
          ?inter rdf:rest*/rdf:first ?node.
          {
              BIND (brick:hasTag as ?p)
              ?node owl:onProperty ?p.
              ?node owl:hasValue ?o.
          } UNION {
              BIND (brick:measures as ?p)
              ?node owl:onProperty ?p.
              ?node owl:hasValue ?o.
          }
        }""")
        class2tag = defaultdict(set)
        for (cname, p, o, rest) in res:
            cname = cname.split('#')[1]
            o = o.split('#')[1]
            if p == BRICK.hasTag:
                class2tag[cname].add(o)
        for cname, tagset in class2tag.items():
            self.lookup[tuple(tagset)].add(cname)

    def lookup_tagset(self, tagset):
        """
        Returns the Brick classes and tagsets that are supersets OR
        subsets of the given tagsets

        Args:
            tagset (list of str): a list of tags
        """
        s = set(map(lambda x: x[0].upper() + x[1:], tagset))
        return [(klass, tagset) for tagset, klass in self.lookup.items()
                if s.issuperset(set(tagset)) or s.issubset(set(tagset))]

    # TODO: save for haystack
    # s = set(map(lambda x: tagmap[x.lower()] if x in tagmap else x, orig_s))
    def most_likely_tagsets(self, orig_s):
        s = set(map(lambda x: x[0].upper() + x[1:], orig_s))
        tagsets = [(klass, set(tagset)) for tagset, klass
                   in self.lookup.items()
                   if s.issuperset(set(tagset)) or s.issubset(set(tagset))]
        if len(tagsets) == 0:
            # no tags
            return [], orig_s
        # find the highest number of tags that overlap
        most_overlap = max(map(lambda x: len(s.intersection(x[1])), tagsets))

        # return the class with the fewest tags >= the overlap size
        candidates = list(filter(lambda x:
                                 len(s.intersection(x[1])) == most_overlap,
                                 tagsets))

        # When calculating the minimum difference, we calculate it form the
        # perspective of the candidate tagsets because they will have more tags
        # We want to find the tag set(s) who has the fewest tags over what was
        # provided
        min_difference = min(map(lambda x: len(x[1].difference(s)),
                                 candidates))
        most_likely = list(filter(lambda x:
                                  len(x[1].difference(s)) == min_difference,
                                  candidates))

        leftover = s.difference(most_likely[0][1])
        most_likely_classes = [list(x[0])[0] for x in most_likely]
        # return most likely classes (list) and leftover tags
        # (what of 'orig_s' wasn't used)
        return most_likely_classes, leftover


class HaystackInferenceSession(TagInferenceSession):
    """
    Wraps TagInferenceSession to provide inference of a Brick model
    from a Haystack model. The haystack model is expected to be encoded
    as a dictionary with the keys "cols" and "rows"; I believe this is
    a standard Haystack JSON export.
    TODO: double check this
    """

    def __init__(self):
        super(HaystackInferenceSession, self).__init__()
        self._tagmap = {
            'cmd': 'command',
            'sp': 'setpoint',
            'temp': 'temperature',
            'lights': 'lighting',
            'rtu': 'RTU',
            'ahu': 'AHU',
            'freq': 'frequency',
            'equip': 'equipment',
        }
        self._filters = [
                lambda x: not x.startswith('his'),
                lambda x: not x.endswith('Ref'),
                lambda x: not x.startswith('cur'),
                lambda x: x != ('disMacro'),
                lambda x: x != 'navName',
                lambda x: x != 'tz',
                lambda x: x != 'mod',
                lambda x: x != 'id',
                ]
        self._point_tags = ['point', 'sensor', 'command', 'setpoint', 'alarm',
                            'status', 'parameter', 'limit']

    def infer_entity(self, tagset, namespace, identifier=None):
        """
        Produces the Brick triples representing the given Haystack tag set

        Args:
            tagset (list of str): a list of tags representing a Haystack entity
            namespace (str): namespace into which the inferred
                             Brick entities are deposited

        Keyword Args:
            identifier (str): if provided, use this identifier for the entity,
                              otherwise, generate a random string.
        """
        triples = []
        infer_results = []
        BLDG = Namespace(namespace)
        if identifier is None:
            raise Exception("PROVIDE IDENTIFIER")

        non_point_tags = set(tagset).difference(self._point_tags)
        non_point_tags.add('equip')
        inferred_equip_classes, leftover_equip = \
            self.most_likely_tagsets(non_point_tags)

        # choose first class for now
        equip_entity_id = identifier.replace(' ', '_') + '_equip'
        point_entity_id = identifier.replace(' ', '_') + '_point'

        # check if this is a point; if so, infer what it is
        if set(tagset).intersection(self._point_tags):
            if 'point' in tagset:
                tagset.remove('point')
            inferred_point_classes, leftover_points = \
                self.most_likely_tagsets(tagset)
            triples.append((BLDG[point_entity_id], A,
                            BRICK[inferred_point_classes[0]]))
            infer_results.append(
                (identifier, list(tagset), inferred_point_classes)
            )

        if len(inferred_equip_classes) > 0 and \
           inferred_equip_classes[0] != 'Equipment':
            triples.append((BLDG[equip_entity_id], A,
                           BRICK[inferred_equip_classes[0]]))
            triples.append((BLDG[equip_entity_id], BRICK.hasPoint,
                           BLDG[point_entity_id]))
            infer_results.append(
                (identifier, list(tagset), inferred_equip_classes)
            )
        return triples, infer_results

    def infer_model(self, model, namespace):
        """
        Produces the inferred Brick model from the given Haystack model

        Args:
            model (dict): a Haystack model
            namespace (str): namespace into which the inferred
                             Brick entities are deposited
        """
        entities = model['rows']
        # index the entities by their ID field
        entities = {e['id'].replace('"', ''): {'tags': e} for e in entities}
        BLDG = Namespace(namespace)
        brickgraph = Graph(load_brick=True)

        # marker tag pass
        for entity_id, entity in entities.items():
            marker_tags = {k for k, v in entity['tags'].items()
                           if v == 'm:' or v == 'M'}
            for f in self._filters:
                marker_tags = list(filter(f, marker_tags))
            # translate tags
            entity_tagset = list(map(lambda x: self._tagmap[x]
                                     if x in self._tagmap else x, marker_tags))
            # infer tags for single entity
            triples, _ = self.infer_entity(entity_tagset, namespace,
                                           identifier=entity_id)
            brickgraph.add(*triples)

        # take a pass through for relationships
        for entity_id, entity in entities.items():
            relships = {k: v for k, v in entity['tags'].items()
                        if k.endswith('Ref')}
            # equip_entity_id = entity_id.replace(' ', '_') + '_equip'
            point_entity_id = entity_id.replace(' ', '_') + '_point'
            if 'equipRef' not in relships:
                continue
            reffed_equip = relships['equipRef'].replace(' ', '_')\
                                               .replace('"', '') + '_equip'
            if BLDG[point_entity_id] in brickgraph.nodes:
                brickgraph.add((BLDG[reffed_equip], BRICK.hasPoint,
                                BLDG[point_entity_id]))
        return brickgraph
