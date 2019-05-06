"""
https://www.pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/
"""
import matplotlib.pyplot as plt
import numpy as np

import signalwave


def main():
    # Normal wave
    data = signalwave.load_wave('ex.wav', time=2, stereo=True)

    freqs = signalwave.fft(data)

    filtered_freqs = filter_low_value(freqs, 50)

    signalwave.plots([freqs, filtered_freqs], limit=20000)

    recovered_signal = np.fft.ifft(filtered_freqs)
    # signalwave.plot(recovered_signal, limit=3000)
    print(recovered_signal)
    signalwave.save_wave(
        recovered_signal,
        amplitude=0, file_path='ex_filtered.wav')


def filter_low_value(freqs, value):
    """Automaticamente pega a maior intensidade de frequencia e filtra ela."""
    # max_index = np.argmax(freqs)
    # print('max_index:', max_index)
    return [f if i > value else 0 for i, f in enumerate(freqs)]

    # return [
    #     f if (f > 1) and (max_index - 10 < i < max_index + 10) else 0
    #     for i, f in enumerate(freqs)]


if __name__ == '__main__':
    main()
