from classes import Trabalhador, Computador, Caneta

func1 = Trabalhador('Jhonathan')
func2 = Trabalhador('Feliphe')
print(func1.nome)
print(func2.nome)

caneta1 = Caneta('Bic')
print(caneta1.marca)

pc1 = Computador('Microsoft')
print(pc1.sistema)

# Fazendo relação de associação
func1.ferramenta = caneta1
func1.ferramenta.usar()

func2.ferramenta = pc1
func2.ferramenta.usar()