from json.decoder import JSONDecodeError
from random import randint
from json import dumps, loads


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

        # Fiding digit
        produto = [num1*num2 for num1, num2 in zip(numbers, lista_dígitos)]
        digito = 11 - (sum(produto) % 11)

        # Verifying validity digit
        if digito > 9:
            digito = 0
        numbers.append(digito)

    return numbers # returning as list


def multiple_generation(quantity):
    cnpj_dict = {}
    for _ in range(quantity):
        list_numbers = digit_calc()
        cnpj_str = [str(num) for num in list_numbers]
        CNPJ = ''.join(cnpj_str)
        cnpj_dict[CNPJ] = 'Valid'
    return cnpj_dict

def write_dict(dict):
    # dict_json = dumps(dict, indent = True, ensure_ascii=False)
    with open('cnpj_generated.json', 'w+', encoding='utf8') as file:
        existing_data = file.read() #reading
        
        try:
            existing_data = loads(existing_data) #converting to dict
            updated = existing_data.update(dict) #adding dict
            new_data = dumps(updated, indent = True, ensure_ascii=False)
        except JSONDecodeError:
            new_data = dumps(dict, indent = True, ensure_ascii=False)

        file.write(new_data)
        

cnpjs = multiple_generation(10)
write_dict(cnpjs)


