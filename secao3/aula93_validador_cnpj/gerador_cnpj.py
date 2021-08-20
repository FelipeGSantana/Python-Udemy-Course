import json
from json.decoder import JSONDecodeError
from random import randint



def digit_calc():
    numbers = [randint(0, 9) for _ in range(0, 9)]
    reverse_thousand = [0, 0, 1]
    numbers.extend(reverse_thousand)

    for _ in range(0, 2):
        # Seting numbers to multiply
        if len(numbers) == 12:
            lista_dígitos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        else:
            lista_dígitos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        # Finding digit
        produto = [num1*num2 for num1, num2 in zip(numbers, lista_dígitos)]
        digito = 11 - (sum(produto) % 11)

        # Verifying validity digit
        if digito > 9:
            digito = 0
        numbers.append(digito)

    return numbers # returning as list

# generate cnpjs
def multiple_generation(quantity):
    cnpj_dict = {}
    for _ in range(quantity):
        list_numbers = digit_calc()
        cnpj_str = [str(num) for num in list_numbers]
        new_cnpj = ''.join(cnpj_str)
        cnpj_dict[new_cnpj] = 'Valid'
    return cnpj_dict


# Save all generated cnpjs
def write_dict(dictionary):
    with open('json_data/cnpj_generated.json', 'r+') as file:
        # Verify existing data and update
        try:
            open_data = json.load(file)
            open_data.update(dictionary)
            file.seek(0)
        except JSONDecodeError:
            open_data = dictionary

        #Write update
        json.dump(open_data, file, indent=2)
        print('Salvo com sucesso!')

cnpjs = multiple_generation(100)
write_dict(cnpjs)


