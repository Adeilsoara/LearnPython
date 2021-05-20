'''
Faça um programa que leia uma quantidade indeterminada de números positivos e
conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.
'''

intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0
num = True
while num > 0:
    num = int(input('Informe um número: '))
    if num >= 0 and num <=25:
        intervalo1 += 1
    elif num > 25 and num <=50:
        intervalo2 += 1
    elif num > 50 and num <=75:
        intervalo3 += 1
    elif num > 75 and num <=100:
        intervalo4 += 1
    else:
        print('Este número está fora do intervalo que desejamos analizar')
print(f'A quantidade de números que estão entre [0-25] = {intervalo1}')
print(f'A quantidade de números que estão entre [26-50] = {intervalo2}')
print(f'A quantidade de números que estão entre [51-75] = {intervalo3}')
print(f'A quantidade de números que estão entre [76-100] = {intervalo4}')