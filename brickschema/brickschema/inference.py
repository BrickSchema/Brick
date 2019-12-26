# This file provides inference of Brick entities from sets of tags.
# Currently assumes that all tags are Brick tags

import pkgutil
import pickle
from .namespaces import BRICK, A, RDF
from .graph import Graph
from collections import defaultdict
from rdflib import Namespace
import owlrl


class RDFSInferenceSession:
    """
    Provides methods and an inferface for producing the deductive closure
    of a graph under RDFS semantics
    """

    def __init__(self):
        """
        Creates a new RDFS Inference session
        """
        self.g = Graph(load_brick=True)

    def expand(self, graph):
        for triple in graph:
            self.g.add(triple)
        owlrl.DeductiveClosure(owlrl.RDFS_Semantics).expand(self.g)


class OWLRLInferenceSession:
    """
    Provides methods and an inferface for producing the deductive closure
    of a graph under OWL-RL semantics. WARNING this may take a long time
    """

    def __init__(self):
        """
        Creates a new OWLRL Inference session
        """
        self.g = Graph(load_brick=True)

    def expand(self, graph):
        for triple in graph:
            self.g.add(triple)
        owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(self.g)


class InverseEdgeInferenceSession:
    """
    Provides methods and an inferface for producing the deductive closure
    of a graph that adds all properties implied by owl:inverseOf
    """

    def __init__(self):
        """
        Creates a new OWLRL Inference session
        """
        self.g = Graph(load_brick=True)

    def expand(self, graph):
        for triple in graph:
            self.g.add(triple)
        # inverse relationships
        query = """
        INSERT {
            ?o ?invprop ?s
        } WHERE {
            ?s ?prop ?o.
            ?prop owl:inverseOf ?invprop.
        }
        """
        self.g.update(query)


