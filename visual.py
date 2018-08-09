#!/usr/bin/env python3
"""
Executable script for visualizing the results from the SGLsolver.
It plots the potential, energies, wavefunctions and expected values.

@author: charlotte
"""

import argparse
from functions.executer import visualize

parser = argparse.ArgumentParser(description='Executes visualizer\
                                              for given input files')
parser.add_argument('-d', '--directory', default='',
                    help='Choose directory of the input documents\
                    (default value: .)')
parser.add_argument('-sc', '--scaling', default=0.3, type=float,
                    help='Choose scaling factor for the displayed wavefuncs.\
                    (default value: 0.3)')

args = parser.parse_args()

visualize(args.directory, args.scaling)
