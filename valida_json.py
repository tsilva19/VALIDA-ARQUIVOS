import json

# Defina sua string JSON
json_string = '{"nome": "João", "idade": 300000.00}'

try:
    # Tente carregar a string JSON
    json_object = json.loads(json_string)
    print("JSON válido")
except json.JSONDecodeError:
    # Se houver um erro, trate-o aqui
    print("JSON inválido")
