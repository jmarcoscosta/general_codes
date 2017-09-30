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

def _cos(x,n_,w_):
	return v1(x)*np.cos(x*n_*w_)
	


	
def _sin(x,n_,w_):
	return v1(x)*np.sin(x*n_*w_)
	
def an_bn(T0,n=10):
	bn=np.zeros(n)
	W = 2*np.pi/T0
	an=np.zeros(n)

	for i in range(n):
		an[i]=(2/T0)*(integrate.quad(_cos,0,T0,args=(i,W))[0])
		bn[i]=(2/T0)*(integrate.quad(_sin,0,T0,args=(i,W))[0])

	return an,bn

	
a_n,b_n = an_bn(T0,21)


def rebuild(an_coefs,bn_coefs,T,x):
	w0 = 2*np.pi/T
	N = len(an_coefs)
	f_sum = 0
	for n in range(N):
		f_sum += an_coefs[n]*np.cos(x*n*w0)
		f_sum += bn_coefs[n]*np.sin(x*n*w0)
	return f_sum
	
	
	
v1_rec = rebuild(a_n,b_n,T0,x)

plt.subplot(211)
plt.title("V1(t): Sinal original")
plt.ylabel("Amplitude (V)")
plt.xlabel("tempo (s)")
plt.plot(x,v1(x))

plt.subplot(212)
plt.title("V1(t): Sinal reconstruído pela Série de Fourier")
plt.ylabel("Amplitude (V)")
plt.xlabel("tempo (s)")
plt.plot(x,v1_rec,'r')

plt.tight_layout()
plt.show()


	

