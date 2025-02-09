import pandas as pd
from langdetect import detect, DetectorFactory, LangDetectException

# Assurer la reproductibilité de la détection de langue
DetectorFactory.seed = 0  

# Charger les données des avis
df = pd.read_excel("feedbacks.xlsx")

# Charger les critères positifs et négatifs en minuscules
def load_criteria(filename):
    return [x.lower().strip() for x in pd.read_excel(filename, header=None)[0].tolist()]

criteres_positifs_en = load_criteria('criteres_positifs@EN.xlsx')
criteres_negatifs_en = load_criteria('criteres_negatifs@EN.xlsx')
criteres_positifs_fr = load_criteria('criteres_positifs@FR.xlsx')
criteres_negatifs_fr = load_criteria('criteres_negatifs@FR.xlsx')

# Fonction pour détecter la langue d'un avis
def detect_language(feedback):
    try:
        return detect(feedback)
    except LangDetectException:
        return 'fr'  # Langue par défaut si la détection échoue

# Fonction pour analyser les avis
def analyze_feedback(feedback, language):
    criteria_positive = criteres_positifs_fr if language == 'fr' else criteres_positifs_en
    criteria_negative = criteres_negatifs_fr if language == 'fr' else criteres_negatifs_en

    words = feedback.lower().split()
    positive_count = sum(1 for word in words if word in criteria_positive)
    negative_count = sum(1 for word in words if word in criteria_negative)

    return positive_count, negative_count

# Liste pour stocker les résultats
results = []

for index, row in df.iterrows():
    feedback = row['Avis']
    relation = row['Relation']
    language = detect_language(feedback)

    positive_count, negative_count = analyze_feedback(feedback, language)
    results.append([row['ID'], language, positive_count, negative_count, relation, feedback])

# Créer un DataFrame avec les résultats
results_df = pd.DataFrame(results, columns=['ID', 'Language', 'PositiveCount', 'NegativeCount', 'Relation', 'Feedback'])

# Ajouter une colonne `Priority`
results_df['Priority'] = results_df['PositiveCount'] - results_df['NegativeCount']

# Calcul des résultats globaux
total_positives = results_df['PositiveCount'].sum()
total_negatives = results_df['NegativeCount'].sum()

# Calcul des statistiques pour chaque employé
employee_stats = results_df.groupby('ID').agg({'PositiveCount': 'sum', 'NegativeCount': 'sum'}).reset_index()
employee_stats['Score'] = employee_stats['PositiveCount'] - employee_stats['NegativeCount']

# Trier les employés par score
employee_stats_sorted = employee_stats.sort_values(by='Score', ascending=False)

# Trouver le meilleur employé
best_employee = employee_stats_sorted.iloc[0]

# Sélectionner les avis remarquables : 5 par employé
remarkable_feedbacks = []
for emp_id in results_df['ID'].unique():
    emp_feedbacks = results_df[results_df['ID'] == emp_id]
    emp_feedbacks_sorted = emp_feedbacks.sort_values(by=['Priority', 'PositiveCount', 'NegativeCount'], 
                                                     ascending=[True, False, False])
    remarkable_feedbacks.append(emp_feedbacks_sorted.head(5))

# Concaténation des avis remarquables
remarkable_feedbacks_df = pd.concat(remarkable_feedbacks)

# Enregistrer les résultats dans un fichier Excel
with pd.ExcelWriter('feedback_analysis_results.xlsx', engine='xlsxwriter') as writer:
    employee_stats_sorted.to_excel(writer, sheet_name='EmployeeStats', index=False)
    remarkable_feedbacks_df.to_excel(writer, sheet_name='RemarkableFeedbacks', index=False)
    pd.DataFrame({'Total Positives': [total_positives], 'Total Negatives': [total_negatives]}).to_excel(writer, sheet_name='GlobalStats', index=False)
    pd.DataFrame({'Best Employee ID': [best_employee['ID']], 'Best Employee Score': [best_employee['Score']]}).to_excel(writer, sheet_name='BestEmployee', index=False)

print("Les résultats ont été enregistrés dans 'feedback_analysis_results.xlsx'.")
