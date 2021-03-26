altura = float(input('Digite sua altura: '))

pesoIdealHomens = (72.7*altura) - 58
pesoIdealMulheres = (62.1*altura) - 44.7

print(f'Peso ideal para Homens baseado na altura informada: {pesoIdealHomens:.2f} Kg')
print(f'Peso ideal para Mulheres baseado na altura informada: {pesoIdealMulheres:.2f} Kg')
