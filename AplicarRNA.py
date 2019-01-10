# -*- coding: cp1252 -*-
# Trabalho de IA e SD
# Bruna, Bruno, Diego, Murilo e Thomaz

# Bibliotecas
from pybrain.tools.customxml.networkreader import NetworkReader
import librosa
def AplicarRNA(NomeAudio, rede):
    # Ler o áudio
    y, sr = librosa.load(NomeAudio)
    # Conveter para escala mel
    mfccs = librosa.feature.melspectrogram(y=y, sr=sr)
    # Conveter para uma lista (entrada da rede neural)
    a=[]
    for j in range(20):
        a[0+130*j:130+130*j] = mfccs[j][0:130]
    
    # Testa o audio
    z= rede.activate(a)
    
    # Resultado
    #print ("Previsao : ", str(z[0]))
    if z[0] > 0.75 and z[0] < 1.25:
        print("Liberado");
    else:
        print("Negado");

# Ler arquivo do treinamento
rede = NetworkReader.readFrom('treinamento.xml')

# Aplicar a RNA
# WAV, 3s, mono, 16 bits, 22050Hz, falando "LIBERAR"
AplicarRNA("file.wav", rede)

