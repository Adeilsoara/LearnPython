'''Faça um Programa que leia três números e mostre o maior deles.'''

num1 = int(input('Digite o 1ª número: '))
num2 = int(input('Digite o 2ª número: '))
num3 = int(input('Digite o 3ª número: '))

if (num1 > num2) and (num1 > num3):
    print(f'O maior número é o: {num1}')
elif num2 > num3:
    print(f'O maior número é o : {num2}')
else:
    print(f'O maior número é o: {num3}')