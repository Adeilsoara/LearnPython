'''Faça um programa para imprimir:

        1
        1   2
        1   2   3
        .....
        1   2   3   ...  n

    para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha. '''
def imprimirNumeros(n):
    for l in range(1, n+1):
        for c in range(1, l+1):
            print(c, end='  ')
        print('')
n= int(input('Digite um número: '))
imprimirNumeros(n)