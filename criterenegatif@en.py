import pandas as pd

# Liste des mots-clés négatifs en anglais (avec des répétitions)
criteres_negatifs_anglais = [
    "bad", "terrible", "awful", "horrible", "negative", "poor", "unpleasant", 
    "unhelpful", "useless", "ineffective", "inefficient", "unreliable", "disappointing", 
    "low quality", "mediocre", "subpar", "unsatisfactory", "unacceptable", 
    "frustrating", "dismal", "unfriendly", "unproductive", "failure", "weak", 
    "unsuccessful", "unfavorable", "negative feedback", "rude", "dishonest", 
    "untrustworthy", "disrespectful", "ignorant", "stubborn", "uncooperative", 
    "deceptive", "irresponsible", "chaotic", "messy", "unorganized", "incomplete", 
    "disorganized", "unprofessional", "disengaging", "boring", "uninspiring", 
    "unmotivated", "uncaring", "selfish", "hostile", "unfriendly attitude", 
    "defensive", "suspicious", "unreliable service", "impatient", "overwhelming", 
    "unapproachable", "unempathetic", "confrontational", "dismissive", "irritating", 
    "troublesome", "unreliable", "unhelpful", "unacceptable", "unfair", 
    "dissatisfying", "frustrating experience", "annoying", "disrespectful behavior", 
    "poor quality", "uninspiring performance", "non-responsive", "unclear", 
    "unpredictable", "substandard", "undesirable", "uncomfortable", "unsafe", 
    "dangerous", "lacking", "lousy", "pathetic", "unskilled", "clumsy", "horrendous", 
    "vicious", "disappointing results", "suboptimal", "unprofessional behavior", 
    "unqualified", "irregular", "problematic", "non-compliant", "insufficient", 
    "difficult", "inefficient service", "unsuitable", "unimpressive", "inadequate", 
    "poor communication", "unpleasant experience", "distracting", "boring work", 
    "unattractive", "stressful", "unreliable results", "unnecessary", "insincere"
]

# Utilisation d'un set pour éliminer les répétitions
criteres_negatifs_anglais_uniques = set(criteres_negatifs_anglais)

# Convertir la liste unique en DataFrame pandas
df_criteres_negatifs_anglais = pd.DataFrame(criteres_negatifs_anglais_uniques, columns=["Critères Négatifs"])

# Créer un fichier Excel
excel_path = "criteres_negatifs@EN.xlsx"
df_criteres_negatifs_anglais.to_excel(excel_path, index=False)

print(f"Le fichier Excel a été créé avec succès : {excel_path}")
