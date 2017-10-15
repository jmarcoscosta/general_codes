# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 17:59:25 2017

@author: joaomarcos
"""



from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

f0 = 100e3
BW = 30e3
Q = f0/BW
G = (3*Q-1)/Q
w0 = 2*np.pi*f0

num = [G,0]
den = [1,w0*(3-G)/Q,w0**2]

H_s = signal.lti(num,den)

w, H_module, H_phase = signal.bode(H_s)

plt.figure()

plt.subplot(211)
plt.title("Resposta em frequência - Módulo ")
plt.semilogx(w/(2*np.pi),H_module) 
plt.ylabel("$|H(\omega)|$ (dB)")
plt.xlabel("Frequência [Hz]")
plt.grid()

plt.subplot(212)
plt.title("Resposta em frequência - Fase ")
plt.grid()
plt.xlabel("Frequência [Hz]")
plt.ylabel("$\phi$ [graus]")
plt.semilogx(w/(2*np.pi),H_phase)

plt.tight_layout()
plt.show()

plt.figure()
plt.plot(w/(2*np.pi),10**(H_module/20))

import sys
print(sys.version)