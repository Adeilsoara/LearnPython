'''
Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma
lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
'''
num = int(input('Informe um número: '))
lista_primos = []
for i in range(num+1):
    if i % 2 == 1 and i != 2:
        lista_primos.append(i)
print(lista_primos)