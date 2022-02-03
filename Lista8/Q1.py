'''Classe Bola: Crie uma classe que modele uma bola:

    Atributos: Cor, circunferência, material
    Métodos: trocaCor e mostraCor'''

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocarCor(self, cor):
        self.cor = cor
    def mostrarCor(self):
        print(f'A cor da Bola é: {self.cor}')

bola = Bola("verde", 2, "couro")
bola.mostrarCor()


