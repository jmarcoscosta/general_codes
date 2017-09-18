import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

x = np.linspace(0,10,10000)
T0 = 1/5000

def v1(t):
	E0 = 8
	f0 = 100*1e3
	Em = 6
	fm = 5*1e3
	em = Em*np.cos(2*np.pi*fm*t)
	e0 = E0*np.cos(2*np.pi*f0*t)
	return 0.5*(em+e0)

def v2(t):
	b1,b2=0.054,0.004
	return b1*v1(t) + b2*v1(t)**2
'''
def find_period(array_y,array_x):
	ts = array_x[1]-array_x[0]
	N_ts = np.where(array_y>max(array_y)*0.99)[0][-1]
	N_ts -= np.where(array_y>max(array_y)*0.99)[0][-2]
	return N_ts*ts
'''


def _cos(x,n_,w_):
	return v2(x)*np.cos(x*n_*w_)
	
def an(T,n=10):
	an=np.zeros(n)
	W = 2*np.pi/T

	for i in range(n):
		an[i]=(2/T)*(integrate.quad(_cos,0,T,args=(i,W))[0])
	return an

N = 25
a_n = an(T0,N)		
	
def _sin(x,n_,w_):
	return v2(x)*np.sin(x*n_*w_)
	
def bn(T,n=10):
	bn=np.zeros(n)
	W = 2*np.pi/T

	for i in range(n):
		bn[i]=(2/T)*(integrate.quad(_sin,0,T,args=(i,W))[0])
	return bn	
	
b_n = bn(T0,N)

def rebuilt(an_coefs,bn_coefs,T,x):
	w0 = 2*np.pi/T
	N = len(an_coefs)
	f_sum = 0
	for n in range(N):
		f_sum += an_coefs[n]*np.cos(x*n*w0)
		f_sum += bn_coefs[n]*np.sin(x*n*w0)
	return f_sum
	
v2_rec = rebuilt(a_n,b_n,T0,x)

plt.subplot(211)
plt.title("V2(t): Sinal original")
plt.ylabel("Amplitude (V)")
plt.xlabel("tempo (s)")
plt.plot(x,v2(x))

plt.subplot(212)
plt.title("V2(t): Sinal reconstruído pela Série de Fourier")
plt.ylabel("Amplitude (V)")
plt.xlabel("tempo (s)")
plt.plot(x,v2_rec,'r')

plt.tight_layout()
plt.show()


	

