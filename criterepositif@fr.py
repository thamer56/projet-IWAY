# Liste des critères positifs (avec des répétitions)
criteres_positifs = [
    "bon", "excellent", "compétent", "professionnel", "dévoué", "efficace", "fiable", "positif", 
    "good", "excellent", "competent", "professional", "devoted", "efficient", "reliable", "positive",
    "attentif", "réactif", "précis", "rapide", "créatif", "proactif", "respectueux", "inspirant",
    "innovant", "fort", "dynamique", "expert", "adorable", "plein de ressources", "à l'écoute", 
    "aimable", "optimiste", "sérieux", "persévérant", "dévoué", "enthousiaste", "patient", 
    "créatif", "responsable", "compétent", "orienté résultats", "passionné", "engagé", "capable",
    "talentueux", "rigoureux", "organisé", "méthodique", "bienveillant", "empathique", "charismatique",
    "motivé", "déterminé", "perspicace", "intègre", "honnête", "loyal", "sincère", "chaleureux",
    "ouvert d'esprit", "flexible", "adaptable", "collaboratif", "diplomate", "visionnaire", "stratège",
    "analytique", "logique", "minutieux", "consciencieux", "altruiste", "généreux", "bien organisé",
    "efficience", "productif", "sûr", "confiant", "ambitieux", "courageux", "résilient", "audacieux",
    "sage", "réfléchi", "calme", "serein", "équilibré", "harmonieux", "inspiré", "motivant", 
    "encourageant", "soutien", "bienveillant", "compréhensif", "tolérant", "respectueux", "gracieux",
    "élégant", "charmant", "attrayant", "séduisant", "magnétique", "captivant", "fascinant", "brillant",
    "lumineux", "radieux", "éclatant", "vibrant", "enthousiasmant", "épanouissant", "éducatif", 
    "instructif", "enrichissant", "stimulant", "challengant", "récompensant", "gratifiant", "fulfillant",
    "agréable", "satisfaisant", "remarquable", "exceptionnel", "extraordinaire", "fantastique", 
    "formidable", "impressionnant", "inoubliable", "mémorable", "parfait", "splendide", "superbe", 
    "admirable", "éblouissant", "émerveillant", "fabuleux", "mirobolant", "prodigieux", "stupéfiant",
    "sublime", "surprenant", "unique", "incomparable", "inégalé", "inimitable", "irréprochable",
    "irrésistible", "magnifique", "merveilleux", "miraculeux", "phénoménal", "prodigieux", "renversant",
    "sensationnel", "spectaculaire", "splendide", "étonnant", "épatant", "époustouflant", "étourdissant",
    "fascinant", "foudroyant", "glorieux", "grandiose", "héroïque", "inouï", "légendaire", "magique",
    "majestueux", "miraculeux", "mythique", "pharaonique", "royal", "souverain", "triomphal", "victorieux",
    "vigoureux", "vivifiant", "volontaire", "zélé", "ardent", "assidu", "constant", "diligent", "infatigable",
    "laborieux", "opiniâtre", "persistant", "tenace", "travailleur", "vaillant", "volontaire", "acharné",
    "combatif", "décidé", "énergique", "ferme", "inflexible", "résolu", "volontaire", "actif", "allègre",
    "débordant", "énergique", "entreprenant", "fringant", "infatigable", "intrépide", "remuant", "robuste",
    "solide", "vigoureux", "vivace", "vif", "alerte", "éveillé", "lucide", "perçant", "perspicace", "sagace",
    "subtile", "fin", "intelligent", "astucieux", "avisé", "clairvoyant", "judicieux", "malin", "prudent",
    "rationnel", "réfléchi", "sensé", "sérieux", "avisé", "calculé", "circonspect", "discernant", "équilibré",
    "pondéré", "raisonnable", "sensé", "ponctuel"
]

# Supprimer les répétitions en utilisant un ensemble
criteres_positifs_uniques = list(set(criteres_positifs))

# Afficher le résultat nettoyé
print(criteres_positifs_uniques)

# Créer un DataFrame avec la liste nettoyée
import pandas as pd
df_criteres_positifs = pd.DataFrame(criteres_positifs_uniques, columns=["Critère Positif"])

# Sauvegarder dans un fichier Excel
df_criteres_positifs.to_excel("criteres_positifs@FR.xlsx", index=False)

print("Fichier 'criteres_positifs_nettoyes.xlsx' généré avec succès!")
