from udemy.secao3.dados import lista, produtos, pessoas

nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))

produtos_maior = filter(lambda p: p['preco'] > 30, produtos)
for produto in produtos_maior:
    print(produto)
print("")

pessoa_menor = filter(lambda p: p['idade'] < 18, pessoas)
for pessoa in pessoa_menor:
    print(pessoa)
