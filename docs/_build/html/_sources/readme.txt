********************
How to use SGLsolver
********************

.. toctree::

	inputfile
	outputfiles


This document is guide on how to use the SGLsolver.

To run the SGLsolver follow the following steps:

1. In bash move to top level directory of SGLsolver (../SGLsolver)

2. Move your input file named **schrodinger.inp** to a directory 
	of your choice. The results will also be saved in this directory.
	(Explanation on the necessary schrodinger.inp structure in **Inputfile structure**)

3. Execute: **solver.py** (optional arguments: -d [--directory] 'directorypath
			of your input file')

4. Now your outputfiles are saved in the directory.

Optional **visualize your results**:

5. Execute: **visual.py**	 
	(optional arguments:

	* -d [--directory] 'directorypath of your input file'
	* -sc [--scaling] 'scaling factor for rescaling the wavefunctions')

6. The graphics are saved in the directory as *curves.pdf* .


The SGLsolver solves the schrodinger equation for a given problem
specified in the inputfile **schrodinger.inp**.
The input file necessarily has to have a certain structure. See also **Inputfile structure**.

Further information to the outputfiles can be seen in **Outputfiles**.
