"""
https://www.pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/
"""
import random

import matplotlib.pyplot as plt
import numpy as np

import signalwave


def main():
    frequency = 500
    sampling_rate = 48000
    amplitude = 16000
    time = 2


    if time is not None:
        num_samples = sampling_rate * time
    noisy_wave = [
        np.sin(2 * np.pi * frequency * t / sampling_rate + random.random())
        for t in range(num_samples)]

    # signalwave.plot(wave)
    # Plot the 2 waves

    signalwave.save_wave(noisy_wave, file_path='noisy_audio.wav')

    plt.plot(noisy_wave[:1000])

    plt.show()


if __name__ == '__main__':
    main()
