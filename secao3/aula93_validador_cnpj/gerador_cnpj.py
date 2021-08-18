from random import randint

numbers = [randint(0,9) for i in range(0,9)]
reverse_thousand = [0,0,1]
numbers.extend(reverse_thousand)
print(numbers)
cnpj_final = []
for i in range(0, 2):

    # Seting numbers to multiply
    if len(numbers) == 12:
        lista_dígitos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    else:
        lista_dígitos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    # Fiding digit
    produto = [num1*num2 for num1, num2 in zip(numbers, lista_dígitos)]
    digito = 11 - (sum(produto) % 11)

    # Verifying validity digit
    if digito > 9:
        digito = 0
    numbers.append(digito)
print(numbers)