'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro
    Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
    (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
     sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''
print('*' * 30)
print('         POSTO BUG')
print('*' * 30)
litros = float(input('Quantos litros de combustível você abasteceu?: '))
tipo_combustivel = input('Qual combustível você colocou A- Alcoól e G-Gasolina: ').lower()

if tipo_combustivel == 'a':
    if litros <= 20:
        desconto = litros * 0.03
        valor_pag = (litros * 1.90) - (desconto * 1.90)
        print(f'Valor a ser Pago R$ {valor_pag} ')
    else:
        desconto = litros * 0.05
        valor_pag = (litros * 1.90) - (desconto * 1.90)
        print(f'Valor a ser Pago R$ {valor_pag} ')

if tipo_combustivel == 'g':
    if litros <= 20:
        desconto = litros * 0.04
        valor_pag = (litros * 2.50) - (desconto * 2.50)
        print(f'Valor a ser Pago R$ {valor_pag} ')
    else:
        desconto = litros * 0.06
        valor_pag = (litros * 2.50) - (desconto * 2.50)
        print(f'Valor a ser Pago R$ {valor_pag} ')