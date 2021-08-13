"""
-> É uma lista de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 e 10 e eles podem ser duplicados

EXERCÍCIO:

-> Crie uma função que encontra uma duplicação, considerando o segundo número como a duplicação.
    Retorne a duplicação considerada.
    Requisitos: a ordem do número duplicado é considerada apartir da segunda ocorrência do número,
    ou seja, o número duplicado em si. Caso não encontrar duplicados, retorne -1.
    Exemplo:
        [1,2,3,3,2,1] -> retorna 3
        [1,2,3,4,5,6] -> retorna -1

lista = [
    [6, 5, 1, 4, 3, 4, 6, 10, 2, 10], # 4
    [10, 9, 7, 3, 7, 8, 9, 1, 4, 10], # 7
    [9, 6, 1, 1, 9, 10, 10, 8, 1, 6], # 1
    [9, 9, 1, 3, 6, 4, 3, 3, 10, 6],  # 9
    [3, 3, 2, 1, 6, 5, 7, 1, 7, 8],   # 3
    [9, 3, 7, 8, 3, 8, 2, 5, 2, 8],   # 3
    [9, 7, 3, 8, 2, 10, 8, 3, 3, 6],  # 8
    [9, 5, 8, 10, 2, 5, 8, 7, 7, 1],  # 5
    [4, 5, 1, 5, 4, 8, 7, 9, 1, 6],   # 5
    [8, 1, 6, 1, 9, 7, 3, 2, 2, 7],   # 1
    [10, 6, 5, 10, 4, 6, 8, 8, 9, 4], # 10
    [1, 7, 7, 5, 1, 2, 1, 9, 2, 8],   # 7
    [1, 3, 4, 10, 6, 3, 9, 10, 9, 1],  # 3
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   # -1
]
"""

lista =[
    [6, 5, 1, 4, 3, 4, 6, 10, 2, 10],
    [10, 9, 7, 3, 7, 8, 9, 1, 4, 10],
    [9, 6, 1, 1, 9, 10, 10, 8, 1, 6],
    [9, 9, 1, 3, 6, 4, 3, 3, 10, 6],
    [3, 3, 2, 1, 6, 5, 7, 1, 7, 8],
    [9, 3, 7, 8, 3, 8, 2, 5, 2, 8],
    [9, 7, 3, 8, 2, 10, 8, 3, 3, 6],
    [9, 5, 8, 10, 2, 5, 8, 7, 7, 1],
    [4, 5, 1, 5, 4, 8, 7, 9, 1, 6],
    [8, 1, 6, 1, 9, 7, 3, 2, 2, 7],
    [10, 6, 5, 10, 4, 6, 8, 8, 9, 4],
    [1, 7, 7, 5, 1, 2, 1, 9, 2, 8],
    [1, 3, 4, 10, 6, 3, 9, 10, 9, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
]

def find_duplicates(sublist):
    alist = []
    for n in sublist:
        if n in alist:
            return n
        alist.append(n)
    return -1

for sublist in lista:
    duplicated = find_duplicates(sublist)
    print(sublist,'duplicado: ', duplicated)
