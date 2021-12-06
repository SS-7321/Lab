# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 20:46:02 2021

@author: Shan
"""

import numpy as np
import matplotlib.pyplot as plt


def LOBF(x, y, std=None):  # Code adapted from A. Golob, "Plotting Data with ErrorBars and Fitting a Line", Ap.smu.ca, 2016. [Online]. Available: http://www.ap.smu.ca/~agolob/phys2300/blog/climate-change/. [Accessed: 25- Oct- 2021]
    #least squares method with errorbars for y only
    if std is None:
        #if no error bars, weight every point the same
        std = np.ones(x.size)
    denom = np.sum(1 / std**2) * np.sum((x / std)**2) - (np.sum(x / std**2))**2
    m = (np.sum(1 / std**2) * np.sum(x * y / std**2) -
         np.sum(x / std**2) * np.sum(y / std**2)) / denom
    yinter = (np.sum(x**2 / std**2) * np.sum(y / std**2) -
         np.sum(x / std**2) * np.sum(x * y / std**2)) / denom
    unc_m = np.sqrt(np.sum(1 / std**2) / denom)
    unc_yinter = np.sqrt(np.sum(x / std**2) / denom)
    return([m, unc_m, yinter, unc_yinter])

def balmer(n,p):
    return (1/n**2)-(1/p**2)

degstd = np.sin(2*0.05*np.pi/180)
truerd = 10973731.6
valD = 10**-3/78.8

resaqua = np.array([0 ,0.057273619 ,0.078459096 ,0.116381831 ,0.155285132 ,-0.040131793 ,-0.070626986 ,-0.119559256 ])
resred = np.array([0 ,0.060177479 ,0.111758003 ,0.159019688 ,0.211040469 ,-0.052335956 ,-0.106553308 ,-0.159306868 ,-0.213030386 ])
#resvio = np.array([0,1.916666667, 4.46666667,6.483333333,8.616666667,-2.1,-4.1,-5.28333333])*(np.pi/180)
resvio = np.array([0 ,0.033445905 ,0.077879099 ,0.112914191 ,0.149822955 ,-0.036643709 ,-0.071497444 ,-0.116381831 ])
xlambda = np.array([0,1,2,3,4,-1,-2,-3,-4])

violine = LOBF(xlambda[:len(xlambda)-1], resvio, np.ones(len(resvio))*degstd)
aqualine = LOBF(xlambda[:len(xlambda)-1], resaqua, np.ones(len(resaqua))*degstd)
redline = LOBF(xlambda, resred, np.ones(len(resred))*degstd)

plt.plot(np.zeros(10),np.linspace(-1, 1, num=10), 'k', lw=1) #y axis
plt.plot(np.linspace(-5, 5, num=10),np.zeros(10), 'k', lw=1)  #x axis
plt.errorbar(xlambda[:len(xlambda)-1], resvio, yerr=degstd, fmt='m.', capsize=5, label="Violet")
plt.plot(np.linspace(-6,6,50),np.linspace(-6,6,50)*violine[0], 'm')
plt.xlabel("Order number")
plt.ylabel("Sine(${\\Theta}$)")
plt.xlim(-4.5, 4.5)
plt.ylim(resvio.min()-(2.5*degstd), resvio.max()+(2.5*degstd))
plt.show()

plt.plot(np.zeros(10),np.linspace(-1, 1, num=10), 'k', lw=1) #y axis
plt.plot(np.linspace(-5, 5, num=10),np.zeros(10), 'k', lw=1)  #x axis
plt.errorbar(xlambda[:len(xlambda)-1], resaqua, yerr=degstd, fmt='c.', capsize=5, label="Aqua")
plt.plot(np.linspace(-6,6,50),np.linspace(-6,6,50)*aqualine[0], 'c')
plt.xlabel("Order number")
plt.ylabel("Sine(${\\Theta}$)")
plt.xlim(-4.5, 4.5)
plt.ylim(resaqua.min()-(2.5*degstd), resaqua.max()+(2.5*degstd))
plt.show()

plt.plot(np.zeros(10),np.linspace(-1, 1, num=10), 'k', lw=1) #y axis
plt.plot(np.linspace(-5, 5, num=10),np.zeros(10), 'k', lw=1)  #x axis
plt.errorbar(xlambda, resred, yerr=degstd, fmt='r.', capsize=5, label="Red")
plt.plot(np.linspace(-6,6,50),np.linspace(-6,6,50)*redline[0], 'r')
plt.xlabel("Order number")
plt.ylabel("Sine(${\\Theta}$)")
plt.xlim(-4.5, 4.5)
plt.ylim(resred.min()-(3*degstd), resred.max()+(3*degstd))
plt.legend()
plt.savefig("C:/Users/User/Desktop/Fig1")
plt.show()

lambdaval = np.array([aqualine[0]*valD,redline[0]*valD])
lambdastd = np.array([aqualine[1]*valD,redline[1]*valD])

print("\ngradients, vio ",violine[0],", aqua ",aqualine[0],", red ",redline[0])
print("\nlambda ", lambdaval)
print("\nuncertainty ", lambdastd)

xrydberg = np.array([balmer(4,2), balmer(3,2)])
yrydberg = 1/lambdaval
yrydstd = yrydberg*(lambdastd/lambdaval)

rydline = LOBF(xrydberg, yrydberg, yrydstd)

m = rydline[0]
c = rydline[2]
plt.errorbar(xrydberg, yrydberg,yerr= yrydstd, fmt='r.', capsize=5)
plt.plot(np.linspace(-6,6,50),np.linspace(-6,6,50)*m+c, 'k')
plt.xlabel("$1/n^2$-$1/p^2$ (Balmer series for hydrogen: $n$=5,4,3 ; $p$=2)")
plt.ylabel("1/${\\lambda}$")
plt.xlim(xrydberg.min()-0.01, xrydberg.max()+0.01)
plt.ylim(0.99*yrydberg.min(), yrydberg.max()*1.01)
plt.show()

print("\nrb constant ",-m)
print("\nmax ",-m+rydline[1]," min ",-m-rydline[1])
print("\nuncertainty +-",rydline[1])
print("\n%uncertainty ",rydline[1]*100/-m)
print("\n%error ",(-truerd-m)*100/truerd)
