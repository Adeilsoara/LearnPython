'''
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
'''
vetorA = []
vetorB = []
for i in range (10):
    numeros = int(input(f'Informe o {i+1}ª elemento da 1ª lista: '))
    vetorA.append(numeros)
for j in range (10):
    numeros = int(input(f'Informe o {j + 1}ª elemento da 2ª lista: '))
    vetorB.append(numeros)
print(f'O 1ª vetor é: {vetorA}')
print(f'O 2ª vetor é: {vetorB}')
print(f'O 3ª vetor é junção do 1ª com o 2ª: {vetorA+vetorB}')