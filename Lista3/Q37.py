'''
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo,
a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um
dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados
deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também
deve ser informados os códigos e valores do clente mais alto, do mais baixo,
do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
'''
cod_usuario = []
altura = []
peso = []
cont = 0
cod = True
while cod != 0:
    cod = (int(input('Informe o seu código: ')))
    if cod == 0:
        print('Programa encerrado')
    else:
        cod_usuario.append(cod)
        altura.append(float(input('Informe sua altura: ')))
        peso.append(float(input('Informe o seu peso: ')))
        cont += 1
cod_mais_alto = altura.index(max(altura))
cod_mais_baixo = altura.index(min(altura))
cod_mais_gordo = peso.index(max(peso))
cod_mais_magro = peso.index(min(peso))
mais_alto = max(altura)
mais_baixo = min(altura)
mais_gordo = max(peso)
mais_magro = min(peso)
print(f'Cod Cliente mais alto: {cod_usuario[cod_mais_alto]} sua altura é: {mais_alto}')
print(f'Cod Cliente mais baixo: {cod_usuario[cod_mais_baixo]} sua altura é: {mais_baixo}')
print(f'Cod Cliente mais gordo: {cod_usuario[cod_mais_gordo]} seu peso é: {mais_gordo}')
print(f'Cod Cliente mais magro: {cod_usuario[cod_mais_magro]} seu peso é: {mais_magro}')