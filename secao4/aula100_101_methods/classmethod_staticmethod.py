from random import randint


class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    #Se refere a instância por isso usa-se o self
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # Retorna a classe novamente tratando ou modificando a entrada antes da construção do objeto
    # No caso o input foi o ano de nascimento, descobrimos a idade e construímos o objeto com esse parametro
    # Se refere à classe em geral por isso usa-se o cls
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    # Como uma função comum só que dentro da classe, não usa nem self nem cls
    @staticmethod
    def gera_id():
        rand = randint(1000, 9999)
        return rand


p1 = Pessoa('luiz', 23)  # Objeto criado normalmente
print(p1.nome, p1.idade)

# Agora o objeto foi RECRIADO só que agora pelo ano de nascimento
p1.get_ano_nascimento()

p2 = Pessoa.por_ano_nascimento('Fernando', 1998)
print(p2.nome, p2.idade)

print(Pessoa.gera_id()) #Pode ser acessado normalmente só usando a classe
print(p2.gera_id()) #Também pode ser acessado usando uma instancia
