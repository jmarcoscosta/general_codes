# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 11:14:20 2017

@author: joaomarcos
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wv

fs, audio = wv.read('voz.wav')

t = np.arange(0,95021)/fs

#audio_S = np.fft.fftshift(np.fft.fft(audio[:,0]))/95021
#freq = np.arange(-fs/2,fs/2,fs/95021)
#plt.plot(freq,np.abs(audio_S))
from scipy.signal import butter, lfilter, freqz


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y
				
audio_BW_limitada = butter_lowpass_filter(audio[:,0],3400,fs)
#audio_BW_limitada_S = np.fft.fftshift(np.fft.fft(audio_BW_limitada))/95021
#audio_gravado = np.asarray(audio_BW_limitada,dtype='int16')
#wv.write('voz_bw_limitada.wav',fs,audio_gravado)
#plt.plot(freq,np.abs(audio_BW_limitada_S))

new_fs = 9000 #Hz, >2*3.4KHz
new_t = np.arange(0,t[-1],1/new_fs)

new_audio = audio_BW_limitada[::95021//19392]


