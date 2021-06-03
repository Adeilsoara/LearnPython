'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a
entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

    Mostre a quantidade de valores que foram lidos;
    Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    Calcule e mostre a soma dos valores;
    Calcule e mostre a média dos valores;
    Calcule e mostre a quantidade de valores acima da média calculada;
    Calcule e mostre a quantidade de valores abaixo de sete;
    Encerre o programa com uma mensagem;
'''
valor = True
notas = []
while valor:
    nota = float(input('Informe uma nota: '))
    notas.append(nota)
    if nota < 0:
        notas.pop() #Remover o -1 que é o último elemento a ser inserido na lista
        notasInvertidas = list(reversed(notas))
        mediaNotas = sum(notas)/len(notas)
        print(f'Quantidade de Valores informados: {len(notas)}')
        print(f'O Valores informados foram: {notas}\n', end='')
        print(f'O Valores informados invertidos: {notasInvertidas}')
        print(f'A soma dos valores informados é: {sum(notas)}')
        print(f'A média dos valores informados é: {mediaNotas:.2f}')
        print('Programa Encerrado')
        break