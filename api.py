import pickle
import pandas as pd
import tldextract
from flask import Flask, request, jsonify

# Charger le modèle de Machine Learning
model_path = "model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Initialiser Flask
app = Flask(__name__)

# Fonction d'extraction des caractéristiques
def extract_features(url):
    features = {
        'Longueur': len(url),
        'Caractères suspects': 1 if ('@' in url or '-' in url) else 0,
        'Nombre de sous-domaines': len(tldextract.extract(url).subdomain.split('.')),
        'domain_encoded': 0  # Placeholder, car l'encodage des domaines est statique
    }
    return pd.DataFrame([features])

# Route API pour scanner une URL
@app.route('/scan', methods=['POST'])
def scan_url():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "Aucune URL fournie"}), 400

    features_df = extract_features(url)
    prediction = model.predict(features_df)[0]

    result = "Phishing" if prediction == 1 else "Légitime"
    
    return jsonify({"url": url, "status": result})

# Lancer l'application Flask
if __name__ == '__main__':
    app.run(port=5000)