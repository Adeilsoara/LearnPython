'''Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; '''

nome = input('Nome: ')
while len(nome) <= 3:
    nome = input('Seu nome deve ter mais que 3 caracteres: ')

idade = int(input('Idade: '))
while idade < 0 or idade > 150:
    idade = int(input('Idade deve estar entre 0 e 150 anos: '))

salario = float(input('Salário: '))
while salario < 0:
    salario = float(input('Salário deve ser maior que 0: '))

sexo = input('Sexo (F/M): ').lower()
while sexo != 'f' and sexo != 'm':
    sexo = input('Sexo deve ser digite um valor válido (F/M): ').lower()

estado_civil = input('Estado Civil ( s, c, v, d): ').lower()
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    estado_civil = input('Informe um Estado Civil válido ( s, c, v, d): ').lower()

print(f' Nome: {nome} \n'
      f' Idade: {idade} \n'
      f' Salário: {salario} \n'
      f' Sexo: {sexo} \n'
      f' Estado Civil: {estado_civil}')