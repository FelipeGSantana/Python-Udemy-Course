"""
Python não tem encapsulamento convencional porém se usa as seguintes convenções:
_atributo: recomenda-se não acessar este atributo fora de sua classe
__atributo: recomenda-se FORTEMENTE não acessar este atributo fora de sua classe

_atributo: acessa usando instancia._atributo
__atributo: acessa usando instancia._Classe__atributo
usando o '__atributo' se qualquer um tentar atribuir novos valores a essa atributo,
o python irá criar um novo atributo com esse nome para proteger o que já temos na classe.
"""
class BaseDeDados:
    def __init__(self) -> None:
        self.__dados = {}
    
    @property
    def dados(self):
        return self.__dados
    
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listar_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id,nome)

    def apagar_cliente(self, id):
        del self.__dados['clientes'][id]



bd = BaseDeDados()
bd.inserir_cliente(1, 'joão')
bd.inserir_cliente(2, 'Paulo')
bd.inserir_cliente(3, 'Maria')
bd.inserir_cliente(4, 'Julia')

bd.listar_clientes()
bd.apagar_cliente(2)
print()
bd.listar_clientes()

bd.__dados = 'outros dados' # Tentando sobreescrever o atributo dados na classe
print(bd.__dados, hex(id(bd.__dados))) # foi criado um novo atributo com mesmo nome (compare endereço de memoria)

print(bd._BaseDeDados__dados, hex(id(bd._BaseDeDados__dados))) # Acessando atributo original por fora da classe
print(bd.dados, hex(id(bd.dados))) # Lendo valores do atributo original (verifique como o endereço de memória é idêntico ao atributo original)

