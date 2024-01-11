# importation de la bibliothèque sr pour la reconnaissance vocale
import speech_recognition as sr

# importation de la fonction path de la bibliothèque os
from os import path

# obtenir le chemin d'accès exact du fichier audio à transcrire
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "Affecter_planning_individuel.wav")

# création d'un objet qui s'occupe de la reconnaissance vocale
r = sr.Recognizer()

# ouverture du fichier audio avec le bloc "with"
with sr.AudioFile(AUDIO_FILE) as source:
    # prends le temps de lire l'entièreté de
    audio = r.record(source) 

# recognize speech using Google Speech Recognition
try:
    # utilisation du clé d'api par défaut de google avec la fonction r.recognize_google()
    # l'argument language="fr-FR" spécifie juste que l'audio est en français
    print("Résulat de SpeechRecognition : " + r.recognize_google(audio, language="fr-FR"))

# permet de faire ressortir les erreurs éventuelles
except sr.UnknownValueError:
    print("Speech Recognition ne comprend pas l'audio")
except sr.RequestError as e:
    print("Erreur lors du contact avec l'API; {0}".format(e))