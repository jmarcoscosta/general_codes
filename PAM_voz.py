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
from scipy.signal import butter, lfilter, freqz,firwin


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

def downsample(array,rate):
    return array[::rate]

def upsample(array,rate):
    from numpy import zeros
    ret =  zeros(rate*len(array))
    ret[::rate] = array 
    return ret

N = 5
new_fs = fs/N  #Hz, >2*3.4KHz

pulsos = np.zeros(len(audio_BW_limitada))
pulsos[::N] = 1 


audio_PAM = audio_BW_limitada*pulsos
#plt.plot(audio_BW_limitada)
#plt.plot(audio_PAM,'r')
audio_gravado = np.asarray(audio_PAM,dtype='int16')
wv.write('voz_PAM.wav',fs,audio_gravado)


#S_audio_PAM = np.fft.fft(audio_PAM)[0:len(audio_PAM)//2] 

fpb_B,fpb_A = butter_lowpass(3400,fs,order=5)
eixo_freq = np.linspace(0,fs/2,len(audio_PAM)/2)

def filter_response(a,b,freq):
    filter_num,filter_den = 0,0
    for i in range(0,len(a)):
        #filter_num += a[i]*freq**i
        filter_den += b[i]*freq**i
    return 1/filter_den
fpb = filter_response(fpb_A,fpb_B,eixo_freq)
        

            
#recuperado = np.fft.ifft(S_audio_PAM)
#recuperado *= len(S_audio_PAM)
#recuperado = np.asarray((recuperado),dtype = 'int16')
#plt.plot(audio_gravado)
#plt.plot(recuperado)
