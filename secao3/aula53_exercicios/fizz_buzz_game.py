# def game(valor):
#     if valor % 2 == 0:
#         return 'Fizz'
#     elif valor % 5 == 0:
#         if valor % 3 == 0:
#             return 'FizzBuzz'
#         else:
#             return 'Buzz'
#     return valor

def game(valor):
    if valor % 3 == 0 and valor % 5 == 0:
        return 'FizzBuzz'
    if valor % 3 == 0:
        return 'Fizz'
    if valor % 5 == 0:
        return 'Buzz'
    return valor

while True:
    num = int(input('Digite um valor: '))
    print(game(num))