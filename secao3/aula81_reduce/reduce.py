from udemy.secao3.dados import produtos, pessoas, lista
from functools import reduce

# reduce acumula valores do mesmo jeito que um contator: "contador +=1"
soma_preco = reduce(lambda soma, p: p['preco'] + soma, produtos,0)
media = soma_preco/len(produtos)
print(media)
print(soma_preco)