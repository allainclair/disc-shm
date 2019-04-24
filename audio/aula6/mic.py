import sounddevice as sd
import wave
import struct
# import numpy as np
# import scipy.io.wavfile as wav

fs = 48000
duration = 3  # seconds
myrecording = sd.rec(duration * fs, samplerate=fs, channels=1,dtype='float64')
sd.wait()
print("Audio recording complete , Play Audio")
sd.play(myrecording, fs)
sd.wait()
print("Play Audio Complete")


print(type(myrecording))
print(myrecording)

amplitude = 16000
sampling_rate = 48000
comptype='NONE'
compname='not compressed'
sampwidth = 2
num_channels = 1
file_path = 'mic.wav'
n_frames = duration*fs
with wave.open('mic.wav', 'w') as wave_file:
    wave_file.setparams((
        num_channels, sampwidth, sampling_rate, n_frames, comptype, compname))
    for a in myrecording:
        wave_file.writeframes(struct.pack('h', int(a[0]*amplitude)))
