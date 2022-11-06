import cv2
from matplotlib import pyplot as plt
import numpy as np
from sklearn.decomposition import PCA

# Loading the image 
img = cv2.imread('group_photo_test.jpg') #you can use any image you want.
plt.imshow(img)

# Splitting the image in R,G,B arrays.
blue,green,red = cv2.split(img) 
#it will split the original image into Blue, Green and Red arrays.

#initialize PCA with first 20 principal components
pca = PCA(20)
 
#Applying to red channel and then applying inverse transform to transformed array.
red_transformed = pca.fit_transform(red)
red_inverted = pca.inverse_transform(red_transformed)
 
#Applying to Green channel and then applying inverse transform to transformed array.
green_transformed = pca.fit_transform(green)
green_inverted = pca.inverse_transform(green_transformed)
 
#Applying to Blue channel and then applying inverse transform to transformed array.
blue_transformed = pca.fit_transform(blue)
blue_inverted = pca.inverse_transform(blue_transformed)



img_compressed = (np.dstack((red_inverted, red_inverted, red_inverted))).astype(np.uint8)

#viewing the compressed image
plt.imshow(img_compressed)