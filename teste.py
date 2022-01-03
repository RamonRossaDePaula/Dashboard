
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


nomes2 = requests.get("https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/?decada=2000")

nomes2 = nomes2.json()

print("Importação de dados 2: ")
print(nomes2)

type.nomes2
