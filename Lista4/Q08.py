'''
Faça um Programa que peça a idade e a altura de 5 pessoas,
armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.

É bem provavél que essa não seja a resposta correta, mas tá perto ou não
'''

idades = []
alturas = []
for i in range(2):
    idade = int(input(f'Informe a idade da {i+1}ª pessoa: '))
    idades.append(idade)
    altura = float(input(f'Informa a altura da {i+1}ª pessoa: '))
    alturas.append(altura)
print(sorted(idades, reverse=True))
print(sorted(alturas, reverse=True))

