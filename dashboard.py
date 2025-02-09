import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd
from dash import Input, Output

# Charger les données à partir de l'Excel
file_path = 'feedback_analysis_results.xlsx'

# Chargement des différentes feuilles
feedback_analysis_df = pd.read_excel(file_path, sheet_name='EmployeeStats')
remarkable_feedbacks_df = pd.read_excel(file_path, sheet_name='RemarkableFeedbacks')
global_stats_df = pd.read_excel(file_path, sheet_name='GlobalStats')
best_employee_df = pd.read_excel(file_path, sheet_name='BestEmployee')

# Supprimer les espaces des noms de colonnes (problème courant dans Excel)
feedback_analysis_df.columns = feedback_analysis_df.columns.str.strip()
remarkable_feedbacks_df.columns = remarkable_feedbacks_df.columns.str.strip()
global_stats_df.columns = global_stats_df.columns.str.strip()
best_employee_df.columns = best_employee_df.columns.str.strip()

# Vérification des colonnes nécessaires
required_columns = {'ID', 'PositiveCount', 'NegativeCount'}
missing_columns = required_columns - set(feedback_analysis_df.columns)
if missing_columns:
    raise ValueError(f"Colonnes manquantes dans EmployeeStats: {missing_columns}")

# Créer un ordre de tri pour la colonne 'Relation'
relation_order = pd.CategoricalDtype(
    categories=['manager', 'superviseur', 'ami'],  # Ordre souhaité
    ordered=True
)

# Appliquer l'ordre de tri à la colonne 'Relation'
remarkable_feedbacks_df['Relation'] = remarkable_feedbacks_df['Relation'].astype(relation_order)

# Créer l'application Dash
app = dash.Dash(__name__)

# Définir la mise en page de l'application
app.layout = html.Div([
    # Affichage du meilleur employé et de son score en haut de la page
    html.Div([
        html.H2(f"🏆 Meilleur Employé: {best_employee_df['Best Employee ID'][0]}",
                style={'textAlign': 'center'}),
        html.H3(f"Score: {best_employee_df['Best Employee Score'][0]} 💯",
                style={'textAlign': 'center'}),
    ], style={'marginBottom': '40px'}),

    # Titre de l'application
    html.H1("Analyse des Feedbacks", style={'textAlign': 'center'}),

    # Sélecteur pour l'employé
    html.Label('Sélectionner un employé'),
    dcc.Dropdown(
        id='employee-dropdown',
        options=[{'label': f'Employé {i}', 'value': i} for i in feedback_analysis_df['ID'].unique()],
        value=None,  # Aucun employé sélectionné par défaut
        multi=False
    ),

    # Résultats pour un employé ou global
    html.Div(id='employee-stats', style={'marginTop': '20px'}),

    # Graphiques des critères
    html.Div([
        dcc.Graph(id='pie-chart'),
        dcc.Graph(id='bar-chart')
    ], style={'display': 'flex', 'justifyContent': 'space-around', 'marginTop': '40px'}),

    # Résumé global
    html.Div(id='global-stats', style={'marginTop': '40px', 'textAlign': 'center'}),

    # Avis remarquables
    html.Div(id='remarkable-feedbacks', style={'marginTop': '40px'})
])


# Callback pour mettre à jour les résultats en fonction de l'employé sélectionné
@app.callback(
    [Output('employee-stats', 'children'),
     Output('pie-chart', 'figure'),
     Output('bar-chart', 'figure'),
     Output('global-stats', 'children'),
     Output('remarkable-feedbacks', 'children')],
    [Input('employee-dropdown', 'value')]
)
def update_stats(selected_employee_id):
    # Si aucun employé n'est sélectionné, afficher le résumé global
    if selected_employee_id is None:
        total_positives = global_stats_df['Total Positives'].sum()
        total_negatives = global_stats_df['Total Negatives'].sum()
        total_feedbacks = remarkable_feedbacks_df.shape[0]

        global_stats = f"Critères positifs totaux : {total_positives}, Critères négatifs totaux : {total_negatives}, Nombre total de feedbacks : {total_feedbacks}"

        # Graphiques globaux
        pie_chart = go.Figure(data=[go.Pie(labels=["Positifs", "Négatifs"], values=[total_positives, total_negatives])])
        bar_chart = go.Figure(data=[go.Bar(x=["Positifs", "Négatifs"], y=[total_positives, total_negatives])])

        return None, pie_chart, bar_chart, global_stats, ""

    # Sélectionner les statistiques de l'employé
    employee_data = feedback_analysis_df[feedback_analysis_df['ID'] == selected_employee_id]

    if employee_data.empty:
        return html.P("Aucune donnée disponible pour cet employé."), go.Figure(), go.Figure(), "", ""

    employee_stats = employee_data.iloc[0]  # Récupérer la première ligne correspondante

    # Récupération des valeurs pour l'employé
    positive_count = employee_stats['PositiveCount']
    negative_count = employee_stats['NegativeCount']
    score = positive_count - negative_count

    employee_info = html.Div([
        html.H3(f"ID de l'employé : {selected_employee_id} 👤", style={'textAlign': 'center'}),
        html.P(f"Critères positifs : {positive_count} 👍"),
        html.P(f"Critères négatifs : {negative_count} 👎"),
        html.P(f"Score : {score} 💯"),
    ])

    # Graphiques pour l'employé sélectionné
    pie_chart = go.Figure(data=[go.Pie(labels=["Positifs", "Négatifs"], values=[positive_count, negative_count])])
    bar_chart = go.Figure(data=[go.Bar(x=["Positifs", "Négatifs"], y=[positive_count, negative_count])])

    # Affichage des 5 avis remarquables pour l'employé sélectionné
    if 'ID' in remarkable_feedbacks_df.columns:
        remarkable_feedbacks = remarkable_feedbacks_df[remarkable_feedbacks_df['ID'] == selected_employee_id]

        if not remarkable_feedbacks.empty:
            # Trier par 'Priority' (ascendant) et 'Relation' (manager > superviseur > ami)
            remarkable_feedbacks = remarkable_feedbacks.sort_values(by=['Priority', 'Relation'], ascending=[True, True])
            top_feedbacks = remarkable_feedbacks.head(5)

            remarkable_info = html.Div([
                html.H3(f"Avis remarquables pour l'employé {selected_employee_id} ✨", style={'textAlign': 'center'}),
                html.Div([
                    html.Div([
                        html.P([
                            html.Strong(f"{row['Relation'].capitalize()}:"),  # Texte en gras pour la relation
                            f" {row['Feedback']}"  # Texte normal pour le feedback
                        ], style={'fontSize': '16px', 'marginBottom': '10px'})
                    ], style={'backgroundColor': '#f0f8ff', 'padding': '10px', 'borderRadius': '8px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)'})
                    for index, row in top_feedbacks.iterrows()
                ])
            ], style={'padding': '20px', 'backgroundColor': '#f0f8ff', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)'})
        else:
            remarkable_info = html.P("Aucun avis remarquable pour cet employé.")
    else:
        remarkable_info = html.P("Données des avis remarquables non disponibles.")

    return employee_info, pie_chart, bar_chart, "", remarkable_info


if __name__ == '__main__':
    app.run_server(debug=True)