# Meta Caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer Caracter (exceto quebra de linha)
# [] Conjunto de Caracteres
import re

text = '''Eu dolore nostrud amet laboris ad nisi commodo ea fugiat anim. Sint quis tempor non ullamco. 
    Nisi minim tempor laboris pariatur eu ex qui reprehenderit adipisicing ad labore officia ut. 
    Amet mollit qui nisi pariatur aliquip irure occaecat elit minim. Eu nostrud nostrud ad eu. 
    Esse Lorem proident pariatur dolore enim non labore quis dolore sit mollit esse et duis.'''

print(re.findall(r'ni.i|pariatur', text))
print(re.findall(r'[n\-N]isi|pariatur', text))
print(re.findall(r'nisi|pariatur', text, flags=re.IGNORECASE))
