import sounddevice as sd
from scipy.io.wavfile import write
fs = 44500#sample_rate

saa= int(input("please enter the recording time :"))
recorded =sd.rec(int (saa *fs),samplerate = fs,channels=2)
sd.wait()
write('recording.wav',fs , recorded )
print("Recording is done check current folder to listen to recording")