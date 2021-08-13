texto = '01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'

lista = list(texto)
[lista.insert(a, '.') for a in range(10, len(lista), 11)]
texto_final = ''.join(lista)

print(texto)
print(texto_final)


n = 10
lista2 = []
lista2 = [texto[i:i + n] for i in range(0,len(texto),n)]
texto_final2 = '.'.join(lista2)
print(texto_final2)






