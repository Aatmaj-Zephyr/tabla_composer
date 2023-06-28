# for bols like kat, where extension is silence
import librosa
import numpy as np
import soundfile as sf

filename="Ke"
# Load the audio file
audio, sr = librosa.load("Bols/"+filename+".wav")

# Duration of silence to add (in seconds)
silence_duration = 2.0

# Compute the number of samples for the silence duration
silence_samples = int(silence_duration * sr)

# Create an array of zeros representing silence
silence = np.zeros(silence_samples)

# Concatenate the original audio with the silence
audio_with_silence = np.concatenate((audio, silence))

# Save the audio with added silence to a new file
sf.write("Bols/"+filename+".wav", audio_with_silence, sr)