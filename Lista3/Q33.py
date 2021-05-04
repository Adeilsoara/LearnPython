'''
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um
programa que leia as um conjunto indeterminado de temperaturas,e informe ao final a menor e a
maior temperaturas informadas, bem como a média das temperaturas.
'''
num_temperaturas = int(input('Quantas temperaturas serão informadas?: '))
temperatura = []
media_temperatura =0
for i in range(num_temperaturas):
    temperatura.append(int(input(f'Informe a {i+1}ª temperatura: ')))
    media_temperatura = round(sum(temperatura)/len(temperatura),2)
print(f' A média das temperaturas: {media_temperatura}º')
print(f' A maior temperatura é: {max(temperatura)}º')
print(f' A menor temperatura é: {min(temperatura)}º')