import os
from pydub import AudioSegment
import speech_recognition as sr
import librosa
import numpy as np

# Set the FFMPEG_PATH environment variable
os.environ["FFMPEG_PATH"] = "C:\_programmes\ffmpeg"

# Chargez l'audio fichier
audio = AudioSegment.from_wav("Affecter_planning_individuel.wav")

# Convertissez l'audio en un tableau numpy
audio_array = np.array(audio.get_array_of_samples(), dtype=np.float32)

# Extrayez des caractéristiques de l'audio
features = librosa.feature.mfcc(y=audio_array, sr=audio.frame_rate)

# Effectuez la segmentation de l'audio par locuteur
labels, _ = librosa.load('Affectation_planning_individuel.wav', sr=audio.frame_rate)
labels = librosa.effects.trim(labels)

# Initialisez le reconnaisseur de parole
r = sr.Recognizer()

# Initialisez la liste des transcriptions
transcriptions = []

# Parcourez chaque segment de parole
for i, label in enumerate(labels):
    # Extrayez le segment de parole actuel
    start = i * 1000  # en supposant 1000 échantillons par seconde
    end = (i + 1) * 1000
    segment = audio_array[start:end]

    # Écrivez le segment actuel dans un fichier temporaire
    temp_audio = AudioSegment(segment, frame_rate=audio.frame_rate, sample_width=audio.sample_width)
    temp_audio.export("temp.wav", format="wav")

    # Effectuez la reconnaissance vocale sur le segment
    with sr.AudioFile("temp.wav") as source:
        audio = r.record(source)
        transcription = r.recognize_google(audio)
        transcriptions.append((transcription, i))

# Affichez les transcriptions avec les locuteurs correspondants
for transcription, i in transcriptions:
    print(f"Locuteur {i}: {transcription}")