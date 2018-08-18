#!/usr/bin/env python3
"""
Module for solving the Schrodinger equation
for a problem given by an input file

"""

import os.path
import numpy as np
import scipy as sp
import scipy.interpolate as spip


# the underscore defines a function as private
def _inputreader(directory):
    """Reads input file and saves relevant variables.

    Args:
        directory: directory of input file

    Returns:
        mass: mass of the particle
        minmax: minimum and maximum x value and number of steps
        evalmaxmin: first and last eigenvalue
        iptype: type of interpolation
        ipoints: sample points as array
    """

    # creating the full path for reading input file
    file = "schrodinger.inp"
    filename = os.path.join(directory, file)

    inputfile = open(filename, "r")  # open file for reading purpose
    data = inputfile.readlines()  # reading input file linewise, save to array
    inputfile.close()

    # declaring variables from data and saving them to separate arrays
    # data.split cuts the lines in the arrays at the given symbol
    # .strip removes whitespace characters
    mass = float(data[0].split("#")[0].strip())  # mass

    minmax = np.array(data[1].split(" ")[0:3], dtype=float)
    # xMin xMax nPoints

    evalmaxmin = np.array(data[2].split(" ")[0:2], dtype=float)
    # first and last eigenvalue

    iptype = data[3].split("#")[0].strip()  # interpolation type

    nip = int(data[4].split("#")[0].strip())  # number of interpolation points

    ipoints = np.zeros((int(nip), 2), dtype=float)  # create array of zeros
    for ii in range(0, int(nip)):    # interpolation points in an array
        data[5+ii] = ' '.join(data[5+ii].split())
        ipoints[ii, :] = np.array(data[5+ii].split(" "), dtype=float)
        # join sets multiple blankspaces to a single one

    return (mass, minmax, evalmaxmin, iptype, ipoints)


def _interpolation(minmax, ipoints, iptype):
    """Interpolates the potential from sample points and saves it to document

    Args:
        minmax: minimum and maximum x value and number of steps
        ipoints: sample points as array
        iptype: type of interpolation

    Returns:
        potwithx: array of xvalues and interpolated potential

    """

    # Extracting x and y values from the input file sample points
    # saved in ipoints for the interpolation
    xx = ipoints[:, 0]
    yy = ipoints[:, 1]

    # Setting up the intervall for the interpolated potential
    xnew = np.linspace(int(minmax[0]), int(minmax[1]), int(minmax[2]))

    # Depending on the type of interpolation given by the user
    # creating the interpolation function and defining the potential
    if iptype == 'linear':
        fl = spip.interp1d(xx, yy, kind='linear')
        pot = fl(xnew)
    elif iptype == 'cspline':
        if np.shape(xx)[0] < 4:
            # For less than four points cubic interpolation isn't possible.
            fl = spip.interp1d(xx, yy, kind='linear')
            print('Not enough points for cubic interpolation.'
                  ' ''Interpolation type changed to linear.')
            pot = fl(xnew)
        else:
            fc = spip.interp1d(xx, yy, kind='cubic')
            pot = fc(xnew)
    elif iptype == 'polynomial':
        fbar = spip.BarycentricInterpolator(xx, yy)
        pot = fbar(xnew)
    else:
        print('Invalid interpolation type.')

    # Transposing row vectors and stacking them to a matrice
    xnew_t = np.reshape(xnew, (int(minmax[2]), 1))
    pot_t = np.reshape(pot, (int(minmax[2]), 1))

    potwithx = np.hstack((xnew_t, pot_t))

    # potwithx fulfills the saving file requirements
    return potwithx


