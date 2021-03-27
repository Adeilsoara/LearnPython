'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante. '''
letra = input('Digite uma letra para saber se é Vogal ou Consoante: ').lower()
#neste caso utilizei a função lower() para forçar que toda letra digitada ficasse
#em minúsculo evitando fazer maiores comparações entre MAIÚSCULAS/minúsculas
vogais = 'aeiou'
if letra in vogais:
    print(f'A letra "{letra}" digitada é uma vogal...')
else:
    print(f'A letra "{letra}" que você digitou é uma consoante..')
