'''Faça um Programa que peça uma data no formato dd/mm/aaaa e
determine se a mesma é uma data válida. '''

'''from datetime import datetime
data = input('Informe uma data(dd/mm/aaaa): ')
data_convertida = datetime.strptime(data, '%d/%m/%Y')
if data == data_convertida:
    print('Data válida')
else:
    print('fim')'''
print('Informe a data na sequência do formato - dd/mm/aaaa')
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

if dia >0 and dia <=31:
    if mes >0 and mes <=12:
        if ano > 0000 and ano <= 9999:
            print(f'{dia}/{mes}/{ano}')
else:
    print('Dados informados não válidos...')
#Não finalizado