import numpy as np
from scipy import ndimage
from skimage import io
from math import log10, sqrt

#function to calculate the mean of image
def mean_image(image):
    height, width = image.shape
    total = 0

    for y in range(height):
        for x in range(width):
            pixel = image[y, x]
            total += np.sum(pixel)

    mean = total / (height * width)
    return mean

#function to calculate Equivalent Number of Look (ENL)
def ENL(image): # If ENL is higher, speckle noise is weaker in the image and the interpretation is better

    nilai_enl = (mean_image(image) ** 2) / np.var(image)
    print('ENL :', nilai_enl)

#function to calculate Peak Signal-to-Noise Ratio
def PSNR(image_ori, image_filtered): #evaluate the performance of speckle noise (or other noise) elimination
    image_psnr = (image_ori - image_filtered) ** 2
    mse = mean_image(image_psnr)
    nilai_psnr = 10 * log10((255**2) / mse)
    print('PSNR :', nilai_psnr)

#function to calculate Normalized Mean
def NM(image_ori, image_filtered): # The ability to save information
    nilai_nm = mean_image(image_filtered) / mean_image(image_ori)
    print('NM :', nilai_nm)
