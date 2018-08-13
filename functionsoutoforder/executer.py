#!/usr/bin/env python3
"""
Executable and public module for solving the schrodinger equation

"""


def sgl_solver(directory):
    """Reads input file and solves the schrodinger equation for the problem.
       It saves the interpolated potential, the wavefunctions, eigenvalues,
       expected value and the uncertainty of of the x-coordinate in separate
       text documents.

    Args:
        directory: directory where inputfile is saved
                   and outputfiles will be saved

    Returns:
        minmax: array with minimum x-value, maximum x-value and number of steps
        evalmaxmin: first and last eigenvalue to calculate
        potwithx: array of x-values and potential at that point
        eigenval: calculated eigenvalues in an array

    """
    import functions.functions
    import os.path
    import numpy as np

    mass, minmax, evalmaxmin, iptype, ipoints =\
        functions.functions._inputreader(directory)

    potwithx = functions.functions._interpolation(minmax, ipoints, iptype)
    np.savetxt(os.path.join(directory, "potential.dat"), potwithx)

    eigenval, wavefuncs, expvalues =\
        functions.functions._eigensolver(evalmaxmin, mass, directory)
    np.savetxt(os.path.join(directory, "energies.dat"), eigenval)
    np.savetxt(os.path.join(directory, "wavefuncs.dat"), wavefuncs)
    np.savetxt(os.path.join(directory, "expvalues.dat"), expvalues)

    return(minmax, evalmaxmin, potwithx, eigenval)


def visualize(directory, scaling):
    """Visualizes the results from the SGLsolver. It reads the textdocuments of
    potential, energies, wavefunctions and expected values and makes plots.

    Args:
        directory: directory where inputfile is saved
                   and outputfiles will be saved
        scaling: scaling factor for visualization of the wavefunctions

    Returns:

    """
    import functions.visualizer

    functions.visualizer._visualizer(directory, scaling)

    return()

