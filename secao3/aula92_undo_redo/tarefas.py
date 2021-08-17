"""
Faça uma lsita de tarefas com as seguintes opções:
    Adicionar tarefas
    Listar tarefas
    Desfazer tarefas (a cada vez que chamarmos, desfaz a última ação)
    Refazer tarefas (a cada vez que chamarmos, refaz a última ação)
"""

from itertools import count

lista_atual = ['mercado', 'roupas', 'comida']
lista_desfeito = []


def adicionar():
    tarefa = input("Digite a tarefa a ser realizada:")
    lista_atual.append(tarefa)
    print('Tarefa adicionada com sucesso!\n')


def listar():
    if not lista_atual:
        print("Não há nenhuma tarefa para mostrar\n")
    else:
        contador = count()
        lista_index = zip(contador, lista_atual)

        for item in lista_index:
            print('[', item[0], ']', item[1])
        print('\n')


def desfazer():
    if not lista_atual:
        print("não há nada para ser desfeito\n")
    else:
        lista_desfeito.append(lista_atual.pop())
        print('Ação desfeita\n')


def refazer():
    if not lista_desfeito:
        print("não há o que refazer\n")
    else:
        lista_atual.append(lista_desfeito.pop())
        print("Ação refeita\n")


while True:
    print("ESCOLHA UMA OPÇÃO")
    print("[1]Adicionar tarefa\n[2]Listar tarefas\n[3]Desfazer última ação\n[4]Refazer última ação")
    escolha = input()
    if escolha == "1":
        adicionar()
    elif escolha == "2":
        listar()
    elif escolha == "3":
        desfazer()
    elif escolha == "4":
        refazer()