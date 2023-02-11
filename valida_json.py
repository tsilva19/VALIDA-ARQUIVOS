import json
import re

# Carregue o arquivo JSON
with open('arquivo.json', encoding='utf-8') as f:
    json_object = json.load(f)

# Compile a expressão regular para encontrar caracteres acentuados
acentos = re.compile(r'[áàãâéêíóôõúüç]', re.IGNORECASE)


# Percorra todos os campos do objeto JSON e verifique se há caracteres
# acentuados
for key in json_object:
    if acentos.search(key) is not None:
        print(f'O campo "{key}" contém caracteres acentuados')
