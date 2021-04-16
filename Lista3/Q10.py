'''Faça um programa que receba dois números inteiros e gere os
números inteiros que estão no intervalo compreendido por eles. '''
num1 = int(input('Digite um número: '))
num2 = int(input('Digite mais um número: '))
if num1 < num2:
    for num in range(num1, num2+1, 1):
        print(num, end=' ')
else:
    for num in range(num1, num2, -1):
        print(num, end=' ')

