#реализованно только для русского микрофона, по хорошему и английскому надо...
from re import A
from vosk import Model, KaldiRecognizer # vosk распознование через встроенную базу данныйх офлайн 
import pyaudio
from threading import Thread # многопоточнось 


#способ через vosk
model = Model(r"C:/Users/supef/Desktop/Nuta/vosk-model-small-ru-0.22") # полный путь к модели
rec = KaldiRecognizer(model, 16000)#настроика чистоты надо следить тут
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16, 
    channels=1, 
    rate=16000,# и тут надо прописать чистоту
    input=True, 
    frames_per_buffer=8000
)
stream.start_stream()

def inputMicrophone():
    while True:
        data = stream.read(4000)
        if len(data) == 0:
            break
        val = rec.Result() if rec.AcceptWaveform(data) else rec.PartialResult()
        #print(val)
        if ( val[5:9] == "text"):
            a = len(val)
            finVal = val[14:a-3]
            #print(finVal)
            return finVal    
'''                
@try_repeat
def error():
    inputMicrophone()
'''