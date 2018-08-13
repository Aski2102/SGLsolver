#!/usr/bin/env python3
"""
Executable script for visualizing the results from the SGLsolver.
It plots the potential, energies, wavefunctions and expected values.

"""

import argparse
from modules.visualizer import visualize

PARSER = argparse.ArgumentParser(description='Executes visualizer\
                                              for given input files')
PARSER.add_argument('-d', '--directory', default='',
                    help='Choose directory of the input documents\
                    (default value: .)')
PARSER.add_argument('-sc', '--scaling', default=0.3, type=float,
                    help='Choose scaling factor for the displayed wavefuncs.\
                    (default value: 0.3)')

ARGS = PARSER.parse_args()

visualize(ARGS.directory, ARGS.scaling)
