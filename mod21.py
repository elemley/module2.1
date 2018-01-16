#Tutorial 1
from math import *

print sin(4)

print "test"
print("test")
print(5/8)

print(5/8.0)

print(1/2.0)**2
print(5*sin(pi/2))

ans = 8*pi

print(ans)

vel = 5.0

print((7+vel/3)**2)

def i(x):
    return x**5


def f(x):
    ans = x**2+1
    return ans

print f(4)

print(f(2.5))

def sum_squares(x,y):
    ans = x**2 + y**2
    return ans

print sum_squares(3,4)

list1=[1,3,5.0]
list2=[1,"one",2,"two"]
list3=[]
print list1, list2, list3

list4 = range(15)
list5=range(5,15)
list6=range(4,15,3)

print list4, list5, list6

dist = 0.0
for item in range(7):
    dist=dist+.25
    print dist

for i in range(10):
    print i, " ", i**2


#Tutorial 2

myList=[1,5,8,10,12]
print len(myList)

print myList[4]

for i in range(len(myList)):
    print myList[i]

myList.append(15)
print myList
#Each point is called a tuple
pointList = [ (1,2),(-1,3),(0,4)]
print pointList
print pointList[1]
print pointList[1][0]

pointList.append((-5,3))
print pointList

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

def g(x):
    return x**4

def h(x):
    return x**6


def getxpoints(a,b,n):
    points = []
    dt = (b-a)/float(n)
    count=0
    x=a
    while count <=n:
        x=a+ count*dt
        points.append(x)
        count+=1
    return points

def getfxpoints(x,f1):
    fxpoints=[]
    for i,xval in enumerate(x):
        fxpoints.append(f1(xval))
    return fxpoints

def myPlot(f1,g1,h1,x1,x2,y1,y2,n):
    fig1 = plt.figure()
    plt.xlim(x1,x2)
    plt.ylim(y1, y2)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('mod2.1')
    xvals = getxpoints(x1,x2,n)
    fxvals = getfxpoints(xvals,f1)
    gxvals = getfxpoints(xvals, g1)
    hxvals = getfxpoints(xvals, h1)
    plt.plot(xvals,fxvals)
    plt.plot(xvals, gxvals)
    plt.plot(xvals, hxvals)
    plt.show()

#myPlot(g,-5,5,-5,5,30)
#myPlot(g,-5,5,-5,5,30)
#myPlot(h,-5,5,-5,5,30)


myPlot(f,g,h,-1,1,-1,1,)





