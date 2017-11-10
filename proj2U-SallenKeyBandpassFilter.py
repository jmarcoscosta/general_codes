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
G = 2.7
w0 = 2*np.pi*f0
R = 8e3
C = 200e-12
A0 = G/(3-G)
print(20*np.log10(A0))
RC = R*C
num = [G/RC,0]
den = [1,1/(RC*Q),(1/RC)**2]

H_s = signal.lti(num,den)

w, H_module, H_phase = signal.bode(H_s,n=1000)


#plt.subplot(211)
plt.title("Resposta em frequência - Módulo ")
plt.semilogx(w/(2*np.pi),H_module) 
#plt.ylim([2.9,3.1])
#plt.xlim([80e3,120e3])
plt.ylabel("$|H(\omega)|$ (dB)")
plt.xlabel("Frequência [Hz]")
plt.grid()

#plt.subplot(212)
#plt.title("Resposta em frequência - Fase ")
#plt.grid()
#plt.xlabel("Frequência [Hz]")
#plt.ylabel("$\phi$ [graus]")
#plt.semilogx(w/(2*np.pi),H_phase)

#plt.tight_layout()
plt.show()



import sys
print(sys.version)