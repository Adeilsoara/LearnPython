'''Faça um programa que leia 5 números e informe o maior número. '''

numeros = []
while len(numeros) < 5:
    numeros.append(input("Digite um número: "))
print (f'Maior numero:  {max(numeros)}')


