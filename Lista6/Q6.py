'''Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário
e imprima a data com o nome do mês por extenso.

    Data de Nascimento: 29/10/1973
    Você nasceu em  29 de Outubro de 1973'''
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR')
data = input('Digite uma data no formato DD/MM/AAAA: ')
data_datetime = datetime.strptime(data, '%d/%m/%Y')
print(datetime.strftime(data_datetime, '%d de %B de %Y'))
