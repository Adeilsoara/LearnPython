'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
    desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a
    quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente'''

print('*' * 30)
print('Frutaria da Dona Maria')
print('*' * 30)

qtd_morango = float(input('Quantos quilos de morango você comprou (em Kg)?: '))
qtd_maca = float(input('Quantos quilos de maçã você comprou (em Kg)?: '))

if qtd_morango <= 5:
    valor_a_pagar_morango = qtd_morango * 2.50
    print(f'Valor da compra de Morangos: R$ {valor_a_pagar_morango:.2f}')
else:
    valor_a_pagar_morango = qtd_morango * 2.20
    print(f'Valor da compra de Morangos: R$ {valor_a_pagar_morango:.2f}')

if qtd_maca <= 5:
    valor_a_pagar_maca = qtd_maca * 1.80
    print(f'Valor da compra de Maçã: R$ {valor_a_pagar_maca:.2f}')
else:
    valor_a_pagar_maca = qtd_maca * 1.50
    print(f'Valor da compra de Maçã: R$ {valor_a_pagar_maca:.2f}')

peso_total_frutas = qtd_maca + qtd_morango
total_a_pagar = valor_a_pagar_maca + valor_a_pagar_morango

if peso_total_frutas > 8 or total_a_pagar > 25:
    total_a_pagar = total_a_pagar - (total_a_pagar * 0.1)
    print(f'Total a pagar com desconto: R$ {total_a_pagar:.2f}')