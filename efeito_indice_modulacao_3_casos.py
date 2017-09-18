import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

# Parâmetros do sinal
Ac = 2                                                         # Amplitude da portadora
Mu = 0.7                                                       # Índice de modulação
fc = 25000                                                     # Frequência da portadora Hz
fm = 5000
N = 10000
Ts = 1e-6                                                      # Tempo de amostragem pequeno (modelar sinal contínuo)
t = np.arange(N)*Ts
s = Ac*(1+Mu*np.cos(2*np.pi*fm*t))*np.cos(2*np.pi*fc*t)


# Gráfico do AM-DSB no tempo
plt.figure(1,[10,7])
plt.subplot(321)
plt.plot(t,s)
plt.title("AM-DSB (padrão), M="+str(Mu))
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")

# Gráfico do AM-DSB na frequência
plt.subplot(322)
plt.title("AM-DSB (padrão), M="+str(Mu))
plt.xlabel("Frequência [kHz]")
plt.ylabel("Magnitude")
S_f = np.abs(np.fft.fftshift(np.fft.fft(s)))
plt.plot(S_f)

plt.subplot(323)

Mu = 1.0
s = Ac*(1+Mu*np.cos(2*np.pi*fm*t))*np.cos(2*np.pi*fc*t)

plt.title("AM-DSB (padrão), M="+str(Mu))
plt.ylabel("Amplitude (v)")
plt.xlabel("Tempo [s]")
plt.plot(t,s)



plt.subplot(324)





plt.title("AM-DSB (padrão), M="+str(Mu))
plt.xlabel("Frequência [kHz]")
plt.ylabel("Magnitude")
S_f = np.abs(np.fft.fftshift(np.fft.fft(s)))

plt.plot(S_f)



plt.subplot(325)
Mu = 2.0
s = Ac*(1+Mu*np.cos(2*np.pi*fm*t))*np.cos(2*np.pi*fc*t)
plt.plot(t,s)
plt.title("AM-DSB (padrão), M="+str(Mu))
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")


plt.subplot(326)





plt.title("AM-DSB (padrão), M="+str(Mu))
plt.xlabel("Frequência [kHz]")
plt.ylabel("Magnitude")
S_f = np.abs(np.fft.fftshift(np.fft.fft(s)))

plt.plot(S_f)



plt.tight_layout()
plt.show()