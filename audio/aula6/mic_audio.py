"""
https://www.pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/
"""
import matplotlib.pyplot as plt
import numpy as np

import signalwave


def main():
    # Normal wave
    data = signalwave.load_wave('mic.wav', time=2)

    freqs = signalwave.fft(data)

    filtered_freqs = filter_freqs(freqs)

    signalwave.plots([freqs, filtered_freqs], limit=5000)

    recovered_signal = np.fft.ifft(filtered_freqs)
    signalwave.plot(recovered_signal, limit=3000)
    # print(recovered_signal)
    signalwave.save_wave(
        recovered_signal,
        amplitude=0, file_path='mic_filtered.wav')


def filter_freqs(freqs):
    """Automaticamente pega a maior intensidade de frequencia e filtra nela."""
    max_index = np.argmax(freqs)
    # print('max_index:', max_index)
    return [
        f if (f > 1) and (max_index - 10 < i < max_index + 10) else 0
        for i, f in enumerate(freqs)]


if __name__ == '__main__':
    main()
