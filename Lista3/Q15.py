'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
'''

n = int(input('Digite um número: '))
numA = 1
numB = 0
cont = 0
while cont < n:
    print(numA, end=' ')
    num = numA + numB
    numB = numA
    numA = num
    cont = cont + 1