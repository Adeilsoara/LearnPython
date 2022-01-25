'''
Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
e indique se é um número
válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.
'''
def formatoCPF(cpf):
    #formato = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
    if (cpf[3] != '.') or (cpf[7]!= '.') or (cpf[11]!= '-'):
        print('CPF no formato inválido')
    else:
        print('CPF no formato válido')

cpfEntrada = input('Informe um CPF (000.000.000-00): ')
formatoCPF(cpfEntrada)