#!/usr/bin/env python3
"""
Executable script for solving the schrodinger equation for a problem defined
by an input file

@author: charlotte
"""

import argparse
from functions.executescript import SGLsolver

parser = argparse.ArgumentParser(description='Executes SGLsolver\
                                              for given input file')
parser.add_argument('-d', '--directory', default='',
                    help='Choose directory of the input document\
                    (default value: .)')

args = parser.parse_args()

SGLsolver(args.directory)
