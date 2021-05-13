'''
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno
e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo.
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas
'''
numero_aluno = []
altura_aluno = []
for i in range(1, 11):
    cod = int(input(f'Informe o número do aluno {i}ª:'))
    numero_aluno.append(cod)
    altura_aluno.append(float(input(f'Informa a altura do aluno {i}ª:')))
cod_mais_alto = altura_aluno.index(max(altura_aluno))
cod_mais_baixo = altura_aluno.index(min(altura_aluno))

mais_alto = max(altura_aluno)
mais_baixo = min(altura_aluno)

print(f'O aluno mais alto possui o código {numero_aluno[cod_mais_alto]} e sua altura é: {mais_alto} ')
print(f'O aluno mais baixo possui o código {numero_aluno[cod_mais_baixo]} e sua altura é: {mais_baixo} ')