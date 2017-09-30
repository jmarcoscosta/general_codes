# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 10:13:37 2017

@author: joaomarcos
"""

import numpy as np
import matplotlib.pyplot as plt

import csv

with open('p2.csv', 'r') as f:
  reader = csv.reader(f)
  p1_ = list(reader)
  
p1_.pop(0)  
p1_.pop(0)  
p1 = np.ndarray(len(p1_),dtype='float64')
t  = np.ndarray(len(p1_),dtype='float64')

#extração dos valores de tensão e tempo correspondentes
for i in range(len(p1)):
    p1[i] = float(p1_[i][1])
    t[i]  = float(p1_[i][0])

t+=0.0003
E0,Em = 2,10
f0,fm = 100e3,5e3
N = 10000

e0 = E0*np.cos(2*np.pi*f0*t)
em = Em*np.cos(2*np.pi*fm*t)

K = 9.4e-3

R,C,L = 47,130e-9,20e-6


modulado = K*e0*em





title = "Sinal modulado"
plt.figure(1)
plt.title(title)
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude [V]")
plt.grid()
plt.plot(t,modulado)
plt.plot(t,p1,'r')
plt.legend([title+" teórico","Sinal modulado real"])

plt.savefig(title+str(".png"))
plt.show()




