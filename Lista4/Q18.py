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
repeticoes = collections.Counter(votos)
print(f'{repeticoes}')
print(f'Foram computados: {len(votos)} votos')

t = len(votos)
porcentagem = list(map(lambda x: repeticoes[x]*100/t, repeticoes))
percentagem = [round(repeticoes[x]*100/t,2) for x in repeticoes]

print(f'{percentagem}')
