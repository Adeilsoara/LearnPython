'''Faça um programa que lê as duas notas parciais obtidas por um aluno
numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos
obedece à tabela abaixo:

      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E. '''

nota1 = float(input('Informe sua primeira nota: '))
nota2 = float(input('Informe sua segunda nota: '))

media = (nota1 + nota2)/2

if media >= 9 and media <= 10:
    print(f'Sua notas foram: {nota1} e {nota2} \n'
          f'Sua média foi: {media:.2f} \n'
          f'Conceito: A \n'
          f'Resultado: Aprovado ')

elif media >= 7.5 and media < 9:
    print(f'Sua notas foram: {nota1} e {nota2} \n'
          f'Sua média foi: {media:.2f} \n'
          f'Conceito: B \n'
          f'Resultado: Aprovado ')

elif media >= 6 and media < 7.5:
    print(f'Sua notas foram: {nota1} e {nota2} \n'
          f'Sua média foi: {media:.2f} \n'
          f'Conceito: C \n'
          f'Resultado: Aprovado ')

elif media >= 4 and media < 6:
    print(f'Sua notas foram: {nota1} e {nota2} \n'
          f'Sua média foi: {media:.2f} \n'
          f'Conceito: D \n'
          f'Resultado: Reprovado ')

elif media >= 0 and media < 4:
    print(f'Sua notas foram: {nota1} e {nota2} \n'
          f'Sua média foi: {media:.2f} \n'
          f'Conceito: E \n'
          f'Resultado: Reprovado ')
    
else:
    print('Digite valores válidos para as notas...')