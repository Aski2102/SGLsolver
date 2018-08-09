#!/usr/bin/env python3
"""
First test try

@author: timo
"""

import functions.functions
import numpy as np
import os.path
import pytest

#potexp1 = np.zeros((1999, 2), dtype=float)
#potexp1[:, 0] = np.linspace(-2, 2, 1999)
#
#potexp2 = np.zeros((1999, 2), dtype=float)
#potexp2[:, 0] = np.linspace(-5, 5, 1999)
#potexp2[:, 1] = (np.linspace(-5, 5, 1999)) ** 2 / 2
#

@pytest.mark.parametrize("directory", [
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/infwell'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/harmonic'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/asymmetric'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/finwell'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/doublelin'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/doublespline')])
def test_potential(directory):
    """Testing the potential"""

    directory = '/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/harmonic'

    mass, minmax, evalmaxmin, iptype, ipoints =\
        functions.functions._inputreader(directory)
    potwithx = functions.functions._interpolation(minmax, ipoints, iptype)

    filename = os.path.join(directory, 'potref.dat')

    inputfile = open(filename, "r")
    data = inputfile.readlines()  # reading input file
    inputfile.close()

    potexp = np.zeros((int(minmax[2]), 2), dtype=float)
    for ii in range(0, int(minmax[2])):    # interpolation points in an array
        potexp[ii, :] = np.array(data[ii].split(" "), dtype=float)

    assert np.allclose(potwithx, potexp, rtol=0.01, atol=0.01,
                       equal_nan=False)

##Infinite well
#energieexp1 = np.zeros((1, 5), dtype=float)
#for ii in range(5):
#    energieexp1[0, ii] = np.pi ** 2 / (2 * mass *
#                                       ((minmax[1] - minmax[0]) ** 2))\
#                                       * ((ii + 1) ** 2)
#    energieexp2 = np.zeros((1, 5), dtype=float)
#    for ii in range(5):
#        energieexp2[0, ii] = (ii + 1/2)/2


@pytest.mark.parametrize("directory", [
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/infwell'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/harmonic'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/asymmetric'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/finwell'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/doublelin'),
    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/doublespline')])
def test_energie(directory):
    """Testing the eigenvalues"""

    directory = '/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/harmonic'

    mass, minmax, evalmaxmin, iptype, ipoints =\
        functions.functions._inputreader(directory)

    potwithx = functions.functions._interpolation(minmax, ipoints, iptype)
    np.savetxt(os.path.join(directory, "potential.dat"), potwithx)

    eigenval, wavefuncs, expvalues =\
        functions.functions._eigensolver(evalmaxmin, mass, directory)

    filename = os.path.join(directory, 'enerref.dat')

    inputfile = open(filename, "r")
    data = inputfile.readlines()  # reading input file
    inputfile.close()

    energieexp = np.zeros((int(evalmaxmin[1] - evalmaxmin[0] + 1), 1), dtype=float)
    for ii in range(0, int(evalmaxmin[1] - evalmaxmin[0] + 1)):    # interpolation points in an array
        energieexp[ii, 0] = np.array(data[ii], dtype=float)

    eigenval = np.reshape(eigenval, (5, 1))

    assert np.allclose(eigenval, energieexp, rtol=0.01, atol=0.01,
                       equal_nan=False)

#test_energie()
#test_potential()
