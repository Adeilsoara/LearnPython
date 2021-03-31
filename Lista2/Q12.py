'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos
são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e
3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao
Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua
hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas
    conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220. '''

valor_hora = float(input('Digite o valor da sua hora de trabalho R$: '))
qtd_horas = int(input('Informe quantas hora você trabalhou no mês(h/Mês): '))

salario_bruto = valor_hora * qtd_horas
sindicato = salario_bruto * 0.03
inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11

if salario_bruto <= 900:
    salario_liquido = salario_bruto - (sindicato + inss)
    total_descontos = inss + sindicato
    print('*' * 30)
    print(f'Salário Bruto: R$ {salario_bruto} \n'
          f'(-) IR (Isento): R$ 0.00 \n'
          f'(-) INSS (10%): R$ {inss} \n'
          f'(-) Sindicato (3%): R$ {sindicato} \n'
          f'FGTS (11%): R$ {fgts} \n'
          f'Total de descontos: R$ {total_descontos} \n'
          f'Salário Líquido: R$ {salario_liquido}')
    print('*' * 30)

elif salario_bruto > 900  and salario_bruto <= 1500:
    imposto_de_renda = salario_bruto * 0.05
    salario_liquido = salario_bruto - (sindicato + imposto_de_renda + inss)
    total_descontos = imposto_de_renda + inss + sindicato
    print('*' * 30)
    print(f'Salário Bruto: R$ {salario_bruto} \n'
          f'(-) IR (5%): R$ {imposto_de_renda} \n'
          f'(-) INSS (10%): R$ {inss} \n'
          f'(-) Sindicato (3%): R$ {sindicato} \n'
          f'FGTS (11%): R$ {fgts} \n'
          f'Total de descontos: R$ {total_descontos} \n'
          f'Salário Líquido: R$ {salario_liquido}')
    print('*' * 30)

elif salario_bruto > 1500 and salario_bruto <= 2500:
    imposto_de_renda = salario_bruto * 0.10
    salario_liquido = salario_bruto - (sindicato + imposto_de_renda + inss)
    total_descontos = imposto_de_renda + inss + sindicato
    print('*' * 30)
    print(f'Salário Bruto: R$ {salario_bruto} \n'
          f'(-) IR (10%): R$ {imposto_de_renda} \n'
          f'(-) INSS (10%): R$ {inss} \n'
          f'(-) Sindicato (3%): R$ {sindicato} \n'
          f'FGTS (11%): R$ {fgts} \n'
          f'Total de descontos: R$ {total_descontos} \n'
          f'Salário Líquido: R$ {salario_liquido}')
    print('*' * 30)

else:
    imposto_de_renda = salario_bruto * 0.20
    salario_liquido = salario_bruto - (sindicato + imposto_de_renda + inss)
    total_descontos = imposto_de_renda + inss + sindicato
    print('*' * 30)
    print(f'Salário Bruto: R$ {salario_bruto} \n'
          f'(-) IR (20%): R$ {imposto_de_renda} \n'
          f'(-) INSS (10%): R$ {inss} \n'
          f'(-) Sindicato (3%): R$ {sindicato} \n'
          f'FGTS (11%): R$ {fgts} \n'
          f'Total de descontos: R$ {total_descontos} \n'
          f'Salário Líquido: R$ {salario_liquido}')
    print('*' * 30)