'''
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
'''
vetorA = []
vetorB = []
vetorC = []
for i in range (10):
    numeros = int(input(f'Informe o {i+1}ª elemento da 1ª lista: '))
    vetorA.append(numeros)
for j in range (10):
    numeros = int(input(f'Informe o {j + 1}ª elemento da 2ª lista: '))
    vetorB.append(numeros)
for k in range (10 ):
    numeros = int(input(f'Informe o {k + 1}ª elemento da 3ª lista: '))
    vetorC.append(numeros)
print(f'O 1ª vetor é: {vetorA}')
print(f'O 2ª vetor é: {vetorB}')
print(f'O 3ª vetor é: {vetorC}')
print(f'O 4ª vetor é junção do 1ª, 2ª com o 3ª: {vetorA+vetorB+vetorC}')