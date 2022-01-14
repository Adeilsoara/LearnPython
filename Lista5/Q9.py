'''Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.'''
def reverso(numero):
    nova_string = ''
    i = len(str(numero))
    while i:
        i -= 1
        nova_string += numero[i]
    return nova_string
numero = input('Digite um número: ')
print('Número invertido: ',reverso(numero))