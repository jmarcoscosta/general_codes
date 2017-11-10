# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 19:49:37 2017

@author: joaomarcos
"""

import numpy as np
import matplotlib.pyplot as plt 

R = 1000
T= 1/R
Ts = T/20
Rs = 1/Ts

t = np.arange(0,T,Ts)
pi2 = np.pi*2
K = 20

s0 = np.ones(K)#np.sin(pi2*t*R)
s1 = np.hstack([np.ones(K/2),-np.ones(K/2)])#np.cos(pi2*t*R)

### para s0 transmitido
var = 0
r0 = s0+ np.sqrt(var)*np.random.randn(K)
r1 = np.zeros(K)

cor_r0_s0 = np.correlate(r0,s0,'full')/len(r0)

cor_r0_s1 = np.correlate(r0,s1,'full')/len(r0)

plt.figure(1)
plt.title("Saída do correlator- numpy.correlate")
plt.plot(cor_r0_s0)
plt.plot(cor_r0_s1)
plt.legend(['r0 e s0','r0 e s1'])
plt.xlim([0,K])

plt.grid()

for i in range(K):
	cor_r0_s0[i] = np.sum(r0[0:i]*s0[0:i])
	cor_r0_s1[i] = np.sum(r0[0:i]*s1[0:i])
	
	
plt.figure(2)
plt.title("Saída do correlator- np.sum(r0[0:i]*s0[0:i]) ")
plt.plot(cor_r0_s0)
plt.plot(cor_r0_s1)
plt.legend(['r0 e s0','r0 e s1'])
plt.xlim([0,K])
plt.grid()





