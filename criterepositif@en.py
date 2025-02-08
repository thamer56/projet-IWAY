import pandas as pd

# Liste des mots-clés positifs en anglais (avec des répétitions)
criteres_positifs_anglais = [
    "good", "excellent", "outstanding", "great", "positive", "amazing", "fantastic", 
    "superb", "wonderful", "marvelous", "impressive", "brilliant", "awesome", 
    "remarkable", "favorable", "satisfactory", "helpful", "encouraging", "inspiring", 
    "effective", "efficient", "successful", "exceptional", "high quality", 
    "first class", "top-notch", "reliable", "strong", "proficient", "skilled", 
    "capable", "affordable", "innovative", "valuable", "useful", "outstanding", 
    "brilliant", "quality", "fantastic", "incredible", "terrific", "pleasant", 
    "trustworthy", "reputable", "exceptional", "consistently good", "worthwhile", 
    "fruitful", "progressive", "empowering", "smooth", "awesome", "precise", 
    "solid", "productive", "helpful", "strong performance", "positive outcome", 
    "positive feedback", "satisfying", "successful", "highly recommended", 
    "delightful", "constructive", "engaging", "rewarding", "relevant", 
    "visionary", "effective", "motivational", "engaging", "excellent customer service", 
    "efficient service", "well-structured", "easy to use", "user-friendly", 
    "detailed", "well-organized", "impressive results", "valuable contribution", 
    "positive attitude", "supportive", "respectful", "enthusiastic", "optimistic", 
    "friendly", "energetic", "enjoyable", "cheerful", "grateful", "satisfied", 
    "great customer service", "peaceful", "reliable", "dependable", "considerate", 
    "highly effective", "outstanding quality", "motivated", "great performance", 
    "dynamic", "optimistic", "inspiring", "good communication", "outstanding service"
]

# Utilisation d'un set pour éliminer les répétitions
criteres_positifs_anglais_uniques = set(criteres_positifs_anglais)

# Convertir la liste unique en DataFrame pandas
df_criteres_positifs_anglais = pd.DataFrame(criteres_positifs_anglais_uniques, columns=["Critères Positifs"])

# Créer un fichier Excel
excel_path = "criteres_positifs@EN.xlsx"
df_criteres_positifs_anglais.to_excel(excel_path, index=False)

print(f"Le fichier Excel a été créé avec succès : {excel_path}")
