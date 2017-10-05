#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 14:14:45 2017

@author: pesquisador
"""

import numpy as np
import matplotlib.pyplot as plt
from math import gcd
import heapq

f1 = 30
f2 = 6
f3 = 300

print(gcd(gcd(f1,f2),f3))

fs= 10*f3

t = np.arange(0,10+1/fs,1/fs)

s1 = np.cos(2*np.pi*f1*t)
s2 = np.cos(2*np.pi*f2*t)
s3 = np.cos(2*np.pi*f3*t)

st = s1+s2+s3
SS = np.fft.fftshift(np.fft.fft(st))/len(st)

freq = np.arange(-fs/2,fs/2,fs/len(st))

rxx = np.correlate(np.abs(SS),np.abs(SS),mode='same')

#plt.plot(freq,np.abs(SS))
plt.plot(freq,rxx)
#plt.xlim([-10,10])
plt.show()