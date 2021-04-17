'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada.
'''
num_tabuada = int(input('Informe um número: '))
print('*' * 20)
for num in range(1,11):
    multiplica = num_tabuada * num
    print(f'{num_tabuada} * {num} = {multiplica}')
print('*' * 20)