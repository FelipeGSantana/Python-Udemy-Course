import json

with open('abc.txt', 'w+') as file:
    file.write('linha1\n')
    file.write('linha2\n')
    file.write('linha3\n')
    file.write('linha4\n')
    file.seek(0)
    print(file.read())

# w escreve o arquivo apagando tudo o que tinha dentro
# r lê o arquivo
# a ecreve dados no arquivo sem apagar o que já foi escrito
# + irá adicionar função de leitura ou gravação
# .seek(0) retorna o cursor no inicio do arquivo
# os.remove('abc.txt') apaga o arquivo

d1 = {
    'funcionario1': {
        'nome': 'Luiz Pereira',
        'idade': '35',
        'profissão': 'agricultor'
    },
    'funcionario2': {
        'nome': 'Maria José',
        'idade': '42',
        'profissão': 'Engenheira Agronoma'
    }
}

d1_json = json.dumps(d1, indent = True, ensure_ascii=False)  # converte um dicionário em um padrão Json

with open('funcionarios.json', 'w+', encoding='utf8') as file:
    file.write(d1_json)

with open('funcionarios.json', 'r') as file:
    d2_json = file.read()
    d2_json = json.loads(d2_json) # converte de json para dicionario
    print(d2_json)
