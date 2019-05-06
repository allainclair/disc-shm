"""
https://www.pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/
"""
import matplotlib.pyplot as plt
import numpy as np

import signalwave


def main():
    # data = signalwave.load_wave('noisy_audio.wav', time=3, stereo=False)
    data = signalwave.load_wave('aud.wav', time=3, stereo=False)

    signalwave.plot(data, limit=10000)

    freqs = signalwave.fft(data)

    filtered_freqs = filter_freqs(freqs)

    signalwave.plots([freqs, filtered_freqs], limit=15000)

    recovered_signal = np.fft.ifft(filtered_freqs)
    signalwave.plot(recovered_signal, limit=5000)
    print(recovered_signal)
    signalwave.save_wave(
        recovered_signal,
        amplitude=0, file_path='noisy_audio_fitered.wav')


def filter_freqs(freqs):
    """Automaticamente pega a maior intensidade de frequencia e filtra ela."""
    max_index = np.argmax(freqs)
    print('max_index:', max_index)
    return [
        amp if max_index - 50 < f < max_index + 50 else 0
        for f, amp in enumerate(freqs)]


if __name__ == '__main__':
    main()
