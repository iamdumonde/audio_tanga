import speech_recognition as sr

# Création de liste pour chaque interlocuteur
interlocuteurs = [
    {
        "nom": "interlocuteur 1",
        "texte": [],
    },
    {
        "nom": "interlocuteur 2",
        "texte": [],
    },
]

# Créer un objet de reconnaissance vocale
recognizer = sr.Recognizer()

# Charger l'audio
audio_file = sr.AudioFile("conversation-téléphonique.wav")

# Transcrire l'audio
with audio_file as source:
    audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data, language="fr-FR")  # Utilisez la méthode appropriée ici

# Déterminer l'interlocuteur
interlocuteur = None
for word in text.split():
    if interlocuteur is None:
        interlocuteur = "interlocuteur 1"
    elif interlocuteur == "interlocuteur 1":
        interlocuteur = "interlocuteur 2"

# Ajouter la ligne à la liste de l'interlocuteur correspondant
if interlocuteur in [i["nom"] for i in interlocuteurs]:
    interlocuteur_index = [i["nom"] for i in interlocuteurs].index(interlocuteur)
else:
    interlocuteur_index = None

if interlocuteur_index is not None:
    for ligne in text.splitlines():
        interlocuteurs[interlocuteur_index]["texte"].append(ligne)
else:
    print("Interlocuteur non trouvé dans la liste.")

# Afficher la transcription pour chaque interlocuteur
for interlocuteur in interlocuteurs:
    print(f"{interlocuteur['nom']}: {interlocuteur['texte']}")

