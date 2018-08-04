#!/usr/bin/env python3
"""
Potential interpolation

    This module will take a set of points given to interpolate them linear, cubic or polynominal.
    The type of interpolation is chosen by the user (given in the inputfile).

 @author: charlotte
"""

import numpy as np
import scipy.interpolate as spip

ipoints = np.array([[-2, 0], [2, 0]], dtype=float)
iptype = 'polynomial'
minmax = np.array([-2, 2, 10], dtype=float)

# Extracting x and y values from the input file for the interpolation function
x = ipoints[:, 0]
y = ipoints[:, 1]

# Setting up the intervall for the interpolated potential
xnew = np.linspace(minmax[0], minmax[1], minmax[2])

#Depending on the type of interpolation given by the user
#creating the interpolation function and defining the potential
if iptype == 'linear':
    fl = spip.interp1d(x, y, kind='linear')
    PotV = fl(xnew)
elif iptype == 'cspline':
    if np.shape(x)[0] < 4: #For less than four points cubic interpolation isn't possible.
        fl = spip.interp1d(x, y, kind='linear')
        print('Not enough points for cubic interpolation.'
              ' ''Interpolation type changed to linear.')
        PotV = fl(xnew)
    else:
        fc = spip.interp1d(x, y, kind='cubic')
        PotV = fc(xnew)
elif iptype == 'polynomial':
    fbar = spip.BarycentricInterpolator(x, y)
    PotV = fbar(xnew)
else:
    print('Invalid interpolation type.')

#Changing the row vectors to column vectors and stacking them to a matrice
xnew_t = np.reshape(xnew, (minmax[2],1))
PotV_t = np.reshape(PotV, (minmax[2],1))

Potwithx = np.hstack((xnew_t, PotV_t))

#Saving the potential within a textdocument
np.savetxt("potential.dat", Potwithx)
