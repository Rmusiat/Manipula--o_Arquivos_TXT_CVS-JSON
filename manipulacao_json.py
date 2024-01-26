# JSON - Javasript Object Notation
# Ele é estruturado por chaves e valores (Dicionário)

# JSON é usado para troca de informações entre sistemas, backends
# É o formato utilizado pelas APIs
# Graphql as APIs REST

# Capturar uma informação da Internet

import urllib.request
import json

url = 'http://api.open-notify.org/astros.json'

# Capturar essas informações em dados JSON

pega_json = urllib.request.urlopen(url).read().decode()

# Converter esses valores em dicionarios para manipulação

dic_json = json.loads(pega_json)

# Iterar os valores do dicinario

for c in dic_json.values():
    print(c)

print(dic_json)

for p in dic_json['people']:
    print(p['name'])

# Cria um arquivo JSON com os valores extraidos

with open('Arquivos/nomes.json','w+') as f:
    json.dump(dic_json,f,indent=4)
