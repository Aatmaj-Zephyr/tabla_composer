import librosa
import numpy as np
import librosa.display
import soundfile as sf
speed= 0.1875 *4 #ie 160 bpm
Dha, sr = librosa.load("Bols/Dha.wav",duration=speed)


Ti, sr = librosa.load("Bols/Ta.wav",duration=speed)


Ta, sr = librosa.load("Bols/Ti.wav",duration=speed)

Ga, sr = librosa.load("Bols/Ga.wav",duration=speed)

Tun, sr = librosa.load("Bols/Tun.wav",duration=speed)

Na, sr = librosa.load("Bols/Na.wav",duration=speed)

Ke, sr = librosa.load("Bols/Ke.wav",duration=speed)

Dhin, sr = librosa.load("Bols/Dhin.wav",duration=speed)

s , sr = librosa.load("Bols/s.wav",duration=speed)

teen_taal= [Dha,Dhin,Dhin,Dha,Dha,Dhin,Dhin,Dha,Dha,Tun,Tun,Na,Na,Dhin,Dhin,Dha]
z = np.concatenate(teen_taal) # concentate variables to make array
    
    
sf.write('teen_taal.wav', z, sr) #make sound file