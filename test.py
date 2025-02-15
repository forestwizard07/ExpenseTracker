import librosa
import numpy as np

# Load the audio file
filename = 'testmusic.mp3'
y, sr = librosa.load(filename)

# Run the beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

# Convert beat frames to timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# Ensure tempo is a single value
if isinstance(tempo, np.ndarray):
    tempo = tempo[0]

print(f'Estimated tempo: {tempo:.2f} beats per minute')
#print(f'Beat timestamps: {beat_times}')
C = np.abs(librosa.cqt(y, sr=sr))
print(C.shape) 



