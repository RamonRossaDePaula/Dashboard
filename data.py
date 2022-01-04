
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

## Importação de dados 1

nomes1 = requests.get("https://servicodados.ibge.gov.br/api/v2/censos/nomes")

nomes1 = nomes1.json()

print("Importação de dados 1: ")
print(nomes1)


## Código

app = dash.Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

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

## Layout 1

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[                # Children relaciona o que tem dentro da Div do HTML. Neste caso, é uma lista em Python [ ]
    html.H1(
        children='Dashboard',
        style={
            'textAlign': 'center',
            'color': colors['text']             # Título do dashboard. H1 é título de texto. Pode ser substituído por Markdown: "dcc.Markdown('# Dashboard'),"
        }
    ),

    
    html.Div(children='''Relação da frequência de nomes próprios registrados no Brasil na década de 2010 a 2020''', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    
    # dcc.Markdown('### Relação da quantidade de frutas por cidade'),       # Serve para a mesma função do código acima, porém fica em negrito.

    dcc.Graph(id='example-graph', figure=fig)
])

#______________________________________________________________________________________________________

"""
## Importação de dados 2

nomes2 = requests.get("https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/?decada=2000")

nomes2 = nomes2.json()

print("Importação de dados 2: ")
print(nomes2)                       # É uma lista
"""






if __name__ == '__main__':
    app.run_server(debug=True)





# _________________________________________________________________________________



