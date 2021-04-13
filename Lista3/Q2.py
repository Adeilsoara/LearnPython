'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. '''

nome_usuario = input('Nome de Usuário: ')
senha = input('Digite a senha: ')

while senha == nome_usuario:
    print('ERRO..Senha igual nome de usuário! Insira novamente as informações...')
    nome_usuario = input('Nome de Usuário: ')
    senha = input('Digite a senha: ')

print('*'*25)
print('Login efetuado com sucesso!')
print('*'*25)
