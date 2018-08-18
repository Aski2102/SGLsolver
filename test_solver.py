#!/usr/bin/env python3
"""
Testing the SGLsolver's functionality. It performes tests of potential and
eigenvalues for each six sample problems which are saved within the inputfiles
directory.

"""

import os.path
import pytest
import numpy as np
from modules.calculator import sgl_solver

# parametrized tests for all examples for potential
@pytest.mark.parametrize("directory", [
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/infwell'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/harmonic'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/asymmetric'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/finwell'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/doublelin'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/doublespline')])
def test_potential(directory):
    """Testing if the potential is correctly interpolated for six examples.

    Args: directory: directory of inputfile and reference files
                     (given by the parametrization)
    """

    # calculating the interpolated potential with the SGLsolver function
    minmax, _, potwithx, _ = sgl_solver(directory)

    # creating inputfile path for the reference data
    filename = os.path.join(directory, 'potref.dat')

    inputfile = open(filename, "r")
    data = inputfile.readlines()  # reading reference data
    inputfile.close()

    # saving reference x-values and potential from reference data as an array
    potexp = np.zeros((int(minmax[2]), 2), dtype=float)
    for ii in range(0, int(minmax[2])):
        potexp[ii, :] = np.array(data[ii].split(" "), dtype=float)

    # compare reference and calculated data with the allclose function
    # from the numpy module (tolerance one percent)
    assert np.allclose(potwithx, potexp, rtol=0.01, atol=0.01,
                       equal_nan=False)


# parametrized tests for all examples for energies
@pytest.mark.parametrize("directory", [
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/infwell'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/harmonic'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/asymmetric'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/finwell'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/doublelin'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/doublespline')])
def test_energie(directory):
    """Testing if the eigenvalues are correctly calculated for six examples.

    Args: directory: directory of inputfile and reference files
                     (given by the parametrization)
    """

    # calculating the eigenvalues with the SGLsolver function
    _, evalmaxmin, _, eigenval = sgl_solver(directory)

    # creating inputfile path for the reference data
    filename = os.path.join(directory, 'enerref.dat')

    inputfile = open(filename, "r")
    data = inputfile.readlines()  # reading reference data
    inputfile.close()

    # saving reference eigenvalues from reference data as an array
    energieexp = np.zeros((int(evalmaxmin[1] - evalmaxmin[0] + 1), 1),
                          dtype=float)
    for ii in range(0, int(evalmaxmin[1] - evalmaxmin[0] + 1)):
        energieexp[ii, 0] = np.array(data[ii], dtype=float)

    # transpose eigenvalues calculated by the SGLsolver for comparison
    eigenval = np.reshape(eigenval,
                          (int(evalmaxmin[1] - evalmaxmin[0] + 1), 1))

    # compare reference and calculated data with the allclose function
    # from the numpy module (tolerance one percent)
    assert np.allclose(eigenval, energieexp, rtol=0.01, atol=0.01,
                       equal_nan=False)
