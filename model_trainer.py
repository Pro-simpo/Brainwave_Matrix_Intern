import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# 📌 1️⃣ Charger les données
file_path = "data_encoded.csv"  # Remplacez par votre fichier CSV
data = pd.read_csv(file_path)

# 📌 2️⃣ Prétraitement des données
# Sélectionner les caractéristiques (X) et les labels (y)
X = data[['Longueur', 'Caractères suspects', 'Nombre de sous-domaines', 'domain_encoded']]
y = data['Label']

# Diviser en données d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=5)

# 📌 3️⃣ Entraînement du modèle
model = RandomForestClassifier(n_estimators=1500, random_state=5)
model.fit(X_train, y_train)

# 📌 4️⃣ Évaluation du modèle
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Précision du modèle : {accuracy:.2f}")

# 📌 5️⃣ Sauvegarde du modèle
model_filename = "model.pkl"
with open(model_filename, "wb") as file:
    pickle.dump(model, file)

print(f"🎯 Modèle sauvegardé sous : {model_filename}")