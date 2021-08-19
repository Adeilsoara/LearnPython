import numpy as np
import matplotlib.pyplot as plt
import skimage.util as skiu

# Função que ordena um vetor
def SelectionSort(vetor):
    for i in range(len(vetor)):
        menor = i
        for k in range(i + 1, len(vetor)):
            if vetor[k] < vetor[menor]:
                menor = k

        tmp = vetor[menor]
        vetor[menor] = vetor[i]
        vetor[i] = tmp
# percorre a imagem img e para cada bloco de tamanho 2n+1, o transforma

def filtro_mediana(img):
    num_linhas = img.shape[0]
    num_colunas = img.shape[1]
    filtrada = np.zeros((num_linhas, num_colunas))
# filtra imagem
    for i in range(num_linhas):
        for j in range(num_colunas):
            bloco = img[i - 2:i + 3, j - 2:j + 3]
            vetor = np.resize(bloco, 25)
            SelectionSort(vetor)  # ordena elementos da janela
            mediana = vetor[12]  # elemento central do vetor
            filtrada[i, j] = mediana
    return filtrada
# Início do script
img = plt.imread('lena2.png')
#ruidosa = skiu.random_noise(img, 's&p')  # adiciona ruído

#plt.figure(1)
#plt.imshow(ruidosa, cmap='gray')
#plt.savefig('ruidosa.jpg')
#plt.show()
# Filtra imagem de entrada
saida = filtro_mediana(img)
# Plota imagem de saída
plt.figure(2)
plt.imshow(saida, cmap='gray')
plt.savefig('saida.png')
plt.show()