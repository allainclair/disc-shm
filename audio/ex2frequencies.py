"""
https://www.pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/
"""
import struct
import wave

import numpy as np


def main():
    # Sine function: y(t) = A * sin(2 * pi * f * t)

    # frequency is the number of times a wave repeats a second.
    frequency1 = 1000
    frequency2 = 10000

    num_samples1 = 48000
    num_samples2 = 48000

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
    # ampliture serah de 16000.
    amplitude = 16000

    file = 'test.wav'

    sine_wave1 = [
        np.sin(2 * np.pi * frequency1 * x / sampling_rate)
        for x in range(num_samples1)]

    sine_wave2 = [
        np.sin(2 * np.pi * frequency2 * x / sampling_rate)
        for x in range(num_samples2)]

    nframes = num_samples1 + num_samples2

    comptype = 'NONE'

    compname = 'not compressed'

    nchannels = 1

    # Sample width in bytes.
    # 16 bits = 2 hex (bytes).
    sampwidth = 2

    with wave.open(file, 'w') as wave_file:
        wave_file.setparams((
            nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

        for s in sine_wave1:
            wave_file.writeframes(struct.pack('h', int(s * amplitude)))

        for s in sine_wave2:
            wave_file.writeframes(struct.pack('h', int(s * amplitude)))


if __name__ == '__main__':
    main()
