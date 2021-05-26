'''
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
 imprima o número de alunos com média maior ou igual a 7.0.
'''
notas = []
notasAluno = []

for i in range(1):
    notasAluno = []
    media = 0
    soma = 0
    print(f'{i+1}ª Aluno:')
    for j in range(4):
        notasAluno.append(float(input(f'Digite a {j+1}ª nota do aluno: ')))
        media += notasAluno[j]
    media = media / 4
    notas.append(media)
print(f'A média do aluno : {notas}')

