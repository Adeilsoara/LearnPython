'''
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''
numeros = []
for i in range(1, 11):
    num = float(input(f'Informe o {i}ª do vetor: '))
    numeros.append(num)
print(sorted(numeros, reverse=True))