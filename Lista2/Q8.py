'''Faça um programa que pergunte o preço de três produtos e
informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. '''

produto1 = float(input('Digite o preço do primeiro produto R$: '))
produto2 = float(input('Digite o preço do segundo produto R$: '))
produto3 = float(input('Digite o preço do terceiro produto R$: '))

if (produto1 < produto2) and (produto1 < produto3):
    print(f'Leve este produto é o menor preço: R$ {produto1}')
elif produto2 < produto3:
    print(f'Este é o menor preço: R$ {produto2}')
else:
    print(f'Este é o menor preço, leve o produto: R$ {produto3}')