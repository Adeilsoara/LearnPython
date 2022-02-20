import requests

def requisitarCotacao():
    requisicao = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
    resposta = requisicao.json()
    cotacao = resposta['USDBRL']['high']
    return cotacao

def modelarImpressao():
    return print('*'*10 +'CONVERSOR DE MOEDA USD -> BRL' + '*'*10)

def converterValorParaFloat():
    return round((float(requisitarCotacao()) * dolar), 2)

modelarImpressao()
dolar = float(input('Digite o valor em Dólar: '))
converterValorParaFloat()

print(f'(BRL)  R$ {converterValorParaFloat()}')

