'''
Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares e a quantidade de números impares.
'''
num = 0
pares = 0
impares = 0
while num < 10:
    num = int(input('digite um numero: '))
    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
print(f'A quantidade de pares digitados foram: {pares}\n'
      f'A quantidade de impares digitados foi: {impares}')