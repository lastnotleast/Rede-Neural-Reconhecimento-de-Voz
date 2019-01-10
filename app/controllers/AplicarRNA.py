# -*- coding: cp1252 -*-

# Bibliotecas
from pybrain.tools.customxml.networkreader import NetworkReader
from scipy.io import wavfile
import numpy as np
        
def AplicarRNA(NomeAudio, rede):
    # Ler arquivo
    fs, data = wavfile.read(NomeAudio)
    
    # Conveter
    p = 20*np.log10(np.abs(np.fft.rfft(data)))

    # Ler valores
    b = p.tolist()
    a=[]
    for j in range(3000):
        a = a + [sum(b[(10*j):(10*(j+1))])/10]
    
    # Testa o audio
    z= rede.activate(a)
    
    # Resultado
    #print ("Previsao : ", str(z[0]))
    if z[0] > 0.7:
        print("Liberado");
    else:
        print("Negado");

# Ler arquivo do treinamento
rede = NetworkReader.readFrom('treinamento.xml')

# Aplicar a RNA
# WAV, 3s, mono, 16 bits, 22050Hz, falando "LIBERAR"
AplicarRNA("teste1.wav", rede)

