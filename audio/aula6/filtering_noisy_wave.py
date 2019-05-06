"""
https://www.pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/
"""
import matplotlib.pyplot as plt
import numpy as np

import signalwave


def main():
    data = signalwave.load_wave('noisy_wave.wav', time=3)

    freqs = signalwave.fft(data)

    # As vezes transofmra *2, as vezes *3.
    filtered_freqs = filter_freqs(freqs, 300*3, 800*3)

    signalwave.plots([freqs, filtered_freqs], limit=10000)

    recovered_signal = np.fft.ifft(filtered_freqs)

    signalwave.plot(recovered_signal, limit=5000)

    signalwave.save_wave(
        recovered_signal, amplitude=0, file_path='filtered_noisy_wave.wav')


def filter_freqs(freqs, low, high):
    return [
        f if low < i < high else 0 for i, f in enumerate(freqs)]


if __name__ == '__main__':
    main()
