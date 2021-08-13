# Crie uma função1 que receba uma função2 como parametro e retorne o valorda função2 executada

def funcao2():
    return print('a função2 foi executada')
def func1(funcao2):
    return funcao2()

func1(funcao2)
