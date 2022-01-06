'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus
saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando
não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
'''
saltos =[]
nomeAtleta = input("Nome do Atleta: ")
for i in range(5):
    salto = float(input(f'{i+1}ª Salto: '))
    saltos.append(salto)
mediaSaltos = sum(saltos) / len(saltos)
print("*"*30)
print(f'Resultado Final:')
print(f'Atleta: {nomeAtleta}')
print(f'Saltos: {saltos}')
print(f'Média dos Saltos: {mediaSaltos} m')