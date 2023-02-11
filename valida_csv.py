import csv
import re

# Definir padrões de expressões regulares para cada campo
name_pattern = r'^[a-zA-Z]+(?: [a-zA-Z]+)*$'
number_pattern = r'^\d+(?:\.\d{1,2})?$'

# Ler o arquivo CSV
with open('arquivo.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')

    # Iterar sobre cada linha do arquivo
    for row in csvreader:
        # Validar o primeiro campo
        if not re.match(name_pattern, row[0]):
            print(row[0])
            print('O primeiro campo não é uma string válida')

        # Validar o segundo campo
        if not row[1].isdigit() or len(row[1]) != 4:
            print('O segundo campo não é um número de 4 dígitos')

        # Validar o terceiro campo
        if not re.match(number_pattern, row[2]):
            print('O terceiro campo não é um número com até 2 casas decimais')
