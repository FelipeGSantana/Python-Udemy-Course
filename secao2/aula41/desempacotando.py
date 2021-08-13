
lista = ['a','b','c',1,2,3,4,5,6,7,8,9,100]

# *outrosvalores para criar uma lista com varios valores desempacotados
a, b, c, *outrovalores, ultimovalor = lista
print(a,b,c,outrovalores,ultimovalor)

# *_ para indicar a outros desenvolvedores que os outros valores desempacotados não serão usados
a,b,c, *_ = lista

# trocar variaveis:

x = 10
y = 'a'
z = True
print('Valores originais:')
print('x = {}, y = {}, z = {}'.format(x,y,z))

x,y,z = z, x, y

print('Valores alterados:')
print('x = {}, y = {}, z = {}'.format(x,y,z))