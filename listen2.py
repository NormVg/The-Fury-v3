from vosk import Model , KaldiRecognizer
import pyaudio
import json

modle = Model(r"C:\\Users\\Arun Gupta\\Desktop\\Vishnu Gupta's File\\project\\fury\\database\\vosk-model-small-en-us-0.15")

reco = KaldiRecognizer(modle, 16000)

def recognition():
    cap = pyaudio.PyAudio()

    stream = cap.open(format=pyaudio.paInt16, channels=1 , rate=16000 , input=True , frames_per_buffer=8192)

    stream.start_stream()
    while True:
        data = stream.read(4096)

        if len(data) == 0:
            break

        
        if reco.AcceptWaveform(data):
            rec = reco.Result()
            rec = json.loads(rec)
            rec = rec['text']

            print( rec)


