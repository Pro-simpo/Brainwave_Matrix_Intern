import pandas as pd
from urllib.parse import urlparse

# Définir les caractères suspects
SUSPICIOUS_CHARS = ['@', '-', '_', '=', '&', '%', '$', '!', '?', '*']

def extract_features(url, label):
    parsed = urlparse(url)
    domain_parts = parsed.netloc.split('.')
    domain = parsed.netloc
    return {
        'URL': url,
        'Longueur': len(url),
        'Caractères suspects': sum(url.count(c) for c in SUSPICIOUS_CHARS),
        'Nombre de sous-domaines': max(0, len(domain_parts) - 2),
        'Domaine principal': domain_parts[-2] + '.' + domain_parts[-1] if len(domain_parts) >= 2 else domain,
        'Label': label
    }

def process_files(phishing_file, legit_file, output_file):
    # Lecture des fichiers
    with open(phishing_file, 'r', encoding='utf-8', errors='ignore') as f:
        phishing_lines = f.readlines()

    with open(legit_file, 'r', encoding='utf-8', errors='ignore') as f:
        legit_lines = f.readlines()

    # Extraction des URLs
    phishing_urls = [line.split(',')[1].strip() for line in phishing_lines[1:] if len(line.split(',')) > 1]
    legit_urls = ["https://" + line.split(',')[1].strip() for line in legit_lines if len(line.split(',')) > 1]

    # Transformation en features
    data = [extract_features(url, 1) for url in phishing_urls] + \
           [extract_features(url, 0) for url in legit_urls]

    # Création du DataFrame et exportation
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"Fichier généré avec succès : {output_file}")

if __name__ == "__main__":
    process_files(
        phishing_file='sites phishing.csv',
        legit_file='sites légitimes.csv',
        output_file='urls_features_full.csv'
    )
