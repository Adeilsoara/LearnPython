tamanho_arquivo = int(input('Digite o tamanhp do arquicvo em MB: '))
velocidade_internet = int(input('Digite a velocidade da sua internet em Mbps: '))
temp_down_seg = tamanho_arquivo/(velocidade_internet/8)
temp_down_min = temp_down_seg/60

print(f'Tempo estimado de Download do arquivo em Segundos: {temp_down_seg} Seg')
print(f'Tempo estimado de Download do arquivo em Minutos: {temp_down_min:.2f} Min')