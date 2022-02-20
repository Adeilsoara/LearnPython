import requests

def converter():
    requisicao = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
    resposta = requisicao.json()
    cotacao = resposta['USDBRL']['high']
    return cotacao

print('*'*10 +'CONVERSOR DE MOEDA USD -> BRL' + '*'*10)
real = float(input('Digite o valor em Dólar: '))
conversao = round((float(converter()) * real), 2)

print(f'USD {conversao}')

