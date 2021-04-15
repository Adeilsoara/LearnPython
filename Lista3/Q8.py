'''Faça um programa que leia 5 números e informe a soma e a média dos números. '''

numeros = []
soma = 0
media = 0
qtd_num = 0
while len(numeros) < 5:
    numeros.append(int(input("Digite um número: ")))
    soma = sum(numeros)
    qtd_num = len(numeros)
    media = soma/qtd_num
print(f'Os números digitados foram: {numeros}')
print(f'A soma dos números informados foi: {soma}')
print(f'A média dos números digitados foi: {media}')

