import numpy as np
import matplotlib.pyplot as plt

K = 20
A = 1
l = np.arange(0,K)
s_0 = np.ones(K)
s_1 = np.concatenate((A*np.ones(K//2),-A*np.ones(K//2)),axis=0)

r_0 = np.zeros(K)
r_1 = np.zeros(K)

variancia = np.array([0,0.1,1])
plt.figure(1)
for i in range(len(variancia)):
    noise = np.random.normal(0.0,np.sqrt(variancia[i])+1,K)
    s = s_0
    y = s + noise
    y_0 = np.convolve(y,np.flipud(s_0))
    y_1 = np.convolve(y,np.flipud(s_1))

    plt.subplot(321+2*i)
    plt.xlabel('$\sigma^{2}$= ' +str(variancia[i]) +' & $s_{0}$ é transmitido')
    plt.plot(l,y_0[l],'-')
    plt.plot(l,y_1[l],'--')
    plt.xticks(np.array([0,10,20]),['0','10Tb','20Tb'])
    plt.axis([0,20,-30,30])
    
    s = s_1
    y = s + noise
    y_0 = np.convolve(y,np.flipud(s_0))
    y_1 = np.convolve(y,np.flipud(s_1)) 
                                        

    plt.subplot(322+2*i)
    plt.xlabel('$\sigma^{2}$= ' +str(variancia[i]) +' & $s_{1}$ é transmitido')
    plt.plot(l,y_0[l],'-')
    plt.plot(l,y_1[l],'--')
    plt.xticks(np.array([0,10,20]),['0','10Tb','20Tb'])
    plt.axis([0,20,-30,30])

    
plt.tight_layout()
plt.show()