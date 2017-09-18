import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

T0 = 1/5000
t = np.linspace(0,20,10000)
f_sampling = 1/(t[1]-t[0])
lfft = len(t)

def v1(t):
	E0 = 8
	f0 = 100*1e3
	Em = 6
	fm = 5*1e3
	em = Em*np.cos(2*np.pi*fm*t)
	e0 = E0*np.cos(2*np.pi*f0*t)
	return 0.5*(em+e0)

freq = np.fft.fftfreq(lfft)
freq = np.fft.fftshift(freq)


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
	
def data_cos(data,x,n_,w_):
	return data*np.cos(x*n_*w_)
	
def an(T,n=10):
	an=np.zeros(n)
	W = 2*np.pi/T

	for i in range(n):
		an[i]=(2/T)*(integrate.quad(_cos,0,T,args=(i,W))[0])
	return an

def data_an(data_,x,T,TN,n=10):
	an=np.zeros(n)
	W = 2*np.pi/T
	for i in range(n):
		array = data_cos(data_[TN:2*TN],x[TN:2*TN],i,W)
		an[i]=(2/TN)*(np.trapz(array))
	return an




	
def _sin(x,n_,w_):
	return v2(x)*np.sin(x*n_*w_)
	
def data_sin(data,x,n_,w_):
	return data*np.sin(x*n_*w_)


def bn(T,n=10):
	bn=np.zeros(n)
	W = 2*np.pi/T

	for i in range(n):
		bn[i]=(2/T)*(integrate.quad(_sin,0,T,args=(i,W))[0])
	return bn	


def data_bn(data_,x,T,TN,n=10):
	bn=np.zeros(n)
	W = 2*np.pi/T
	for i in range(n):
		array = data_sin(data_[TN:2*TN],x[TN:2*TN],i,W)
		bn[i]=(2/TN)*(np.trapz(array))
	return bn






def rebuilt(an_coefs,bn_coefs,T,x):
	w0 = 2*np.pi/T
	N = len(an_coefs)
	f_sum = 0
	for n in range(N):
		f_sum += an_coefs[n]*np.cos(x*n*w0)
		f_sum += bn_coefs[n]*np.sin(x*n*w0)
	return f_sum
	


#filtragem do passa-faixas
from scipy.signal import butter
from scipy.signal import lfilter
C = 130*1e-9
L = 20*1e-6
wc = 1/(np.sqrt(L*C))
B = 2*np.pi*14*1e3 #bandwidth
Q = wc/B #quality factor
w_inferior = wc*np.sqrt(1+1/(4*Q**2))-wc/(2*Q)
w_superior = wc*np.sqrt(1+1/(4*Q**2))+wc/(2*Q)

fin=w_inferior/(2*np.pi)
fsup=w_superior/(2*np.pi)



def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

v3 = butter_bandpass_filter(v2(t),fin/10000,fsup/10000,f_sampling,order=1)
v3_S = np.fft.fft(v3,lfft)/lfft
v3_S = np.fft.fftshift(v3_S)


N = 25
TN = 1000
a_n = data_an(v3,t,T0,TN,N)
b_n = data_bn(v3,t,T0,TN,N)

v3_rec = rebuilt(a_n,b_n,14,t)
v3_rec_S = np.fft.fftshift(np.fft.fft(v3_rec))
plt.subplot(211)
plt.title("V3(t): sinal original")
plt.ylabel("Amplitude (V)")
plt.xlabel("tempo (s)")

plt.plot(t[TN:2*TN+200],v3[TN:2*TN+200])

plt.subplot(212)
plt.title("V3(f): sinal reconstruído pela Série de Fourier")
plt.ylabel("Amplitude (V)")
plt.xlabel("tempo (s)")
plt.plot(t,v3_rec,'r')

plt.tight_layout()
plt.show()


	

