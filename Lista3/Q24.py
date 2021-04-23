'''
Faça um programa que calcule o mostre a média aritmética de N notas.
'''
notas = []
cont = 0
media =0
notasInformadas = float(input('Digite quantas notas deseja informar: '))
while len(notas) < notasInformadas:
    cont = cont + 1
    notas.append(float(input(f'Digite a {cont}ª : ')))
    media = sum(notas)/len(notas)
print(f'A média das notas informadas é : {media:.2f}')