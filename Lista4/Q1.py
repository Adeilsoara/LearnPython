'''
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''
numeros = []
for i in range(1,6):
    num = int(input(f'Digite o {i}ª número: '))
    numeros.append(num)
print(f'Os números do vetor são: {numeros}')