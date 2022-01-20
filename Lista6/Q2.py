'''Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e
em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.
Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas. '''

'''nome = input('Digite seu nome: ')
nova_string = ''
i = len(nome)
while i:
    i -= 1
    nova_string += nome[i]
print(nova_string.upper())'''

#Utilizando a notação SLICE
inverter = input('Digite seu nome: ')[::-1]
print(inverter)