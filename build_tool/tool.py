import sys, os
import argparse
from .utils import get_dependencies

def build_parser():
    parser = argparse.ArgumentParser(description='Python SPDX Build Tool Plugin')
    parser.add_argument('--tv', help='output tag-value spdx file', action='store_true')
    parser.add_argument('--rdf', help='output rdf spdx file', action='store_true')
    parser.add_argument('--res', help='Scan python files with reserved names?', action='store_true')
    return parser

def print_arguments(args):
    print("Tag-value?: " + str(args.tv))
    print("RDF?: " + str(args.rdf))
    print("Scan reserved names?: " + str(args.res))

def create_spdx_document(args):
    get_dependencies(args.res)
    
def main(argv):
    parser = build_parser()
    args = parser.parse_args()
    print_arguments(args)
    create_spdx_document(args)

def entry_point():
    """Zero-argument entry point for use with setuptools/distribute."""
    raise SystemExit(main(sys.argv))

if __name__ == '__main__':
    entry_point()
