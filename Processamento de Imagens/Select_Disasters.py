import numpy as np
import argparse
import cv2
a = 0
img = cv2.imread('imagem_qualquer.jpeg')

print(img.shape)
rows,cols, colors = img.shape

for i in range(rows):
    for j in range(cols):
       if np.all(img[i, j] <= [30, 30, 30]):
                        a += 1
                        k = img[i,j]
                        #print(k)

print(a)
