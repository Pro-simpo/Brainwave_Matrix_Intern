import streamlit as st
import requests

# 📌 Configuration de la page (doit être la première commande)
st.set_page_config(page_title="Détection de Phishing", layout="centered")

# 📌 Ajout d'une image de fond via CSS
st.markdown("""
    <style>
    body {
        background-image: url("https://upload.wikimedia.org/wikipedia/commons/6/65/Abstract_background.jpg");
        background-size: cover;
    }
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        font-size: 18px;
        border-radius: 10px;
    }
    .stSuccess {
        color: #28a745;
        font-weight: bold;
    }
    .stError {
        color: #dc3545;
        font-weight: bold;
    }
    .stMarkdown h2 {
        color: #ffffff;
        background-color: rgba(0,0,0,0.7);
        padding: 10px;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# URL du backend Flask
API_URL = "http://127.0.0.1:5000/scan"

# 📌 Section explicative
st.markdown("## À propos de cette application")
st.write("""
Cette application utilise l'intelligence artificielle pour détecter les liens de phishing. Elle est conçue pour être simple d'utilisation et rapide dans l'analyse des URLs suspectes.
""")

# Titre et sous-titre
st.title("🔍 Détecteur de Phishing")
st.subheader("Entrez une URL pour vérifier sa sécurité")

# Saisie utilisateur
url_input = st.text_input("🔗 URL à analyser", placeholder="https://exemple.com")

if st.button("Analyser l'URL"):
    if url_input:
        # Envoyer la requête au backend Flask
        response = requests.post(API_URL, json={"url": url_input})
        print(response.text)  # Affiche le contenu brut de la réponse
        try:
            result = response.json()

            # Affichage du résultat
            if result["status"] == "Phishing":
                st.error(f"⚠️ Ce lien est suspect ! ({result['url']})")
            else:
                st.success(f"✅ Ce lien est sécurisé ! ({result['url']})")
        except requests.exceptions.JSONDecodeError:
            st.error("Erreur : La réponse de l'API n'est pas au format JSON.")
    else:
        st.warning("Veuillez entrer une URL valide.")