# with open('ip.txt', 'r') as arquivo:
#     print(arquivo.read())

with open('ip.txt', 'r') as arquivo:
    ips = arquivo.readlines()

for linhas in ips:
    if '192.' in linhas:
        print(linhas)