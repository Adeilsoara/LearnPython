'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.'''

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1+nota2)/2
if media >= 7 and media < 10:
    print(f'Parabéns você foi aprovado sua média foi: {media}')
elif media < 7:
    print(f'Infelizmente você foi reprovado sua média foi: {media}')
elif media == 10:
    print(f'Parabéns tu é o bichão mermo tua média foi: {media}')
else:
    print('Valores inválidos para uma média')