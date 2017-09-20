import numpy as np
import matplotlib.pyplot as plt

E0 = 8
f0 = 100*1e3
Em = 6
fm = 5*1e3
t = np.linspace(0,20,10000)
f_sampling = 1/(t[1]-t[0])

em = Em*np.cos(2*np.pi*fm*t)
e0 = E0*np.cos(2*np.pi*f0*t)

b1,b2 = 0.3,0.04

v1 = 0.5*(em+e0)
v2 = b1*v1 + b2*v1**2

lfft = len(t)
v1_S = np.fft.fft(v1,lfft)/lfft
v1_S = np.fft.fftshift(v1_S)

v2_S = np.fft.fft(v2,lfft)/lfft
v2_S = np.fft.fftshift(v2_S)

freq = np.fft.fftfreq(lfft)
freq = np.fft.fftshift(freq)




plt.figure(1,[10,7])

plt.subplot(211)
plt.title("V1(t): saída do somador resistivo")
plt.ylabel("Amplitude (V)")
plt.xlabel("tempo (s)")
plt.plot(t,v1)

plt.subplot(212)
plt.title("V1(f): saída do somador resistivo")
plt.ylabel("Amplitude (V)")
plt.xlabel("frequência (kHz)")
plt.plot(freq*lfft/2,np.abs(v1_S))
plt.xlim([-110,110])

plt.tight_layout()
plt.show()


plt.figure(2,[10,7])


plt.subplot(211)
plt.title("V2(t): saída da chave síncrona")
plt.ylabel("Amplitude (V)")
plt.xlabel("tempo (s)")
plt.plot(t,v2)

plt.subplot(212)
plt.title("V2(f): saída da chave síncrona")
plt.ylabel("Amplitude (V)")
plt.xlabel("frequência (kHz)")
plt.plot(freq*lfft/2,np.abs(v2_S))
plt.xlim([-110,110])

plt.tight_layout()
plt.show()

plt.figure(3,[10,7])

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


from scipy.signal import butter, lfilter

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

v3 = butter_bandpass_filter(v2,fin/1000,fsup/1000,f_sampling,order=1)
v3_S = np.fft.fft(v3,lfft)/lfft
v3_S = np.fft.fftshift(v3_S)

plt.subplot(211)
plt.title("V3(t): saída do filtro LC")
plt.ylabel("Amplitude (V)")
plt.xlabel("tempo (s)")

plt.plot(t,v3)

plt.subplot(212)
plt.title("V3(f): saída do filtro LC")
plt.ylabel("Amplitude (V)")
plt.xlabel("frequência (kHz)")
plt.plot(freq*lfft/2,np.abs(v3_S))
plt.xlim([-110,110])

plt.tight_layout()
plt.show()

