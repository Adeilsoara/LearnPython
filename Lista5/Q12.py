'''Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados.
Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível,
de forma aleatória. Padronize em sua função que todos os caracteres
serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados'''
import string
'''import random
valor = 'python'

for x in range(len(valor)):
    print(random.choice(valor), end='')'''

import random
def embaralhar(valor):
    return random.shuffle(valor)
valorEntrada = list(input('Informe uma palavra: '))
embaralhar(valorEntrada)
print(''.join(valorEntrada))
