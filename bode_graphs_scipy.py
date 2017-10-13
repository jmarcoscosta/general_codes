#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 16:05:40 2017

@author: labsim
"""

from scipy import signal

import matplotlib.pyplot as plt




num = [1]
den = [1,1]

H_s = signal.lti(num,den)

w, H_module, H_phase = signal.bode(H_s)

plt.figure()

plt.subplot(211)
plt.title("Resposta em frequência - Módulo ")
plt.semilogx(w,H_module) 
plt.ylabel("$|H(\omega)|$ (dB)")
plt.xlabel("Frequência [rads]")
plt.grid()

plt.subplot(212)
plt.title("Resposta em frequência - Fase ")
plt.grid()
plt.xlabel("Frequência [rads]")
plt.ylabel("$\phi$ [graus]")
plt.semilogx(w,H_phase)

plt.tight_layout()
plt.show()