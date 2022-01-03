
# http://127.0.0.1:8050/


# _________________________________________________________________________________

## Importações

import dash
import dash_core_components as dcc      # Biblioteca de componentes
import dash_html_components as html     # Biblioteca de componentes para HTML
import plotly.express as px
import pandas as pd
import requests                         # Envia requisições HTTP
import json

# _________________________________________________________________________________

## Código

app = dash.Dash(__name__)

df = pd.DataFrame({
    "Nomes": [ "Maria", "José", "Ana", "João", "Antonio", 
                "Francisco", "Carlos", "Paulo", "Pedro", "Lucas", 
                "Luiz", "Marcos", "Luis", "Gabriel", "Rafael", 
                "Francisca", "Daniel", "Marcelo", "Bruno", "Eduardo"],

    "Frequência": [ 11734129, 5754529, 3089858, 2984119, 2576348, 
                    1772197, 1489191, 1423262, 1219605, 1127310, 
                    1107792, 1106165, 935905, 932449, 821638, 
                    725642, 711338, 693215, 668217, 632664],           # Na ordem de Nomes

    "Sexo": [   "Feminino", "Masculino", "Feminino", "Masculino", "Masculino", 
                "Masculino", "Masculino", "Masculino", "Masculino", "Masculino", 
                "Masculino", "Masculino", "Masculino", "Masculino", "Masculino", 
                "Feminino", "Masculino", "Masculino", "Masculino", "Masculino"]
})

fig = px.bar(df, x="Nomes", y="Frequência", color="Sexo", barmode="group")

#______________________________________________________________________________________________________

## Layout

app.layout = html.Div(children=[                # Children relaciona o que tem dentro da Div do HTML. Neste caso, é uma lista em Python [ ]
    #html.H1(children='Dashboard'),              # Título do dashboard. H1 é título de texto. Pode ser substituído por Markdown

    dcc.Markdown('# Dashboard'),

    html.Div(children='''Relação da frequência de nomes próprios registrados no Brasil na década de 2010 a 2020'''),
    
    # dcc.Markdown('### Relação da quantidade de frutas por cidade'),       # Serve para a mesma função do código acima, porém fica em negrito.

    dcc.Graph(id='example-graph', figure=fig),

    dcc.Dropdown(id='dropdown', options=[
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





# _________________________________________________________________________________



nomes = requests.get("https://servicodados.ibge.gov.br/api/v2/censos/nomes")

nomes = nomes.json()

print(nomes)