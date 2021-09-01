class Trabalhador:
    def __init__(self, nome) -> None:
        self.__nome = nome #atributo privado da classe
        self.__ferramenta = None
    
    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Computador:
    def __init__(self,sistema) -> None:  #
        self.__sistema = sistema          # Init já está fazendo a função de setter

    @property
    def sistema(self):
        return self.__sistema
    
    def usar(self):
        print(f'Este funcionário está trabalhando com o computador {self.__sistema}')

class Caneta:
    def __init__(self, marca) -> None:
        self.__marca = marca
    @property
    def marca(self):
        return self.__marca
    
    def usar(self):
        print(f'Este funcionário está trabalhando com a caneta {self.__marca}')
