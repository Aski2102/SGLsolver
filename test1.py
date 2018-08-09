#!/usr/bin/env python3
"""
First test try

@author: timo
"""

import functions.functions
import numpy as np
import os.path
import pytest

potexp1 = np.zeros((1999, 2), dtype=float)
potexp1[:, 0] = np.linspace(-2, 2, 1999)

potexp2 = np.zeros((1999, 2), dtype=float)
potexp2[:, 0] = np.linspace(-5, 5, 1999)
potexp2[:, 1] = (np.linspace(-5, 5, 1999)) ** 2 / 2


#@pytest.mark.parametrize("directory, potexp", [
#    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/infwell', potexp1),
#    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/harmonic', potexp2)])
def test_potential():
    """Testing the potential"""

    # print("Potential test: infinite well")
    directory = '/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/harmonic'

    mass, minmax, evalmaxmin, iptype, ipoints =\
        functions.functions._inputreader(directory)
    potwithx = functions.functions._interpolation(minmax, ipoints, iptype)

    potexp2 = np.zeros((1999, 2), dtype=float)
    potexp2[:, 0] = np.linspace(-5, 5, 1999)
    potexp2[:, 1] = (np.linspace(-5, 5, 1999)) ** 2 / 2

    assert np.allclose(potwithx, potexp2, rtol=0.01, atol=0.01,
                       equal_nan=False)

#Infinite well
energieexp1 = np.zeros((1, 5), dtype=float)
for ii in range(5):
    energieexp1[0, ii] = np.pi ** 2 / (2 * mass *
                                       ((minmax[1] - minmax[0]) ** 2))\
                                       * ((ii + 1) ** 2)


#@pytest.mark.parametrize("directory, potexp", [
#    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/infwell', energieexp1),
#    ('/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/harmonic', potexp2)])
def test_energie():
    """Testing the eigenvalues"""

    directory = '/home/charlotte/Abschlussprojekt/SGLsolver/inputfiles/harmonic'

    mass, minmax, evalmaxmin, iptype, ipoints =\
        functions.functions._inputreader(directory)

    potwithx = functions.functions._interpolation(minmax, ipoints, iptype)
    np.savetxt(os.path.join(directory, "potential.dat"), potwithx)

    eigenval, wavefuncs, expvalues =\
        functions.functions._eigensolver(evalmaxmin, mass, directory)

    energieexp2 = np.zeros((1, 5), dtype=float)
    for ii in range(5):
        energieexp2[0, ii] = (ii + 1/2)/2

 #   eigenval = np.reshape(eigenval, (5, 1))

    assert np.allclose(eigenval, energieexp2, rtol=0.01, atol=0.01,
                       equal_nan=False)

test_energie()
test_potential()
