'''Faça um Programa que leia três números e mostre o maior e o menor deles. '''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

maior = num1
menor = num1

if maior < num2:
	maior = num2

if maior < num3:
	maior = num3

if menor > num2:
	menor = num2

if menor > num3:
	menor = num3

print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')