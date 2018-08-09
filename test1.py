#!/usr/bin/env python3
"""
First test try

@author: timo
"""

import functions.functions
import numpy as np
import os.path


def test_potential_infwell():
    """Testing the potential of the infinite well"""
    
    # print("Potential test: infinite well")
    directory='/home/timo/WiProJekt/SGLsolver/inputfiles/infwell'
    
    mass, minmax, evalmaxmin, iptype, ipoints =\
        functions.functions._inputreader(directory)
    potwithx = functions.functions._interpolation(minmax, ipoints, iptype)
    
    potexp = np.zeros((1999, 2), dtype=float)
    potexp[:, 0] = np.linspace(-2, 2, 1999)
    
    assert np.all(np.abs(potwithx - potexp) < 1e-2)
    
def test_energie_infwell():
    """Testing the eigenvalues for the infinite well"""
    
    directory='/home/timo/WiProJekt/SGLsolver/inputfiles/infwell'
    
    mass, minmax, evalmaxmin, iptype, ipoints =\
        functions.functions._inputreader(directory)

    potwithx = functions.functions._interpolation(minmax, ipoints, iptype)
    np.savetxt(os.path.join(directory, "potential.dat"), potwithx)
    
    eigenval, wavefuncs, expvalues =\
        functions.functions._eigensolver(evalmaxmin, mass, directory)
    
    energieexp = np.zeros((5, 1), dtype=float)
    for ii in range(5):
        energieexp[ii, 0] = np.pi ** 2 / (2 * mass *
                                          ((minmax[1] - minmax[0]) ** 2))\
                                          * ((ii + 1) ** 2)
 
    assert np.all(np.abs(eigenval - energieexp) < 1)

#test_energie_infwell()
test_potential_infwell()

directory='/home/timo/WiProJekt/SGLsolver/inputfiles/infwell'

mass, minmax, evalmaxmin, iptype, ipoints =\
        functions.functions._inputreader(directory)
potwithx = functions.functions._interpolation(minmax, ipoints, iptype)
np.savetxt(os.path.join(directory, "potential.dat"), potwithx)
eigenval, wavefuncs, expvalues =\
        functions.functions._eigensolver(evalmaxmin, mass, directory)
        
energieexp = np.zeros((5, 1), dtype=float)
for ii in range(5):
    energieexp[ii, 0] = np.pi ** 2 / (2 * mass *
                                      ((minmax[1] - minmax[0]) ** 2))\
                                      * ((ii + 1) ** 2)