class ManualBrickInferenceSession:
    """
    Provides methods and an inferface for producing the deductive closure
    of a graph under the semantics expected of Brick 1.1. Due to performance
    issues in the OWLRL inference package, this package hard-codes the OWL
    rules required, which runs much faster. However, it may not be 100%
    complete, and we hope to replace it soon.

    - adds inverse edges
    - does a simple tag <--> class inference
    - does a simple substance <--> class inference
    - applies rdfs reasoning (adds in rdf:type edges)
    """

    def __init__(self):
        """
        Creates a new OWLRL Inference session
        """
        self.g = Graph(load_brick=True)

    def _update_inverse_edges(self):
        # inverse relationships
        query = """
        INSERT {
            ?o ?invprop ?s
        } WHERE {
            ?s ?prop ?o.
            ?prop owl:inverseOf ?invprop.
        }
        """
        self.g.update(query)

    def _get_inferred_properties(self):
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
          } UNION {
              BIND (rdf:type as ?p)
              ?node owl:onProperty ?p.
              ?node owl:hasValue ?o.
          }
        }""")
        self.tag_properties = defaultdict(list)
        self.measures_properties = defaultdict(list)
        self.grouped_properties = defaultdict(list)

        for (classname, prop, obj, groupname) in res:
            if prop == BRICK.hasTag:
                self.tag_properties[classname].append(obj)
            elif prop == BRICK.measures:
                self.measures_properties[classname].append(obj)
            self.grouped_properties[(classname, groupname)].append((prop, obj))

    def _add_properties(self):
        # add properties based on classes
        for (classname, groupname), props in self.grouped_properties.items():
            q = "INSERT {\n"
            q += '\n'.join(
                [f"\t ?inst <{prop}> <{obj}> ." for prop, obj in props]
            )
            q += "\n} WHERE {\n"
            q += '\n'.join(
                [f"\t ?inst rdf:type <{classname}> ."]
            )
            q += "\n}"
            self.g.update(q)

        # add properties based on classes
        for (classname, groupname), props in self.grouped_properties.items():
            q = f"""INSERT {{
            ?inst rdf:type <{classname}>
            }} WHERE {{ \n"""
            q += '\n'.join(
                [f"\t ?inst <{prop}> <{obj}> ." for prop, obj in props]
            )
            q += "}\n"
            self.g.update(q)

    def _add_tags(self):
        # tag inference
        for classname, tags in self.tag_properties.items():
            # find entities of the class and add the tags
            qstr = f"""SELECT ?inst WHERE
                {{ ?inst rdf:type/rdfs:subClassOf* <{classname}>
            }}"""
            for row in self.g.query(qstr):
                inst = row[0]
                for tag in tags:
                    self.g.add((inst, BRICK.hasTag, tag))

    def _add_measures(self):
        # measures inference
        for classname, substances in self.measures_properties.items():
            # find entities with substances and instantiate the class
            qstr = "select ?inst where {\n"
            for substance in substances:
                qstr += f"  ?inst brick:measures <{substance}> .\n"
            qstr += "}"
            for row in self.g.query(qstr):
                inst = row[0]
                self.g.add((inst, RDF.type, classname))

            # find entities of the class and add the substances
            qstr = f"""SELECT ?inst WHERE
                {{ ?inst rdf:type/rdfs:subClassOf* <{classname}>
            }}"""
            for row in self.g.query(qstr):
                inst = row[0]
                for substance in substances:
                    self.g.add((inst, BRICK.measures, substance))

    def expand(self, graph):
        for triple in graph:
            self.g.add(triple)
        self._update_inverse_edges()
        self._get_inferred_properties()
        self._add_properties()
        self._add_tags()
        self._add_measures()


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
        # get ontology data from package
        data = pkgutil.get_data(__name__, "ontologies/taglookup.pickle")
        # TODO: move on from moving pickle to something more secure?
        self.lookup = pickle.loads(data)

    def _make_tag_lookup(self):
        """
        Builds taglookup dictionary. You shouldn't need to do this unless
        the taglookup dictionary is out of date
        """
        self.lookup = defaultdict(set)
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

    def most_likely_tagsets(self, orig_s):
        """
        Returns the list of likely classes for a given set of tags,
        as well as the list of tags that were 'leftover', i.e. not
        used in the inference of a class

        Args:
            tagset (list of str): a list of tags

        Returns:
            most_likely_classes (list of str): list of Brick classes
            leftover (set of str): list of tags not used
        """
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

    def __init__(self, namespace):
        """
        Creates a new HaystackInferenceSession that infers entities into
        the given namespace

        Args:
            namespace (str): namespace into which the inferred Brick entities
                             are deposited. Should be a valid URI
        """
        super(HaystackInferenceSession, self).__init__()
        self._BLDG = Namespace(namespace)
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

    def infer_entity(self, tagset, identifier=None):
        """
        Produces the Brick triples representing the given Haystack tag set

        Args:
            tagset (list of str): a list of tags representing a Haystack entity

        Keyword Args:
            identifier (str): if provided, use this identifier for the entity,
                              otherwise, generate a random string.
        """
        triples = []
        infer_results = []
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
            triples.append((self._BLDG[point_entity_id], A,
                            BRICK[inferred_point_classes[0]]))
            infer_results.append(
                (identifier, list(tagset), inferred_point_classes)
            )

        if len(inferred_equip_classes) > 0 and \
           inferred_equip_classes[0] != 'Equipment':
            triples.append((self._BLDG[equip_entity_id], A,
                           BRICK[inferred_equip_classes[0]]))
            triples.append((self._BLDG[equip_entity_id], BRICK.hasPoint,
                           self._BLDG[point_entity_id]))
            infer_results.append(
                (identifier, list(tagset), inferred_equip_classes)
            )
        return triples, infer_results

    def infer_model(self, model):
        """
        Produces the inferred Brick model from the given Haystack model

        Args:
            model (dict): a Haystack model
        """
        entities = model['rows']
        # index the entities by their ID field
        entities = {e['id'].replace('"', ''): {'tags': e} for e in entities}
        brickgraph = Graph(load_brick=True)

        # marker tag pass
        for entity_id, entity in entities.items():
            marker_tags = {k for k, v in entity['tags'].items()
                           if v == 'm:' or v == 'M'}
            for f in self._filters:
                marker_tags = list(filter(f, marker_tags))
            # translate tags
            entity_tagset = list(map(lambda x: self._tagmap[x.lower()]
                                     if x in self._tagmap else x, marker_tags))
            # infer tags for single entity
            triples, _ = self.infer_entity(entity_tagset, identifier=entity_id)
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
            if self._BLDG[point_entity_id] in brickgraph.nodes:
                brickgraph.add((self._BLDG[reffed_equip], BRICK.hasPoint,
                                self._BLDG[point_entity_id]))
        return brickgraph
