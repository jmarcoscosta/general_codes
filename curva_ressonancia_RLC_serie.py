
"""
Created on Tue Sep 26 15:28:11 2017

@author: Joao Marcos Costa
"""


import numpy as np
import matplotlib.pyplot as plt

R,L,C = 30,20e-3,2e-6
V = 9
pi = np.pi

f1 = (1/(2*pi))*(np.sqrt((R/(2*L))**2+1/(L*C))-R/(2*L))
f2 = (1/(2*pi))*(np.sqrt((R/(2*L))**2+1/(L*C))+R/(2*L))


def curva_R(V,R,L,C,N_samples=1000):
    f_ressonancia = 1/(2*pi*np.sqrt(L*C))
    freq = np.linspace(0,2*f_r,N_samples)
    w = 2*np.pi*freq
    return freq,V/(R+1j*(w*L-1/(w*C))),f_ressonancia


freq,curva,f_r = curva_R(9,R,L,C)
legendas = []
for i in range(1,4):
    plt.plot(curva_R(V,R,L,C)[0],curva_R(9,R*i,L,C)[1])
    legendas.append("Resistencia = "+str(R*i))
    plt.text(f_r,V/(R*i),"I="+str(1000*V/(R*i))+"mA")


    

plt.legend(legendas,loc='upper left')
plt.grid()
plt.title("Curva de Ressonancia : RLC em serie")
plt.xlabel("Frequencia [$\omega$]")
plt.ylabel("Corrente [A]")
plt.show()

    
