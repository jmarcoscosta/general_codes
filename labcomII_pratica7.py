#from numpy import genfromtxt
#p3 = genfromtxt('p3wave.csv', delimiter=',',dtype='float64',usemask=False)
#
#import csv
#
#with open('p3wave.csv', 'r') as f:
#  reader = csv.reader(f)
#  your_list = list(reader)
#  
import csv
import numpy as np
with open('p3wave.csv', 'r') as f:
  reader = csv.reader(f)
  p3_ = list(reader)
  
p3_.pop(0)  
p3_.pop(0)  
p3 = np.ndarray(len(p3_),dtype='float64')
t = np.ndarray(len(p3_),dtype='float64')

for i in range(len(p3)):
    p3[i] = float(p3_[i][1])
    t[i]  = float(p3_[i][0])

import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(t,p3)
plt.show()

b = 10
c = 0.3

E0,Em = 8,6

w0,wm = 100e3*2*np.pi,5e3*2*np.pi

Av = -4.68

e1 = Av*(E0+Em*np.cos(wm*t))*np.cos(w0*t)
v3 = b*e1 + c*e1**2
plt.figure(2)
plt.plot(t,v3)

