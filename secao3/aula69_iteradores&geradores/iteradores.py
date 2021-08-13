"""
Iteráveis são objetos iteraveis, ou seja, conseguimos passar por cada um de seus elementos usando um ITERADOR
por exemplo uma lista é um objeto iterável, mas não é um iterador, porém, podemos transformala em um iretador se usarmos
a função iter() junto da função next() para iterar
"""

lista = [0, 1, 2, 3] # essa lista é iterável porém não é um iterador

# aqui transformamos a lista em iterador
lista = iter(lista)

# aqui percorremos os itens da lista
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))