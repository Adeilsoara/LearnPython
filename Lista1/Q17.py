tamanho_parede = float(input('Digite o tamanho da área em metros²: '))
litros = tamanho_parede/6
qtd_latas = round(tamanho_parede/108)
qtd_galoes = round(litros/3.6)

print(f'A quantidade de latas para pintar a area em (m²) informada é: {qtd_latas}')
print(f'A quantidade de galões para pintar a área em (m²) é: {qtd_galoes}')
