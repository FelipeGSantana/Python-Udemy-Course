"""
0 4 2 5 2 0 1 1 / 0 0 0 1 - 10
04252011000110
5 4 3 2 9 8 7 6   5 4 3 2
6 5 4 3 2 9 8 7   6 5 4 3   2
primeiro dígito 11 - (somadosprodutos % 11)

"""



produto = []

cnpj_input = input('Digite o CNPJ sem pontuação: \n')
CNPJ = [int(num) for num in cnpj_input]
cnpj_temporario = CNPJ[0:-2]


def calcula(cnpj_temporario):
    if len(cnpj_temporario) == 12:
        lista_digitos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    else:
        lista_digitos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    
    produto = [num1 * num2 for num1, num2 in zip(cnpj_temporario, lista_digitos)]
    digito = 11 - (sum(produto) % 11)

    if digito > 9:
        digito = 0
    cnpj_temporario.append(digito)

calcula(cnpj_temporario)
calcula(cnpj_temporario)

print(CNPJ)
print(cnpj_temporario)

if CNPJ == cnpj_temporario:
    print('VÁLIDO')
else:
    print('INVÁLIDO')
