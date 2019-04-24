"""
https://www.pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/
"""
import signalwave


def main():
    frequency = 500
    sampling_rate = 48000
    amplitude = 16000
    time_ = 2

    wave1 = signalwave.signalwave(frequency, sampling_rate, time=time_)
    abs_wave = [abs(signal) for signal in wave1]

    # Plot the 2 waves
    signalwave.plot(wave1, abs_wave)

    signalwave.save_wave(wave1, file_path='wave.wav')
    signalwave.save_wave(abs_wave, file_path='abs_wave.wav')


if __name__ == '__main__':
    main()
