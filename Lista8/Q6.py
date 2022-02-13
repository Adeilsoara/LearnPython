'''
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz
de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o
 nível do volume permanecem dentro de faixas válidas.
'''

class Televisao:
    def __init__(self, numeroCanal, aumentarVolume, diminuirVolume):
        self.numeroCanal = numeroCanal
        self.aumentarVolume = aumentarVolume
        self.diminuirVolume = diminuirVolume

    def informarCanal(self, canal):
        self.numeroCanal = canal

    def aumentarVolume(self, volumeMais):
        self.aumentarVolume += volumeMais
        return self.aumentarVolume

    def diminuirVolume(self, volumeMenos):
        self.diminuirVolume -= volumeMenos
        return volumeMenos

televisao = Televisao(12,23,12)
print(televisao.__dict__)
televisao.informarCanal(1)
print(televisao.__dict__)
televisao.aumentarVolume(12)
print(televisao.__dict__)