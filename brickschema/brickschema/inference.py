# This file provides inference of Brick entities from sets of tags.
# Currently assumes that all tags are Brick tags

from brickschema.namespaces import BRICK
from brickschema.graph import Graph
from collections import defaultdict


class TagInferenceSession:
    def __init__(self):
        """
        Creates new Tag Inference session
        """
        self.g = Graph(load_brick=True)
        self.lookup = defaultdict(set)
        self._make_tag_lookup()

    def _make_tag_lookup(self):
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
