'''
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar
se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
'''
idades = []
media = 0
cont = 0
idade = int(input('Informe a quantidade de idades que deseja calcular a média: '))
while len(idades) < idade:
    cont = cont + 1
    idades.append(int(input(f'Informe a {cont}ª idade: ')))
    media = sum(idades)/len(idades)
if media > 0 and media <=25:
    print(f'A média da turma é {media:.2f} anos, considerados Jovens')
elif media > 25 and media <= 60:
    print(f'A média da turma é {media:.2f} anos, considerados Adultos')
else:
    print(f'A média da turma é {media:.2f} anos, considerados Idosos')

