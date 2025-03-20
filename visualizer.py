import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Load an audio file (must be .wav)
audio_file = "C:/Users/Alina/mymodules/musicvisualizer/base.wav"  # Replace with your file
sample_rate, data = wavfile.read(audio_file)

# Normalize the waveform (for better visualization)
data = data / np.max(np.abs(data))

# Create a time axis
time = np.linspace(0, len(data) / sample_rate, num=len(data))

# Plot the waveform
plt.figure(figsize=(12, 4))
plt.plot(time, data, color='purple', linewidth=1)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Waveform Visualization")
plt.ylim(-1, 1)  # Keep scale consistent
plt.grid(True)
plt.show()