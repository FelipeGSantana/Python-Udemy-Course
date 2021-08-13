carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))


total = sum([float(x[1]) for x in carrinho]) # float colocado para caso tenha alguma string no lugar de float no valor
print(total)