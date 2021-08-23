from classes import Pessoa

p1 = Pessoa('Luiz', 37, comendo=False, falando=False)

p1.comer('Banana')
p1.parar_comer()

p1.falar('Mídia social favorita')
p1.parar_falar()

p1.parar_comer()
p1.parar_falar()

p1.comer('Cana')
p1.falar('Assoviar')

p1.parar_comer()

p1.falar('Assoviar')
p1.comer('Cana')