def mult(x,y):
    return x * y

print(mult(2,2))

a = lambda x, y: x * y # a se torna uma função
print(a(2,2)) # retorna o mesmo que a função mult

lista = [
    ['P1', 10],
    ['P2', 7],
    ['P3', 2],
    ['P4', 21],
    ['P5', 19],
    ['P6', 18],
]
#função que ira percorrer a lista e encontrar o item[1] de cada sublista
def func(item):

    return item[1]
print('Lista original: ', lista)
lista.sort(key=func) #Organiza a lista por preço crescente usando a func prara auxiliar
print('Lista organizada por preço crescente: ', lista)

lista.sort(key= lambda item: item[0]) #Organiza a lista por nome do item
print('Lista organizada por nome: ', lista)

#Organiza a lista por preçço decrescente
print('Lista orgranizada por preço decrescente: ', sorted(lista, key= lambda i: i[1], reverse = True))

