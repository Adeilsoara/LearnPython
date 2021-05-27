'''
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

Neste exercício optei por utilizar a função "prod" nativa da biblioteca math do
python, que faz o cálculo do produto de um vetor
'''

from math import prod
numeros = []
for i in range (5):
    numeros.append(int(input(f'Digite o {i+1}ª número: ')))
print(f'Os números informados são: {numeros}')
print(f'A soma dos números informados é: {sum(numeros)}')
print(f'A multiplicação dos números informados é: {prod(numeros)}')

