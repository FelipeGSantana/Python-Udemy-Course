"""
append, insert, extend, pop, del, clear, min, max
"""

l1 = [1,2,3]
l2 = [4,5,6]
print(l1, l2)

# concatenando listas
l3 = l1 + l2
print(l3)

# extend tem a mesma funcção da concatenação
l1.extend(l2)
print(l1, l2, l3)

# append adiciona um item no final da lista
l2.append('b')
print(l2)

# Insere um item em determinado indice (não remove ou substitui nenhum outro)
l2.insert(0, 'banana')
print(l2)

# Remove o item da lista com a possibilidade de salvalo em uma váriavel
# Se o índice não for explícito é removido o ultimo item
pop1 = l2.pop(0)
print(pop1, l2)

# deleta o item especificado pelo indice
# se o índice não for explícito é removido o último item
del(l2[3])
print(l2)

# Retorna o maior ou menor valor
print(max(l2))
print(min(l2))
l5 = ['a','b','c','dado']
print(max(l5))
print(min(l5))

# preenche uma lista com valores no range
l4 = list(range(0,11))
print(l4)