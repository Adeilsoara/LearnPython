'''Altere o programa anterior permitindo ao usuário informar as populações e as
 taxas de crescimento iniciais. Valide a entrada e permita repetir a operação. '''

populacaoA = int(input('Informe a população da cidade A: '))
txCrescimentoA = float(input('Informe a taxa de crecimento da cidade A (%):'))
populacaoB = int(input('Informe a população da cidade B: '))
txCrescimentoB = float(input('Informe a taxa de crecimento da cidade B (%):'))
anos = 0

while populacaoA < populacaoB:
    populacaoA = round(populacaoA + (populacaoA * txCrescimentoA/100))
    populacaoB = round(populacaoB + (populacaoB * txCrescimentoB/100))
    anos +=1
print(f' A população de A se Igualará a de B em: {anos} anos')
print(f' A população de A será de: {populacaoA} habitantes')
print(f' A população de B será de: {populacaoB} habitantes')


