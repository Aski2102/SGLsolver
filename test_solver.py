#!/usr/bin/env python3
"""
First test try

@author: timo
"""

import os.path
import pytest
import numpy as np
from functions.executer import SGLsolver

# parametrized tests for all examples
@pytest.mark.parametrize("directory", [
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/infwell'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/harmonic'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/asymmetric'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/finwell'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/doublelin'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/doublespline')])
def test_potential(directory):
    """Testing the potential"""

    minmax, _, potwithx, _ = SGLsolver(directory)

    filename = os.path.join(directory, 'potref.dat')

    inputfile = open(filename, "r")
    data = inputfile.readlines()  # reading input file
    inputfile.close()

    potexp = np.zeros((int(minmax[2]), 2), dtype=float)
    for ii in range(0, int(minmax[2])):    # interpolation points in an array
        potexp[ii, :] = np.array(data[ii].split(" "), dtype=float)

    assert np.allclose(potwithx, potexp, rtol=0.01, atol=0.01,
                       equal_nan=False)


@pytest.mark.parametrize("directory", [
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/infwell'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/harmonic'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/asymmetric'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/finwell'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/doublelin'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/doublespline')])
def test_energie(directory):
    """Testing the eigenvalues"""

    _, evalmaxmin, _, eigenval = SGLsolver(directory)

    filename = os.path.join(directory, 'enerref.dat')

    inputfile = open(filename, "r")
    data = inputfile.readlines()  # reading input file
    inputfile.close()

    energieexp = np.zeros((int(evalmaxmin[1] - evalmaxmin[0] + 1), 1),
                          dtype=float)
    for ii in range(0, int(evalmaxmin[1] - evalmaxmin[0] + 1)):
        energieexp[ii, 0] = np.array(data[ii], dtype=float)

    eigenval = np.reshape(eigenval,
                          (int(evalmaxmin[1] - evalmaxmin[0] + 1), 1))

    assert np.allclose(eigenval, energieexp, rtol=0.01, atol=0.01,
                       equal_nan=False)
