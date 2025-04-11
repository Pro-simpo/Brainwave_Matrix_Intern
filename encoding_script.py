import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Charger le fichier CSV
file_path = "urls_features_full.csv"  # Remplacez par le chemin de votre fichier
data = pd.read_csv(file_path)

# Initialiser le LabelEncoder
encoder = LabelEncoder()

# Encoder la variable textuelle 'Domaine principal'
data['domain_encoded'] = encoder.fit_transform(data['Domaine principal'])

# Afficher un aperçu des données encodées
print(data[['Domaine principal', 'domain_encoded']].head())

# Sauvegarder les données encodées dans un nouveau fichier CSV
output_path = "data_encoded.csv"
data.to_csv(output_path, index=False)
print(f"Fichier encodé enregistré sous : {output_path}")