import pandas as pd

# 📌 Charger les données
file_path = "data_encoded.csv"  # Chemin vers votre fichier CSV
data = pd.read_csv(file_path)

# 📌 Identifier les classes majoritaires et minoritaires
legitimate_data = data[data['Label'] == 0]  # Données légitimes (label 0)
phishing_data = data[data['Label'] == 1]    # Données de phishing (label 1)

print(f"Nombre de données légitimes : {len(legitimate_data)}")
print(f"Nombre de données phishing : {len(phishing_data)}")

# 📌 Sous-échantillonner les données légitimes pour équilibrer
balanced_legitimate_data = legitimate_data.sample(n=len(phishing_data), random_state=42)  # Prendre un échantillon aléatoire

# 📌 Combiner les données équilibrées
balanced_data = pd.concat([balanced_legitimate_data, phishing_data])

# 📌 Sauvegarder les données équilibrées dans un nouveau fichier CSV
output_path = "balanced_data.csv"
balanced_data.to_csv(output_path, index=False)

print(f"Dataset équilibré sauvegardé sous : {output_path}")
print(f"Nombre total de données équilibrées : {len(balanced_data)}")