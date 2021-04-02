'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário
nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e
     o programa não deve fazer pedir os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais.
        Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; '''

import math
a = float(input('Informe o valor de A da equação: '))

if a == 0:
    print('Essa não é uma equação do segundo grau... programa encerrado')
    exit()

b = float(input('Informa o valor de B da equação: '))
c = float(input('Informe o valor de C da equação: '))

delta = math.pow(b,2) - 4 *(a) * (c)
if delta < 0:
    print('A equação não possui valores reais para sua raiz... programa encerrado')
    exit()
elif delta == 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    print(f'A equação possui uma raiz: X: {x1}')
elif delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f'A equação possui duas raízes: X¹: {x1} e X²: {x2}')
else:
    print('Os valores de Delta não correspondem a nenhum valor válido...')