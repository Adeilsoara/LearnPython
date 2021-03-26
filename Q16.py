tamanho_parede = float(input('Digite o tamanho em metros² da parede a ser pintada: '))
litros = tamanho_parede/3
qtd_latas = tamanho_parede/(54)
preco_total = qtd_latas * 80
print(f' A quantidade de latas será: {qtd_latas:.2f} Latas')
print(f' Total em Litros {litros:.2f}')
print(f' O preço da lata fracionada será de : R${preco_total:.2f}')

