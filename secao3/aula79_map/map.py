from Udemy.secao3.dados import produtos, pessoas

# só retortana o preço dos produtos
novos_produtos = map(lambda p: p['preco'] * 1.05, produtos)

for produto in novos_produtos:
    print(produto)


# retorna o dicionario estruturado com preços alterados

def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.5, 2)
    return p


novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)

print("")


# adicionar item no dicionario

def menor(pessoa):
    if pessoa['idade'] < 18:
        pessoa['menor'] = True
    return pessoa


pessoa_menor = map(menor, pessoas)

for pessoa in pessoa_menor:
    print(pessoa)
