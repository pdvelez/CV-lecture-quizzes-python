import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Helper functions
def normalize_image(image):
    """normalize the image between 0-255 and setting data type=uint8"""
    minImg, maxImg = np.min(image)*1., np.max(image)*1.
    return (((image - minImg)/(maxImg-minImg))*255).astype(np.uint8)

def imshow(title, image):
    """normalize the image between 0-255 and then show"""
    print 'To show, first normalizing the image between 0-255 and then setting data type=uint8'
    image = normalize_image(image)
    cv2.imshow(title, image)

# Apply a Gaussian filter to remove noise
img = cv2.imread('images/saturn.png', 0) # Read image as grayscale (because of 0. for color, use 1. for unchanged, use -1)
imshow('Img_original', img)
X, Y = map(np.arange, img.shape)
X, Y = np.meshgrid(X, Y, indexing='ij')

# TODO: Add noise to the image
noise_sigma = 25 # noise standard deviation
noise = (np.random.randn(*img.shape))*noise_sigma

img_noisy = img + noise
imshow('Img_noisy',img_noisy)

# TODO: Now apply a Gaussian filter to smooth out the noise
gauss_filter = cv2.getGaussianKernel(11,2) # this is just 1D gaussian with spacial sigma of 2 cells.
print gauss_filter
img_getGaussianKernel = cv2.sepFilter2D(img_noisy, -1, gauss_filter, gauss_filter) # desired depth=-1 (sets depth (or dtype) of new image same as src image)
imshow('Img_getGaussianKernel', img_getGaussianKernel)

# TODO: Using GaussianBlur
img_GaussianBlur = cv2.GaussianBlur(img_noisy,(11,11),2)
imshow('Img_GaussianBlur', img_GaussianBlur)

# fig=plt.figure()
# ax=Axes3D(fig)
# ax.plot_surface(X, Y, noise)
# plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()