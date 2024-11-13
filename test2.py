import matplotlib.pyplot as plt
import numpy as np
import wave

# Load the recorded audio file
audio_file = 'Instrument.m4a'  # Replace with your audio file path
wave_file = wave.open(audio_file, 'rb')

# Get audio file parameters
sample_width = wave_file.getsampwidth()
frame_rate = wave_file.getframerate()
num_frames = wave_file.getnframes()

# Read audio data
audio_data = wave_file.readframes(num_frames)
audio_data = np.frombuffer(audio_data, dtype=np.int16)

# Create a time axis
time = np.linspace(0, num_frames / frame_rate, num_frames)

# Create a figure for plotting
plt.figure(figsize=(12, 4))

# Plot the audio data on an oscilloscope-like display
plt.plot(time, audio_data, color='blue')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Audio Waveform (Oscilloscope-like)')
plt.grid(True)

plt.show()
