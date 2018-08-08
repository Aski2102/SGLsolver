# -*- coding: utf-8 -*-
"""
Visualizer is supposed to visiualize the graphs from the outputfiles
of the SGLsolver

@author: charlotte
"""

import numpy as np
import matplotlib.pyplot as plt


def _visualizer():
    """Visualizes the results from the SGLsolver. It reads the textdocuments of
    potential, energies, wavefunctions and expected values and makes plotts.

    Args:

    Returns:

    """

    # POTENTIAL

    inputpot = open("potential.dat", "r")
    potdata = inputpot.readlines()  # reading input file
    inputpot.close()

    # creates arrays of potential and xvalues for plotting
    nn = np.shape(potdata)[0]
    pot = np.zeros((nn, ), dtype=float)
    xx = np.zeros((nn, ), dtype=float)
    for ii in range(0, nn):
        pot[ii, ] = np.array(potdata[ii].split(" ")[1], dtype=float)
        xx[ii, ] = np.array(potdata[ii].split(" ")[0], dtype=float)

    # ENERGIE

    inputener = open("energies.dat", "r")
    enerdata = inputener.readlines()  # reading input file
    inputener.close()

    # creates array of energie for plotting
    mm = np.shape(enerdata)[0]
    ener = np.zeros((mm, ), dtype=float)
    for ii in range(0, mm):
        ener[ii, ] = np.array(enerdata[ii], dtype=float)

    # WAVEFUNCS

    inputwave = open("wavefuncs.dat", "r")
    wavedata = inputwave.readlines()  # reading input file
    inputwave.close()

    # creates array of wavefunctions for plotting
    waves = np.zeros((nn, mm), dtype=float)
    for ii in range(0, nn):
        for jj in range(0, mm):
            waves[ii, jj] = np.array(wavedata[ii].split(" ")[jj+1],
                                     dtype=float)

    # EXPVALUES
    inputexp = open("expvalues.dat", "r")
    expdata = inputexp.readlines()  # reading input file
    inputexp.close()

    # creates arrays of uncertainty and expected xvalues for plotting
    expxval = np.zeros((mm, ), dtype=float)
    uncer = np.zeros((mm, ), dtype=float)
    for ii in range(0, mm):
        expxval[ii, ] = np.array(expdata[ii].split(" ")[0], dtype=float)
        uncer[ii, ] = np.array(expdata[ii].split(" ")[1], dtype=float)

    # PLOTTING

    factor = float(input('Factor for nicer dicer? '))

    # FIRST plot: potential, energies, wavefunctions and expected xvalues
    plt.subplot(1, 2, 1)
    plt.title('Potential, eigenstates, <x>', fontsize=14)

    plt.xlabel("x [Bohr]", fontsize=14)
    plt.ylabel("Energy [Hartree]", fontsize=14)

    # add potential
    plt.plot(xx, pot, linewidth=1.5, color='k',
             label='Potential')
    # add energies
    plt.hlines(ener, xx[0]-(xx[nn-1]-xx[0])/10, xx[nn-1]+(xx[nn-1]-xx[0])/10,
               colors='0.8', linestyles='solid', label='Energies')

    # add wavefunctions on height of the corresponding eigenvalue
    for ii in range(0, mm):
        energy = ener[ii]
        wave = waves[:, ii]
        if ii % 2:  # alternating colors for better graphical appearance
            color = "red"
        else:
            color = "blue"
        plt.plot(xx, factor * wave + energy, linewidth=1.0, linestyle="-",
                 color=color)

    # add expected x-value
    plt.scatter(expxval, ener, c='green', marker='x', s=100, linewidths=1)

    # modify axes appearance
    ax = plt.gca()
    ax.set_xlim(xx[0]-(xx[nn-1]-xx[0])/10, xx[nn-1]+(xx[nn-1]-xx[0])/10)
    ax.set_ylim(min(pot)-(max(ener)-min(pot))/10,
                max(ener)+(max(ener)-min(pot))/6)

    plt.tick_params(axis='y', which='both', right=False)
    plt.tick_params(axis='x', which='both', top=False)

    # SECOND plot: energies and uncertainty
    plt.subplot(1, 2, 2)
    plt.title('Uncertainty', fontsize=14)
    plt.xlabel("[Bohr]", fontsize=14)

    # add energies
    plt.hlines(ener, xx[0], 1.1 * xx[nn-1], colors='0.8', linestyles='solid',
               label='Energies')
    # add uncertainty
    plt.scatter(uncer, ener, c='purple', marker='+', s=150, linewidths=2)

    # modify axes appearance
    ax = plt.gca()
    ax.set_xlim(0, 1.1 * xx[nn-1])
    ax.set_ylim(min(pot)-(max(ener)-min(pot))/10,
                max(ener)+(max(ener)-min(pot))/6)

    plt.tick_params(axis='y', which='both', left=False, right=False,
                    labelleft=False)
    plt.tick_params(axis='x', which='both', top=False)

    # Save the curves in a pdf-document
    plt.savefig('curves.pdf', format='pdf')

    return()
