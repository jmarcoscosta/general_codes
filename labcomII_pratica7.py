
#leitura do arquivo .csv
import csv
import numpy as np
with open('p3wave.csv', 'r') as f:
  reader = csv.reader(f)
  p3_ = list(reader)
  
p3_.pop(0)  
p3_.pop(0)  
p3 = np.ndarray(len(p3_),dtype='float64')
t = np.ndarray(len(p3_),dtype='float64')

#extração dos valores de tensão e tempo correspondentes
for i in range(len(p3)):
    p3[i] = float(p3_[i][1])
    t[i]  = float(p3_[i][0])
#estimação de b e c    
b = 24*1e-3
c = 0.3*1e-3
#geração dos sinais
E0,Em = 8,6
w0,wm = 100e3*2*np.pi,5e3*2*np.pi
Av = -4.68
e1 = Av*(E0+Em*np.cos(wm*t))*np.cos(w0*t)
v3 = b*e1 + c*e1**2
#offset no vetor das amostras de tempo
t = t+0.0006
#visualização

import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(t,v3)
#plt.plot(t,p3)
#plt.title("Medição e simulação da tensão no ponto 3: Saída do diodo")
plt.title("Simulação do sinal no ponto 3 (saída do diodo)")
plt.xlabel("Tempo [s]")
plt.ylabel("Tensão [V]")
#plt.legend(["Sinal calculado","Sinal medido"])
plt.grid()
plt.show()


