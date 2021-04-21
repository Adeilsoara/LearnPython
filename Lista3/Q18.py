'''
Faça um programa que, dado um conjunto de N números,
determine o menor valor, o maior valor e a soma dos valores.
'''
numero = []
qtd_numeros = int(input('Digite quantos números deseja informar: '))

while len(numero) < qtd_numeros:
    numero.append(int(input('Digite um número: ')))

print('*'*30)
print(f'O menor número é: {min(numero)}')
print(f'O maior número é: {max(numero)}')
print(f'O a soma dos números é: {sum(numero)}')
print('*'*30)