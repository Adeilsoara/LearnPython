'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

    Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
    Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
    A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
    Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o
    programa permitindo que o usuário digite o salário inicial do funcionário.
'''
salario = 1000
ano_contrato = 1996
ano_atual = 2021
ajuste = 1.5
for i in range(ano_contrato, ano_atual+1):
    ajuste = ajuste * 2
    salario_atual =  salario + (salario * (ajuste/100))
    print(f'{i} {salario_atual}')

