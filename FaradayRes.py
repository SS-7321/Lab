# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 09:58:25 2022

@author: Shan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 13:13:07 2022

@author: alexwong
"""

import numpy as np
import matplotlib.pyplot as plt

#%%
def addunc(stdx,stdy):
    stdz= ((stdx**2)+(stdy**2))**0.5
    return stdz

def multunc(x,stdx,y,stdy,z):
    stdz = z*np.sqrt((stdx/x)**2+(stdy/y)**2)
    return stdz

#%%

pr_0V = np.loadtxt("C:\\Users\\User\\Documents\\Labs\\Faraday\\fr.csv", delimiter=',', skiprows=3, usecols=1, max_rows=15)
pr_1V = np.loadtxt("C:\\Users\\User\\Documents\\Labs\\Faraday\\fr.csv", delimiter=',', skiprows=3, usecols=3, max_rows=17)
pr_2V = np.loadtxt("C:\\Users\\User\\Documents\\Labs\\Faraday\\fr.csv", delimiter=',', skiprows=3, usecols=5, max_rows=12)
sd_0V = np.loadtxt("C:\\Users\\User\\Documents\\Labs\\Faraday\\fr.csv", delimiter=',', skiprows=22, usecols=1, max_rows=15)*10**-3
sd_1V = np.loadtxt("C:\\Users\\User\\Documents\\Labs\\Faraday\\fr.csv", delimiter=',', skiprows=22, usecols=3, max_rows=17)*10**-3
sd_2V = np.loadtxt("C:\\Users\\User\\Documents\\Labs\\Faraday\\fr.csv", delimiter=',', skiprows=22, usecols=5, max_rows=12)*10**-3


#%%

prvstd = 0.01
sdvstd = 0.1

pr_r = 18
sd_r = 27

prrstd = pr_r*0.05
sdrstd = sd_r*0.05

#%%
pr_0 = pr_0V**2/pr_r
pr_1 = pr_1V**2/pr_r
pr_2 = pr_2V**2/pr_r

sd_0 = sd_0V**2/sd_r
sd_1 = sd_1V**2/sd_r
sd_2 = sd_2V**2/sd_r

sd0std = multunc(sd_0V**2, multunc(sd_0V,sdvstd,sd_0V,sdvstd,sd_0V**2), sd_r, sdrstd, sd_0)
sd1std = multunc(sd_1V**2, multunc(sd_1V,sdvstd,sd_1V,sdvstd,sd_1V**2), sd_r, sdrstd, sd_1)
sd2std = multunc(sd_2V**2, multunc(sd_2V,sdvstd,sd_2V,sdvstd,sd_2V**2), sd_r, sdrstd, sd_2)


#%%
fit_efficiency0f, cov_efficiency0f = np.polyfit(pr_0, sd_0, 1, w=sd0std, cov=True)
p_efficiency0f = np.poly1d(fit_efficiency0f)

fit_efficiency1f, cov_efficiency1f = np.polyfit(pr_1, sd_1, 1, w=sd1std, cov=True)
p_efficiency1f = np.poly1d(fit_efficiency1f)

fit_efficiency2f, cov_efficiency2f = np.polyfit(pr_2, sd_2, 1, w=sd2std, cov=True)
p_efficiency2f = np.poly1d(fit_efficiency2f)

efficiency0f = fit_efficiency0f[0]
efficiency1f = fit_efficiency1f[0]
efficiency2f = fit_efficiency2f[0]

sig00f = np.sqrt(cov_efficiency0f[0,0])
sig01f = np.sqrt(cov_efficiency1f[0,0])
sig02f = np.sqrt(cov_efficiency2f[0,0])
#%%

plt.plot(pr_0, sd_0, 'x', mew=1, ms=5, label='No Ferrite', color='blue')
plt.plot(pr_1, sd_1, 'x', mew=1, ms=5, label='1 Ferrite Core', color='red')
plt.plot(pr_2, sd_2, 'x', mew=1, ms=5, label='2 Ferrite Cores', color='green')
plt.title('Powers of Coils')
plt.xlabel('Power of pr coil (W)')
plt.ylabel('Power of sd coil (W)')
plt.legend()
plt.plot(pr_0, p_efficiency0f(pr_0), '-')
plt.plot(pr_1, p_efficiency1f(pr_1), '-', color='red')
plt.plot(pr_2, p_efficiency2f(pr_2), '-', color='lime')
#plt.savefig("C:/Users/User/Desktop/Faraday.png", dpi=1200)
#%%
print(f'Efficiency with no ferrite cores: {efficiency0f*100} +/- {sig00f*100} %')
print(f'Efficiency with 1 ferrite core: {efficiency1f*100} +/- {sig01f} %')
print(f'Efficiency with 2 ferrite cores: {efficiency2f*100} +/- {sig02f} %')
