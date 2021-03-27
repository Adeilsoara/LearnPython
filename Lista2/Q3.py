'''Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra, escrever: F - Feminino, M - Masculino, Sexo Inválido. '''
letra = input('Digite uma letra (m/f): ')
if letra == 'f' or letra == 'F' :
    print(f'A letra {letra} corresponde ao sexo: Feminino')
elif letra == 'm' or letra == 'M':
    print(f'A letra {letra} corresponde ao sexo: Masculino')
else:
    print('A letra digitada não corresponde a nenhum sexo')