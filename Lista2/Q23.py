'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.'''

num = float(input('Informe um número: '))
if num % 2 != 0 and num % 2 != 1:
    print(f'{num} este é um número decimal')
else:
    print(f'Este é um número inteiro')
