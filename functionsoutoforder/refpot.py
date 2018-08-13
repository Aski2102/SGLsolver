# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 16:57:57 2018

@author: charlotte
"""
import numpy as np

potexp1 = np.zeros((1999, 2), dtype=float)
potexp1[:, 0] = np.linspace(-2, 2, 1999)

np.savetxt("potref.dat", potexp1)


#potexp1 = np.zeros((1999, 2), dtype=float)
#potexp1[:, 0] = np.linspace(-2, 2, 1999)
#
#potexp2 = np.zeros((1999, 2), dtype=float)
#potexp2[:, 0] = np.linspace(-5, 5, 1999)
#potexp2[:, 1] = (np.linspace(-5, 5, 1999)) ** 2 / 2
#

