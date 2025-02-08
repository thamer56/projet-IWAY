import pandas as pd

# Charger le fichier Excel
df = pd.read_excel("feedbacks.xlsx")

# Afficher les premières lignes du DataFrame pour vérifier la structure
print("Aperçu des données :")
print(df.head())

# Vérifier la présence de valeurs manquantes
print("\nVérification des valeurs manquantes :")
print(df.isnull().sum())

# Nettoyage des données : 
# Suppression des lignes avec des valeurs manquantes (si nécessaire)
df = df.dropna()

# Standardisation des textes : mettre tout en minuscules et supprimer la ponctuation
df["Avis"] = df["Avis"].str.lower()  # Mettre en minuscules

# Optionnel : Si nécessaire, on peut aussi supprimer la ponctuation
import string
df["Avis"] = df["Avis"].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)))

# Vérifier à nouveau la structure du DataFrame
print("\nAperçu après nettoyage :")
print(df.head())

# Sauvegarder les données nettoyées dans un nouveau fichier Excel
df.to_excel("feedbacks_cleaned.xlsx", index=False)

print("\nLes données ont été nettoyées et sauvegardées dans 'feedbacks_cleaned.xlsx'.")
