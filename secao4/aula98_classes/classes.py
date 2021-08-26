"""
Classes são moldes de objetos que tem atributos, quando instanciado cada objeto gerado por esse molde leva esses atributos
Nome sempre com iniciado com maiúscula seguindo o PascalCase
"""
class Pessoa:
    variavel_global = "Exemplo de variável global"

    def __init__(self, nome, idade, comendo= False, falando=True): # Construtor
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando # variável da instância que pode ser usada em outras funções
        variavel_local = "Exemplo de variável local"

    def falar(self, assunto):
        if self.falando:
            print(f"{self.nome} já está falando")
            return
        if self.comendo:
            print(f"{self.nome} não pode falar de boca cheia!")
            return

        print(f"{self.nome} está falando sobre {assunto}")
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f"{self.nome} não está falando nada")
            return 
        print(f"{self.nome} parou de falar")
        self.falando = False

    
    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome} já está comendo")
            return
        if self.falando:
            print(f"{self.nome} está falando e não pode falar de boca cheia!")
            return

        print(f"{self.nome} está comendo {alimento}")
        self.comendo =True

    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo nada")
            return
        print(f"{self.nome} parou de comer")
        self.comendo =False
    