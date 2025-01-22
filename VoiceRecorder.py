import sounddevice
from scipy.io.wavfile import write
fs=44100 
second=int(input("Ingrese la Duracion de la Grabacion en Segundos: "))
print("Grabando....\n")
record_voice=sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
sounddevice.wait()
write("GrabacionEjemplo.wav",fs,record_voice)
print("Finalizando...\nPor Favor Espere...")