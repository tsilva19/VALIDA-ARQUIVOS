import json
import re


# Carregue o arquivo JSON
with open('arquivo.json', encoding='utf-8') as f:
    json_object = json.load(f)

# Compile a expressão regular para verificar se um valor está no formato
# "00000.00"
regex = re.compile(r'^\d{5}\.\d{2}$')

# Percorra todos os campos do objeto JSON e verifique se o valor está no
# formato desejado
for key in json_object:
    if isinstance(json_object[key], str):
        if not regex.match(json_object[key]):
            print(f'O campo "{key}" não está no formato "00000.00"')
