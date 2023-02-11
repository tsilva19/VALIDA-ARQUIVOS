import xml.etree.ElementTree as ET
import re

# Carrega o arquivo XML
tree = ET.parse('arquivo.xml')
root = tree.getroot()

# Verifica se as tags possuem caracteres acentuados
for elem in root.iter():
    tag = elem.tag
    verdade = re.search('[áéíóúâêîôûàèìòùäëïöü]', tag, re.IGNORECASE)
    if verdade:
        print(f"A tag {tag} contém caracteres acentuados")
if verdade is None:
    print("ARQUIVO XML VALIDADO")
