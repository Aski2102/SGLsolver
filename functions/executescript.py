#!/usr/bin/env python3
"""
Executable script for solving the schrodinger equation

@author: timo
"""


def SGLsolver(directory):
    """Reads input file and solves the schrodinger equation for the problem.
       It saves the interpolated potential, the wavefunctions, eigenvalues,
       expected value and the uncertainty of of the x-coordinate in separate
       text documents.

    Args:
        directory: directory where inputfile is saved
        and outputfiles will be saved

    Returns:

    """
    import functions.functions
    import os.path
    import numpy as np

    mass, minmax, evalmaxmin, iptype, ipoints =\
        functions.functions._inputreader(directory)

    potwithx = functions.functions._interpolation(minmax, ipoints, iptype)
    np.savetxt(os.path.join(directory, "potential.dat"), potwithx)

    eigenval, wavefuncs, expvalues =\
        functions.functions._eigensolver(evalmaxmin, mass)
    np.savetxt(os.path.join(directory, "energies.dat"), eigenval)
    np.savetxt(os.path.join(directory, "wavefuncs.dat"), wavefuncs)
    np.savetxt(os.path.join(directory, "expvalues.dat"), expvalues)

    return()


def visualizer():
    """Visualizes the results from the SGLsolver. It reads the textdocuments of
    potential, energies, wavefunctions and expected values and makes plotts.

    Args:

    Returns:

    """
    import functions.visualizer

    functions.visualizer._visualizer()

    return()

#directory=''
#SGLsolver(directory)
#visualizer()