def _eigensolver(evalmaxmin, mass, directory):
    """Solves the schrodinger problem and calculates derivated quantities

    Args:
        evalmaxmin: first and last eigenvalue
        mass: mass of the particle
        directory: directory of the input file

    Returns:
        eigenval: eigenvalues of the given schrodingerproblem in an array
        wavefuncs: xvalues and corresponding normalized wave functions in an
                    array
        expvalues: expected values and uncertainty in an array

    """
    filename = os.path.join(directory, "potential.dat")
    inputfile = open(filename, "r")
    data = inputfile.readlines()
    inputfile.close()

    # variables that come from the other functions
    nn = np.shape(data)[0]  # number of discrete points
    pot = np.zeros((nn, ), dtype=float)  # data preallocation
    xx = np.zeros((nn, ), dtype=float)
    for ii in range(0, nn):    # extracting x-values and potential points
        pot[ii, ] = np.array(data[ii].split(" ")[1], dtype=float)
        xx[ii, ] = np.array(data[ii].split(" ")[0], dtype=float)

    xmax = xx[nn-1, ]  # minimum and maximum x-value
    xmin = xx[0, ]

    # new variables for solving the eigenvalue problem
    delta = (xmax - xmin) / (nn - 1)
    aa = 1/(mass*(delta)**2)

    # creating matrix for solving the eigenvalue problem
    matrix = np.diag(aa + pot, k=0) +\
        np.diag(-1/2*aa * np.ones((nn - 1,), dtype=float), k=1) +\
        np.diag(-1/2*aa * np.ones((nn - 1,), dtype=float), k=-1)

    # solving the problem with the scipy function linalg.eigh
    eigenval, eigenvec = sp.linalg.eigh(matrix,
                                        eigvals=(int(evalmaxmin[0]-1),
                                                 int(evalmaxmin[1]-1)))
#                                        additional function arguments
#                                        which are currently not necessary
#                                        b=None, lower=True,
#                                        eigvals_only=False, overwrite_a=False,
#                                        overwrite_b=False,

    # calculating the norm and the normalized eigenvectors
    # using clever matrix multiplication(np.dot)
    deltavec = delta * np.ones((1, nn), dtype=float)
    eigenvec2 = eigenvec**2  # the square is executed componentwise
    norm2 = np.dot(deltavec, eigenvec2)

    norm = 1 / (norm2 ** 0.5)
    eigenvec_n = np.dot(eigenvec,  # normalized eigenvector
                        np.diag(np.reshape(norm, (len(eigenval), )), k=0))

    # creating the matrix that is supposed to be saved
    # (x-values and wavefunctions)
    xx_t = np.reshape(xx, (nn, 1))
    wavefuncs = np.hstack((xx_t, eigenvec_n))

    # calculating related quantities (expected x-value and uncertainty)
    expecx = delta*np.dot(xx, eigenvec_n**2)
    expecx2 = delta*np.dot(xx**2, eigenvec_n**2)
    uncer = np.sqrt(expecx2 - expecx**2)

    # creating matrix of these quantities
    expvalues = np.hstack((np.reshape(expecx, (len(eigenval), 1)),
                           np.reshape(uncer, (len(eigenval), 1))))

    return(eigenval, wavefuncs, expvalues)


def sgl_solver(directory):
    """Reads input file and solves the schrodinger equation for the problem.
       It saves the interpolated potential, the wavefunctions, eigenvalues,
       expected value and the uncertainty of of the x-coordinate in separate
       text documents.

    Args:
        directory: directory where inputfile is saved
                   and outputfiles will be saved

    Returns:
        Four arrays with data that is important for testing the solver.

        **minmax:**
            minimum x-value, maximum x-value and number of steps
        **evalmaxmin:**
            first and last eigenvalue to calculate
        **potwithx:**
            array of x-values and potential at that point
        **eigenval:**
            calculated eigenvalues in an array

    """

    # using private inputreader function to extract the necessary data from
    # the input file
    mass, minmax, evalmaxmin, iptype, ipoints = _inputreader(directory)

    # using private interpolation function to interpolate the potential from
    # the given sample points and saving it into a text document
    potwithx = _interpolation(minmax, ipoints, iptype)
    np.savetxt(os.path.join(directory, "potential.dat"), potwithx)

    # calculating eigenvalues, -vectors, uncertainty and expected x-value with
    # the private eigensolver function and saving them into text documents
    eigenval, wavefuncs, expvalues = _eigensolver(evalmaxmin, mass, directory)
    np.savetxt(os.path.join(directory, "energies.dat"), eigenval)
    np.savetxt(os.path.join(directory, "wavefuncs.dat"), wavefuncs)
    np.savetxt(os.path.join(directory, "expvalues.dat"), expvalues)

    return(minmax, evalmaxmin, potwithx, eigenval)
