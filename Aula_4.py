# Meta Caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer Caracter (exceto quebra de linha)
# [] Conjunto de Caracteres
# * 0 ou n vezes
# + 1 ou n vezes
# ? 0 ou 1 vezes
# {} {min, max}}
import re

text = '''<p>Texto 1</p><p>Texto 2</p><p>Texto 3</p><div>Texto 4</div>'''

print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>',text))