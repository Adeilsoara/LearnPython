import math
numInt1 = int(input('Digite um número inteiro: '))
numInt2 = int(input('Digite outro número inteiro: '))
numReal = float(input('Digite um número Real: '))

produto = (2*numInt1) + (numInt2/2)
soma = (3*numInt1) + numReal
cubo = math.pow(numReal,3)

print(f'O produto do dobro de {numInt1} com metade de {numInt2} é: {produto} ')
print(f'A soma do triplo de {numInt1} com o {numReal} é : {soma} ')
print(f'O {numReal}³ elevado ao cubo é: {cubo}')
