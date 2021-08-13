from random import randint

for lis in range(0,13):
    lista = []
    for item in range(0,10):
        num = randint(1,10)
        lista.insert(-1, num)
    print(lista)