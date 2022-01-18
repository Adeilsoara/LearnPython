'''Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘.
 Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo
 igual a 1 e o valor máximo é 20.
Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante. '''

def desenhaMoldura(linha, coluna):
    caracter='+-|'
    for _ in range(linha):
        for _ in range(coluna):
            print(caracter, end=' ')
        print('\n', end='')


linhaEntrada = int(input('Quantidade de Linhas: '))
colunaEntrada = int(input('Quantidade de Colunas: '))
desenhaMoldura(linhaEntrada, colunaEntrada)