import pandas as pd

# Liste des mots-clés négatifs (avec des répétitions)
criteres_negatifs = [
    "mauvais", "médiocre", "inefficace", "peu fiable", "négatif", "mauvaise", 
    "poor", "bad", "mediocre", "inefficient", "unreliable", "negative", 
    "désorganisé", "lent", "inefficace", "passif", "indifférent", "insensible", 
    "insatisfait", "inefficace", "rude", "désagréable", "désintéressé", "arrogant", 
    "désengagé", "désordonné", "déséquilibré", "incompétent", "malhonnête", 
    "inefficient", "irresponsable", "désinvolte", "pessimiste", "insensible", 
    "égoïste", "intolérant", "lourd", "lenteur", "fou", "colérique", "impulsif", 
    "impoli", "sévère", "inflexible", "prétentieux", "dispersé", "nonchalant", 
    "irrespectueux", "mauvais comportement", "désagréable", "dédaigneux", 
    "injuste", "pervers", "rancunier", "machiavélique", "désespéré", "douloureux", 
    "incapable", "faible", "negligent", "insuffisant", "arrogant", "dépassé", 
    "distrait", "surmené", "moralement faible", "instable", "incohérent", 
    "irrespectueux", "débile", "barbare", "abusif", "ignorant", "difficile", 
    "chaotique", "hostile", "lourd", "irascible", "désespérant", "démoralisant", 
    "désagréable", "imprudent", "manque de tact", "violente", "futile", 
    "généralement négatif", "sans valeur", "inutile", "gênant", "inutile", 
    "nocif", "néfaste", "défectueux", "inutile", "désastreux", "sans intérêt", 
    "perturbateur", "stressant", "déséquilibré", "inquiet", "déstabilisant", 
    "indésirable", "exaspérant", "désenchanté", "mauvaise gestion", "mal conçu", 
    "relativement faible", "impuissant", "dégradant", "sans conviction", 
    "désespérant", "détourné", "dangereux", "ineptie", "stressant", "insouciant", 
    "volatil", "désapprouvé", "fluctuant", "chaotique", "incompétent", "nocif", 
    "trop exigeant", "détaché", "toxique", "irrationnel", "impraticable", 
    "déséquilibré", "perturbant", "délétère", "vulnérable", "accablant", 
    "problématique", "inhumain", "désordonné", "insupportable", "prisonnier", 
    "désorienté", "brouillon", "insatisfaisant", "irréparable", "dysfonctionnel", 
    "obsolète", "incompatible", "difficilement gérable", "perturbant", 
    "irréversible", "prisonnier", "répréhensible", "révoltant", "déprimant", 
    "instable", "insupportable", "injustifiable", "inopérant", "impardonnable", 
    "incompréhensible", "désintéressé", "désobligeant", "insultant", 
    "désagréablement", "pervers", "contreproductif", "risqué", "subversif", 
    "dérangeant", "inutilement complexe", "encombrant", "pessimiste", "méchant", 
    "déficient", "non sécurisé", "insignifiant", "contreproductif", "déroutant", 
    "irréel", "absurde", "anormal", "ineffable", "dégradé", "désespéré", 
    "inadéquat", "inapproprié", "déséquilibré", "dérangé", "imparfait", 
    "déstabilisant", "désagréable", "désengagé", "perdu", "trop lent", "en retard", 
    "non fiable", "déséquilibré", "impraticable", "instable", "inopérant", 
    "injustifiable", "problématique"
]

# Utilisation d'un set pour éliminer les répétitions
criteres_negatifs_uniques = set(criteres_negatifs)

# Convertir la liste unique en DataFrame pandas
df_criteres_negatifs = pd.DataFrame(criteres_negatifs_uniques, columns=["Critères Négatifs"])

# Créer un fichier Excel
excel_path = "criteres_negatifs@FR.xlsx"
df_criteres_negatifs.to_excel(excel_path, index=False)

print(f"Le fichier Excel a été créé avec succès : {excel_path}")
