#!/usr/bin/env python3
"""
Solver for the eigenvalue problem

    This module creates and solves the eigenvalue problem for the solution of the
    schrodingerequation.

@author: charlotte
"""

import numpy as np
import scipy as sp

#variables that actually come from the other modules
N = 10
mass = 2
xmax = 2
xmin = -2
PotV_t = np.zeros((N,), dtype=float)
evalmaxmin = np.array([1, 5], dtype=float)
xnew = np.linspace(xmin, xmax, N)

#newly defined variables for solving the eigenvalue problem
delta = (xmax - xmin) / (N - 1)
aa = 1/(mass*(delta)**2)
#matrice diagonal and offdiagonal for the eigenvalue problem
ond = aa + PotV_t
ofd = -1/2*aa * np.ones((N-1,), dtype=float)

matrix = np.diag(ond, k=0) + np.diag(ofd, k=1) + np.diag(ofd, k=-1)

#solving the problem with the scipy function linalg.eigh
eigenval, eigenvec = sp.linalg.eigh(matrix, b=None, lower=True,
                                    eigvals_only=False, overwrite_a=False,
                                    overwrite_b=False,
                                    eigvals=(evalmaxmin[0]-1,
                                             evalmaxmin[1]-1))

#calculating the norm and the normalized eigenvectors
deltavec = delta * np.ones((1, N), dtype=float)
eigenvec2 = eigenvec**2
norm2 = np.dot(deltavec, eigenvec2)

norm = 1 / (norm2 ** 0.5)
eigenvec_n = np.dot(eigenvec,
                    np.diag(np.reshape(norm, (len(eigenval), )), k=0))

#creating the matrices that are supposed to be saved
energie = np.reshape(eigenval, (len(eigenval), 1))

xnew_t = np.reshape(xnew, (N, 1))
wavefuncs = np.hstack((xnew_t, eigenvec_n))

#saving energies and wavefunctions in textdocuments
np.savetxt("energies.dat", energie)
np.savetxt("wavefuncs.dat", wavefuncs)
