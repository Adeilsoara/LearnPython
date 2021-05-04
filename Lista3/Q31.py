'''
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja
de conveniências. Faça um programa que implemente uma caixa registradora rudimentar.
O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
Um valor zero deve ser informado pelo operador para indicar o final da compra.
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto
inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

    Lojas Tabajara
    Produto 1: R$ 2.20
    Produto 2: R$ 5.80
    Produto 3: R$ 0
    Total: R$ 9.00
    Dinheiro: R$ 20.00
    Troco: R$ 11.00
    ...
'''
produtos = []
cont = 0
valorTotal = 0
while True:
    cont += 1
    produtos = float(input(f"Produto {cont}: R$: "))
    valorTotal += produtos
    if produtos == 0.00:
       break
print("*"*30)
print(f'Total: R$ {valorTotal:.2f}')
print("*"*30)
pagamento = float(input('Valor para o pagamento: R$ '))
troco = pagamento - valorTotal
print(f'Seu troco é de R$: {troco:.2f}')

reiniciar = int(input("Para encerrar digite 1, para continuar digite 0: "))
if reiniciar == 0:
    while True:
        cont += 1
        produtos = float(input(f"Produto {cont}: R$: "))
        valorTotal += produtos
        if produtos == 0.00:
            break
    print("*" * 30)
    print(f'Total: R$ {valorTotal:.2f}')
    print("*" * 30)
    pagamento = float(input('Valor para o pagamento: R$ '))
    troco = pagamento - valorTotal
    print(f'Seu troco é de R$: {troco:.2f}')
else:
    print("****Finalizando o sistema****")
