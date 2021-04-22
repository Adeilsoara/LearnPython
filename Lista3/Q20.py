'''
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial
várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
'''

numero = int(input("Digite um número: "))
fatorial = 1
cont = 1
if numero > 0 and numero < 16 :
    while cont <= numero:
        fatorial = fatorial * cont
        cont = cont + 1
else:
    print('Valores fora do range entre 0 e 16')
print(fatorial)