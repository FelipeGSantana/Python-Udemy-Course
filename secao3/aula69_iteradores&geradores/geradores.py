import sys
import time
"""
Uma função geradora vai gerar um objeto iterável e rotarna um elemento por vez deste iterável pode ser feita usando
a palavar chave "yield" que irá retornar a função sem destruir a mesma, e quando for chamada novamente a função irá
iniciar do último yeld.
"""

def gera():
    for n in range(100):
        yield n             # Retorna um valor a cara for
        time.sleep(0.01)

g = gera()

for v in g:
    print(v)

"""
Geradores só podem consumir suas "variáveis" apenas uma vez, caso não haja mais nada para ser consumido ele irá gerar
uma excessão, caso estiver dentro de um for apenas não irá fazer nada.
"""
print("outro for")
for v in g:
    print(v)

"""
Neste caso a função irá retornar uma resposta de cada vez.
"""

# def gera():
#     p1 = input('pergunta1:')
#     yield p1
#     p2 = input('pergunta2:')
#     yield p2
#     p3 = input('pergunta3:')
#     yield p3
# g = gera()
# print(next(g))
# print(next(g))
# print(next(g))

"""
O interessante de geradores é que ele só irá armazenar na memória o valor quando for solicitado, diferente das
listas que já armazena os valores na memória assim que é criada. Podemos criar um gerador só usando os parênteses
veja o exemplo abaixo:
"""

l1 = [x for x in range(10)] # Gerando uma lista comum com list comprehension
print(type(l1),sys.getsizeof(l1))

l2 = (x for x in range(10)) # Criando um gerador (só utilizar os parênteses)
print(type(l2),sys.getsizeof(l2))

for v in l2:
    print(v)
