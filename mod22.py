from math import *
import numpy as np
import matplotlib.pyplot as plt

def myPlot(t,P,x1,x2,y1,y2,title,filename):
    fig1 = plt.figure()
    plt.xlim(x1,x2)
    plt.ylim(y1, y2)
    plt.xlabel('t')
    plt.ylabel('P')
    plt.title(title)
    plt.plot(t,P)
    plt.savefig(filename)
    plt.show()

#Bacteria Growth Problem - Example is in Module 2.2. of Intro to Computational Sciences

#p =population (# if item)
#p = []
#p_0 initial population at time t_0
p_0=100
#r = constant growth/decay rate (units)
r=0.10
#t = current time (put units here)
#delta_t= time step
delta_t=[1, .5, .1, .05, .01, .005]
#t_0 = start time
t_0=0
t_n=20

for j in range(len(delta_t)):
    p=[]
    t=np.linspace(t_0,t_n+delta_t[j],int((t_n-t_0)/delta_t[j]))
    p.insert(0,p_0)
    growth=0
    for i in range(1,len(t)):
        growth = p[i-1]*r*delta_t[j]
        p.insert(i,p[i-1]+growth)
    title_base = "Bacteria Growth"
    title = title_base + " delta_t = " + str(delta_t[j])
    filename = "mod22_bacteria_growth_" + str(delta_t[j]) + ".png"
    myPlot(t,p,t_0,t_n,0,max(p),title,filename)
    #del t[:]
    del p[:]

