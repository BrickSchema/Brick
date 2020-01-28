from argparse import ArgumentParser
from rdflib import Graph, Namespace, URIRef, Literal
from logging import getLogger
from os.path import dirname, splitext
import sys
import ntpath

"""
Argument Parsing:
info: log operation description
"""
parser = ArgumentParser(description='Update Brick models.')
parser.add_argument('models', metavar='model', type=str, nargs='+',
                    help='a turtle file with a brick model')
parser.add_argument('--info',
                    help='get information related to ongoing operations', action='store_true')
args = parser.parse_args()


# set log level to INFO if required.
if args.info:
    getLogger().setLevel("INFO")

models=args.models

# deal with one file for now
model = models[0]
(model_name, ext) = splitext(ntpath.basename(model))
parsed_model = model_name + '_prefixed' + ext

model_graph = Graph()
model_graph.parse(model, format='turtle')

findReplace = [(':', '_COLON_'),
               ('/', '_SLASH_'),
               ('%', '_PERCENT_'),
               ('&', '_AMPERSAND_'),
               ('.', '_DOT_'),
               ('[', '_L-BRACKET_'),
               (']', '_R-BRACKET_')]

def replace(term):
  token = str(term)
  if type(term) == URIRef and token.startswith("http") and '#' in token :
    (prefix, name) = token.split('#', 1)
    if len(name) :
      if name[0].isdigit() :
        name = '_' + name
      for find, replace in findReplace :
        name = replace.join(name.split(find))
      return URIRef(prefix + '#' + name)
  return term

print('# of triples:', len(model_graph))
for s, p, o in model_graph :
  replacedS = replace(s)
  replacedP = replace(p)
  replacedO = replace(o)
  if (s, p, o) != (replacedS, replacedP, replacedO) :
    model_graph.add((replacedS, replacedP, replacedO))
    model_graph.remove((s, p, o))

model_graph.serialize(parsed_model, format='turtle')
