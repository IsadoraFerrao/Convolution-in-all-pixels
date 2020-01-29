import numpy as np
import imageio
import matplotlib.pyplot as plt
import imageio
import time


# executa a convolução em todos os pixels da imagem
def convolution(f, w, debug=False):
    N,M = f.shape
    n,m = w.shape #pega as coordenadas
    
    a = int((n-1)/2) #delimitando as bordas
    b = int((m-1)/2)

    # filtro invertido
    w_flip = np.flip( np.flip(w, 0) , 1)
    #nova imagem para armazenar pixels filtrados
    g = np.array(f, copy=True)

    # faz um loop por cada pixel:
    for x in range(a,N-a):
        for y in range(b,M-b):
            sub_f = f[ x-a : x+a+1 , y-b:y+b+1 ] #obtem submatriz de vizinhança de pixels 
            if (debug==True):
                print(str(x)+","+str(y)+" - subimage:\n"+str(sub_f))
                
            # executar convolução convertendo para uint8
            g[x,y] = np.sum( np.multiply(sub_f, w_flip)).astype(np.uint8)
    return g
    
imagem = imageio.imread("img02.jpg")
filtro1 = np.matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])/9.0
filtro2 = np.matrix([[1, 2, 0], [1, 4, 0], [0, 0, 0]])/8.0
 
inicio = time.time()
  
g = convolution(imagem, filtro2)
img_mean = convolution(imagem, filtro1)

fim = time.time()
print("Tempo : ", fim - inicio)
print("Filtro arbitrario \n", g)
print("Filtro simetrico \n", img_mean)


# showing images
plt.figure(figsize=(12,12))
plt.subplot(121) 
plt.imshow(imagem, cmap="gray", vmin=0, vmax=255)
plt.title("Imagem Original")
plt.axis('off')
plt.subplot(122)
plt.imshow(img_mean, cmap="gray", vmin=0, vmax=255)
plt.title("Filtro Simetrico")
plt.axis('off')
plt.show()

plt.figure(figsize=(12,12))
plt.subplot(121) 
plt.imshow(imagem, cmap="gray", vmin=0, vmax=255)
plt.title("Imagem Original")
plt.axis('off')
plt.subplot(122)
plt.imshow(g, cmap="gray", vmin=0, vmax=255)
plt.title("Filtro Arbitrario")
plt.axis('off')
plt.show()













