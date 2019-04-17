"""
https://www.pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/
"""
import random
import struct
import wave

import numpy as np


def make_frequencies(n=40, start=100, end=5000):
    return [random.randint(start, end) for _ in range(n)]


def main():
    # Sine function: y(t) = A * sin(2 * pi * f * t)

    freqs = make_frequencies(50)

    time = 10
    second_sample = 48000
    second_factor = 6
    num_samples = time * second_sample

    sampling_rate = 48000

    amplitude = 16000

    file = 'test.wav'

    sine_wave = []

    sample = int(second_sample / second_factor)
    freq = random.choice(freqs)
    for x in range(num_samples):
        if x % sample == 0:
            freq = random.choice(freqs)
        # for _ in range(sample):
        y = np.sin(2 * np.pi * freq * x / sampling_rate)
        sine_wave += [y]


    # for t in range(time):
    #     for sf in range(second_factor):
    #         sample = int(second_sample / second_factor)
    #         freq = random.choice(freqs)
    #         for s in range(sample):
    #             y = np.sin(2 * np.pi * freq * x / sampling_rate)
    #             sine_wave += [y]

    nframes = num_samples

    comptype = 'NONE'

    compname = 'not compressed'

    nchannels = 1

    # Sample width in bytes.
    # 16 bits = 2 hex (bytes).
    sampwidth = 2

    with wave.open(file, 'w') as wave_file:
        wave_file.setparams((
            nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

        for s in sine_wave:
            wave_file.writeframes(struct.pack('h', int(s * amplitude)))


if __name__ == '__main__':
    main()
