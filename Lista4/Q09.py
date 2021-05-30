'''
Faça um Programa que leia um vetor A com 10 números inteiros,
calcule e mostre a soma dos quadrados dos elementos do vetor.
'''
vetorA = []
for i in range (10):
    numeros = int(input(f'Informe o {i+1}ª: '))
    vetorA.append(numeros**2)
print(f'Os elementos ao quadrado do vetor informado é: {vetorA}')
print(f'A soma dos elementos informados é: {sum(vetorA)}')