'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.'''

num1 = float(input('Digite o 1ª número: '))
num2 = float(input('Digite o 2ª número: '))
operacao = int(input('Qual operação aritmética você deseja realizar? \n'
                 '1 - Soma \n'
                 '2 - Subtração \n'
                 '3 - Multiplicação \n'
                 '4 - Divisão \n'
                 'Informe, digite uma opção: '))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

par = soma % 2 == 0
impar = soma % 2 == 1
if operacao == 1:
    print(f'Soma é: {soma} ')
    if par == True:
        print('A soma é Par')
    else:
        print('A Soma é Ímpar')
    if soma >= 0:
        print('A soma é Positiva')
    else:
        print('A soma é Negativa')
    if round(soma) == soma:
        print('A soma é Inteira')
    else:
        print('A soma é Decimal')
elif operacao == 2:
    print(f'Subtração é: {subtracao}')
    if par == True:
        print('A subtração é Par')
    else:
        print('A subtração é Ímpar')
    if subtracao >= 0:
        print('A subtração é Positiva')
    else:
        print('A subtração é Negativa')
    if round(subtracao) == subtracao:
        print('A subtração é Inteira')
    else:
        print('A subtração é Decimal')
elif operacao == 3:
    print(f'Multiplicação é: {multiplicacao:.2f}')
    if par == True:
        print('A multiplicação é Par')
    else:
        print('A multiplicação é Ímpar')
    if multiplicacao >= 0:
        print('A multiplicação é Positiva')
    else:
        print('A multiplicação é Negativa')
    if round(multiplicacao) == multiplicacao:
        print('A multiplicação é Inteira')
    else:
        print('A multiplicação é Decimal')
elif operacao == 4:
    print(f'Divisão é: {divisao:.2f}')
    if par == True:
        print('A divisão é Par')
    else:
        print('A divisão é Ímpar')
    if divisao >= 0:
        print('A divisão é Positiva')
    else:
        print('A divisão é Negativa')
    if round(divisao) == divisao:
        print('A divisão é Inteira')
    else:
        print('A divisão é Decimal')
else:
    print('Informe uma opção válida por favor...')
