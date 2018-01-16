# TwoCompartDilantin.py
# Two Compartment model of drug dosage of dilantin
# Pulse of dosage amount of drug every interval hours
# starting at time start

from math import *
import numpy as np
import matplotlib.pyplot as plt

def myPlot(x,y,x1,x2,xlabel, y1,y2, ylabel, title,filename):
    fig1 = plt.figure()
    plt.xlim(x1,x2)
    plt.ylim(y1, y2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.plot(x,y)
    plt.savefig(filename)
    plt.show()


def OneCompartDilantin(DT=10, simLength=240):
    numIterations = int(simLength / DT) + 1
    iterationsPerSec = int(1 / DT)
    print "t\tDrug in System\tConcentration"
    half_life = 22
    MEC = 10
    MTC = 20
    start = 0
    startIteration = 0
    interval = 8
    intervalIteration = interval * iterationsPerSec
    volume = 2000
    dosage = 100 * 1000
    absorption_fraction = 0.08
    elimination_constant = -log(0.5) / half_life
    drug_in_system = 0

    concentration = drug_in_system / volume
    concentrationLst = [concentration]
    t = 0
    timeLst = [0]
    elimination = elimination_constant * drug_in_system

    if (t == start):
        pulse = True
    else:
        pulse = False
    print '%10.2f\t%12.2f\t%12.2f' % (t, drug_in_system, concentration)

    for i in range(1, numIterations):
        t = i * DT
        timeLst.append(t)
        if pulse:
            drug_in_system = drug_in_system + absorption_fraction * dosage - (elimination) * DT
        else:
            drug_in_system = drug_in_system - (elimination) * DT
        concentration = drug_in_system / volume
        concentrationLst.append(concentration)
        if ((i - (start * iterationsPerSec)) % (interval * iterationsPerSec) == 0):
            pulse = True
        else:
            pulse = False
        elimination = elimination_constant * drug_in_system

        # Change 100 to a smaller number in the following
        # to display more frequently.
        # For DT = 0.01, displays every 0.01 * 100 = 1 time unit
        if (i % 100 == 0):
            print '%10.2f\t%12.2f\t%12.2f' % (t, drug_in_system, concentration)
    myPlot(timeLst, concentrationLst, min(timeLst), max(timeLst), min(concentrationLst),
           max(concentrationLst), "Dilantin conc. in plasma", "plasma_dilantin1.png")


OneCompartDilantin(0.001, 240)
