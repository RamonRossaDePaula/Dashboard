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
    "Frutas": ["Maçãs", "Laranjas", "Bananas", "Uvas", "Maçãs", "Laranjas", "Bananas", "Uvas"],
    "Quantidade": [4, 1, 2, 5, 2, 4, 5, 1],           # Na ordem de Frutas
    "Cidade": ["Porto Alegre", "Porto Alegre", "Porto Alegre", "Porto Alegre", "Torres", "Torres", "Torres", "Torres"]
})

fig = px.bar(df, x="Frutas", y="Quantidade", color="Cidade", barmode="group")

#______________________________________________________________________________________________________


app.layout = html.Div(children=[                # Children relaciona o que tem dentro da Div do HTML. Neste caso, é uma lista em Python [ ]
    #html.H1(children='Dashboard'),              # Título do dashboard. H1 é título de texto. Pode ser substituído por Markdown

    dcc.Markdown('# Dashboard'),

    html.Div(children='''Relação da quantidade de frutas por cidade'''),
    
    # dcc.Markdown('### Relação da quantidade de frutas por cidade'),       # Serve para a mesma função do código acima, porém fica em negrito.

    dcc.Graph(id='example-graph', figure=fig),

    dcc.Dropdown(id='dropdown',
        options=[
            {'label': 'Porto Alegre', 'value': 'POA'},
            {'label': 'Torres', 'value': 'TRS'},
        ],
        value='POA'
    ),
    html.Div(id='dd-output-container')
])



#______________________________________________________________________________________________________


if __name__ == '__main__':
    app.run_server(debug=True)