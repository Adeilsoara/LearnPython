'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                          Até 5 Kg           Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não
    há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente
    receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a
    quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
    tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. '''
print('*' * 55)
print('                       Até 5 Kg           Acima de 5 Kg')
print(' File            R$ 4,90 por Kg          R$ 5,80 por Kg')
print(' Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg')
print(' Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg')
print('*' * 55)
print('*** Você pode comprar apenas um tipo de carne ***')

PRECO_FILE1 = 4.90
PRECO_FILE2 = 5.80
PRECO_ALCATRA1 = 5.90
PRECO_ALCATRA2 = 6.80
PRECO_PICANHA1 = 6.90
PRECO_PICANHA2 = 7.80
DESCONTO_CARTAO = 0.05

tipo_carne = input('Informe aqui qual carne você escolheu: ').lower()

if tipo_carne == 'file':
    qtd_carne = float(input(f'Quantos quilos você deseja de {tipo_carne} (Kg)?: '))
    if qtd_carne < 5:
        preco_tot_file = qtd_carne * PRECO_FILE1
    else:
        preco_tot_file = qtd_carne * PRECO_FILE2

if tipo_carne == 'alcatra':
    qtd_carne = float(input(f'Quantos quilos você deseja de {tipo_carne} (Kg)?: '))
    if qtd_carne < 5:
        preco_tot_alcatra = qtd_carne * PRECO_ALCATRA1
    else:
        preco_tot_alcatra = qtd_carne * PRECO_ALCATRA2

if tipo_carne == 'picanha':
    qtd_carne = float(input(f'Quantos quilos você deseja de {tipo_carne} (Kg)?: '))
    if qtd_carne < 5:
        preco_tot_picanha = qtd_carne * PRECO_PICANHA1
    else:
        preco_tot_picanha = qtd_carne * PRECO_PICANHA2

