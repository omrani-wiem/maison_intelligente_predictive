import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import random
import pickle

pieces = ['Salon', 'Chambre', 'Cuisine']

# Charger le modèle ML
with open("ml_model.pkl", "rb") as f:
    model = pickle.load(f)

# Initialiser Dash
app = dash.Dash(__name__)

# Générer une lecture aléatoire pour toutes les pièces
def nouvelle_lecture():
    lectures = []
    for piece in pieces:
        temp = random.randint(15, 30)
        light = random.randint(0, 100)
        motion = random.randint(0, 1)
        action = model.predict([[temp, light, motion]])[0]
        lectures.append({"Piece": piece, "Temp": temp, "Light": light, "Motion": motion, "Action": action})
    return lectures

# Layout avec style amélioré
app.layout = html.Div([
    html.H1("🏠 Maison intelligente prédictive", style={'text-align':'center', 'color':'#2C3E50'}),
    html.Button("Nouvelle lecture", id="bouton", n_clicks=0,
                style={'margin':'20px','padding':'10px 20px','font-size':'16px','background-color':'#2980B9','color':'white','border':'none','border-radius':'5px','cursor':'pointer'}),
    html.Div(id="lectures_div", style={'display':'flex','justify-content':'center'})
])

# Callback pour afficher les lectures avec style
@app.callback(
    Output("lectures_div", "children"),
    Input("bouton", "n_clicks")
)
def update(n_clicks):
    data = nouvelle_lecture()
    children = []
    for d in data:
        status = "Chauffage Allumé 🔥" if d["Action"] == 1 else "Chauffage Éteint ❄️"
        color = "#E74C3C" if d["Action"] == 1 else "#27AE60"
        card_style = {
            'border':'2px solid #34495E',
            'border-radius':'10px',
            'padding':'20px',
            'margin':'10px',
            'width':'250px',
            'background-color':'#ECF0F1',
            'box-shadow':'2px 2px 10px rgba(0,0,0,0.2)',
            'text-align':'center'
        }
        children.append(html.Div([
            html.H2(f"{d['Piece']}", style={'color':'#2C3E50'}),
            html.P(f"Température : {d['Temp']}°C", style={'font-size':'16px'}),
            html.P(f"Lumière : {d['Light']}%", style={'font-size':'16px'}),
            html.P(f"Mouvement : {d['Motion']}", style={'font-size':'16px'}),
            html.P(status, style={'color': color, 'font-weight':'bold','font-size':'18px'})
        ], style=card_style))
    return children

if __name__ == "__main__":
    app.run(debug=True)

