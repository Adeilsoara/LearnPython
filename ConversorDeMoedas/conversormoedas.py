import requests

def requisitarCotacao():
    requisicao = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
    resposta = requisicao.json()
    cotacao = resposta['USDBRL']['high']
    return cotacao

def modelarImpressao():
    return print('*'*10 +'CONVERSOR DE MOEDA USD -> BRL' + '*'*10)

def converterValorParaFloat():
    return round((float(requisitarCotacao()) * real), 2)

modelarImpressao()
real = float(input('Digite o valor em Dólar: '))
converterValorParaFloat()

print(f'USD {converterValorParaFloat()}')

