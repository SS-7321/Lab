# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 09:58:25 2022

@author: Shan
"""
# Results data
#   	No ferrite core		With ferrite core		With 2 ferrite cores	
# Primary	Vrms/V	Power/W	Vrms/V	Power/W	Vrms/V	Power/W
# coil						
# 	3.62	0.728022222	3.64	0.736088889	3.63	0.73205
# 	3.48	0.6728	3.5	0.680555556	3.18	0.5618
# 	3.35	0.623472222	3.2	0.568888889	2.96	0.486755556
# 	3.14	0.547755556	3.1	0.533888889	2.39	0.317338889
# 	2.9	0.467222222	2.9	0.467222222	2.03	0.228938889
# 	2.75	0.420138889	2.7	0.405	1.81	0.182005556
# 	2.6	0.375555556	2.4	0.32	1.62	0.1458
# 	2.28	0.2888	2.3	0.293888889	1.35	0.10125
# 	2.02	0.226688889	2.1	0.245	1.09	0.066005556
# 	1.77	0.17405	2	0.222222222	0.83	0.038272222
# 	1.43	0.113605556	1.7	0.160555556	0.55	0.016805556
# 	1.27	0.089605556	1.4	0.108888889	0.31	0.005338889
# 	0.92	0.047022222	1.2	0.08		
# 	0.72	0.0288	1.1	0.067222222		
# 	0.7	0.027222222	1	0.055555556		
# 			0.91	0.046005556		
# 			0.73	0.029605556		
# Secondary	Vrms/mV	Power/W	Vrms/mV	Power/W	Vrms/mV	Power/W
# coil						
# 	24.1	2.15E-05	126.5	0.000592676	161.2	0.000962424
# 	23.1	1.98E-05	121.5	0.00054675	140	0.000725926
# 	22.2	1.83E-05	114.9	0.000488963	129.8	0.000624001
# 	20.8	1.60E-05	108.3	0.000434403	104.3	0.000402907
# 	19.3	1.38E-05	101.7	0.00038307	88	0.000286815
# 	18.1	1.21E-05	94.2	0.000328653	78.2	0.00022649
# 	17.1	0.00001083	83.9	0.000260711	69.8	0.000180446
# 	15	8.33E-06	80	0.000237037	57.8	0.000123735
# 	13.2	6.45E-06	73.5	0.000200083	46.6	8.04E-05
# 	11.6	4.98E-06	67.6	0.00016925	35.2	4.59E-05
# 	9.4	3.27E-06	56.9	0.000119911	23.5	2.05E-05
# 	8.3	2.55E-06	47.5	8.36E-05	13.4	6.65E-06
# 	6	1.33E-06	42.1	6.56E-05		
# 	4.7	8.18E-07	38.7	0.00005547		
# 	4.5	0.00000075	33.9	4.26E-05		
# 			30.2	3.38E-05		
# 		24.3	0.00002187		
# 
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
