'''Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo,
que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas. '''

def somaImposto(taxaImposto, custo):
    return (1 + taxaImposto/100) * custo

taxa = float(input('Informe a taxa em % do imposto: '))
custo = float(input('Informe o valor do produto em R$: '))
print('Valor total com imposto: R$', somaImposto(taxa,custo))