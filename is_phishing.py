import pickle
import pandas as pd
import tldextract

# 📌 1️⃣ Charger le modèle entraîné
model_path = "model.pkl"  # Remplacez par le chemin de votre modèle sauvegardé
with open(model_path, "rb") as file:
    model = pickle.load(file)

# 📌 2️⃣ Fonction pour extraire les caractéristiques de l'URL
def extract_features(url):
    features = {}
    features['Longueur'] = len(url)
    features['Caractères suspects'] = 1 if ('@' in url or '-' in url or '_' in url or '=' in url or '&' in url or '%' in url or '$' in url or '!' in url or '?' in url or '*' in url) else 0
    features['Nombre de sous-domaines'] = len(tldextract.extract(url).subdomain.split('.'))
    features['domain_encoded'] = 0  # Placeholder (pas utilisé pour la prédiction directe)
    return features

# 📌 3️⃣ Fonction pour scanner une URL
def scan_url(url):
    # Extraire les caractéristiques
    features = extract_features(url)
    df = pd.DataFrame([features])  # Convertir en DataFrame

    # Faire la prédiction avec le modèle
    prediction = model.predict(df)

    # Résultat
    if prediction[0] == 1:
        return f"⚠️ Attention : Le lien '{url}' semble être du phishing !"
    else:
        return f"✅ Ce lien '{url}' est sécurisé."

# 📌 4️⃣ Exemple d'utilisation
if __name__ == "__main__":
    url_test = input("Entrez l'URL à scanner : ")
    result = scan_url(url_test)
    print(result)