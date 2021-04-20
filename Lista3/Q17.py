'''
Faça um programa que calcule o fatorial de um número inteiro
fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''
numero = int(input("Digite um número: "))
fatorial = 1
cont = 1
while cont <= numero:
    fatorial = fatorial * cont
    cont = cont + 1
print(fatorial)

