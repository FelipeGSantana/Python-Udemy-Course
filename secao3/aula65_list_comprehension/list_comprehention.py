l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ex1 = [variavel for variavel in l1]

ex2 = [variavel * 2 for variavel in l1]

ex3 = [(v1, v2) for v1 in l1 for v2 in range(3)]

# a linha acima tem a mesma função da iteração abaixo

ex3_1 = []
for v1 in l1:
    for v2 in range(3):
        ex3_1.append((v1,v2))

l2 = ['Luiz', 'Maria', 'Maurilho']

ex4 = [l.find('i') for l in l2]
print(ex4)


