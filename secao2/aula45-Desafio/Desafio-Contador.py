"""
0 - 10
1 - 9
2 - 8
3 - 7
4 - 6
5 - 5
6 - 4
7 - 3
8 - 2
9 - 1
10 - 0
"""
# maneira simples
print('maneira simples:')
for i in range(0,11):
    print(i, 10-i)

# maneira com enumerate:

print('Maneira com enumerate')

for v1, v2 in enumerate(range(10,-1,-1)):
    print(v1,v2)