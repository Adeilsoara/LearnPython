'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
'''
numeros20 = []
numerosPar = []
numerosImpar = []
for i in range(20):
    numeros20.append(int(input(f'Informe o {i + 1}ª número, faltam {20 - i} números: ')))
    if numeros20[i] % 2 == 0:
        numerosPar.append(numeros20[i])
    else:
        numerosImpar.append(numeros20[i])
print(f'Os números armazenados foram: {numeros20}')
print(f'Os números Pares armazenados foram: {numerosPar}')
print(f'Os números Ímpares armazenados foram: {numerosImpar}')