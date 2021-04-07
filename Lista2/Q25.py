'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"

    O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
    Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
    entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". '''
print('*' * 30)
print('Programa CSI Investigação')
print('Responda com S ou N')
print('*' * 30)
p1 = input('Telefonou para a vítima?: ').lower()
p2 = input('Esteve no local do crime?: ').lower()
p3 = input('Mora perto da vítima?: ').lower()
p4 = input('Devia para a vítima?: ').lower()
p5 = input('Já trabalhou com a vítima?: ').lower()

if p1 == 's':
    p1 = 1
else:
    p1 = 0

if p2 == 's':
    p2 = 1
else:
    p2 = 0

if p3 == 's':
    p3 = 1
else:
    p3 = 0

if p4 == 's':
    p4 = 1
else:
    p4 = 0

if p5 == 's':
    p5 = 1
else:
    p5 = 0

respostas = p1 + p2 + p3 + p4 + p5

if respostas <= 1:
    print('Você é inocente')
elif respostas <= 2:
    print('Você é suspeito')
elif respostas > 2 and respostas <= 4:
    print('Você é cumplice')
elif respostas == 5:
    print('Você é o assasino')
else:
    print('Informe valores válidos')