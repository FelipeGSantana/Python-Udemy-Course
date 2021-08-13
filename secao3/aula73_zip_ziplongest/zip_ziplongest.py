"""
Zip - Função de unir iteráveis
Ziplongest - Une sequindo a quantidade do maior iterável
"""
from itertools import zip_longest, count

cidades = ['Belo Horizonte', 'São Paulo', 'Salvador', 'Rio Branco', 'outra_cidade']
estados = ['MG', 'SP', 'Ba', 'AC']
indice = count()

cidades_estados = zip(indice, cidades, estados)



for indice, cidade, estado in cidades_estados:

    print('[{}] {}-{}'.format(indice,cidade,estado))

cidades_estados2 = zip_longest(cidades, estados)
print(list(cidades_estados2))

# EXERCÍCIO

lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [1, 2, 3, 4]


lista_res = [x + y for x, y in zip(lista1, lista2)]

print(lista1)
print(lista2)
print(lista_res)
