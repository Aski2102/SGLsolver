******************
Testing the solver
******************

This document describes how to run pytest on SGLsolver:

1. In bash move to top level directory of SGLsolver (../SGLsolver)

2. execute in bash: **python3 -m pytest**

3. The results of the test will be shown. It takes about 20 seconds.


The test runs some specified schrodinger problems including:

* infinite potential well

* finite potential well

* harmonic oscillator

* double well (with linear potential interpolation)

* double well (with cubic spline interpolation)

* asymmetric potential well

Running pytest will execute the SGLsolvers functions for solving 
the schrodinger problem for any case (see above). 
After solving it, it will compare the calculated results with 
reference data saved in *enerref.dat* and *potref.dat* .