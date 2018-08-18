--------------------------------
Inputfile structure
--------------------------------

The inputfile has to have the following structure 
(please note that all entries have to be in atomic units):

1. The first line contains **mass of the particle** [as float].

2. In the second line the **minimum and maximum x-value** [as float] 
   are defined next to the wanted **number of x-values** after 
   interpolation [as integer]. (separated via single blank space)

3. The third line contains **first and last eigenvalue** to calculate [as integer].
   (separated via single blank space)

4. In the fourth line the **interpolation type** is declared.
   (possible: linear, cspline, polynomial)

5. The fifth line defines the **number of sample points** for 
   potential interpolation [as integer].

6. All further lines are the **sample points** for the potential. 
   Each line contains one sample point with *x-coordinate* 
   and *potential value*. [as float] (separated via blank spaces)


**Example (infinite well):**

| 2.0            # mass
| -2.0 2.0 1999  # xMin xMax nPoint
| 1 5            # first and last eigenvalue to print
| linear         # interpolation type
| 2              # nr. of interpolation points and xy declarations
| -2.0  0.0
| 2.0  0.0
