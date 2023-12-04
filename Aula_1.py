import re

text = 'Deserunt exercitation cillum amet consequat id veniam consequat quis veniam sint quis.'

#Procura no texto
print(re.search(r'cillum', text))
#Mostra todas as ocorrências
print(re.findall(r'consequat', text))
#Substitui a primeira ocorrência
print(re.sub(r'consequat', 'optum', text))
#Count indica quantas ocorrências alterar
print(re.sub(r'quis', 'lessum', text, count=1))

#Evita compilação da mesma expressão
reg = re.compile(r'consequat')
reg.search()
