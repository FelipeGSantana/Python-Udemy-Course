# Faça uma função1 executar duas funções que recebam um número diferente de argumentos

def multiplicar(*args):
    valores = args
    produto = 1
    for numero in valores:
        produto *= numero
    return produto

def soma(*args):
    valores = args
    soma = 0
    for numero in valores:
        soma += numero
    return soma

def func1():
    valores = []
    while True:
        valor = input('Digite valores para somar e multiplicar (digite uma letra para sair): ')
        try:
            valores.append(int(valor))
        except:
            print('Você decidiu sair')
            break

    print('A soma de ',end='')
    print( *valores, sep=' + ', end='')
    print(' =', soma(*valores))
    print('A multiplicação de ',end='')
    print(*valores, sep=' * ', end='')
    print(' =', multiplicar(*valores))

func1()
print('Método 2')


def mestre(func, *args):
    return func(*args)


def fala_oi(nome):
    return print('oi', nome)

def saudacao(saudacao, nome):
    return print(saudacao, nome)

mestre(fala_oi, 'joão')
mestre(saudacao,'olá','Pedro')

