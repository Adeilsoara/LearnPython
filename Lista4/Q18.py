import collections
votos = []
while True:
    voto = int(input('Número do jogador (0=fim): '))
    if voto == 0:
        print('Contagem de votos finalizada')
        break
    if voto < 1 or voto > 23:
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
        break
    votos.append(voto)
print(collections.Counter(votos))
print(len(votos))
print(votos)
