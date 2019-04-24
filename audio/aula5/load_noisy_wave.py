"""
https://www.pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/
"""
import signalwave

import matplotlib.pyplot as plt


def main():
    time_ = 2

    # Normal wave
    data = signalwave.load_wave('noisy_wave.wav', time=2)

    signalwave.plot(data)

    freqs = signalwave.fft(data)


    plt.subplot(2,1,1)

    plt.plot(data[:1000])

    plt.title('Original audio wave')

    plt.subplot(2, 1, 2)

    plt.plot(freqs)

    plt.title('Frequencies found')

    plt.xlim(0, 3000)

    plt.show()


if __name__ == '__main__':
    main()
