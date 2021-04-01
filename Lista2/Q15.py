'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados formem um
triângulo, se o mesmo é: equilátero, isósceles ou escaleno. '''

ladoA = int(input('Digite o 1ª lado: '))
ladoB = int(input('Digite o 2ª lado: '))
ladoC = int(input('Digite o 3ª lado: '))

if (ladoA + ladoB < ladoC) and (ladoA + ladoC < ladoB) and (ladoB + ladoC < ladoA):
    print(f'Com os valores informados: {ladoA }, {ladoB }, {ladoC } não é possível ser um '
          f'Triângulo...')
elif (ladoA == ladoB) and (ladoA == ladoC):
    print('Triângulo Equilátero')
elif (ladoA == ladoB) or (ladoA == ladoC) or (ladoB == ladoC):
    print('Triângulo Isóseles')
else:
    print('Triângulo Escaleno')