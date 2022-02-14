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



pr_noferrite = np.loadtxt("C:/Users/User/Documents/Labs/Faraday/fr.csv", delimiter=',', skiprows=3, )
pr_1ferrite = np.array([0.736089, 0.680556, 0.568889, 0.533889, 0.467222, 0.405000, 0.320000, 0.293889, 0.245000, 0.222222, 0.160556, 0.108889, 0.080000, 0.067222, 0.055556, 0.046006, 0.029606])
pr_2ferrite = np.array([0.732050, 0.561800, 0.486756, 0.317339, 0.228939, 0.182006, 0.145800, 0.101250, 0.066006, 0.038272, 0.016806, 0.005339])
sd_noferrite = np.array([2.15E-05, 1.98E-05, 1.83E-05, 1.60E-05, 1.38E-05, 1.21E-05, 1.08E-05, 8.33E-06, 6.45E-06, 4.98E-06, 3.27E-06, 2.55E-06, 1.33E-06, 8.18E-07, 7.50E-07])
sd_1ferrite = np.array([0.000593, 0.000547, 0.000489, 0.000434, 0.000383, 0.000329, 0.000261, 0.000237, 0.000200, 0.000169, 0.000120, 0.000084, 0.000066, 0.000055, 0.000043, 0.000034, 0.000022])
sd_2ferrite = np.array([0.000962424, 0.000725926, 0.000624001, 0.000402907, 0.000286815, 0.000226490, 0.000180446, 0.000123735, 0.000080428, 0.000045890, 0.000020454, 0.000006650])

prresstd = 18*0.05
sdresstd = 27*0.05
prvstd = 0.01
sdvstd = 0.1



#%%
fit_efficiencynf, cov_efficiencynf = np.polyfit(pr_noferrite, sd_noferrite, 1, cov=True)
p_efficiencynf = np.poly1d(fit_efficiencynf)

fit_efficiency1f, cov_efficiency1f = np.polyfit(pr_1ferrite, sd_1ferrite, 1, cov=True)
p_efficiency1f = np.poly1d(fit_efficiency1f)

fit_efficiency2f, cov_efficiency2f = np.polyfit(pr_2ferrite, sd_2ferrite, 1, cov=True)
p_efficiency2f = np.poly1d(fit_efficiency2f)

efficiencynf = fit_efficiencynf[0]
efficiency1f = fit_efficiency1f[0]
efficiency2f = fit_efficiency2f[0]

sig0nf = np.sqrt(cov_efficiencynf[0,0])
sig01f = np.sqrt(cov_efficiency1f[0,0])
sig02f = np.sqrt(cov_efficiency2f[0,0])
#%%

plt.plot(pr_noferrite, sd_noferrite, 'x', mew=1, ms=5, label='No Ferrite', color='blue')
plt.plot(pr_1ferrite, sd_1ferrite, 'x', mew=1, ms=5, label='1 Ferrite Core', color='red')
plt.plot(pr_2ferrite, sd_2ferrite, 'x', mew=1, ms=5, label='2 Ferrite Cores', color='green')
plt.title('Powers of Coils')
plt.xlabel('Power of pr coil (W)')
plt.ylabel('Power of sd coil (W)')
plt.legend()
plt.plot(pr_noferrite, p_efficiencynf(pr_noferrite), '-')
plt.plot(pr_1ferrite, p_efficiency1f(pr_1ferrite), '-', color='red')
plt.plot(pr_2ferrite, p_efficiency2f(pr_2ferrite), '-', color='lime')
#plt.savefig("C:/Users/User/Desktop/Faraday.png", dpi=1200)
#%%
print(f'Efficiency with no ferrite cores: {efficiencynf*100} +/- {sig0nf*100} %')
print(f'Efficiency with 1 ferrite core: {efficiency1f*100} +/- {sig01f} %')
print(f'Efficiency with 2 ferrite cores: {efficiency2f*100} +/- {sig02f} %')