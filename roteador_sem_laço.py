import numpy as np 
import matplotlib.pyplot as plt 
import time 

d_passo = 5
d_dimensao = 200

start_time = time.clock()

x = np.arange(d_passo,d_dimensao,d_passo)
y = np.arange(d_passo,d_dimensao,d_passo)
X,Y = np.meshgrid(x,y)

roteador_1_coords = X + 1j*Y - (d_dimensao/2 + 0.8*d_dimensao*1j)
roteador_2_coords = X + 1j*Y - (d_dimensao/2 + 0.2*d_dimensao*1j)

roteador_1_pot_dbm = 10*np.log10(1/np.abs(roteador_1_coords)**4/1e-3)
roteador_2_pot_dbm = 10*np.log10(1/np.abs(roteador_2_coords)**4/1e-3)

roteador_1_2_pot_dbm = np.maximum(roteador_1_pot_dbm,roteador_2_pot_dbm)

stop_time = time.clock()

plt.matshow(roteador_1_2_pot_dbm)
tempo_de_exec_sem_for = stop_time-start_time
plt.title("Sistema sem laço FOR:"+str(tempo_de_exec_sem_for)+"\n")
plt.colorbar()
plt.show()
