#!/usr/bin/env python3
"""
Read input file

    This module reads the input file and saves all relevant variables

@author: charlotte
"""

import numpy as np
import scipy as sp

inputfile = open("inputfiles/schrodinger1.inp", "r")



data = inputfile.readlines() #reading input file

#declaring variables

mass = float(data[0].split("#")[0].strip()) #mass

minmax = np.array(data[1].split(" ")[0:3], dtype=float) #xMin xMax nPoints

eigenval = np.array(data[2].split(" ")[0:2], dtype=float) #first and last eigenvalue

iptype = data[3].split("#")[0].strip() #interpolation type

nip = int(data[4].split("#")[0].strip()) #number of interpolation points

#ipoints = np.zeros((int(nip),2), dtype=float)
for ii in range(0, nip):            #interpolation points in an array
    ipoints[ii,:] = np.array(data[5+ii].split(" "), dtype=float)


