import numpy as np
import sounddevice as sd

# Define parameters
sample_rate = 44100  # Sampling rate in Hz
duration = 0.5  # Duration of each power chord in seconds
amplitude = 0.6  # Amplitude of the notes
t = np.linspace(0, duration, int(sample_rate * duration))

# Frequencies for power chords in E, C, and G
frequencies = {
    "E": 82.41,  # E note
    "A": 110.00,  # A note
    "E": 329.63,  # E note
    "G": 392.00,  # G note
    "B": 493.88,  # B note
    "C": 261.63,  # C note
    "E_high": 659.26,  # High E note
    "D": 146.83,  # D note
}

# Generate power chords
em_power_chord = amplitude * (np.sin(2 * np.pi * frequencies["E"] * t) +
                              np.sin(2 * np.pi * frequencies["A"] * t))

c_power_chord = amplitude * (np.sin(2 * np.pi * frequencies["C"] * t) +
                             np.sin(2 * np.pi * frequencies["A"] * t))

g_power_chord = amplitude * (np.sin(2 * np.pi * frequencies["G"] * t) +
                             np.sin(2 * np.pi * frequencies["D"] * t))

# Concatenate the power chords for the riff
metal_riff = np.concatenate((em_power_chord, c_power_chord, g_power_chord))

for i in range(3):
    # Play the metal riff
    sd.play(metal_riff, sample_rate)
    sd.wait()
