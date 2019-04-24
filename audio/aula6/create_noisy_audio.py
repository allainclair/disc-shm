"""
https://www.pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/
"""
import matplotlib.pyplot as plt

import signalwave


def main():
    # Mudar freqs para testar
    frequency = 1000
    time = 2

    noisy_wave = signalwave.signalwave(frequency, time=time, noisy=True)

    signalwave.plot(noisy_wave)
    plt.show()

    signalwave.save_wave(
        noisy_wave, amplitude=8000, file_path='noisy_audio.wav')


if __name__ == '__main__':
    main()
