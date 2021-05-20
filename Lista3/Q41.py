'''
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

    Os juros e a quantidade de parcelas seguem a tabela abaixo:

    Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
    1       0
    3       10
    6       15
    9       20
    12      25

    Exemplo de saída do programa:

    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1.000,00     0               1                       R$  1.000,00
    R$ 1.100,00     100             3                       R$    366,00
    R$ 1.150,00     150             6                       R$    191,67
'''

'''*******Programa não finalizado********'''
divida = float(input('Informe o valor atual da sua dívida: '))
parcela = int(input('Informe a quantidade de parcelas: '))
print('Valor da Dívida |', end=' ')
print('Valor dos Juros |', end=' ')
print('Quantidade de Parcelas |', end=' ')
print('Valor da Parcela ', end=' ')
juros = 0
valorParcela = 0
for i in range (5):
    valorParcela = (divida + juros) / parcela
    if parcela == 1 or parcela == 2:
        juros = 0
    elif parcela >= 3 or parcela < 6:
        juros = divida * (10/100)
    elif parcela >= 6 or parcela < 9:
        juros = divida * (15/100)
    elif parcela >= 9 or parcela < 12:
        juros = divida * (20/100)
    else:
        juros = divida * (25/100)


print(f'{divida}', end=' ')
print(f'{juros}', end=' ')
print(f'{parcela}', end=' ')
print(f'{valorParcela}')