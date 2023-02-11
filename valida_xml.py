import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
# import re

# Carrega o arquivo XML
tree = ET.parse('arquivo.xml')
root = tree.getroot()

# Verifica se o XML é válido
# Aqui você pode adicionar suas próprias validações
# Para mais informações: https://docs.python.org/3/library/
# xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree

# for elem in root.iter():
#     tag = elem.tag
#     if re.search('[áéíóúâêîôûàèìòùäëïöü]', tag, re.IGNORECASE):
#         print(f" ================ A tag {tag} contém caracteres acentuados")


if not root:
    print("Arquivo XML inválido")
else:
    print("Arquivo XML válido")

# Formata o XML
xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
with open('arquivo_formatado.xml', 'w') as f:
    f.write(xml_str)
