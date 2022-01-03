# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

#______________________________________________________________________________________________________


import dash
import dash_core_components as dcc      # Biblioteca de componentes
import dash_html_components as html     # Biblioteca de componentes para HTML
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

#______________________________________________________________________________________________________


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

#______________________________________________________________________________________________________

df = pd.DataFrame({
    "Frutas": ["Maçãs", "Laranjas", "Bananas", "Maçãs", "Laranjas", "Bananas"],
    "Quantidade": [4, 1, 2, 2, 4, 5],           # Na ordem de Frutas
    "Cidade": ["Porto Alegre", "Porto Alegre", "Porto Alegre", "Torres", "Torres", "Torres"]
})

fig = px.bar(df, x="Frutas", y="Quantidade", color="Cidade", barmode="group")

#______________________________________________________________________________________________________


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)