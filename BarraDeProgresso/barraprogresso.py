from tqdm import tqdm
import time

# for i in tqdm(range(10)):
#     time.sleep(1)

# with tqdm(total=100) as barra_progresso:
#     for i in range(10):
#         time.sleep(1)
#         barra_progresso.update(10)

import requests

with open("ceps.txt", "r") as arquivo:
    ceps = arquivo.read()
ceps = ceps.split("\n")

endereco_rj = []
for cep in tqdm(ceps):
    link = f'https://cep.awesomeapi.com.br/json/{cep}'
    requisicao = requests.get(link)
    resposta = requisicao.json()
    cidade = resposta['city']
    bairro = resposta['district']
    if cidade == "Rio de Janeiro":
        endereco_rj.append((cep, bairro))

print(endereco_rj)