import datetime

class pessoa():
    def __init__(self, sexo, idade, altura, peso):
        self.sexo = sexo
        self.idade = idade
        self.altura = altura
        self.peso = peso
    def imc(self):
        return self.peso/(self.altura**2)
    def adn(self):
        year = datetime.date.today().year
        return year - self.idade

p = pessoa('M', 18, 1.76, 62.8)
print(p.imc())
print(p.adn())
