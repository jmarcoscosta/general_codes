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


	
def saida(x):
	Av = -18.83
	Em,E0=10,2
	fm = 5e3
	K=-8e-4
	return 0.7*np.cos(2*np.pi*fm*x)*K*Av*Em*E0**2 	
	
def saidad(x):
	s = np.cos(2*5e3*np.pi*x)*42.4e-3
	s+= np.cos(2*3e3*np.pi*x)*143e-3
	s+= np.cos(2*7e3*np.pi*x)*95.2e-3
	return s
import csv


#IMPORTAÇÃO DOS CSV:
#with open('col.csv', 'r') as f:
#  reader = csv.reader(f)
#  col_ = list(reader)
#  
#col_.pop(0)  
#col_.pop(0)  
#col = np.ndarray(len(col_),dtype='float64')
#t = np.ndarray(len(col_),dtype='float64')
#
#for i in range(len(col)):
#    col[i] = float(col_[i][1])
#    t[i]  = float(col_[i][0])

with open('dout.csv', 'r') as f:
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

an,bn = fs.an_bn(saidad,1/1000,50)
saidad_rec = fs.rebuild(an,bn,1/5000,t)
plt.figure(1)
plt.title("Saída do MODEM com $\Delta f = 2KHz$")
plt.plot(t,saidad_rec,'r')
plt.plot(t,col)
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude [V]")
plt.xlim([0.0000,0.0010])
plt.grid()
#plt.legend(["calculado","medido"])
plt.show()