'''
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
Imprima as consoantes.
 Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três ve'''
vogais = ['a','e','i','o','u']
consoantes = []
cont = 0
for i in range(11):
    consoantes.append(input(f'Digite o {i+1}ª caracter: '))
    conso = consoantes[i]
    if conso not in vogais:
        cont +=1
print(f'A quantidade de consoantes é: {cont}')