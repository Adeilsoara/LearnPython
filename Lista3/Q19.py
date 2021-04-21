'''
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''
numeros = []
cont = 0
qtd_numeros = int(input('Digite quantos números deseja informar: '))

while qtd_numeros != cont:
     numero = int(input('Digite um número: '))
     while numero > 1000  or numero < 0:
         numero = int(input('Digite um número: '))
     numeros.append(numero)
     cont = cont + 1
print(f'O menor número é: {min(numero)}')
print(f'O maior número é: {max(numero)}')
print(f'O a soma dos números é: {sum(numero)}')