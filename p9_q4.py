import numpy as np
import fseries as fs
import matplotlib.pyplot as plt

def e0l(x):
	E0l = 2
	f0 = 100e3
	return E0l*np.cos(np.pi*f0*2*x)

def et(x):
	Em,E0=10,2
	fm,f0 = 5e3,100e3
	K=8e-4
	Av = -18.83
	return Av*K*Em*E0*0.5*np.cos((fm+f0)*2*np.pi*x)+Av*K*Em*E0*0.5*np.cos((f0-fm)*2*np.pi*x)

def e1(x):
	return et(x)*e0l(x) + 2*et(x)


	
	
import csv


#IMPORTAÇÃO DOS CSV:
with open('col.csv', 'r') as f:
  reader = csv.reader(f)
  col_ = list(reader)
  
col_.pop(0)  
col_.pop(0)  
col = np.ndarray(len(col_),dtype='float64')
t = np.ndarray(len(col_),dtype='float64')

for i in range(len(col)):
    col[i] = float(col_[i][1])
    t[i]  = float(col_[i][0])
t+=0.0003	

an,bn = fs.an_bn(e1,1/5000,n=50)	
coletor_rec = fs.rebuild(an,bn,1/5000,t)		
plt.figure(1)
plt.title("Sinal no coletor (Série de Fourier)")
plt.plot(t,coletor_rec)
plt.plot(t,col,'k')
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude [V]")
plt.grid()
plt.legend(["reconstruído ","medido"])
plt.show()