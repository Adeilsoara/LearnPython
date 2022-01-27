# with open('ip.txt', 'r') as arquivo:
#     print(arquivo.read())

import os

def ipValido(ip):
    partes = ip.split('.')
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit():
            return False
        parte_int = int(parte)
        if parte_int < 0 or parte_int > 255:
            return False
    return True

if os.path.exists('ip.txt'):
    ips = open('ip.txt', 'r')
    lista_de_ips = ips.read().split('\n')

    validos = []
    invalidos = []

    for ip in lista_de_ips:
        if ipValido(ip) == True:
            validos.append(ip)
        else:
            invalidos.append(ip)

    if len(validos) > 0 or len(invalidos) > 0:
        arquivo_ips_verificados = open("resposta.txt", 'wt')

        if len(validos) > 0:
            arquivo_ips_verificados.write('Endereços Válidos \n')
            for valido in validos:
                arquivo_ips_verificados.write(valido+'\n')

        if len(invalidos) > 0:
           arquivo_ips_verificados.write('\n Endereços Inválidos\n')
           for invalido in invalidos:
               arquivo_ips_verificados.write(invalido + '\n')

        arquivo_ips_verificados.close()
        