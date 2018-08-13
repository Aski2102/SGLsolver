--------------------
Outputfiles
--------------------


The results from SGLsolver are saved in:

* **potential.dat** (potential interpolated from sample points and referring x values) 

	x1 V(x1) 

	...

	xN V(xN)

* **energies.dat** (eigenvalues representing the energie levels)

	E1

	...

	EM

* **wavefuncs.dat** (normalized eigenvectors representing the wavefunctions)

	x1 wf1(x1) ... wfM(x1)

	...

	xN wf1(xN) ... wfM(xN)

* **expvalues.dat** (expected x value and the spatial uncertainty for every eigenvalue)

	expx1 uncer1

	...

	expxM uncerM

*N* is the number of interpolation points (number of x values).
*M* is the index for the requested eigenvalues (from ... to ...).
*N* and *M* are both specified in the inputfile.
