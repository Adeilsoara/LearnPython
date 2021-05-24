'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
'''
numeros20 = []
for i in range(20):
    numeros20.append(int(input(f'Informe o {i + 1}ª número, faltam {20 - i} números: ')))
print(f'Os números armazenados foram: {numeros20}')