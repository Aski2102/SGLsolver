#!/usr/bin/env python3
"""
Executable script for solving the schrodinger equation for a problem defined
by an input file

"""

import argparse
from modules.calculator import sgl_solver

# using argument parser to make the sgl_solver function executable from shell
# with optional input arguments(directory)
PARSER = argparse.ArgumentParser(description='Executes SGLsolver\
                                              for given input file')
PARSER.add_argument('-d', '--directory', default='',
                    help='Choose directory of the input document\
                    (default value: .)')

ARGS = PARSER.parse_args()

sgl_solver(ARGS.directory)
