'''
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com
mais de 13 anos possuem altura inferior à média de altura desses alunos.
'''
idadesAlunos = []
alturasAlunos = []
alunos13 = []
mediaAbaixo = []
num = 0
for i in range(3):
    idade = int(input(f'Informe a idade do {i+1}ª aluno: '))
    idadesAlunos.append(idade)
    if idadesAlunos[i] > 13:
        alunos13.append(idade)
    num += 1
    altura = float(input(f'Informe a altura do {i+1}ª aluno: '))
    alturasAlunos.append(altura)

cont = 0
media = sum(alturasAlunos) / len(alturasAlunos)
for i in range(len(alunos13)):
    if alunos13[cont] < media:
        mediaAbaixo.append(alunos13[cont])
    cont+=1
print(f'Alunos com mais de 13 anos: {alunos13}')
print(f'Media de altura dos alunos: {media}')
print(f'Quantidae de alunos com mais de 13 anos que possuem altura inferior a média: {len(mediaAbaixo)}')