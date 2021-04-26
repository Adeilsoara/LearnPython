'''
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
'''
alunosTurma = []
turma = 1
qtdTurmas = int(input("Quantas turmas deseja informar sua quantidade de alunos? : "))
for i in range(qtdTurmas):
    alunos = int(input("Digite a quantidade de alunos: "))
    while alunos > 40:
        alunos = int(input("A turma não pode ter + de 40 alunos, informe valor < : "))
    turma += 1
    alunosTurma.append(alunos)
mediaAlunosTurma = sum(alunosTurma) / len(alunosTurma)
print(f'A média de alunos por turma é {mediaAlunosTurma} alunos')