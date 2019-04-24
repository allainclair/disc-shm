import struct
import wave

import matplotlib.pyplot as plt
import numpy as np


def load_wave(
        file_path='test.wav', num_frames=96000, sampling_rate=48000, time=None):
    if time is not None:
        num_frames = sampling_rate * time
    with wave.open(file_path) as wave_file:
        data = wave_file.readframes(num_frames)
        data = struct.unpack('{n}h'.format(n=num_frames), data)
        return np.array(data)


def fft(data, abs_=True):
    data = np.fft.fft(data)
    if abs_:
        data = np.abs(data)
    print('1000', data[1000])
    print('2000', data[2000])
    print('200', data[200])
    print('Argmax:', np.argmax(data))
    print('max:', max(data))
    return data


def plot(wave1, wave2=None):
    plt.plot(wave1)
    if wave2 is not None:
        plt.plot(wave2)
    plt.show()


def save_wave(
        wave_, amplitude=16000, sampling_rate=48000, comptype='NONE',
        compname='not compressed', sampwidth=2, num_channels=1,
        file_path='test.wav'):
    n_frames = len(wave_)  # Len of the wave is the number of the frames.
    with wave.open(file_path, 'w') as wave_file:
        wave_file.setparams((
            num_channels, sampwidth, sampling_rate, n_frames, comptype, compname))
        for signal in wave_:
            value = int(signal * amplitude)
            # if value > amplitude:
            #     value = amplitude
            wave_file.writeframes(struct.pack('h', value))


def signalwave(frequency=1000, num_samples=48000, sampling_rate=48000, time=None):
    """Sine function: y(t) = A * sin(2 * pi * f * t)."""
    if time is not None:
        num_samples = sampling_rate * time
    return [  # Problema com essa declaracao em Python?
        np.sin(2 * np.pi * frequency * t / sampling_rate)
        for t in range(num_samples)]
