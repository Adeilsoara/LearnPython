'''Faça um Programa que peça um número correspondente a um determinado ano e em seguida
informe se este ano é ou não bissexto.'''

ano = int(input('Digite um ano qualquer para saber se é ou não Bissexto: '))
if ano % 400 == 0:
    print(f'O ano {ano} informado é Bissexto')
elif ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano {ano} informado é Bissexto')
else:
    print(f'O ano {ano} informado não é Bissexto')