'''Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado. '''
def contarNumeros(numero):
    return len(str(numero))

numero = int(input('Informe um número: '))
print('A quantidade de digitos é: ', contarNumeros(numero))
