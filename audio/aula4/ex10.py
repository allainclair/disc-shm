"""
https://www.pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/
"""
import random
import struct
import wave

# import matplotlib.pyplot as plt
import numpy as np


def main():
    # Sine function: y(t) = A * sin(2 * pi * f * t)

    # frequency is the number of times a wave repeats a second.
    frequency = 440   # Periodo eh o inverso da frequencia = 1/f.

    num_samples = 200000

    # The sampling rate of the analog to digital convert.
    sampling_rate = 48000
    # sampling_rate = 4000

    # Qualquer valor de amplitude pode ser usado em geral para ver em graficos.
    # Geralmente valor 1. Mas para sinal sonoro temos que mudar isso.
    # Arquivos wave sao escritos em 16 bits.
    # Um numero "float" nao vai representar certo isso (exemplo = 1.0 no
    # maximo).
    # Temos que converter o "float" para um ponto fixo. Dessa forma vamos
    # multiplicar por uma constante.
    # Maximo de 16 bits = 2^15 -1 = 32767 (um bit pro sinal lembrando,
    # por isso 2^15).
    # Aqui iremos mais ou menos ateh a metade da amplitude apenas, ou seja,
    # amplitude serah de 16000.
    amplitude = 16000  # Testar diferentes amplitudes.

    file = 'test.wav'

    # start_pertub, end_pertub = -1, 1

    sine_wave = []
    for t in range(num_samples):
        perturb = random.random()
        # perturb1 = random.randint(1, 1000)
        y = abs(np.sin((2 * np.pi * frequency * t / sampling_rate)))
        sine_wave += [y]

    # sine_wave = [
    #     np.sin(2 * np.pi * frequency * t / sampling_rate)
    #     for t in range(num_samples)]

    nframes = num_samples

    comptype = 'NONE'

    compname = 'not compressed'

    nchannels = 1

    # Sample width in bytes.
    # 16 bits = 2 hex (bytes).
    sampwidth = 2

    with wave.open(file, 'w') as wave_file:
        wave_file.setparams((
            nchannels, sampwidth, sampling_rate, nframes, comptype, compname))

        for s in sine_wave:
            wave_file.writeframes(struct.pack('h', int(s * amplitude)))

    # plt.plot(sine_wave)


if __name__ == '__main__':
    main()
