'''
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:

    Código da cidade;
    Número de veículos de passeio (em 1999);
    Número de acidentes de trânsito com vítimas (em 1999).
    Deseja-se saber:
    Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
    Qual a média de veículos nas cinco cidades juntas;
    Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''
codigoCidade = []
numVeiculos = []
numAcidentes = []

for i in range (1, 6):
    codigo = int(input(f'Codigo da {i} cidade: '))
    codigoCidade.append(codigo)
    numVeiculos.append(int(input(f'Informe o número de veículos da COD:{codigo} cidade: ')))
    numAcidentes.append(int(input(f'Informe o número de acidentes com vítimas da cidade COD:{codigo}: ')))

maiorIndiceAcidentes = numAcidentes.index(max(numAcidentes))
menorIndiceAcidentes = numAcidentes.index(min(numAcidentes))
mediaVeiculos = sum(numVeiculos) / len(numVeiculos)
print('*********** RELATÓRIO DE TRÂNSITO ***********')
print('*'*40)
print(f'O maior índice de acidentes é da cidade {codigoCidade[maiorIndiceAcidentes]}\n'
      f'E o número de acidentes foram de: {max(numAcidentes)}')
print('*'*40)
print(f'A média dos veículos das 5 cidades informadas é de: {mediaVeiculos} por cidade')