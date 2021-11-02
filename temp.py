# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt


def adduncert(stdx,stdy):
    stdz= np.sum(((stdx**2)+(stdy**2))**0.5)
    return stdz

def multuncert(stdx,stdy,x,y,z):
    stdz = np.sum(z**(((stdx/x)**2+(stdy/y)**2)**0.5))
    return stdz

def percuncert(x,stdx):
    return stdx/x

def fstd (fwhm):
    return fwhm/(2*np.sqrt(2*np.log(2)))

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
    xinter = -1*yinter/m
    unc_xinter = multuncert(m, yinter, unc_m, unc_yinter, xinter)
    return([m, unc_m, yinter, unc_yinter, xinter, unc_xinter])



red1V = np.array([1.5566, 1.7621,1.8563, 1.9506, 1.9838 ,1.999  ,2.1736 ,2.2284 ,2.2786])
red1A = np.array([ 0.064,   0.7436  ,3.289   ,7.58    ,9.49   ,10.24   ,21.58   ,25.63   ,29.5   ])
blueV = np.array([2.3582, 2.4216 ,2.4957 ,2.5113 ,2.5335 ,2.5499 ,2.5665 ,2.5796 ,2.6412 ,2.7829 ,2.6842 ,2.6986 ,2.7253 ,2.7441 ,2.7992 ,2.8405 ,2.8695 ,2.8883 ,2.9218 ,2.9346])
blueA = np.array([0.0576,0.2418,1.0932,1.4366,2.0406,2.5716,3.1854,3.7568,6.73,16.03,9.33,10.23,11.99,13.33,17.39,20.69,23.23,24.94,28.11,29.41])
violetV = np.array([2.7718,2.7868,2.7863,2.8612,2.9117,2.9501,2.9827,3.0495,3.0603,3.0788,3.0895,3.0978,3.1108,3.1365,3.1501,3.1737,3.1897,3.2039,3.2247,3.2358,3.2453,3.3473])
violetA = np.array([0.0558,0.078,0.0774,0.4446,1.2618,2.3346,3.5212,6.75,7.28,8.32,8.96,9.49,10.25,11.93,12.87,14.53,15.74,16.85,18.5,19.35,20.14,29.42])
red2V = np.array([1.5833,1.6676,1.6845,1.6955,1.7204,1.7393,1.7744,1.7858,1.7917,1.8498,1.8649,1.8727,1.8887,1.9043,1.9242,1.9475,1.975,1.9772,1.9916,2.003,2.017,2.0377,2.049,2.0537,2.0586,2.0647])
red2A = np.array([0.009,0.061,0.0922,0.122,0.2314,0.3784,0.8948,1.158,1.3208,3.86,4.75,5.29,6.45,7.7,9.52,11.85,13.86,15.48,17.35,18.92,21.01,24.34,26.34,27.42,28.39,29.39])
greenV = np.array([1.7406,1.7763,1.8417,1.8564,1.8757,1.9293,1.9565,2.0011,2.0142,2.0545,2.0747,2.1062,2.1182,2.1431,2.1725,2.1855,2.2176,2.2372,2.2536,2.2751,2.3034,2.3251,2.3411,2.3523,2.3703])
greenA = np.array([0.0974,0.1956,0.6754,0.8732,1.2034,2.6346,3.6364,5.67,6.31,8.45,9.6,11.46,12.19,13.78,15.56,16.52,18.63,19.95,21.07,22.54,24.54,26.05,27.19,27.88,29.31])
amberV = np.array([1.6097,1.6594,1.7193,1.7343,1.8067,1.8443,1.8712,1.8993,1.9374,1.9573,1.9799,2.0064,2.0266,2.0599,2.0828,2.0967,2.1095,2.1341,2.1491,2.1697,2.1764,2.2074,2.2285,2.2481,2.2588,2.2686])
amberA = np.array([0.0048,0.0148,0.0692,0.103,0.6332,1.34,2.095,3.069,4.85,5.85,7.11,8.74,10.04,12.33,13.98,15.03,16.01,17.91,19.15,20.76,21.34,23.83,25.66,27.35,28.34,29.12])

