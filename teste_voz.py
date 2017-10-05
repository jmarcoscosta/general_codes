# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 22:15:18 2017

@author: joaomarcos
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wv

fs, audio = wv.read('voz.wav')

a = np.array([1,2,3,4,5])
a = np.reshape(a,[5,1])
b = np.reshape(a,[1,5])

plt.figure(1)
plt.subplot(411)
plt.title("Áudio original, shape : (95021,2): Vetor linha [NÃO PLOTA]")
plt.subplot(412)
audio = np.transpose(audio)
plt.plot(audio[0])
plt.title("Audio, shape: (2,95021) - Transposto/Vetor coluna [PLOTA]")


plt.subplot(413)
plt.plot(a)
plt.title("Vetor a (linha), shape :(5,)[PLOTA]")
plt.subplot(414)
plt.plot(b)
plt.title("Vetor b (coluna), shape: (1,5)[NÃO PLOTA]")

plt.tight_layout()

#POR QUE O ÁUDIO VETOR COLUNA APARECE NO GRÁFICO, E O VETOR LINHA NÃO?
#ENQUANTO ISSO, NO TESTE COM A E B, O RESULTADO É O OPOSTO
plt.show()