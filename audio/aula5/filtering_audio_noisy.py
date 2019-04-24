"""
https://www.pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/
"""
import matplotlib.pyplot as plt
import numpy as np

import signalwave


def filter_freqs(freqs):
    max_index = np.argmax(freqs)
    print('max_index:', max_index)
    max_index = max_index//2
    print('max_index//2:', max_index)
    return [f if (f > 1) and (max_index - 20 < i < max_index + 20) else 0 for i, f in enumerate(freqs)]

def main():
    time_ = 2

    # Normal wave
    data = signalwave.load_wave('noisy_audio.wav', time=2)

    freqs = signalwave.fft(data)

    # *2 devido ao "bug" da frequencia dobrada
    filtered_freqs = filter_freqs(freqs)

    plt.subplot(2,1,1)

    plt.plot(freqs)

    plt.title('Original freqs')

    plt.subplot(2, 1, 2)

    plt.plot(filtered_freqs)

    plt.title('Filtered freqs')

    plt.xlim(0, 1200)

    plt.show()

    recovered_signal = np.fft.ifft(filtered_freqs)
    plt.plot(recovered_signal)
    plt.show()
    # print(recovered_signal)
    signalwave.save_wave(np.abs(recovered_signal), file_path='noisy_audio_fitered.wav')


if __name__ == '__main__':
    main()
