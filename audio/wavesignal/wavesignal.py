import numpy as np


def simple(frequency=1000, sampling_rate=48000, num_samples=48000):
    return [
        np.sin(2 * np.pi * frequency * x / sampling_rate)
        for x in range(num_samples)]

