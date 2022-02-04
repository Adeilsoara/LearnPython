'''Classe Quadrado: Crie uma classe que modele um quadrado:

    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área; '''

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarValorLado(self, novoLado):
        self.lado = novoLado

    def retornarValorLado(self):
        print( self.lado)

    def calcularArea(self):
        area = self.lado**2
        print(area)
quadrado1 = Quadrado(3)
print(quadrado1.__dict__)
quadrado1.retornarValorLado()
quadrado1.calcularArea()

quadrado1.mudarValorLado(5)
print(quadrado1.__dict__)
quadrado1.retornarValorLado()
quadrado1.calcularArea()
