'''
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.
'''
numA = 1
numB = 0
num = 0
print(numA, end=' ')
while num < 500:
    num = numA + numB
    numB = numA
    numA = num
    if num < 500:
        print(num, end=' ')
    else:
        print('O próximo valor será maior que 500')