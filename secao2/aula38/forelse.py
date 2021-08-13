list = ['aJoão','Luíz Otavio', 'Maria', 'Judith']



for nome in list:
    print(nome)
    if nome.lower().startswith('j'):
        break
# O else só é executado quando o laço for iterado até o final
# se a qualquer momento o laço for quebrado o else não será executado
#***Aparentemente esta versão 3.8.9 não tem este recurso
else:
    print('nenhum nome começa com j')
