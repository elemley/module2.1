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

#Make Figure 2.3.1 -- specified parameters below
#Logistic Model

#Make Figure 2.3.2 -- specified parameters below
#Logistic Model

#p =population (# if item)
#p = []
#p_0 initial population at time t_0
p_0=20
#r = constant growth/decay rate (units)
r=0.50
#t = current time (put units here)
#delta_t= time step
delta_t=[1, .5, .1]
#t_0 = start time
t_0=0
t_n=16
M = 1000

for j in range(len(delta_t)):
    p=[]
    t=np.linspace(t_0,t_n+delta_t[j],int((t_n-t_0)/delta_t[j]))
    p.insert(0,p_0)
    growth=0
    death=0
    for i in range(1,len(t)):
        growth = p[i-1]*r*delta_t[j]
        #growth = B*D (from notes)
        death = (p[i-1]**2)*r*delta_t[j]/M
        #death = D*P (from notes)
        p.insert(i,p[i-1]+growth-death)
    title_base = "Population Growth (Logistic Model) Fig. 2.3.1"
    title = title_base + " delta_t = " + str(delta_t[j])
    filename = "mod23_pop_growth_" + str(delta_t[j]) + ".png"
    myPlot(t,p,t_0,t_n,0,max(p),title,filename)
    #del t[:]
    del p[:]


#Make Figure 2.3.1 -- specified parameters below
#Logistic Model

