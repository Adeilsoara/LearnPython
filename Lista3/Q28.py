'''
Faça um programa que calcule o valor total investido por um colecionador em sua
coleção de CDs e o valor médio gasto em cada um deles.
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
'''
valor_cds = []
numero_cds = int(input("Quantos CDs, deseja informar? : "))
for colecao in range(1,numero_cds+1):
    valor_cds.append(int(input(f'Informe o valor do CD {colecao}')))
valor_total = numero_cds * (sum(valor_cds))
valor_medio = sum(valor_cds) / numero_cds
print(f'O valor total da sua coleção de CDs é de: {valor_total}')
print(f'O valor médio por CD da sua é coleção de CDs é de: {valor_medio}')

