from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    requisicao = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL')
    resposta = requisicao.json()
    cotacaoBaixa = resposta['USDBRL']['low']
    cotacaoAlta = resposta['USDBRL']['high']
    cotacaoAltaEU = resposta['EURBRL']['high']
    cotacaoBaixaEU = resposta['EURBRL']['low']
    atualizacaoUSD = resposta['USDBRL']['create_date']
    atualizacaoEU = resposta['EURBRL']['create_date']
    return render_template("home.html", cotacaoBaixa=cotacaoBaixa, cotacaoAlta = cotacaoAlta, cotacaoAltaEU=cotacaoAltaEU,
                           cotacaoBaixaEU=cotacaoBaixaEU, atualizacaoUSD=atualizacaoUSD, atualizacaoEU=atualizacaoEU)


# def requisitarCotacao():
#     requisicao = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
#     resposta = requisicao.json()
#     cotacao = resposta['USDBRL']['high']
#     return render_template("home.html", cotacao=cotacao)

# def modelarImpressao():
#     return print('*'*10 +'CONVERSOR DE MOEDA USD -> BRL' + '*'*10)

# def converterValorParaFloat():
#     return round((float(requisitarCotacao()) * dolar), 2)

#modelarImpressao()
#dolar = float(input('Digite o valor em Dólar: '))
#converterValorParaFloat()
#
# print(f'(BRL)  R$ {converterValorParaFloat()}')

if __name__  == "__main__":
    app.run(debug=True)