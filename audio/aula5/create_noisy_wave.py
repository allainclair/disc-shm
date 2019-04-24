"""
https://www.pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/
"""
import matplotlib.pyplot as plt
import numpy as np

import signalwave


def main():
    frequency = 500
    noisy_freq = 100
    noisy_freq2 = 500
    sampling_rate = 48000
    amplitude = 10000
    time_ = 2

    wave1 = signalwave.signalwave(frequency, sampling_rate, time=time_)
    noisy_wave = signalwave.signalwave(noisy_freq, sampling_rate, time=time_)
    noisy_wave2 = signalwave.signalwave(noisy_freq2, sampling_rate, time=time_)

    wave = np.array(wave1) + np.array(noisy_wave)

    # signalwave.plot(wave)
    # Plot the 2 waves

    signalwave.save_wave(wave, amplitude, file_path='noisy_wave.wav')

    plt.subplot(3,1,1)

    plt.title('Original sine wave')

    plt.subplots_adjust(hspace=.5)

    plt.plot(wave1[:500])

    plt.subplot(3,1,2)

    plt.title('Noisy wave')

    plt.plot(noisy_wave[:1000])

    plt.subplot(3,1,3)

    plt.title('Original + Noise')

    plt.plot(wave[:3000])

    plt.show()


if __name__ == '__main__':
    main()
