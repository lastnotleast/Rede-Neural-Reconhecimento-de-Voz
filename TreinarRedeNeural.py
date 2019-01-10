# -*- coding: cp1252 -*-

# Bibliotecas
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.customxml.networkwriter import NetworkWriter
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

# Para gerar gráficos
def GraficoDbxFreq (fs, p):
    f = np.linspace(0, fs/2.0, len(p))
    print(len(p))
    plt.plot(f, p)
    plt.xlabel("Frequencia (Hz)")
    plt.ylabel("Ganho (dB)")
    plt.show()

# Define a rede neural
rede = buildNetwork(3000, 300, 1, bias = True)
base = SupervisedDataSet(3000,1)

# Aprovado
for i in range(1,8,1):
    if i <10:
        nome = "Aprovado/M0" + str(i) + ".wav"
    else:
        nome = "Aprovado/M" + str(i) + ".wav"
        
    fs, data = wavfile.read(nome)
    p = 20*np.log10(np.abs(np.fft.rfft(data)))
    # GraficoDbxFreq(fs,p)
    b = p.tolist()
    a=[]
    for j in range(3000):
        a = a + [sum(b[(10*j):(10*(j+1))])/10]

    base.addSample(tuple(a),(1))
    

# Negado
for i in range(1,18,1):
    if i <10:
        nome = "Negado/0" + str(i) + ".wav"
    else:
        nome = "Negado/" + str(i) + ".wav"
        
    fs, data = wavfile.read(nome)
    p = 20*np.log10(np.abs(np.fft.rfft(data)))
    #f = np.linspace(0, fs/2.0, len(p))
    b = p.tolist()
    a=[]
    for j in range(3000):
        a = a + [sum(b[(10*j):(10*(j+1))])/10]

    base.addSample(tuple(a),(0))

# Prepara para o treinamento
treinamento = BackpropTrainer(rede, dataset=base, learningrate = 0.01, momentum = 0.06)

# treina a rede com a base de dados
for i in range(1, 300):
    erro = treinamento.train()
    #if i%100 == 0:
    print("Erro ", i, " - ", erro)
    if erro <= 0.05:
        break;

# Salva o resultado do treinamento
NetworkWriter.writeToFile(rede, 'treinamento.xml')

