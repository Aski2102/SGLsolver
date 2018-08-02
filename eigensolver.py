#!/usr/bin/env python3
"""
Solver for the eigenvalue problem

    This module creates and solves the eigenvalue problem for the solution of the
    schrodingerequation.

@author: charlotte
"""
import scipy.linalg
import numpy as np
#from scipy.linalg import eigh_tridiagonal

N = 10
mass = 2
xmax = 2
xmin = -2
PotV_t = np.zeros((N,), dtype=float)
evalmaxmin = np.array([1, 5], dtype=float)


delta = (xmax - xmin) / (N - 1)
aa = 1/(mass*(delta)**2)

diag = aa + PotV_t
ofdiag = -1/2*aa * np.ones((N-1,), dtype=float)

eigenval, eigenvec = scipy.linalg.eigh_tridiagonal(diag, ofdiag, eigvals_only=False,
                                      select='v',
                                      select_range=((evalmaxmin[0] - 1),
                                                    evalmaxmin[1]),
                                      check_finite=True, tol=0.0,
                                      lapack_driver='auto')

print(eigenval, eigenvec)
