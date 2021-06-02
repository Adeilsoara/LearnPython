'''
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
'''
temperaturaMediaMes = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
         'Outubro', 'Novembro', 'Dezembro']
for i in range(12):
    print(f'Informe a temperatura do mês de {meses[i]}')
    temperatura = float(input(f'Informe a temperatura do {i+1}ª mês: '))
    temperaturaMediaMes.append(temperatura)
mediaAnual = sum(temperaturaMediaMes) / 12
print(mediaAnual)
for i in range(12):
    if temperaturaMediaMes[i] > mediaAnual:
        print(f'Esse mês teve a temperatura maior que a média anual: {meses[i]}')
