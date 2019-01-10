import threading
import pyaudio
import wave
import librosa


class RecordingThread (threading.Thread):
    def __init__(self, rede):
        super(RecordingThread, self).__init__()
        self.rede = rede
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 22050
        self.CHUNK = 1024
        self.RECORD_SECONDS = 3.05
        self.WAVE_OUTPUT_FILENAME = "app/static/file.wav"
        self.audio = pyaudio.PyAudio()
        imagem = "CadeadoFechado.png"
        self.fechadura = imagem


    def run(self):
        # start Recording
        stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                                 rate=self.RATE, input=True,
                                 frames_per_buffer=self.CHUNK)
        print("recording...")
        frames = []

        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            frames.append(data)
        print("finished recording")

        # stop Recording
        stream.stop_stream()
        stream.close()
        self.audio.terminate()

        waveFile = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(self.CHANNELS)
        waveFile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        waveFile.setframerate(self.RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()

    def stop(self):
        self.isRunning = False


    def __del__(self):
      pass



class Audio(object):
    def __init__(self, rede):
        self.rede = rede
        # Open a camera
        # Initialize video recording environment
        self.is_record = False
        self.out = None

        # Thread for recording
        self.recordingThread = None

    def start_record(self):
        self.is_record = True
        self.recordingThread = RecordingThread(self.rede)
        self.recordingThread.start()

    def stop_record(self):
        self.is_record = False

        if self.recordingThread != None:
            self.recordingThread.stop()

class RNA (threading.Thread):
    def __init__(self, rede):
        super(RNA, self).__init__()
        self.rede = rede
        self.WAVE_OUTPUT_FILENAME = "app/static/file.wav"
        imagem = "CadeadoFechado.png"
        self.fechadura = imagem


    def run(self):
        # start Recording
        self.AplicarRNA(self.WAVE_OUTPUT_FILENAME, self.rede)

    def AplicarRNA(self, NomeAudio, rede):
        # Ler o Ã¡udio
        y, sr = librosa.load(NomeAudio)
        # Conveter para escala mel
        mfccs = librosa.feature.melspectrogram(y=y, sr=sr)
        # Conveter para uma lista (entrada da rede neural)
        a = []
        for j in range(20):
            a[0 + 130 * j:130 + 130 * j] = mfccs[j][0:130]

        # Testa o audio
        z = rede.activate(a)

        # Resultado
        # print ("Previsao : ", str(z[0]))
        if z[0] > 0.75 and z[0] < 1.25:
            print("Liberado")
            self.fechadura = "CadeadoAberto.png"
        else:
            print("Negado")
            self.fechadura = "CadeadoFechado.png"

    def get_frame(self):
        return self.fechadura

    def __del__(self):
      pass