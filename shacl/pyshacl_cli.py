#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse

from pyshacl import validate
from pyshacl.errors import ReportableRuntimeError, ValidationFailure

parser = argparse.ArgumentParser(description='Run the pySHACL validator from the command line.')
parser.add_argument('data', metavar='DataGraph', type=argparse.FileType('rb'),
                    help='The file containing the Target Data Graph.')
parser.add_argument('-s', '--shacl', dest='shacl', action='store', nargs='?',
                    help='A file containing the SHACL Shapes Graph.')
parser.add_argument('-e', '--ont-graph', dest='ont', action='store', nargs='?',
                    help='A file path or URL to a docucument containing extra ontological information to mix into the data graph.')
parser.add_argument('-i', '--inference', dest='inference', action='store',
                    default='none', choices=('none', 'rdfs', 'owlrl', 'both'),
                    help='Choose a type of inferencing to run against the Data Graph before validating.')
parser.add_argument('-m', '--metashacl', dest='metashacl', action='store_true',
                    default=False, help='Validate the SHACL Shapes graph against the shacl-shacl '
                    'Shapes Graph before before validating the Data Graph.')
parser.add_argument('--imports', dest='imports', action='store_true',
                    default=False, help='Allow import of sub-graphs defined in statements with owl:import.')
parser.add_argument('-a', '--advanced', dest='advanced', action='store_true',
                    default=False, help='Enable features from the SHACL Advanced Features specification.')
parser.add_argument('--abort', dest='abort', action='store_true',
                    default=False, help='Abort on first error.')
parser.add_argument('-d', '--debug', dest='debug', action='store_true',
                    default=False, help='Output additional runtime messages.')
parser.add_argument('-f', '--format', dest='format', action='store',
                    help='Choose an output format. Default is \"human\".',
                    default='human', choices=('human', 'turtle', 'xml', 'json-ld', 'nt', 'n3'))
parser.add_argument('-df', '--data-file-format', dest='data_file_format', action='store',
                    help='Explicitly state the RDF File format of the input DataGraph file. Default=\"auto\".',
                    default='auto', choices=('auto', 'turtle', 'xml', 'json-ld', 'nt', 'n3'))
parser.add_argument('-sf', '--shacl-file-format', dest='shacl_file_format', action='store',
                    help='Explicitly state the RDF File format of the input SHACL file. Default=\"auto\".',
                    default='auto', choices=('auto', 'turtle', 'xml', 'json-ld', 'nt', 'n3'))
parser.add_argument('-ef', '--ont-file-format', dest='ont_file_format', action='store',
                    help='Explicitly state the RDF File format of the extra ontology file. Default=\"auto\".',
                    default='auto', choices=('auto', 'turtle', 'xml', 'json-ld', 'nt', 'n3'))
parser.add_argument('-o', '--output', dest='output', nargs='?', type=argparse.FileType('w'),
                    help='Send output to a file (defaults to stdout).',
                    default=sys.stdout)


def main():
    args = parser.parse_args()

    validator_kwargs = {'debug': args.debug}
    if args.shacl is not None:
        validator_kwargs['shacl_graph'] = args.shacl
    if args.ont is not None:
        validator_kwargs['ont_graph'] = args.ont
    if args.format != 'human':
        validator_kwargs['serialize_report_graph'] = args.format
    if args.inference != 'none':
        validator_kwargs['inference'] = args.inference
    if args.imports:
        validator_kwargs['do_owl_imports'] = True
    if args.metashacl:
        validator_kwargs['meta_shacl'] = True
    if args.advanced:
        validator_kwargs['advanced'] = True
    if args.abort:
        validator_kwargs['abort_on_error'] = True
    if args.shacl_file_format:
        f = args.shacl_file_format
        if f != "auto":
            validator_kwargs['shacl_graph_format'] = f
    if args.ont_file_format:
        f = args.ont_file_format
        if f != "auto":
            validator_kwargs['ont_graph_format'] = f
    if args.data_file_format:
        f = args.data_file_format
        if f != "auto":
            validator_kwargs['data_graph_format'] = f
    try:
        is_conform, v_graph, v_text = validate(args.data, **validator_kwargs)
        if isinstance(v_graph, BaseException):
            raise v_graph
    except ValidationFailure as vf:
        args.output.write("Validator generated a Validation Failure result:\n")
        args.output.write(str(vf.message))
        sys.exit(1)
    except ReportableRuntimeError as rre:
        sys.stderr.write("Validator encountered a Runtime Error:\n")
        sys.stderr.write(str(rre.message))
        sys.stderr.write("If you believe this is a bug in pyshacl, open an Issue on the pyshacl github page.\n")
        sys.exit(2)
    except NotImplementedError as nie:
        sys.stderr.write("Validator feature is not implemented:\n")
        sys.stderr.write(str(nie.args[0]))
        sys.stderr.write("If your use-case requires this feature, open an Issue on the pyshacl github page.\n")
        sys.exit(3)
    except RuntimeError as re:
        sys.stderr.write("Validator encountered a Runtime Error.")
        sys.exit(2)

    if args.format == 'human':
        args.output.write(v_text)
    else:
        if isinstance(v_graph, bytes):
            v_graph = v_graph.decode('utf-8')
        args.output.write(v_graph)
    args.output.close()
    if is_conform:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
