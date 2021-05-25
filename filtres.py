import matplotlib.pyplot as plt
img = plt.imread(path)
#1
img = plt.imread(path)
img = 10 - img
plt.imshow(img)
plt.axis('off')
plt.show()
#2
img = plt.imread(path)
plt.imshow(img.mean(2))
plt.axis('off')
plt.cmap = 'plasma'
plt.show()

#3
from PIL import Image
import numpy as np

img = Image.open(path).convert('L')
data = np.array(img)

img.show()
#4
kernel = np.ones((3, 3))
data1 = 0
modified = np.zeros_like(data)

 for row in range(1, img.shape[0] - 2):
        for col in range(1, img.shape[1] - 2):
            modified[row, col] = (img[row:row + 3, col:col + 3]
            *kernel).mean()
    plt.imshow(modified, cmap = 'gray')
    plt.axis('off')
    plt.show()
    
#5    
def convolve (img, kernel):
    for row in range(1, img.shape[0] - 2):
        for col in range(1, img.shape[1] - 2):
            modified[row, col] = (img[row:row + 3, col:col + 3]
            *kernel).mean()
    return modified 
  
  
  kernel2 = np.array(
    [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
    ]
)

modifed = convolve (img, kernel2)
plt.imshow(modified, cmap = 'gray')
plt.axis('off')
plt.show()

#6
import cv2
# Gaussian Blur

Gaussian = cv2.GaussianBlur(image, (7, 7), 0)

cv2.imshow('Gaussian Blurring', Gaussian)

cv2.waitKey(0)

  
# Median Blur

median = cv2.medianBlur(image, 5)

cv2.imshow('Median Blurring', median)

cv2.waitKey(0)

  

  
#two side

bilateral = cv2.bilateralFilter(image, 9, 75, 75)

cv2.imshow('Bilateral Blurring', bilateral)

cv2.waitKey(0)

cv2.destroyAllWindows()
