# Meta Caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer Caracter (exceto quebra de linha)
# [] Conjunto de Caracteres
# * 0 ou n vezes
# + 1 ou n vezes
# ? 0 ou 1 vezes
# {} {min, max}
# ( ) \1 Grupo e Retrovisor
# ( ) ( ) \1 \2
# ^ Começa com
# $ Termina com
# [^a-z] Negação

import re

cpf = '123.456.789-01'
print(re.findall(r'^[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}$', cpf))
print(re.findall(r'[^0-9]+', cpf))
