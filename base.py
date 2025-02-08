import pandas as pd
from faker import Faker
import random

# Initialisation de Faker pour générer des avis en anglais et en français
faker_fr = Faker('fr_FR')
faker_en = Faker('en_US')

# Définition des types de relations possibles
relations = ["manager", "superviseur", "ami"]

# Liste pour stocker les données
data = []

# Génération des données pour 950 employés
for i in range(1, 951):  # 950 employés
    num_avis = random.randint(15, 19)  # Chaque employé reçoit entre 15 et 19 avis
    for _ in range(num_avis):
        avis = faker_fr.sentence() if random.choice([True, False]) else faker_en.sentence()
        relation = random.choice(relations)
        data.append([i, avis, relation])

# Création du DataFrame
df = pd.DataFrame(data, columns=["ID", "Avis", "Relation"])

# Sauvegarde dans un fichier Excel
df.to_excel("feedbacks.xlsx", index=False)

print("Fichier 'feedbacks.xlsx' généré avec succès avec 950 employés et plusieurs avis par employé !")
