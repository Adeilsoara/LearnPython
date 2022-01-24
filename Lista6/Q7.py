'''Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

    quantos espaços em branco existem na frase.
    quantas vezes aparecem as vogais a, e, i, o, u. '''

def contarVogais(frase):
    vogais = 'aeiou'
    quantidadeVogais = 0
    for letra in frase:
        if letra in vogais:
            quantidadeVogais +=1
    return quantidadeVogais

#contar com Regex
import re
def contarVogaisregex(frase):
   contar = re.findall('[aeiou]', frase)
   return len(contar)

def contarEspacos(frase):
    contarEspacos = re.findall(' ', frase)
    return len(contarEspacos)

frase = input('Digite uma frase qualquer: ')
print(f'Contagem de Vogais: ', contarVogais(frase))
print(f'Contagem de Vogais com Regex: ', contarVogaisregex(frase))
print(f'Contagem de Espaços: ', contarEspacos(frase))