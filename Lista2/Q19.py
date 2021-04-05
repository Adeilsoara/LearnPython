'''Faça um Programa que leia um número inteiro menor que 1000 e imprima
a quantidade de centenas, dezenas e unidades do mesmo.

    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades
    Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16 '''

numero = int(input('Informe um número: '))
#o operador // retorna a divisão inteiro
centenas = numero // 100 % 10
dezenas = numero // 10 % 10
unidades = numero // 1 % 10

if numero < 1000:
    if centenas > 1:
        print(f'O número possui {centenas} centenas ')
    elif centenas <= 1:
        print(f'O número possui {centenas} centena ')
    if dezenas > 1:
        print(f'O número possui {dezenas} dezenas ')
    elif dezenas <= 1:
        print(f'O número possui {dezenas} dezena ')
    if unidades > 1:
        print(f'O número possui {unidades} unidades ')
    elif unidades <= 1:
        print(f'O número possui {unidades} unidade ')
else:
    print('Informe um número menor que 1000...')