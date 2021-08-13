"""
CPF: 237.680.459-00

2 * 10
3 * 9
7 * 8
6 * 7
8 * 6
0 * 5
4 * 4
5 * 3
9 * 2
SOMA

11 - (SOMA % 11) = VALOR

SE VALOR > 9 ENTÃO DIGITO = 0

"""

from random import randint

while True:

    cpf = ''
    opcao = 0
    while 1 > opcao < 2:
        print('Digite a opção desejada:')
        print('[1] Gerar CPF')
        print('[2] Validar CPF')
        opcao = int(input())


    if opcao == 2:
        while True:
            cpf = input('Digite um CPF sem pontuação')
            if len(cpf) == 11:
                break
            else:
                print('Digite um CPF com 11 dígitos')
    else:
        cpf = str(randint(100000000,999999999))

    def calc_digito(cpf):
        soma = 0
        for indice, multiplicador in enumerate(range(len(cpf)+1,1,-1)):
            soma += int(cpf[indice]) * multiplicador
        digito = 11 - (soma % 11)
        if digito > 9:
            digito = 0

        return digito

    cpf_temporario = cpf[:9] + str(calc_digito(cpf[:9]))

    cpf_temporario += str(calc_digito(cpf_temporario))


    if cpf_temporario == cpf and cpf != cpf[0] * 11:
        print('CPF válido')
    else:
        print('CPF inválido')

    print('CPF temporário:', cpf_temporario)
    print('CPF original:', cpf)
