Jogadas = 50                # Número de jogadas do dado
Jogadores = 10000

## Simulando as jogadas
# Faremos aqui a criação das jogadas para cada jogador. Montaremos uma
# matriz em que as linhas representarão os resultados e as colunas
# representarão os jogadores. Em seguida será calculado a pontuação de cada
# jogador somando os pontos de cada jogada. Queremos mostrar também o
# quanto é prejudicial em termos de tempo o uso do laço FOR. Simularemos
# para os dois casos e computaremos o tempo:
import numpy as np   
import time 
import matplotlib.pyplot as plt
from scipy import stats


n = Jogadas                                     # Para um número "n" de jogadas
# Implementação com laço for:
dcfs = time.clock()                                             # Inicia o cronômetro
x = np.ndarray([n,Jogadores])
y = np.ndarray([len(x[1,:])])
for ic in range(n):
	x[ic,:]=np.ceil(6*np.random.rand(1,Jogadores))        # Gera números aleatórios entre o intervalo de 1 a 6 (faces do dado)

for ik in range(len(x[1,:])):
	y[ik]=sum(x[:,ik])                             # Soma os pontos de cada jogador
	df = time.clock() - dcfs
    # Inicia o cronômetro
x = np.ceil(6*np.random.rand(n,Jogadores))                          # Gera matriz com jogadas
y = sum(x)       # Calcula a pontuação de cada jogador, equivalente a sum(x,1) do Matlab
    #np.sum(x,1) não retorna o que queremos


binCtrs = np.arange(0,n*6+2)                                       # Centro de cada coluna dependem de "n"
#plt.hist(y,bins=binCtrs,color='purple')                                        # Plota Histograma para cada eixo
    # Histograma gaussiano estimado
mi = np.mean(y)                                           # Calcula média de cada jogador
des = np.std(y)                                           # Calcula desvio padrão de cada jogador
    #ye = des*randn(1,length(y))+mi                        # Histograma estimado 
Tp = 1/Jogadores
xi = np.arange(np.min(y),np.max(y)+Tp,Tp)
ye = Jogadores*stats.norm.pdf(xi,mi,des)                        # Histograma estimado 
    #[yPlot, xPlot] = hist(ye,binCtrs)                     # Retorna posição do histohrama sem plotar 

plt.hist(y,bins=binCtrs)    
plt.xlim([3*n,4*n])
plt.plot(xi,ye,'r')
plt.show()