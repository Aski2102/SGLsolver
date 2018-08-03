#!/usr/bin/env python3
"""
Executable script for solving the schrodinger equation

@author: timo
"""

import numpy as np
import scipy as sp
import scipy.interpolate as spip
from functionsforSGLsolver.py import inputreader, interpolation, eigensolver

mass, minmax, evalmaxmin, iptype, nip, ipoints = inputreader()

interpolation(minmax, ipoints, iptype)

wavefuncs, eigenval = eigensolver(evalmaxmin, mass)
