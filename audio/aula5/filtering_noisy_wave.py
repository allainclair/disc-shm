"""
https://www.pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/
"""
import matplotlib.pyplot as plt
import numpy as np

import signalwave


def main():
    time_ = 2

    # Normal wave
    data = signalwave.load_wave('noisy_wave.wav', time=2)

    freqs = signalwave.fft(data)

    # *2 devido ao "bug" da frequencia dobrada
    filtered_freqs = filter_freqs(freqs, value=500*2)

    plt.subplot(2, 1, 1)

    plt.plot(freqs)

    plt.title('Original freqs')

    plt.subplot(2, 1, 2)

    plt.plot(filtered_freqs)

    plt.title('Filtered freqs')

    plt.xlim(0, 5000)

    plt.show()

    recovered_signal = np.fft.ifft(filtered_freqs)
    plt.plot(recovered_signal)
    plt.show()

    signalwave.save_wave(np.abs(recovered_signal), file_path='filtered_noisy_wave.wav')


def filter_freqs(freqs, value):
    return [
        f if (f > 1) and (value - 50 < i < value + 50) else 0
        for i, f in enumerate(freqs)]


if __name__ == '__main__':
    main()
