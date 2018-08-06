#!/usr/bin/env python3
"""
Created on Mon Aug  6 03:05:23 2018
Module forsolving the Schrodinger equation
for a problem given by an input file

@author: timo
"""

import numpy as np
import scipy as sp
import scipy.interpolate as spip


def inputreader():
    inputfile = open("schrodinger1.inp", "r")
    data = inputfile.readlines()  # reading input file
    inputfile.close()

    # declaring variables

    mass = float(data[0].split("#")[0].strip())  # mass

    minmax = np.array(data[1].split(" ")[0:3], dtype=float)
    # xMin xMax nPoints

    evalmaxmin = np.array(data[2].split(" ")[0:2], dtype=float)
    # first and last eigenvalue

    iptype = data[3].split("#")[0].strip()  # interpolation type

    nip = int(data[4].split("#")[0].strip())  # number of interpolation points

    ipoints = np.zeros((int(nip), 2), dtype=float)
    for ii in range(0, nip):    # interpolation points in an array
        ipoints[ii, :] = np.array(data[5+ii].split(" "), dtype=float)

    return (mass, minmax, evalmaxmin, iptype, nip, ipoints)


def interpolation(minmax, ipoints, iptype):

    # Extracting x and y values from the input file
    # for the interpolation function
    x = ipoints[:, 0]
    y = ipoints[:, 1]

    # Setting up the intervall for the interpolated potential
    xnew = np.linspace(minmax[0], minmax[1], minmax[2])

    # Depending on the type of interpolation given by the user
    # creating the interpolation function and defining the potential
    if iptype == 'linear':
        fl = spip.interp1d(x, y, kind='linear')
        PotV = fl(xnew)
    elif iptype == 'cspline':
        if np.shape(x)[0] < 4:
            # For less than four points cubic interpolation isn't possible.
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

    # Changing the row vectors to column vectors and stacking them to a matrice
    xnew_t = np.reshape(xnew, (minmax[2], 1))
    PotV_t = np.reshape(PotV, (minmax[2], 1))

    Potwithx = np.hstack((xnew_t, PotV_t))

    # Saving the potential within a textdocument
    np.savetxt("potential.dat", Potwithx)

    return ()


def eigensolver(evalmaxmin, mass):
    inputfile = open("potential.dat", "r")
    data = inputfile.readlines()  # reading input file
    inputfile.close()

    # variables that actually come from the other modules
    N = np.shape(data)[0]
    PotV = np.zeros((N, ), dtype=float)
    xx = np.zeros((N, ), dtype=float)
    for ii in range(0, N):    # interpolation points in an array
        PotV[ii, ] = np.array(data[ii].split(" ")[1], dtype=float)
        xx[ii, ] = np.array(data[ii].split(" ")[0], dtype=float)

    xmax = xx[N-1, ]
    xmin = xx[0, ]

    # newly defined variables for solving the eigenvalue problem
    delta = (xmax - xmin) / (N - 1)
    aa = 1/(mass*(delta)**2)

    # matrice diagonal and offdiagonal for the eigenvalue problem
    ond = aa + PotV
    ofd = -1/2*aa * np.ones((N-1,), dtype=float)

    matrix = np.diag(ond, k=0) + np.diag(ofd, k=1) + np.diag(ofd, k=-1)


   # solving the problem with the scipy function linalg.eigh
    eigenval, eigenvec = sp.linalg.eigh(matrix, b=None, lower=True,
                                        eigvals_only=False, overwrite_a=False,
                                        overwrite_b=False,
                                        eigvals=(evalmaxmin[0]-1,
                                                 evalmaxmin[1]-1))

    # calculating the norm and the normalized eigenvectors
    deltavec = delta * np.ones((1, N), dtype=float)
    eigenvec2 = eigenvec**2
    norm2 = np.dot(deltavec, eigenvec2)

    norm = 1 / (norm2 ** 0.5)
    eigenvec_n = np.dot(eigenvec,
                    np.diag(np.reshape(norm, (len(eigenval), )), k=0))

    # creating the matrix that is supposed to be saved
    xx_t = np.reshape(xx, (N, 1))
    wavefuncs = np.hstack((xx_t, eigenvec_n))


   # saving energies and wavefunctions in textdocuments
    np.savetxt("energies.dat", eigenval)
    np.savetxt("wavefuncs.dat", wavefuncs)
    
    # calculating related quantities
    expecx = delta*np.dot(xnew, eigenvec_n**2)
    expecx2 = delta*np.dot(xnew**2, eigenvec_n**2)
    uncer = np.sqrt(expecx2 - expecx**2)

    # creating matrix and saving it in expvalues.dat
    expvalues = np.hstack((np.reshape(expecx,(len(eigenval), 1)),
                           np.reshape(uncer,(len(eigenval), 1))))

    np.savetxt("expvalues.dat", expvalues)

    return(wavefuncs, eigenval)

wavefuncs, eigenval = eigensolver(evalmaxmin, mass)
