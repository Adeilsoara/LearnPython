'''Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos. '''
def tresArgumentos(a, b, c):
    return print('A soma é :',a + b + c)

print('**** INFORME 3 NÚMEROS ****')
a = int(input('Informe 1ª número: '))
b = int(input('Informe 2ª número: '))
c = int(input('Informe 3ª número: '))
tresArgumentos(a, b, c)
