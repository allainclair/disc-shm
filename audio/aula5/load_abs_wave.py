"""
https://www.pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/
"""
import signalwave

import matplotlib.pyplot as plt


def main():
    frequency = 1000
    sampling_rate = 48000
    amplitude = 16000
    time_ = 2

    # Normal wave
    data = signalwave.load_wave('wave.wav', time=2)

    # Abs wave
    data_abs = signalwave.load_wave('abs_wave.wav', time=2)

    # signalwave.plot(data, data_abs)

    freqs = signalwave.fft(data)
    freqs_abs = signalwave.fft(data_abs)


    plt.subplot(2,1,1)

    plt.plot(data_abs[:300])

    plt.title('Original audio wave')

    plt.subplot(2, 1, 2)

    plt.plot(freqs_abs)

    plt.title('Frequencies found')

    plt.xlim(0, 1200)

    plt.show()


if __name__ == '__main__':
    main()