x = np.linspace(1.5,3.5)*10**6

cVal = 2.99792458*10**8
eVal = 1.602176634*10**-19

red1w = 630.991394 * 10**-9
red2w = 616.0325317 * 10**-9
bluew = 470.2113037 * 10**-9
greenw = 562.7641602 * 10**-9
amberw = 594.3807617 * 10**-9

arrlambda = np.array([red1w, bluew, red2w, greenw, amberw])
arrlambdastd = np.array([fstd(12.2120792 * 10**-9),fstd(10.762567 * 10**-9),fstd(22.13484 * 10**-9),fstd(18.1176047 * 10**-9),fstd(13.6166059 * 10**-9)])
#plotting data
# plt.errorbar(amberV, amberA, yerr=0.0001, xerr=0.0001, fmt="y.")
# plt.errorbar(red1V, red1A, yerr=0.0001, xerr=0.0001, fmt="r.")
# plt.errorbar(blueV, blueA, yerr=0.0001, xerr=0.0001, fmt="b.")
# #plt.errorbar(violetV, violetA, yerr=0.0001, xerr=0.0001, fmt="ko")
#plt.errorbar(greenV, greenA, yerr=0.0001, xerr=0.0001, fmt="g")
# plt.errorbar(red2V, red2A, yerr=0.0001, xerr=0.0001, fmt="k.")
#info of linear lines
red1graph = LOBF(red1V[4::], red1A[4::], np.repeat(0.0001,len(red1V[4::])))
bluegraph = LOBF(blueV[11::],blueA[11::], np.repeat(0.0001,len(blueV[11::])))
violetgraph = LOBF(violetV[11::],violetA[11::], np.repeat(0.0001,len(violetV[11::])))
red2graph = LOBF(red2V[15::], red2A[15::], np.repeat(0.0001,len(red2V[15::])))
greengraph = LOBF(greenV[9::], greenA[9::], np.repeat(0.0001,len(greenV[9::])))
ambergraph = LOBF(amberV[10::], amberA[10::], np.repeat(0.0001,len(amberV[10::])))
#linear lines for Vt
# plt.plot(x,red1graph[0]*x+red1graph[2], "r--", label="Red 1 LED")
# plt.plot(x,red2graph[0]*x+red2graph[2], "k--", label="Red 2 LED")
# plt.plot(x,bluegraph[0]*x+bluegraph[2], "b--", label="Blue LED")
# #plt.plot(x,violetgraph[0]*x+violetgraph[2], "k")
#plt.plot(x,greengraph[0]*x+greengraph[2], "g--", label="Green LED")
# plt.plot(x,ambergraph[0]*x+ambergraph[2], "y--", label="Amber LED")
#plt.xlim(1.5, 3)
#plt.ylim(0, 30)
# plt.xlabel("Voltage/V")
# plt.ylabel("Current/mA")
# plt.legend()
# plt.savefig("C:/Users/User/Desktop/LED IV graph.png")
# plt.show()


arrVt = np.array([red1graph[4], bluegraph[4], red2graph[4],greengraph[4],ambergraph[4]])
arrVtstd = np.array([red1graph[5], bluegraph[5], red2graph[5],greengraph[5],ambergraph[5]])

# plt.errorbar(1/arrlambda, arrVt,yerr = arrVtstd, xerr = (1/arrlambda)*percuncert(arrlambda,arrlambdastd)/100,capsize=5, fmt="k.")
graphVt = LOBF(1/arrlambda, arrVt)
# plt.plot(x,graphVt[0]*x+graphVt[1], "r")

# plt.xlim(1.5*10**6, 2.2*10**6)
# plt.ylim(1.8,2.6)
# plt.xlabel("1/peak wavelength / m^-1")
# plt.ylabel("Threshold voltage/V")

#plt.savefig("C:/Users/User/Desktop/Vt by lambda.png")

hVal = graphVt[0]*eVal/cVal
print ("h = ", hVal)
print ("std h = ", percuncert(graphVt[0], graphVt[1]))
truehVal = 6.62607015*10**-34
print ("percentage error ", percuncert((hVal-truehVal), truehVal))

