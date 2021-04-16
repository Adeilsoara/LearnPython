'''
Faça um programa que receba dois números inteiros e gere os números inteiros que
estão no intervalo compreendido por eles.
Altere o programa anterior para mostrar no final a soma dos números.
'''
num1 = int(input('Digite um número: '))
num2 = int(input('Digite mais um número: '))
soma = 0
if num1 < num2:
    for num in range(num1, num2+1, 1):
        print(num, end=' ')
        soma = soma + num
else:
    for num in range(num1, num2, -1):
        print(num, end=' ')
        soma = soma + num
print(f'A soma dos números é: {soma}')