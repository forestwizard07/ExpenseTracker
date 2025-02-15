import librosa
import numpy as np

# Load audio
y, sr = librosa.load("testmusic.mp3", sr=None)

# Compute CQT (Constant-Q Transform)
n_bins = 84  # 7 octaves (C1 to C8)
C = np.abs(librosa.cqt(y, sr=sr, n_bins=n_bins, fmin=librosa.note_to_hz('C1')))

# Compute the average energy of each frequency bin
mean_energy = np.mean(C, axis=1)

# Define a threshold for detecting notes (adjust if needed)
threshold = np.max(mean_energy) * 0.3  # 30% of max energy

# Get bin indices where energy is above the threshold
active_bins = np.where(mean_energy > threshold)[0]

# Get the actual note names
note_names = librosa.midi_to_note(librosa.hz_to_midi(librosa.cqt_frequencies(n_bins, fmin=librosa.note_to_hz('C1'))))

# Get detected notes
detected_notes = [note_names[i] for i in active_bins]

# Output detected notes
print("Detected Notes:", detected_notes)
