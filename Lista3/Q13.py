'''
Faça um programa que peça dois números, base e expoente,
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
'''

base = int(input('Digite o número base: '))
expoente = int(input('Digite o expoente: '))

potencia = base ** expoente
print(f'O número {base} elevado à {expoente} = {potencia}')