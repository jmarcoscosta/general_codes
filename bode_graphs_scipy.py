#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 16:05:40 2017

@author: labsim
"""

from scipy import signal

import matplotlib.pyplot as plt

num = [1,0]
den = [1,2,3]

H_s = signal.lti(num,den)

w, H_module, H_phase = signal.bode(H_s)

plt.figure()
plt.semilogx(w,H_module) 
plt.ylabel("|H| (dB)")
plt.xlabel("frequency (rads)")
plt.title("Bode Diagram")


plt.figure()
plt.title("Bode Diagram")
plt.xlabel("frequency (rads)")
plt.ylabel("$\phi$ (degrees)")
plt.semilogx(w,H_phase)


plt.show()