from flask import Flask, request
import requests

app = Flask(__name__)

# Remplacez par votre token de bot Telegram
TELEGRAM_BOT_TOKEN = "7646166036:AAFyFykauVkFczWlv003fz7VvCuHOuFBnAg"
# Remplacez par votre Chat ID (utilisateur ou groupe)
TELEGRAM_CHAT_ID = "6784396054"

def send_to_telegram(data):
    """
    Envoie les données reçues du formulaire au bot Telegram.
    """
    message = "📋 Nouvelle soumission de formulaire :\n\n"
    for key, value in data.items():
        message += f"📝 *{key.capitalize()}* : {value}\n"

    # URL de l'API Telegram pour envoyer un message
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    # Envoi de la requête et gestion des erreurs
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ Message envoyé sur Telegram avec succès !")
    else:
        print(f"❌ Erreur lors de l'envoi à Telegram : {response.status_code} - {response.text}")

@app.route('/submit-form', methods=['POST'])
def submit_form():
    """
    Route pour recevoir les données du formulaire.
    """
    # Récupérer les données du formulaire
    data = request.form
    print("Données reçues depuis le formulaire :")
    for key, value in data.items():
        print(f"{key}: {value}")

    # Envoyer les données au bot Telegram
    send_to_telegram(data)

    return "✅ Données reçues et envoyées à Telegram !", 200

if __name__ == '__main__':
    # Lancer le serveur Flask
    app.run(port=5000)
