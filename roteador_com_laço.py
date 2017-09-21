import numpy as np
import matplotlib.pyplot as plt 
import time 

d_passo = 5
d_dimensao = 200
NL = (d_dimensao-2*d_passo)//d_passo +1 

start_time = time.clock()
X = np.ndarray([NL,NL])
Y = np.ndarray([NL,NL])

for i in range(NL):                    
    for j in range(NL):                
        X[i,j] = d_passo + j*d_passo    
        Y[j,i] = X[i,j]
        
roteador_1_coords = np.ndarray([NL,NL],dtype=complex)
roteador_2_coords = np.ndarray([NL,NL],dtype=complex)
roteador_1_pot_dbm = np.ndarray([NL,NL])
roteador_2_pot_dbm = np.ndarray([NL,NL])
roteador_1_2_pot_dbm = np.ndarray([NL,NL])
for l in range(NL):
    for k in range(NL):
        roteador_1_coords[l,k] = X[l,k] + Y[l,k]*1j - ( d_dimensao/2 + 0.8*d_dimensao*1j)
        roteador_2_coords[l,k] = X[l,k] + Y[l,k]*1j - ( d_dimensao/2 + 0.2*d_dimensao*1j)
        roteador_1_pot_dbm[l,k] = 10*np.log10(1/np.abs(roteador_1_coords[l,k])**4/1e-3)
        roteador_2_pot_dbm[l,k] = 10*np.log10(1/np.abs(roteador_2_coords[l,k])**4/1e-3)
        roteador_1_2_pot_dbm[l,k] = np.maximum(roteador_1_pot_dbm[l,k],roteador_2_pot_dbm[l,k])
        
stop_time = time.clock()
tempo_de_exec_com_for = stop_time-start_time
plt.matshow(roteador_1_2_pot_dbm)
plt.colorbar()
plt.title("Sistema com laço for:"+str(tempo_de_exec_com_for)+"\n")
plt.show()
