# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

import numpy as np
import matplotlib.pyplot as plt
import stomtools as stm
import scipy as sp
from scipy.optimize import curve_fit
from scipy.signal import find_peaks

def chisq(x,y,A,L):
    chi_sum=0
    diff=(y-A*np.exp(-x/L))**2
    chi_sum=np.sum(diff)
    return chi_sum

data = stm.generate_data()

#%%
bin_heights, bin_edges, patches = plt.hist(data, range = [104,155], bins = 45)
plt.show()
# #%%
x = bin_edges+(((155-104)/200)/2)
# plt.scatter(x[:-1], bin_heights, marker='x')
# plt.show()


test_data = stm.get_B_expectation(x, 35000, 30) # exp dist with arbitrary vals for A and Lamb
plt.plot(x,test_data)
plt.show()
# above was a test to find the interval of A and Lambda to iterate over

#%%


x_samp=np.array([])
y_samp=np.array([])
for val in range(0,len(x)):
    if x[val]<120:
        x_samp=np.append(x_samp,x[val])
        y_samp=np.append(y_samp,bin_heights[val])
    else:
        continue
print(x_samp)
print(y_samp)
#%%
iterA = np.linspace(35000,39000,100)
iterLamb = np.linspace(1,100,100)
minA=0
minLamb=0
chi=chisq(x_samp,y_samp, iterA[0], iterLamb[0])
for i in range(0,len(iterA)):
    for j in range(0,len(iterLamb)):
        test_chi = chisq(x_samp, y_samp, iterA[i], iterLamb[j])
        if test_chi<chi:
            chi=chisq(x_samp,y_samp, iterA[i], iterLamb[j])
            minA=iterA[i]
            minLamb=iterLamb[j]
            
            


#%%
bin_heights, bin_edges, patches = plt.hist(data, range = [104,155], bins = 45)
test_data = stm.get_B_expectation(x, minA, minLamb) # exp dist with arbitrary vals for A and Lamb
plt.plot(x,test_data)
plt.show()