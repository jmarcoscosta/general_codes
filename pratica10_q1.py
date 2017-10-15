import fseries as fs
import numpy as np
import matplotlib.pyplot as plt

#IMPORTAÇÃO DOS CSV:
#with open('col.csv', 'r') as f:
#  reader = csv.reader(f)
#  col_ = list(reader)
#  
#col_.pop(0)  
#col_.pop(0)  
#col = np.ndarray(len(col_),dtype='float64')
#t = np.ndarray(len(col_),dtype='float64')
#
#for i in range(len(col)):
#    col[i] = float(col_[i][1])
#    t[i]  = float(col_[i][0])
f_s = 2000e3
T = 0.0005
t = np.arange(0,T,1/f_s)

def e_t(t):
    E0 = 3
    wm = 2*np.pi*5000
    w0 = 2*np.pi*100000
    beta = 2
    return E0*np.cos(w0*t)*np.cos(beta*np.sin(wm*t))-E0*np.sin(w0*t)*np.sin(beta*np.sin(wm*t))

an,bn = fs.an_bn(e_t,1/5000,n=30)
plt.figure(1)
plt.title("Expressao teorica de $e(t)$")
plt.plot(t,e_t(t))
plt.grid()
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude [V]")
plt.show()