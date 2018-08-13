# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 17:08:09 2018

@author: charlotte
"""

import numpy as np

energieexp1 = np.zeros((5, 1), dtype=float)
for ii in range(5):
    energieexp1[ii, 0] = np.pi ** 2 / (2 * 2 *
                                       ((2 + 2) ** 2))\
                                       * ((ii + 1) ** 2)

np.savetxt("enerref.dat", energieexp1)

##Infinite well
#energieexp1 = np.zeros((1, 5), dtype=float)
#for ii in range(5):
#    energieexp1[0, ii] = np.pi ** 2 / (2 * mass *
#                                       ((minmax[1] - minmax[0]) ** 2))\
#                                       * ((ii + 1) ** 2)
#    energieexp2 = np.zeros((1, 5), dtype=float)
#    for ii in range(5):
#        energieexp2[0, ii] = (ii + 1/2)/2
