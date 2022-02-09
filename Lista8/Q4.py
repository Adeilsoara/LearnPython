'''Classe Pessoa: Crie uma classe que modele uma pessoa:

    Atributos: nome, idade, peso e altura
    Métodos: Envelhercer, engordar, emagrecer, crescer.
    Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.'''

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        return self.idade

    def engordar(self, quilos):
        self.peso += quilos
        return self.peso
    def emagrecer(self,quilos_perdidos):
        self.peso -= quilos_perdidos
        return self.peso
    def crescer(self, anos):
        if self.idade < 21:
           self.altura += (0.05)*anos
        return self.altura
Adeilson = Pessoa('Adeilson', 18, 64, 1.75)
print(Adeilson.__dict__)
print(f'Seu nome é: {Adeilson.nome}, você tem {Adeilson.idade} anos, pesa {Adeilson.peso} kg e tem de altura {Adeilson.altura} m ')


Adeilson.envelhecer(1)
Adeilson.crescer(1)
