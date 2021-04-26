'''
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
'''
candidato1 = 0
candidato2 = 0
candidato3 = 0

totalEleitores = int(input("Quantos eleitores estão aptos? : "))
for eleitor in range(0, totalEleitores):
    candidatos = int(input("Você vota em qual candidato? \n"
                           "Para o Candidato 1 - 1 \n"
                           "Para o Candidato 2 - 2 \n"
                           "Para o Candidato 3 - 3 \n"
                           "Informe seu voto: "))
    if candidatos == 1:
        candidato1 += 1
    elif candidatos == 2:
        candidato2 += 1
    elif candidatos == 3:
        candidato3 += 1
    else:
        print('Número de candidato inexistente')
print(f'O candidato 1 recebeu {candidato1} votos')
print(f'O candidato 2 recebeu {candidato2} votos')
print(f'O candidato 3 recebeu {candidato3} votos')
