"""
OPERADOR TERNÁRIO
"""

user_logged = True
msg = 'Usuario logado' if user_logged else 'Faça seu loggin!'

print(msg)

age = 17

permiss = 'Permitido' if age >=18 else 'Não permitido!'
print(permiss)


a = False
b = False
c = False
d = False
e = 42
# irá tentar dar print nas variáveis, se não for false irá mostrar na tela
print(a or b or c or d or e)