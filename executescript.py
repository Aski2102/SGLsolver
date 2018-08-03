#!/usr/bin/env python3
"""
Executable script for solving the schrodinger equation

@author: timo
"""

import numpy as np
import scipy as sp
import scipy.interpolate as spip


def SGLsolver():
    """Reads input file and solves the schrodinger equation for the problem.
       It saves the interpolated potential, the wavefunctions, eigenvalues,
       expected value and the uncertainty of of the x-coordinate in separate
       text documents.

    Args:

    Returns:

    """
    import functions.functions

    mass, minmax, evalmaxmin, iptype, ipoints = functions.functions._inputreader()

    #potwithx =
    functions.functions._interpolation(minmax, ipoints, iptype)
    # np.savetxt("potential.dat", potwithx)

    #eigenval, wavefuncs, expvalues = functions.functions._eigensolver(evalmaxmin, mass)
#    np.savetxt("energies.dat", eigenval)
#    np.savetxt("wavefuncs.dat", wavefuncs)
#    np.savetxt("expvalues.dat", expvalues)

    functions.functions._eigensolver(evalmaxmin, mass)

    return()

SGLsolver()

