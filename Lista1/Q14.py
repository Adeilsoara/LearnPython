peso_peixe = float(input('Digite o peso dos peixes do dia: '))
excesso = peso_peixe - 50
multa = excesso * 4
print(f'A quantidade em Quilos acima do permitido foi: {excesso}Kg ')
print(f'A multa de R$/Kg é {excesso} Kg x R$4.00 = R$ {multa}')
