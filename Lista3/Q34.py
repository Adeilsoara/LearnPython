'''
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
Um número primo é aquele que é divisível apenas por um e por ele mesmo.
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo
'''
num = int(input('Digite um número: '))
if num % 2 == 0 and num != 2:
    print(f'{num} não é primo...')
else:
    print(f'{num} é primo...')