import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

x = np.linspace(0,10,10000)
T0 = 1/5000


def v1(t):
    b = 10
    c = 0.3

    E0,Em = 8,6

    w0,wm = 100e3*2*np.pi,5e3*2*np.pi

    Av = -4.68

    e1 = Av*(E0+Em*np.cos(wm*t))*np.cos(w0*t)
    v3 = b*e1 + c*e1**2
    return v3
def _cos(x,n_,w_):
	return v1(x)*np.cos(x*n_*w_)
	
def an(T,n=10):
	an=np.zeros(n)
	W = 2*np.pi/T

	for i in range(n):
		an[i]=(2/T)*(integrate.quad(_cos,0,T,args=(i,W))[0])
	return an

a_n = an(T0,23)		
	
def _sin(x,n_,w_):
	return v1(x)*np.sin(x*n_*w_)
	
def bn(T,n=10):
	bn=np.zeros(n)
	W = 2*np.pi/T

	for i in range(n):
		bn[i]=(2/T)*(integrate.quad(_sin,0,T,args=(i,W))[0])
	return bn	
	
b_n = bn(T0,23)


def rebuilt(an_coefs,bn_coefs,T,x):
	w0 = 2*np.pi/T
	N = len(an_coefs)
	f_sum = 0
	for n in range(N):
		f_sum += an_coefs[n]*np.cos(x*n*w0)
		f_sum += bn_coefs[n]*np.sin(x*n*w0)
	return f_sum
	
	
	
v1_rec = rebuilt(a_n,b_n,T0,x)

plt.title("Ponto 3: Sinal original")
plt.ylabel("Amplitude (V)")
plt.xlabel("tempo (s)")
plt.plot(x,v1(x)*2.28/2000)
plt.plot(x,v1_rec*2.28/2000,'r')

plt.legend(["Sinal original","Sinal reconstruído"])


plt.show()


	

