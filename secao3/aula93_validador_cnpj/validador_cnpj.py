"""
0 4 2 5 2 0 1 1 / 0 0 0 1 - 10
5 4 3 2 9 8 7 6   5 4 3 2
6 5 4 3 2 9 8 7   6 5 4 3   2
primeiro dígito 11 - (somadosprodutos % 11)

"""

cnpj = [0, 4, 2, 5, 2, 0, 1, 1, 0, 0, 0, 1, 1, 0]
cnpj_temporario = cnpj[0:-2]
lista_primeiro_digito = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
lista_segundo_digito = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
produto = []

for num1, num2 in zip(cnpj_temporario, lista_primeiro_digito):
    produto.append(num1 * num2)
digito1 = 11 - (sum(produto) % 11)
if digito1 > 9:
    digito1 = 0

cnpj_temporario.append(digito1)

for num1, num2 in zip(cnpj_temporario, lista_segundo_digito):
    produto.append(num1 * num2)
digito2 = 11 - (sum(produto) % 11)
if digito2 > 9:
    digito2 = 0

cnpj_temporario.append(digito2)
print(cnpj)
print(cnpj_temporario)
if cnpj == cnpj_temporario:
    print('VÁLIDO')
else:
    print('INVÁLIDO')
