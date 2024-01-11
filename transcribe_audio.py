# import module speech_recognition and json
import speech_recognition as sr
import ffmpeg
import os
import json

# la fonction qui permettra de transcrire le fichier audio en texte, la fonction prendra en argument le fichier audio
def transcribe(audio_file):
    print('Hi')
    if os.path.isfile(audio_file):
        print("le fichier existe")
    else:
        print('Le fichier n\'existe pas .')
    # Création d'un objet qui reconnait la parole dans le fichier audio
    voice_recognizer = sr.Recognizer()
    
    # if voice_recognizer:
    #     print(dir(voice_recognizer))

    # Ouverture du fichier audio_file
    with sr.AudioFile(audio_file) as source:
        #lecture du fichier audio
        audio = voice_recognizer.record(source)
    
    #Transcription de l'audio
    transcription = ''
    
    try:
        # Utiliser le modèle de reconnaissance vocale Google
        file_extension = os.path.splitext(audio_file)[1].lower()
        supported_extensions = ['.wav', '.flac', '.mp3']

        if file_extension in supported_extensions:
            transcription = voice_recognizer.recognize_google(audio, language="fr-FR")
            print('ok')
        else: 
            transcription = "Format non pris en charge"
            print('maladif')
    except sr.UnknownValueError:
        # La transcription n'a pas pu être générée
        transcription = "Transcription non disponible"
    except sr.RequestError as e:
        #Une erreur est survenue lors de la demande de transcription
        transcription = "Erreur de requête : {}".format(e)
    
    #créer un objet JSON
    json_data = {
        "transcription": transcription
    }
    
    #retourner la transcription
    return json_data
    
        
#Chemin du fichier audio
file = "conversation-téléphonique.wav"
# file_wav = "conversation-téléphonique.wav"
# ffmpeg.input(file_mp3).output(file_wav).run()

json_data = transcribe(file)
print(json_data)