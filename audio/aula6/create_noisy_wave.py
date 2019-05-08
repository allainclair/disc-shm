"""
https://www.pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/
"""
import matplotlib.pyplot as plt
import numpy as np

import signalwave


def main():
    frequencies = [100, 200, 500, 1000, 1500]
    sampling_rate = 48000
    amplitude = 3000
    time_ = 3

    waves = []
    for freq in frequencies:
        wave = signalwave.signalwave(freq, sampling_rate, time=time_)
        waves.append(np.array(wave))
    sum_wave = sum(waves)

    signalwave.plot(sum_wave, limit=5000)

    signalwave.save_wave(sum_wave, amplitude, file_path='noisy_wave.wav')

if __name__ == '__main__':
    main()
