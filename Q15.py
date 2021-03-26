valor_hora = float(input('Quanto você ganha por hora R$ ?: '))
qtd_horas = int(input('Número de horas trabalhadas no mês: '))

salario_bruto = valor_hora * qtd_horas
ir_salario = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liq = salario_bruto - (ir_salario+ inss + sindicato)

print(f'Salário Bruto :  R${salario_bruto}')
print(f'Imposto de Renda(11%):  R${ir_salario}')
print(f'INSS (8%) : R${inss}')
print(f'Sindicato (5%): R${sindicato}')
print(f'Todos os Descontos: R${ir_salario+ inss + sindicato}')
print(f'Salario Líquido: R${salario_liq}')

