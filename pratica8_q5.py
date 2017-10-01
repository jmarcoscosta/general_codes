# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 20:38:03 2017

@author: joaomarcos
"""

import numpy as np
import matplotlib.pyplot as plt
#import fseries as fs
import csv


#IMPORTAÇÃO DOS CSV:
with open('p1.csv', 'r') as f:
  reader = csv.reader(f)
  p1_ = list(reader)
  
p1_.pop(0)  
p1_.pop(0)  
p1 = np.ndarray(len(p1_),dtype='float64')
t = np.ndarray(len(p1_),dtype='float64')

for i in range(len(p1)):
    p1[i] = float(p1_[i][1])
    t[i]  = float(p1_[i][0])


with open('p2.csv', 'r') as f:
  reader = csv.reader(f)
  p2_ = list(reader)
  
p2_.pop(0)  
p2_.pop(0)  
p2 = np.ndarray(len(p2_),dtype='float64')
t2 = np.ndarray(len(p2_),dtype='float64')

for i in range(len(p1)):
    p2[i] = float(p2_[i][1])
    t2[i]  = float(p2_[i][0])



#DEFINIÇÃO DOS SINAIS TEORICOS:
t+=0.0003
t2+=0.0003
E0,Em = 2,10
f0,fm = 100e3,5e3
N = 10000

e0 = E0*np.cos(2*np.pi*f0*t)
em = Em*np.cos(2*np.pi*fm*t)

K = 9.4e-3

R,C,L = 47,130e-9,20e-6
A = 1.94e-2

import fseries as fs

def modulado(t):
	return -K*Em*np.cos(2*np.pi*fm*t)*E0*np.cos(2*np.pi*f0*t)

def coletor(x):
	return modulado(x) + -A*Em*np.cos(2*np.pi*fm*x)

an2,bn2 = fs.an_bn(modulado,1/5000,n=50)
an1,bn1 = fs.an_bn(coletor,1/5000,n=50)

modulado_rec = fs.rebuild(an2,bn2,1/5000,t)
coletor_rec = fs.rebuild(an1,bn1,1/5000,t2)

plt.figure(1,[10,7])
plt.subplot(212)
plt.title("Reconstrução do sinal via Série de Fourier: Saída do modulador")
plt.plot(t2,p2)
plt.plot(t2,modulado_rec)
plt.legend(["Sinal Original","Sinal reconstruído"])

plt.subplot(211)
plt.title("Reconstrução do sinal via Série de Fourier: Saída do coletor")
plt.plot(t,p1)
plt.plot(t,coletor_rec)
plt.legend(["Sinal Original","Sinal reconstruído"])
plt.show()				

plt.savefig("Reconstrução do sinal via Série de Fourier.png")
