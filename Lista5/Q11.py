'''Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e
 devolva uma string no formato D de mesPorExtenso de AAAA.
 Opcionalmente, valide a data e retorne NULL caso a data seja inválida'''

import locale
from datetime import datetime
locale.setlocale(locale.LC_ALL, 'pt_BR')
def dataExtenso(data):
    try:
        datetime.strptime(data,'%d/%m/%Y')
    except ValueError:
        print('Formato inválido, deve ser DD/MM/AAAA')
        return None
    else:
        data_datetime = datetime.strptime(data, '%d/%m/%Y')
        return datetime.strftime(data_datetime,'%d de %B de %Y')
data = input('Digite uma data no formato DD/MM/AAAA: ')
data_completa = dataExtenso(data)

if data_completa is not None:
    print(data_completa)